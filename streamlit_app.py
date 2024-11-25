import streamlit as st
from transformers import pipeline
from PIL import Image

model_id = "mistralai/Mistral-7B-Instruct"
pipe = pipeline("text-generation", model=model_id)

def main():
    st.title("Mistral-Powered Text Generation")

    user_input = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if user_input:
            with st.spinner("Generating text..."):
                response = pipe(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
                st.write(response)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
