import openai
import json
import os
import time
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
os.makedirs("results", exist_ok=True)

MODELS = ["gpt-4", "gpt-3.5-turbo", "gpt-4o"]
TEMPERATURE = 0.7
N_SAMPLES = 3

# Create output directory
os.makedirs("results", exist_ok=True)

# Set your OpenAI key via environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai_model(model, prompt):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=TEMPERATURE
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"

def run_experiments():
    for model in MODELS:
        print(f"\n🚀 Running experiments with model: {model}")
        model_safe_name = model.replace("-", "_")
        model_dir = f"results/{model_safe_name}"
        os.makedirs(model_dir, exist_ok=True)

        for filename in os.listdir("prompts"):
            with open(f"prompts/{filename}", "r") as f:
                prompt_set = json.load(f)

            results = []
            for condition, prompt in prompt_set.items():
                for i in range(N_SAMPLES):
                    output = query_openai_model(model, prompt)
                    results.append({
                        "timestamp": datetime.now().isoformat(),
                        "model": model,
                        "temperature": TEMPERATURE,
                        "prompt": prompt,
                        "response": output,
                        "condition": condition,
                        "sample_index": i
                    })
                    time.sleep(1)

            output_path = os.path.join(model_dir, filename.replace(".json", "_results.json"))
            with open(output_path, "w") as out:
                json.dump(results, out, indent=2)
            print(f"✅ Saved: {output_path}")

    print("\n🏁 All model experiments completed.")

if __name__ == "__main__":
    run_experiments()