import streamlit as st
from scrape import (
    split_dom_content,
    clean_body_content,
    extract_body_content,
    dynamic_content
)
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter the Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website...")

    dynamic_html = dynamic_content(url)
    body_content = extract_body_content(dynamic_html)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM content", cleaned_content, height=300)
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what information you're interested in: ")

    if st.button("See content"):
        if parse_description:
            st.write("Extracting content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)