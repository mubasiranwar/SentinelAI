import streamlit as st
import requests
import datetime

API_URL = "http://127.0.0.1:8000/analyze"

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="SentinelAI | Disinformation Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Sidebar (Context & Branding)
# ----------------------------
st.sidebar.title("🛡️ SentinelAI")
st.sidebar.markdown("""
### AI-Based Cyber & Disinformation Intelligence  

SentinelAI detects **coordinated emotional manipulation** and  
**hostile information operations** targeting Pakistan.

**Core Capabilities**
- Sentiment & Emotion Analysis  
- Narrative & Phrase Tracking  
- Coordinated Behavior Detection  
- Explainable Risk Scoring  

**Designed for**
- Cyber Cells  
- Media Houses  
- Election Monitoring  
- Crisis Response
""")

st.sidebar.markdown("---")
st.sidebar.caption(" AI-Based Cyber Security")

# ----------------------------
# Main Header
# ----------------------------
st.markdown("## 🧠 Disinformation Intelligence Dashboard")
st.markdown(
    "Monitoring emotional narratives and coordinated campaigns in real time."
)

st.markdown("---")

# ----------------------------
# Input Section
# ----------------------------
st.markdown("### 📝 Social Media Input")
st.caption("Enter public social media posts related to a topic, crisis, or event.")

posts = []

for i in range(3):
    with st.container():
        col1, col2 = st.columns([4, 2])
        with col1:
            text = st.text_input(
                f"Post {i+1} Content",
                placeholder="",
                key=f"text_{i}"
            )
        with col2:
            timestamp = st.text_input(
                f"Timestamp",
                value=str(datetime.datetime.now()),
                key=f"time_{i}"
            )

        if text.strip():
            posts.append({
                "text": text,
                "timestamp": timestamp
            })

st.markdown("---")

# ----------------------------
# Analysis Trigger
# ----------------------------
analyze_btn = st.button("🔍 Analyze Disinformation Risk", use_container_width=True)

if analyze_btn and posts:
    with st.spinner("Analyzing narratives, emotions, and coordination patterns..."):
        response = requests.post(API_URL, json=posts)

    if response.status_code == 200:
        data = response.json()

        st.success("Analysis Completed Successfully")

        # ----------------------------
        # Risk Summary Section
        # ----------------------------
        st.markdown("## ⚠️ Disinformation Risk Summary")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            label="Overall Risk Score",
            value=data["risk"]["risk_score"]
        )

        col2.metric(
            label="Threat Classification",
            value=data["risk"]["level"]
        )

        col3.metric(
            label="Posts Analyzed",
            value=data["posts_analyzed"]
        )

        st.markdown("---")

        # ----------------------------
        # Intelligence Signals
        # ----------------------------
        st.markdown("## 📊 Detected Intelligence Signals")

        col1, col2 = st.columns(2)

        with col1:
            st.info(f"📈 **Sentiment Spike Detected:** {data['spike_detected']}")

        with col2:
            st.info(
                f"🧩 **Narrative Repetition Score:** {round(data['repetition_score'], 2)}"
            )

        st.caption(
            "High repetition and sudden emotional spikes indicate coordinated activity."
        )

        st.markdown("---")

        # ----------------------------
        # Post-Level Intelligence
        # ----------------------------
        st.markdown("## 🧠 Post-Level Intelligence Analysis")

        for idx, detail in enumerate(data["details"]):
            with st.expander(f"Post {idx+1} — Analysis Details"):
                st.write("**Cleaned Text:**", detail["text"])
                st.write("**Negative Sentiment Probability:**", detail["negative_probability"])
                st.write("**Detected Emotion:**", detail["emotion"])
                st.write("**Emotional Intensity:**", detail["emotional_intensity"])

    else:
        st.error("Unable to connect to SentinelAI backend.")

elif analyze_btn:
    st.warning("Please enter at least one post before analysis.")

else:
    st.info("Enter posts above and click **Analyze Disinformation Risk**.")

st.markdown("---")
st.markdown("## ⚖️ Ethics, Privacy & Responsible AI")

st.info("""
**SentinelAI Ethical Commitments**

• Analyzes only **publicly available text**  
• Does **not collect or store personal identities**  
• Focuses on **narratives and patterns**, not individuals  
• Provides **risk indicators**, not automated decisions  
• All high-risk outputs require **human interpretation**  

This system is designed to **support informed decision-making**, not censorship or surveillance.
""")
