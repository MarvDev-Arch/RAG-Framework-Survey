
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Load the shared document
loader = TextLoader("corpus/rag-introduction.txt", encoding="utf-8")
documents = loader.load()

# 2. Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# 3. Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Create FAISS vector store
vector_store = FAISS.from_documents(chunks, embeddings)

print("LANGCHAIN VECTOR STORE CREATED SUCCESSFULLY")
print("--------------------------------------------")
print(f"Documents loaded: {len(documents)}")
print(f"Chunks created: {len(chunks)}")
print("Embedding model: all-MiniLM-L6-v2")
print("Vector database: FAISS")

# 5. Test retrieval using the common questions
with open("corpus/test-questions.txt", "r", encoding="utf-8") as file:
    questions = [line.strip() for line in file if line.strip()]

print("\nLANGCHAIN RETRIEVAL RESULTS")
print("---------------------------")

for question in questions:
    results = vector_store.similarity_search(question, k=2)

    print(f"\nQuestion: {question}")

    for index, result in enumerate(results, start=1):
        print(f"\nResult {index}:")
        print(result.page_content)