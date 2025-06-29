# app.py
import streamlit as st
from crawler import get_internal_links, is_valid_url
from extractor import extract_clean_content
from parser import parse_modules
from output_format import format_output
import json

st.set_page_config(page_title="Pulse-AI Module Extractor", layout="wide")
st.title(" Pulse-AI Module Extraction AI Agent")
st.markdown("Extract modules and submodules from help documentation URLs using AI-powered summarization.")

#  User Input
urls = st.text_area("Enter help documentation URLs (comma-separated)", "", height=150)
run_button = st.button(" Extract Modules")

if run_button:
    url_list = [u.strip() for u in urls.split(',') if u.strip()]
    all_outputs = []

    if not url_list:
        st.warning("Please enter at least one valid URL.")
    else:
        for url in url_list:
            if not is_valid_url(url):
                st.warning(f" Invalid URL: {url}")
                continue

            with st.spinner(f"🔍 Crawling: {url}"):
                links = get_internal_links(url, max_depth=1)
                st.success(f" Found {len(links)} relevant internal links.")

            all_blocks = []
            for i, link in enumerate(links):
                with st.spinner(f" Extracting content from page {i+1}/{len(links)}"):
                    blocks = extract_clean_content(link)
                    all_blocks.extend(blocks)

            if not all_blocks:
                st.warning(f"No usable content found at {url}")
                continue

            with st.spinner(" Inferring modules and summarizing using LLM..."):
                modules = parse_modules(all_blocks)
                output_json = format_output(modules)
                all_outputs.extend(output_json)

        if all_outputs:
            st.subheader(" Extracted Module Hierarchy")
            st.json(all_outputs)
        else:
            st.error(" No structured modules could be generated.")
