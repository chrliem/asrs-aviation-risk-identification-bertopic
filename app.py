import streamlit as st
from bertopic import BERTopic
from huggingface_hub import snapshot_download
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Aviation Risk Identification", layout="wide")

@st.cache_resource
def load_model():
    model_dir = snapshot_download(repo_id="chrliem/asrs-aviation-risk-topics-bertopic")
    return BERTopic.load(model_dir)

try:
    topic_model = load_model()
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

st.sidebar.title("About")
st.sidebar.markdown("**Author:** Christian Darma Setiawan")
st.sidebar.markdown("---")
st.sidebar.markdown("""
The increasing volume of aviation incident narratives presents both an opportunity and a challenge for safety analysis. This study introduces a dynamic topic modeling framework based on BERTopic to automatically identify and trace aviation safety risk factors from 57,292 reports in NASA’s Aviation Safety Reporting System (2013–2023). 

The framework integrates transformer-based embeddings, dimensionality reduction (UMAP), and density-based clustering (HDBSCAN) to discover coherent topics without predefined parameters. Topic representations were refined through KeyBERTInspired and Maximal Marginal Relevance (MMR), while labeling was supported by large language models and validated against ICAO taxonomies. 

The best-performing model (M5) achieved the highest coherence (c_v = 0.646) and diversity (0.829), generating seventeen distinct and interpretable risk factors encompassing technical, operational, and behavioral dimensions of aviation safety.
""")

st.sidebar.markdown("---")
st.sidebar.caption("Disclaimer: This tool is for research and demonstration purposes only. It is not an official aviation safety management system and should not be used for operational decision-making.")

st.title("Aviation Risk Factor Identification - Topic Modeling Approach using BERTopic")

user_input = st.text_area("Enter aviation incident report narrative here:", height=200)

if st.button("Analyze Report"):
    if user_input:
        topics, probs = topic_model.transform([user_input])
        topic_info = topic_model.get_topic_info(topics[0])
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("Primary Risk Factor", topic_info['CustomName'].values[0])
        with col2:
            conf = probs[0] if probs is not None else 0
            st.metric("Confidence Score", f"{conf*100:.1f}%")
    else:
        st.warning("Please enter text first.")

with st.expander("Research Methodology"):
    st.image("method diagram 600dpi.png", caption="Research Methodology Framework")

with st.expander("Research Results"):
    st.image("doctopics_600dpi.png", caption="Document and Topic Distribution")
    st.image("stacked topic distribution.png", caption="Topic Distribution Over Time")
    st.image("topic intensity.png", caption="Topic Intensity Evolution")
