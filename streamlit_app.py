import streamlit as st
from huggingface_hub import InferenceApi

# Hugging Face Token
API_TOKEN = "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"

# Initialize Hugging Face API
api_token = API_TOKEN # Replace with your Hugging Face token
model_id = "EleutherAI/gpt-neo-2.7B"  # Replace with your chosen model
inference = InferenceApi(repo_id=model_id, token=api_token)

# Streamlit App
def main():
    st.title("🧠 Hugging Face Inference API App")
    st.write("Generate text using Hugging Face's Inference API.")

    # User input for the model
    user_input = st.text_area(
        "Enter your query/prompt:",
        placeholder="Once upon a time in a faraway land,",
        height=150,
    )

    # Button to trigger inference
    if st.button("Generate Text"):
        if user_input.strip():
            with st.spinner("Generating response..."):
                try:
                    # Query the Hugging Face model
                    response = inference(inputs=user_input)
                    st.success("Response generated!")
                    
                    # Display the result
                    st.subheader("Generated Text")
                    st.write(response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt to generate text.")

    # Sidebar for model info
    with st.sidebar:
        st.header("Model Info")
        st.write(f"**Model ID:** {model_id}")
        st.write("**Description:** A text generation model from EleutherAI.")
        st.markdown(
            """
            - **Use cases:** Story generation, text completion, etc.
            - **Limitations:** May produce biased or nonsensical outputs.
            """
        )

# Run the app
if __name__ == "__main__":
    main()

