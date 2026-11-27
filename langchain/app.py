
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Load document
loader = TextLoader("corpus/rag-introduction.txt", encoding="utf-8")
documents = loader.load()

# 2. Split document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# 3. Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Create FAISS vector store
vector_store = FAISS.from_documents(chunks, embeddings)

# 5. Display results
print("LANGCHAIN VECTOR STORE CREATED SUCCESSFULLY!")
print("---------------------------------------------")
print(f"Documents loaded: {len(documents)}")
print(f"Chunks created: {len(chunks)}")
print("Embedding model: all-MiniLM-L6-v2")
print("Vector database: FAISS")
print("Vector store is ready for retrieval!")

# 6. Test document retrieval
query = "What are embeddings?"

results = vector_store.similarity_search(query, k=2)

print("\nLANGCHAIN RETRIEVAL TEST")
print("-----------------------")
print(f"Question: {query}")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}:")
    print(result.page_content)
