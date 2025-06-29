# llm_summarizer.py
from transformers import pipeline

# Load once
summarizer = pipeline("summarization", model="google/flan-t5-small", tokenizer="google/flan-t5-small")


def summarize_text(text, max_tokens=150):
    if len(text) < 30:
        return text
    try:
        summary = summarizer(text, max_length=max_tokens, min_length=20, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"LLM Summarization error: {e}")
        return text
    

