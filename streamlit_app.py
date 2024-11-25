import streamlit as st
from huggingface_hub import InferenceApi

# Hugging Face Token
API_TOKEN = "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"

# Initialize the Inference API
inference = InferenceApi(repo_id="EleutherAI/gpt-neo-2.7B", token=API_TOKEN)  # Replace "gpt2" with your model

def query_huggingface(model_input):
    """
    Query Hugging Face API with input and return the output.
    """
    try:
        response = inference(inputs=model_input)
        return response
    except Exception as e:
        return f"Error: {e}"

# Streamlit App
def main():
    st.title("Hugging Face Inference API Demo")
    
    st.write(
        "This app demonstrates how to use Hugging Face's Inference API to generate text responses."
    )
    
    # User input
    user_input = st.text_area(
        "Enter your query:",
        placeholder="Type something here...",
        height=150,
    )
    
    if st.button("Generate Response"):
        if user_input:
            with st.spinner("Processing..."):
                response = query_huggingface(user_input)
            st.subheader("Response")
            st.write(response)
        else:
            st.warning("Please enter a query!")

    # Footer
    st.markdown("---")
    st.markdown(
        "**Powered by Hugging Face Inference API**"
    )

if __name__ == "__main__":
    main()
