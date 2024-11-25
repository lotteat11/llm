import streamlit as st
from huggingface_hub import InferenceApi

# Hugging Face Token
API_TOKEN = "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"

# Initialize the Inference API
inference = InferenceApi(repo_id="EleutherAI/gpt-neo-2.7B", token=API_TOKEN)  # Replace "gpt2" with your model
inference = InferenceApi(repo_id="EleutherAI/gpt-neo-2.7B", token=API_TOKEN)

def query_huggingface(model_input):
    try:
        response = inference(inputs=model_input)  # No task override
        return response
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("Hugging Face API Demo")

    query = st.text_area("Enter your prompt:")
    if st.button("Generate"):
        if query:
            with st.spinner("Generating..."):
                result = query_huggingface(query)
            st.write("**Response:**")
            st.write(result)
        else:
            st.warning("Please enter a prompt!")

if __name__ == "__main__":
    main()
