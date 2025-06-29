from llm_summarizer import summarize_text

def format_output(modules_dict):
    output = []
    for module, subtexts in modules_dict.items():
        all_text = " ".join(subtexts)
        summary = summarize_text(all_text)  # NEW

        submodules = {}
        for i, item in enumerate(subtexts):
            submodules[f"Submodule_{i+1}"] = item  # Use raw text


        output.append({
            "module": module,
            "Description": summary,
            "Submodules": submodules
        })
    return output


"""if __name__ == "__main__":
    sample_input = {
        "Account Settings": [
            "Change username instructions",
            "Delete account steps"
        ],
        "Reels": [
            "Create a reel",
            "Share a reel"
        ]
    }

    result = format_output(sample_input)
    import json
    print(json.dumps(result, indent=2))"""