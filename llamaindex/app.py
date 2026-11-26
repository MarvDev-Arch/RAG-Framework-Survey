from pathlib import Path

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding


# Configure local embedding model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Locate corpus folder
BASE_DIR = Path(__file__).resolve().parent
CORPUS_DIR = BASE_DIR.parent / "corpus"

# Load documents
documents = SimpleDirectoryReader(
    input_dir=str(CORPUS_DIR)
).load_data()

print(f"Successfully loaded {len(documents)} document(s).")

# Create vector index
index = VectorStoreIndex.from_documents(documents)

# Configure retriever
retriever = index.as_retriever(similarity_top_k=2)

# Ask questions
while True:
    question = input("\nAsk a question (type 'exit' to stop): ")

    if question.lower() == "exit":
        print("LlamaIndex session ended.")
        break

    results = retriever.retrieve(question)

    print("\nRetrieved information:")

    for result in results:
        print(result.text)
        print("-" * 50)