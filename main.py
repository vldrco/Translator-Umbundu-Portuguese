import streamlit as st
from app import translate

st.title('Tradutor Português - Umbundo')

api_key = st.sidebar.text_input('Chave OpenAI', type='password')
st.sidebar.page_link("pages/translations.py", label="Traduções disponíveis", icon="📄")

with st.form('my_form'):
    user_text = st.text_area("Insira uma palavra para traduzir")
    submit_text = st.form_submit_button('Submeter')

    if submit_text:
        if user_text == "":
            st.warning('Por favor insira um texto para traduzir!', icon='⚠')
        else:
            response = translate(user_text, api_key)
            st.info(response)

st.caption("A IA pode cometer erros, por favor verifique a tradução após o uso da ferramenta.")
