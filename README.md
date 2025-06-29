# Pulse-AI Module Extraction AI Agent

An AI-powered Streamlit application that extracts structured module and submodule information from documentation-based help websites using lightweight LLM summarization.

---

##  Objective

This tool is built to **automatically crawl**, **clean**, and **structure** documentation content into a machine-readable format like:

```json
{
  "module": "Account Settings",
  "Description": "Manages user credentials, privacy, and preferences.",
  "Submodules": {
    "Change Password": "Steps to update account password.",
    "Deactivate Account": "Guide to temporarily disable your profile."
  }
}
````

It is designed to help product teams, technical writers, and AI agents understand and organize documentation faster.

---

## Features

*  Accepts one or more documentation URLs
*  Recursively crawls all internal links
*  Cleans content by removing menus, footers, and scripts
*  Extracts module and submodule hierarchy
*  Uses LLM (Flan-T5) to generate clean summaries
*  JSON output ready for downstream use
*  LLM Toggle: Summarization On/Off for faster performance

---

##  Installation

### 1️ Clone the Repository

```bash
git clone <your-repo-url>
cd pulse_ai_module_extractor
```

### 2️ Create a Virtual Environment (Name: `Assignment`)

```bash
python -m venv Assignment
```

### 3️ Activate the Environment

Windows:

  bash
  Assignment\Scripts\activate
  


### 4️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the App

```bash
streamlit run app.py
```

---

##  Project Structure

```
pulse_ai_module_extractor/

 app.py                 # Streamlit interface
 crawler.py             # URL crawler for internal links
 extractor.py           # Content cleaner and parser
 parser.py              # Logic to identify modules/submodules
 output_format.py       # Structure final JSON (with LLM support)
 llm_summarizer.py      # Lightweight LLM summarization
 requirements.txt       # Python dependencies
 README.md              # This file
```

---

##  Tested URLs

* [https://help.zluri.com/](https://help.zluri.com/)
* [https://wordpress.org/documentation/](https://wordpress.org/documentation/)
* [https://support.neo.space/hc/en-us](https://support.neo.space/hc/en-us)
* [https://www.chargebee.com/docs/2.0/](https://www.chargebee.com/docs/2.0/)

---

##  Demo Video

((https://drive.google.com/drive/folders/1ZTk6lr2-BH0kXFZ_TjIrKjMunem6iu7Z?usp=sharing))*

---

##  Technologies Used

*  Python 3.9+
*  BeautifulSoup + Requests
*  Streamlit
*  Hugging Face Transformers (`flan-t5-small`)
*  Summarization via LLM
*  Runs on CPU (No GPU Required)

---

##  Limitations

* Works best with well-structured HTML-based help sites
* LLM summarization may be slower on CPU — toggle available
* Doesn't yet support PDF-based documentation

---

##  Future Improvements

* Add semantic grouping via embeddings (e.g. sentence-transformers)
* Add confidence scores per module
* Add caching, Docker container, and REST API endpoint
* Improve parser with heading level-based weights

---


