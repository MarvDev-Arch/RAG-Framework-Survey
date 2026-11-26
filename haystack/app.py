
from pathlib import Path

from haystack import Document, Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore

from haystack_integrations.components.embedders.sentence_transformers import (
    SentenceTransformersDocumentEmbedder,
    SentenceTransformersTextEmbedder
)

from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever


# 1. Locate corpus folder
BASE_DIR = Path(__file__).resolve().parent
CORPUS_DIR = BASE_DIR.parent / "corpus"

# 2. Load text document
file_path = CORPUS_DIR / "rag-introduction.txt"
content = file_path.read_text(encoding="utf-8")

documents = [Document(content=content)]

print(f"Loaded {len(documents)} document(s).")

# 3. Create document store
document_store = InMemoryDocumentStore()

# 4. Generate document embeddings
document_embedder = SentenceTransformersDocumentEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

document_embedder.warm_up()

embedded_documents = document_embedder.run(
    documents
)["documents"]

document_store.write_documents(embedded_documents)

# 5. Create retrieval pipeline
pipeline = Pipeline()

pipeline.add_component(
    "text_embedder",
    SentenceTransformersTextEmbedder(
        model="sentence-transformers/all-MiniLM-L6-v2"
    )
)

pipeline.add_component(
    "retriever",
    InMemoryEmbeddingRetriever(
        document_store=document_store,
        top_k=1
    )
)

pipeline.connect(
    "text_embedder.embedding",
    "retriever.query_embedding"
)

print("Haystack retrieval pipeline is ready.")

# 6. Ask questions
while True:
    question = input("\nAsk a question (type 'exit' to stop): ")

    if question.lower() == "exit":
        print("Haystack session ended.")
        break

    result = pipeline.run({
        "text_embedder": {
            "text": question
        }
    })

    print("\nRetrieved information:")

    for document in result["retriever"]["documents"]:
        print(document.content)
        print("-" * 50)
