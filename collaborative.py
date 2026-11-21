
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def recommend_for_student(student_id, top_n=5):
    ratings = pd.read_csv("data/ratings.csv")

    # Create student-course rating matrix
    matrix = ratings.pivot_table(
        index="student_id",
        columns="course_id",
        values="rating"
    ).fillna(0)

    if student_id not in matrix.index:
        raise ValueError("Student ID not found.")

    # Calculate similarity between students
    similarity = cosine_similarity(matrix)

    similarity_df = pd.DataFrame(
        similarity,
        index=matrix.index,
        columns=matrix.index
    )

    similar_students = similarity_df[student_id].drop(student_id)

    # Calculate weighted scores for unrated courses
    scores = {}

    for course_id in matrix.columns:
        if matrix.loc[student_id, course_id] == 0:
            numerator = 0
            denominator = 0

            for other_student, sim_score in similar_students.items():
                rating = matrix.loc[other_student, course_id]

                if rating > 0 and sim_score > 0:
                    numerator += sim_score * rating
                    denominator += sim_score

            if denominator > 0:
                scores[course_id] = numerator / denominator

    if not scores:
        return pd.DataFrame(columns=["title", "predicted_rating"])

    # Sort recommendations
    recommendations = pd.DataFrame(
        scores.items(),
        columns=["course_id", "predicted_rating"]
    )

    courses = pd.read_csv("data/courses.csv")

    recommendations = recommendations.merge(
        courses[["course_id", "title", "category"]],
        on="course_id"
    )

    return recommendations.sort_values(
        "predicted_rating",
        ascending=False
    ).head(top_n)[["title", "category", "predicted_rating"]]


if __name__ == "__main__":
    result = recommend_for_student("S1")

    print("\nCollaborative Filtering Recommendations:")
    print(result.to_string(index=False))
