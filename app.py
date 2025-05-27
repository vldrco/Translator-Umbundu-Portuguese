from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def chat_openai_instance(api_key):
    return ChatOpenAI(
        openai_api_key=api_key,
        max_completion_tokens=1000,
        model="ft:gpt-4o-mini-2024-07-18:personal:translator-umbundu:AzrnStGy",
    )

def format_prompt(input_text):
    return ChatPromptTemplate.from_messages([
    ("system", "You are a Portuguese to Umbundu translator."),
    ("user", "{input}")
    ])

def translate(input_text, api_key):
    llm = chat_openai_instance(api_key)
    prompt = format_prompt(input_text)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    response = chain.invoke({"input": input_text})
    return response