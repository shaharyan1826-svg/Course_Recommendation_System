
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_courses():
    return pd.read_csv("data/courses.csv")


def recommend_courses(interests, career_goal, top_n=5):
    courses = load_courses()

    # Combine course information
    courses["combined"] = (
        courses["category"].fillna("") + " " +
        courses["skills"].fillna("") + " " +
        courses["career_goal"].fillna("") + " " +
        courses["description"].fillna("")
    )

    # Convert course text into TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words="english")
    course_vectors = vectorizer.fit_transform(courses["combined"])

    # Build student preference profile
    student_profile = interests + " " + career_goal
    student_vector = vectorizer.transform([student_profile])

    # Calculate similarity
    scores = cosine_similarity(
        student_vector, course_vectors
    ).flatten()

    # Rank courses
    courses["score"] = scores
    recommendations = courses.sort_values(
        by="score", ascending=False
    ).head(top_n)

    return recommendations[
        ["course_id", "title", "category", "career_goal", "score"]
    ]


if __name__ == "__main__":
    results = recommend_courses(
        interests="Python programming data analysis",
        career_goal="Data Scientist"
    )

    print("\nRecommended Courses:")
    print(results.to_string(index=False))
