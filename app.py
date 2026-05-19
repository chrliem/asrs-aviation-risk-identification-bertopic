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
st.sidebar.markdown("""
This tool implements a topic modeling framework based on research identifying 17 critical risk factors in aviation incident reports. 

The model was trained on 57,292 NASA Aviation Safety Reporting System (ASRS) reports (2013–2023) using Dynamic Trend BERTopic.
""")

st.title("✈️ Aviation Risk Factor Identification - Topic Modeling Approach using BERTopic")

user_input = st.text_area("Enter aviation incident report narrative here:", height=200)

if st.button("Analyze Report"):
    if user_input:
        topics, _ = topic_model.transform([user_input])
        topic_info = topic_model.get_topic_info(topics[0])
        
        st.success(f"Risk Factor: {topic_info['CustomName'].values[0]}")
    else:
        st.warning("Please enter text first.")

with st.expander("Research Methodology"):
    st.image("method diagram 600dpi.png")

with st.expander("Research Results"):
    st.image("doctopics_600dpi.png")
    st.image("stacked topic distribution.png")
    st.image("topic intensity.png")
