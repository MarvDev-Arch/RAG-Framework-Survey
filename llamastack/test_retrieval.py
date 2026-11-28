from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")

results = client.vector_stores.search(
    vector_store_id="vs_a6ea0d18-5fcc-48e2-9580-7b003eeb8937",
    query="What are embeddings?"
)

print("RETRIEVAL RESULTS:")
print(results)