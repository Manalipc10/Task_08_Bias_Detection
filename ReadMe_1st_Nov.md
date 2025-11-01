# Bias Detection in LLM-Generated Data Narratives

---

##  Summary

This research investigates whether **Large Language Models (LLMs)** exhibit bias when interpreting identical datasets under different prompt framings. Using synthetic sports statistics for three anonymized players (A, B, and C), we varied prompt wording across five bias categories and compared results from **GPT-4** and **GPT-3.5-turbo** and **GPT-4o**.

The results demonstrate that LLM outputs are **sensitive to linguistic framing and demographic cues**:
- Negative framings (e.g., “struggling”) led to harsher evaluations.
- Inclusion of demographics (e.g., “senior”, “junior”) altered coaching recommendations.
- Hypothesis-priming (“Player B is weakest”) prompted agreement without justification.

While GPT-4 showed more stability, both models exhibited measurable framing and confirmation biases. These findings underscore the need for **bias mitigation in LLM-driven analytics and reporting systems**.

---

## Methodology


### Hypotheses

| ID | Description |
|----|--------------|
| H1 | “Struggling” vs “Developing” framing influences recommendations |
| H2 | Mentioning demographics changes coaching focus |
| H3 | “What went wrong?” vs “What opportunities exist?” shifts tone |
| H4 | Broad vs specific prompts affect which stats are emphasized |
| H5 | Hypothesis-priming reinforces confirmation bias |

### Tools and Models

- **Models:** GPT-4, GPT-3.5-turbo, GPT-4o 
- **Libraries:** `openai`, `pandas`, `matplotlib`, `vaderSentiment`, `re`
- **Scripts:**  
  - `run_experiment.py` – Executes prompts on multiple models  
  - `analyze_bias.py` – Sentiment and tone analysis  
  - `validate_claims.py` – Checks factual consistency  
- **Prompt variations:** stored under `/prompts`

Each prompt pair differed by a single controlled phrase to isolate bias effects.

---

## Results

### 1. Sentiment Analysis

We applied **VADER sentiment scoring** to assess tone across prompt variations.

- **H1 (Framing):** “Struggling” prompts averaged sentiment **–0.31**, while “Developing” averaged **+0.27**.  
- **H3 (Framing):** “What went wrong?” yielded more negative tones than “Growth opportunities”.  

See plots in: `analysis/sentiment_plot.png`  
Detailed results: `analysis/sentiment_results.csv`


---

## Bias Catalogue

| Bias Type | Trigger | Example | Severity |
|------------|----------|----------|----------|
| **Framing Bias** | “Struggling” phrasing | Player C criticized harshly | Moderate |
| **Demographic Bias** | Mentioning seniority | Player A favored for leadership | High |
| **Confirmation Bias** | Hypothesis priming | Model agrees without evidence | Moderate |
| **Selection Bias** | Narrow prompts | Omits non-targeted players | Low |
| **Hallucination Bias** | Misstated stats | “20 goals” instead of 25 | Low–Moderate |

---

## Mitigation Strategies

1. **Prompt Neutralization** – Avoid emotionally loaded terms like “struggling” or “failing.”  
2. **Cross-Model Validation** – Run analyses through multiple LLMs for consistency.  
3. **Grounded Reasoning Prompts** – Instruct models to cite exact statistics in conclusions.  
4. **Post-Processing Filters** – Flag unsupported or fabricated numeric claims.  
5. **User Transparency** – Disclose potential linguistic sensitivity in end-user interfaces.  

---

## Limitations

- The dataset is synthetic and lacks real-world demographic nuance.  
- Limited to three OpenAI models; no results from Claude or Gemini.  
- Randomness (temperature = 0.7) introduces natural output variance.  
- Results may vary if prompts include reasoning chains or multi-turn dialogue.  