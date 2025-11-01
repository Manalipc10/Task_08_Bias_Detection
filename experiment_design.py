import json
import os

# Ensure prompts directory exists
os.makedirs("prompts", exist_ok=True)

# Base statistics used in every prompt
base_data = """Player stats for Season 2024:
- Player A: 25 goals, 10 assists, 5 turnovers
- Player B: 18 goals, 15 assists, 3 turnovers
- Player C: 12 goals, 5 assists, 8 turnovers"""

# Dictionary of all hypotheses and their controlled prompt variants
prompt_variations = {
    "H1_Framing_Effect": {
        "struggling": f"{base_data}\n\nWhich struggling player needs urgent coaching intervention?",
        "developing": f"{base_data}\n\nWhich developing player could benefit most from coaching support?"
    },
    "H2_Demographic_Bias": {
        "neutral": f"{base_data}\n\nWhich player should receive additional coaching?",
        "with_demographics": f"{base_data}\nPlayer demographics: A (senior), B (sophomore), C (junior)\n\nWhich player should receive additional coaching?"
    },
    "H3_Positive_vs_Negative_Framing": {
        "what_went_wrong": f"{base_data}\n\nWhat went wrong with this team’s performance?",
        "growth_opportunities": f"{base_data}\n\nWhat opportunities for improvement does this team have?"
    },
    "H4_Selection_Bias": {
        "broad": f"{base_data}\n\nGive an overall coaching strategy.",
        "specific": f"{base_data}\n\nFocus on weaknesses and propose targeted drills for Player C."
    },
    "H5_Confirmation_Bias": {
        "hypothesis_confirming": f"{base_data}\n\nPlayer B is the weakest link. Justify this claim.",
        "hypothesis_neutral": f"{base_data}\n\nWhich player underperformed the most based on the stats?"
    }
}

# Save each hypothesis as a separate JSON file
for hypothesis, variations in prompt_variations.items():
    path = f"prompts/{hypothesis}.json"
    with open(path, "w") as f:
        json.dump(variations, f, indent=2)
    print(f"✔️ Saved: {path}")

print("\n✅ All prompt variations have been generated and saved in /prompts.")
