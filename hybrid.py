
import pandas as pd
from recommendation import recommend_courses
from collaborative import recommend_for_student


def hybrid_recommend(interests, career_goal, student_id, top_n=5):

    # Content-based recommendations
    content = recommend_courses(
        interests,
        career_goal,
        top_n=15
    )

    content = content[["course_id", "score"]].copy()

    # Collaborative recommendations
    collaborative = recommend_for_student(
        student_id,
        top_n=15
    )

    courses = pd.read_csv("data/courses.csv")

    collaborative = collaborative.merge(
        courses[["title", "course_id"]],
        on="title"
    )

    collaborative = collaborative[
        ["course_id", "predicted_rating"]
    ]

    # Combine both recommendation scores
    hybrid = content.merge(
        collaborative,
        on="course_id",
        how="outer"
    ).fillna(0)

    # Normalize collaborative rating to 0-1
    hybrid["collaborative_score"] = (
        hybrid["predicted_rating"] / 5
    )

    hybrid["hybrid_score"] = (
        0.5 * hybrid["score"] +
        0.5 * hybrid["collaborative_score"]
    )

    hybrid = hybrid.merge(
        courses[["course_id", "title", "category", "career_goal"]],
        on="course_id"
    )

    return hybrid.sort_values(
        "hybrid_score",
        ascending=False
    ).head(top_n)[
        ["title", "category", "hybrid_score"]
    ]


if __name__ == "__main__":
    result = hybrid_recommend(
        interests="Python programming data analysis",
        career_goal="Data Scientist",
        student_id="S1"
    )

    print("\nHybrid Course Recommendations:")
    print(result.to_string(index=False))
