import streamlit as st
from app import translate

st.title('Dicionario tradutor Umbundo - Português')

with st.form('my_form'):
    user_text = st.text_area("Insira uma palavra para traduzir")
    source_language = st.selectbox("Linguagem fonte", ["Portuguese", "Umbundu"])
    target_language = st.selectbox("Linguagem destino", ["Portuguese", "Umbundu"])
    submit_text = st.form_submit_button('Submeter')
    
    if submit_text:
        if source_language == target_language:
            st.warning('A linguagem fonte e a linguagem destino devem ser diferentes!', icon='⚠')
        elif user_text == "":
            st.warning('Por favor insira um texto para traduzir!', icon='⚠')
        elif source_language == "":
            st.warning('Por favor insira uma linguagem fonte!', icon='⚠')
        elif target_language == "":
            st.warning('Por favor insira uma linguagem destino!', icon='⚠')
        else:
            response = translate(user_text, source_language, target_language)
            st.info(response)