import streamlit as st
from transformers import AutoTokenizer

def front_end():
    if "button_1" not in st.session_state:
        st.session_state.button_1 = False
    container = st.container(border=True)
    with container:
        input=st.text_input("Your Input")
        col1, col2 = st.columns(2)
        left_container = col1.container(border=True)
        right_container = col2.container(border=True)
        with left_container:
            st.write("Tokenizer 1")
            model_1 = st.selectbox("Select Tokenizer", ["Option 1", "Option 2", "Other"],key="model_1")
            if model_1 == "Other":
                st.text_input("tokenizer_id",key="tokenizer1_id")
            if st.session_state.button_1 == True:
                result_container = st.container(border=True)
                with result_container:
                    st.write(f"Tokenizer 1: {model_1}")
                    st.write(f"Tokenizer 1: {input}")


        with right_container:
            st.write("Tokenizer 2")
            model_2 = st.selectbox("Select Tokenizer", ["Option 1", "Option 2", "Other"],key="model_2")
            if model_2 == "Other":
                st.text_input("tokenizer_id",key="tokenizer2_id")
            if st.session_state.button_1 == True:
                result_container = st.container(border=True)
                with result_container:
                    st.write("Tokenizer 1")
        button_1 = st.button("Generate")
        if button_1:
            st.session_state.button_1 = True


if __name__ == "__main__":
    front_end()