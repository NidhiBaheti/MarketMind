from transformers import pipeline

class LocalLLM:
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct-v0.2"):
        self.model_name = model_name
        print(f"🔧 Using Hugging Face-hosted model: {model_name}")
        self.generator = pipeline(
            "text-generation",
            model=self.model_name,
            trust_remote_code=True
        )

    def generate(self, prompt, max_tokens=100):
        output = self.generator(prompt, max_length=max_tokens, num_return_sequences=1, do_sample=True)
        return output[0]["generated_text"].strip().replace(prompt, "").strip()