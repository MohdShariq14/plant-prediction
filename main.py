import streamlit as st
import requests

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Leaf Disease Detection",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= PREMIUM CSS =================
st.markdown("""
<style>

/* GLOBAL BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #000000, #0b2b2e, #1b4332);
    color: #e0f7fa;
}

/* HEADINGS */
h1, h2, h3, h4, h5, h6 {
    color: #e3f2fd !important;
    letter-spacing: 0.5px;
}

/* RESULT CARD */
.result-card {
    background: rgba(18, 18, 18, 0.95);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 8px 28px rgba(0,255,180,0.15);
    padding: 2.5em 2em;
    margin: 1.5em 0;
    transition: all 0.35s ease;
}
.result-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0,255,180,0.35);
}

/* TITLES */
.disease-title {
    color: #69f0ae;
    font-size: 2.2em;
    font-weight: 700;
    text-shadow: 0 0 12px rgba(105,240,174,0.3);
}
.section-title {
    color: #ffeb3b;
    font-size: 1.2em;
    font-weight: 600;
}

/* BADGES */
.info-badge {
    display: inline-block;
    background: rgba(255,235,59,0.12);
    color: #ffeb3b;
    border: 1px solid rgba(255,235,59,0.3);
    border-radius: 10px;
    padding: 0.35em 0.9em;
    margin: 0.3em 0.3em 0.3em 0;
}

/* LISTS */
.symptom-list li,
.cause-list li,
.treatment-list li {
    color: #e0f2f1;
    margin-bottom: 6px;
}

/* FILE UPLOADER */
div[data-testid="stFileUploader"] {
    background: #000000 !important;
    border-radius: 14px;
    padding: 18px;
    border: 1px solid rgba(255,255,255,0.15);
}
div[data-testid="stFileUploader"] label,
div[data-testid="stFileUploader"] span {
    color: #e0f7fa !important;
}
div[data-testid="stFileUploader"] button {
    background: linear-gradient(135deg, #ffeb3b, #fdd835);
    color: #1a1a1a;
    border-radius: 10px;
    font-weight: 600;
}
div[data-testid="stFileUploader"] button:hover {
    background: linear-gradient(135deg, #69f0ae, #00e676);
    color: #003d1f;
}

/* DETECT BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #ffeb3b, #fdd835);
    color: #1a1a1a;
    border-radius: 14px;
    font-weight: 700;
    padding: 0.7em 1.6em;
    box-shadow: 0 8px 26px rgba(255,235,59,0.45);
    animation: pulseGlow 2.2s infinite;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #69f0ae, #00e676);
    color: #003d1f;
    transform: translateY(-3px);
}

@keyframes pulseGlow {
    0% { box-shadow: 0 0 12px rgba(255,235,59,0.35); }
    50% { box-shadow: 0 0 26px rgba(255,235,59,0.65); }
    100% { box-shadow: 0 0 12px rgba(255,235,59,0.35); }
}

.timestamp {
    color: #9e9e9e;
    text-align: right;
    font-size: 0.9em;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div style='text-align:center; margin-top:1em;'>
    <span style='font-size:2.5em;'>🌿</span>
    <h1>Leaf Disease Detection</h1>
    <p>Upload a leaf image to detect diseases and get expert recommendations.</p>
</div>
""", unsafe_allow_html=True)

# ================= API =================
api_url = "https://leaf-diseases-detect.vercel.app"

# ================= LAYOUT =================
col1, col2 = st.columns([1, 2])

with col1:
    uploaded_file = st.file_uploader(
        "Upload Leaf Image",
        type=["jpg", "jpeg", "png"]
    )
    if uploaded_file:
        st.image(uploaded_file, caption="Preview")

with col2:
    if uploaded_file:
        if st.button("🔍 Detect Disease", use_container_width=True):

            placeholder = st.empty()

            with placeholder.container():
                with st.spinner("Analyzing image and contacting API..."):
                    try:
                        files = {
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                uploaded_file.type
                            )
                        }

                        response = requests.post(
                            f"{api_url}/disease-detection-file",
                            files=files,
                            timeout=60
                        )

                        if response.status_code == 200:
                            result = response.json()

                            st.markdown("<div class='result-card'>", unsafe_allow_html=True)

                            if result.get("disease_detected"):
                                st.markdown(
                                    f"<div class='disease-title'>🦠 {result.get('disease_name')}</div>",
                                    unsafe_allow_html=True
                                )
                                for key in ["disease_type", "severity", "confidence"]:
                                    st.markdown(
                                        f"<span class='info-badge'>{key.replace('_',' ').title()}: {result.get(key)}</span>",
                                        unsafe_allow_html=True
                                    )

                            else:
                                st.markdown(
                                    "<div class='disease-title'>✅ Healthy Leaf</div>",
                                    unsafe_allow_html=True
                                )

                            st.markdown(
                                f"<div class='timestamp'>🕒 {result.get('analysis_timestamp')}</div>",
                                unsafe_allow_html=True
                            )
                            st.markdown("</div>", unsafe_allow_html=True)

                        else:
                            st.error(f"API Error: {response.status_code}")
                            st.write(response.text)

                    except Exception as e:
                        st.error(f"Error: {str(e)}")
