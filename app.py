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

