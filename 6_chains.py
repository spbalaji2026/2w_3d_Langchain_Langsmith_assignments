import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load the .env file from your project folder
load_dotenv()

# 2. Now initialize ChatOpenAI
model = ChatOpenAI(model="gpt-4o-mini")


#Create the three pieces
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Prompt: a template with a blank {topic} to fill in
prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")

# 2. Model: the OpenAI chat model
model = ChatOpenAI(model="gpt-4o-mini")

# 3. Output parser: turn the model's reply into plain text
output_parser = StrOutputParser()

print("All three pieces are ready!")

#Join them into a chain
chain = prompt | model | output_parser
print("Chain is ready!")

#Run the chain
#We call .invoke() and pass values for the blanks in the prompt. The whole pipeline runs automatically.
answer = chain.invoke({"topic": "Python"})
print(answer)