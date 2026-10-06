import numpy as np


def calculate_similarity(embedding_1, embedding_2):
    """
    Calculate cosine similarity between two embeddings.
    Returns a score between 0 and 1.
    """

    if not embedding_1 or not embedding_2:
        return 0.0

    vector_1 = np.array(embedding_1)
    vector_2 = np.array(embedding_2)

    similarity = np.dot(vector_1, vector_2) / (
        np.linalg.norm(vector_1) * np.linalg.norm(vector_2)
    )

    return round(float(similarity), 4)


def similarity_percentage(similarity_score):
    """
    Convert similarity score into percentage.
    """

    return round(similarity_score * 100, 2)


def get_similarity_category(score):
    """
    Classify semantic similarity.
    """

    if score >= 0.80:
        return "Highly Similar"

    if score >= 0.65:
        return "Relevant"

    if score >= 0.50:
        return "Partially Relevant"

    return "Low Similarity"


if __name__ == "__main__":

    embedding_1 = [1.0, 0.0, 0.0]
    embedding_2 = [0.9, 0.1, 0.0]

    score = calculate_similarity(
        embedding_1,
        embedding_2
    )

    percentage = similarity_percentage(score)
    category = get_similarity_category(score)

    print("Semantic Similarity Scorer")
    print("--------------------------")
    print("Similarity Score:", score)
    print("Similarity Percentage:", percentage, "%")
    print("Category:", category)