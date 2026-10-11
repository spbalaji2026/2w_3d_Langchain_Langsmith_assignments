import os
from dotenv import load_dotenv

# Pass the exact custom filename
load_dotenv(".env.first_langsmith")

# Now os.getenv() will read from it
langsmith_key = os.getenv("LANGCHAIN_API_KEY")

#Run a LangChain chain — it is traced automatically
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")
model = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | model | StrOutputParser()

# This run is automatically recorded in LangSmith.
print(chain.invoke({"topic": "LangSmith"}))