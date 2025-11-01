import json
import os
import re
import pandas as pd

# Ground truth stats
ground_truth = {
    "Player A": {"goals": 25, "assists": 10, "turnovers": 5},
    "Player B": {"goals": 18, "assists": 15, "turnovers": 3},
    "Player C": {"goals": 12, "assists": 5, "turnovers": 8}
}

RESULTS_DIR = "results"
OUTPUT_DIR = "analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Pattern matcher to check hallucinations
def validate_response(text):
    hallucinations = []
    for player, stats in ground_truth.items():
        if player not in text:
            continue
        for stat, true_val in stats.items():
            pattern = rf"{player}.*?{stat}.*?(\d+)"
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    val = int(match.group(1))
                    if abs(val - true_val) > 2:  # Tolerance of ±2
                        hallucinations.append((player, stat, val, true_val))
                except:
                    continue
    return hallucinations

# Collect and validate
report = []

for model_dir in os.listdir(RESULTS_DIR):
    model_path = os.path.join(RESULTS_DIR, model_dir)
    if not os.path.isdir(model_path):
        continue

    for file in os.listdir(model_path):
        if file.endswith(".json"):
            with open(os.path.join(model_path, file), "r") as f:
                try:
                    data = json.load(f)
                    for item in data:
                        hallucinations = validate_response(item["response"])
                        report.append({
                            "model": item.get("model", model_dir),
                            "file": file,
                            "condition": item["condition"],
                            "hallucination_count": len(hallucinations),
                            "hallucinated_details": hallucinations
                        })
                except Exception as e:
                    print(f"⚠️ Skipping {file}: {e}")

# Save validation results
df = pd.DataFrame(report)
df.to_csv(f"{OUTPUT_DIR}/validation_report.csv", index=False)

print("✅ Validation complete. Report saved to /analysis/validation_report.csv")
