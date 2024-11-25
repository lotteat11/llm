import streamlit as st
from transformers import pipeline
import torch

model_id = "meta-llama/llama-3.2-1B"
token = "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"


from transformers import pipeline

pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B")



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
