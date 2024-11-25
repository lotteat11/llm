from huggingface_hub import InferenceApi
from huggingface_hub import InferenceApi

model_id = "EleutherAI/gpt-neo-2.7B"  # Replace with a suitable model
api_token="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"
inference = InferenceApi(repo_id=model_id, token=api_token)

def main():
    st.title("Hugging Face Inference API App")
    st.write("Generate text using Hugging Face's Inference API.")

    user_input = st.text_area(
        "Enter your prompt:",
        placeholder="Once upon a time...",
        height=150,
    )

    if st.button("Generate Text"):
        if user_input.strip():
            with st.spinner("Generating response..."):
                try:
                    # Directly use the model's default behavior
                    response = inference(inputs=user_input)
                    st.success("Response generated!")
                    st.subheader("Generated Text")
                    st.write(response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()

