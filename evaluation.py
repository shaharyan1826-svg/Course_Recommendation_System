
def precision_at_k(recommended, relevant, k=5):
    recommended_top_k = recommended[:k]

    if not recommended_top_k:
        return 0.0

    relevant_count = sum(
        1 for course in recommended_top_k
        if course in relevant
    )

    return relevant_count / len(recommended_top_k)


def recall_at_k(recommended, relevant, k=5):
    if not relevant:
        return 0.0

    recommended_top_k = recommended[:k]

    relevant_count = sum(
        1 for course in recommended_top_k
        if course in relevant
    )

    return relevant_count / len(relevant)


if __name__ == "__main__":
    recommended = [
        "Data Visualization",
        "Java Programming",
        "Power BI Analytics",
        "Frontend Development",
        "Data Science with Python"
    ]

    relevant = [
        "Data Visualization",
        "Power BI Analytics",
        "Data Science with Python"
    ]

    precision = precision_at_k(recommended, relevant)
    recall = recall_at_k(recommended, relevant)

    print("Recommendation Evaluation")
    print("-------------------------")
    print(f"Precision@5: {precision:.2f}")
    print(f"Recall@5: {recall:.2f}")
