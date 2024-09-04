import streamlit as st
from utils import *

def front_end():
    st.header("Tokenizer Comparator 🧭 ")
    container = st.container(border=True)


    with st.form(key="form"):
        input=st.text_area("Your Input")
        
        col1, col2 = st.columns(2)
        left_container = col1.container(border=True)
        right_container = col2.container(border=True)
        submit_button = st.form_submit_button(label="Generate",use_container_width=True,type="primary")
        with left_container:
            st.write("Tokenizer 1")
            model_1 = st.selectbox("Select Tokenizer", ["abdeljalilELmajjodi/darija-ary-tokenizer", "abdeljalilELmajjodi/darija-ary-tokenizer_v33k","core42/jais-13b"],key="model_1")
            use_tokenizer_id=st.checkbox("Use tokenizer_id",key="use_tokenizer1_id")
            tokenizer_id=st.text_input("tokenizer_id",key="tokenizer1_id")
            if submit_button:
                result_container = st.container(border=True)
                if use_tokenizer_id:
                    tokenizer = get_tokenizer(tokenizer_id)
                else:
                    tokenizer = get_tokenizer(model_1)
                with result_container:
                    result=get_tokenization(tokenizer,input)
                    st.write(f"Tokenizer size: {get_vocab_size(tokenizer)}")
                    tokens_count = len(result)
                    tokens_ratio = tokens_count / len(input) if len(input) > 0 else 0
                    st.write(f"Tokens: {tokens_count}")
                    st.write(f"Tokens/Character Ratio: {tokens_ratio:.4f}")
                    tokens_html = ' '.join([f'<span style="background-color: #e6f3ff; padding: 2px 5px; margin-right: 5px; border-radius: 3px;">{token}</span>' for token in result])
                    st.markdown(f'<div style="line-height: 2.5;">{tokens_html}</div>', unsafe_allow_html=True)




        with right_container:
            st.write("Tokenizer 2")
            model_2 = st.selectbox("Select Tokenizer", ["abdeljalilELmajjodi/darija-ary-tokenizer_v33k","Xenova/gpt-4o"],key="model_2")
            use_tokenizer_id=st.checkbox("Use tokenizer_id",key="use_tokenizer2_id")
            tokenizer_id=st.text_input("tokenizer_id",key="tokenizer2_id")
            if submit_button:
                result_container = st.container(border=True)
                if use_tokenizer_id:
                    tokenizer = get_tokenizer(tokenizer_id)
                else:
                    tokenizer = get_tokenizer(model_2)
                with result_container:
                    result2=get_tokenization(tokenizer,input)
                    st.write(f"Tokenizer size: {get_vocab_size(tokenizer)}")
                    tokens_count = len(result2)
                    tokens_ratio = tokens_count / len(input) if len(input) > 0 else 0
                    st.write(f"Tokens: {tokens_count}")
                    st.write(f"Tokens/Character Ratio: {tokens_ratio:.4f}")
                    tokens_html = ' '.join([f'<span style="background-color: #fa87b5; padding: 2px 5px; margin-right: 5px; border-radius: 3px;">{token}</span>' for token in result2])
                    st.markdown(f'<div style="line-height: 2.5;">{tokens_html}</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    front_end()