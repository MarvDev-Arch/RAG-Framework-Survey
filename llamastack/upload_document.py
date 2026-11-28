from pathlib import Path
from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")

document = Path("corpus/rag-introduction.txt")

# Upload document
with document.open("rb") as file:
    uploaded = client.files.create(
        file=file,
        purpose="assistants"
    )

print("File uploaded:", uploaded.id)

# Attach document to vector store
result = client.vector_stores.files.create(
    vector_store_id="vs_a6ea0d18-5fcc-48e2-9580-7b003eeb8937",
    file_id=uploaded.id
)

print("Document attached:", result)