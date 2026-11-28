from pathlib import Path

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# 1. Locate project folders
BASE_DIR = Path(__file__).resolve().parent
CORPUS_DIR = BASE_DIR.parent / "corpus"

# 2. Load shared document
documents = SimpleDirectoryReader(
    input_files=[str(CORPUS_DIR / "rag-introduction.txt")]
).load_data()

print(f"Documents loaded: {len(documents)}")

# 3. Load embedding model
embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Create vector index
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

# 5. Create retriever
retriever = index.as_retriever(similarity_top_k=2)

print("LlamaIndex vector index created successfully.")

# 6. Load common test questions
questions_file = CORPUS_DIR / "test-questions.txt"

questions = [
    line.strip()
    for line in questions_file.read_text(encoding="utf-8").splitlines()
    if line.strip()
]

# 7. Test retrieval
print("\nLLAMAINDEX RETRIEVAL RESULTS")
print("----------------------------")

for question in questions:
    results = retriever.retrieve(question)

    print(f"\nQuestion: {question}")

    for number, result in enumerate(results, start=1):
        print(f"\nResult {number}:")
        print(result.text)
        print("-" * 50)