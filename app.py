from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def chat_openai_instance():
    return ChatOpenAI(
        openai_api_key="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",
        model="gpt-4o-mini",
    )

def format_prompt(source_language, target_language, input_text):
    return ChatPromptTemplate.from_messages([
    ("system", "Translate from {source_language} to {target_language}. You respond only in {target_language}"),
    ("user", "{input}")
    ])

def translate(input_text, source_language, target_language):
    llm = chat_openai_instance()
    prompt = format_prompt(source_language, target_language, input_text)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    response = chain.invoke({"input": input_text, "source_language": source_language, "target_language": target_language})
    return response

