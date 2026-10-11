#Step 1 Build a vector store
#We need the free embeddings + FAISS:
#pip install langchain-huggingface sentence-transformers faiss-cpu - I had already installed these, so I didn't need to do it again.
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

texts = [
    "Python is a programming language used for AI.",
    "Streamlit is used to build web apps quickly.",
    "LangChain helps connect AI models with your data.",
    "Dogs are friendly and loyal animals."
]

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.from_texts(texts, embeddings)

print("Vector store ready!")

#Step 2 Create a Retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})  # return top 2 results
print("Retriever is ready!")

#Step 3: Ask a question
#The retriever finds the most relevant chunks for our question.
question = "What is used to build web apps?"

results = retriever.invoke(question)

print("Question:", question)
print("\nRelevant information found:")
for r in results:
    print("-", r.page_content)