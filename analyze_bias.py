import json
import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

analyzer = SentimentIntensityAnalyzer()

RESULTS_DIR = "results"
OUTPUT_DIR = "analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

all_data = []

# Recursively traverse all model subfolders in /results
for model_folder in os.listdir(RESULTS_DIR):
    model_path = os.path.join(RESULTS_DIR, model_folder)
    if not os.path.isdir(model_path):
        continue

    for filename in os.listdir(model_path):
        if filename.endswith(".json"):
            with open(os.path.join(model_path, filename), "r") as f:
                try:
                    data = json.load(f)
                    for entry in data:
                        sentiment = analyzer.polarity_scores(entry["response"])
                        all_data.append({
                            "model": entry.get("model", model_folder),
                            "file": filename,
                            "condition": entry["condition"],
                            "sentiment": sentiment["compound"],
                            "text": entry["response"]
                        })
                except Exception as e:
                    print(f"⚠️ Error parsing {filename}: {e}")

# Convert to DataFrame
df = pd.DataFrame(all_data)
df.to_csv(f"{OUTPUT_DIR}/sentiment_results.csv", index=False)

# Grouped boxplot: Sentiment by model and condition
plt.figure(figsize=(12, 7))
df["group"] = df["model"] + " | " + df["condition"]
df.boxplot(column="sentiment", by="group", grid=False, rot=45)
plt.title("Sentiment Distribution by Model and Prompt Condition")
plt.suptitle("")
plt.xlabel("Model | Condition")
plt.ylabel("Compound Sentiment Score")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/sentiment_plot.png")

print("✅ Sentiment analysis complete. Results saved in /analysis.")
