from pathlib import Path
from llama_stack_client import LlamaStackClient

# 1. Connect to LlamaStack
client = LlamaStackClient(
    base_url="http://localhost:8321"
)

# 2. Locate common test questions
BASE_DIR = Path(__file__).resolve().parent
CORPUS_DIR = BASE_DIR.parent / "corpus"

questions_file = CORPUS_DIR / "test-questions.txt"

questions = [
    line.strip()
    for line in questions_file.read_text(encoding="utf-8").splitlines()
    if line.strip()
]

# 3. Run retrieval tests
VECTOR_STORE_ID = "vs_a6ea0d18-5fcc-48e2-9580-7b003eeb8937"

print("\nLLAMASTACK RETRIEVAL RESULTS")
print("----------------------------")

for question in questions:

    results = client.vector_stores.search(
        vector_store_id=VECTOR_STORE_ID,
        query=question
    )

    print(f"\nQuestion: {question}")

    for index, item in enumerate(results.data, start=1):
        print(f"\nResult {index}:")

        for content in item.content:
            if content.text:
                print(content.text)

        print(f"Similarity score: {item.score}")
        print("-" * 50)