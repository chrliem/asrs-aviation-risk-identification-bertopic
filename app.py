import streamlit as st
from bertopic import BERTopic
from huggingface_hub import snapshot_download

st.set_page_config(page_title="Aviation Risk Dashboard", layout="wide")

@st.cache_resource
def load_model():
    repo_id = "chrliem/asrs-aviation-risk-topics-bertopic"
    model_path = snapshot_download(repo_id=repo_id)
    return BERTopic.load(model_path)

topic_model = load_model()

st.title("Aviation Risk Factor - Topic Modeling Dashboard")

user_input = st.text_area("Enter aviation incident report narrative here:", height=200)

if st.button("Analyze Topic"):
    if user_input:
        topics, _ = topic_model.transform([user_input])
        topic_info = topic_model.get_topic_info(topics[0])
        st.success(f"Detected Topic: {topic_info['Name'].values[0]}")
        keywords = topic_model.get_topic(topics[0])
        st.write([word for word, score in keywords])
    else:
        st.warning("Please enter text first.")
