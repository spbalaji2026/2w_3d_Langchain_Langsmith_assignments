import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load environment variables
load_dotenv(".env.first_langsmith")

# 2. Get runtime input from the user in the terminal
user_topic = input("Enter a topic you want explained: ")

# 3. Initialize components
prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")
model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# 4. Build the LCEL pipeline and invoke with the dynamic user input
chain = prompt | model | parser
result = chain.invoke({"topic": user_topic})

# 5. Print the output
print("\nAI Response:")
print(result)
