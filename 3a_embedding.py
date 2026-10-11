from langchain_huggingface import HuggingFaceEmbeddings
text = "I love programming in Python."
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector = embeddings.embed_query(text)

print("How many numbers in this vector?", len(vector))
print("First 5 numbers:", vector[:5])