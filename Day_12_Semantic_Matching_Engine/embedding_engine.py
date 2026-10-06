from sentence_transformers import SentenceTransformer


# Pre-trained semantic embedding model
MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def generate_embedding(text):
    """
    Convert text into a semantic embedding vector.
    """
    if not text:
        return []

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()


def generate_embeddings(texts):
    """
    Generate embeddings for multiple text documents.
    """
    if not texts:
        return []

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings.tolist()


if __name__ == "__main__":

    sample_text = """
    Python developer with experience building REST APIs,
    machine learning applications and backend services.
    """

    embedding = generate_embedding(sample_text)

    print("Semantic Embedding Engine")
    print("-------------------------")
    print("Model:", MODEL_NAME)
    print("Embedding Dimensions:", len(embedding))
    print("Embedding Generated Successfully!")