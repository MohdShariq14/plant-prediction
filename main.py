import streamlit as st
import requests

# Set Streamlit theme to light and wide mode
st.set_page_config(
    page_title="Leaf Disease Detection",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Enhanced modern CSS
st.markdown("""
<style>

/* ===== GLOBAL BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #000000, #0b2b2e, #1b4332);
    color: #e0f7fa;
}

/* ===== HEADINGS ===== */
h1, h2, h3, h4, h5, h6 {
    color: #e3f2fd !important;
    letter-spacing: 0.5px;
}

/* ===== RESULT CARD ===== */
.result-card {
    background: rgba(18, 18, 18, 0.95);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 8px 28px rgba(0,255,180,0.15);
    padding: 2.5em 2em;
    margin-top: 1.5em;
    margin-bottom: 1.5em;
    transition: all 0.35s ease;
}

.result-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0,255,180,0.35);
}

/* ===== TITLES ===== */
.disease-title {
    color: #69f0ae;
    font-size: 2.2em;
    font-weight: 700;
    margin-bottom: 0.6em;
    text-shadow: 0 0 12px rgba(105,240,174,0.3);
}

.section-title {
    color: #ffeb3b;
    font-size: 1.2em;
    margin-top: 1.2em;
    margin-bottom: 0.4em;
    font-weight: 600;
}

/* ===== BADGES ===== */
.info-badge {
    display: inline-block;
    background: rgba(255,235,59,0.12);
    color: #ffeb3b;
    border: 1px solid rgba(255,235,59,0.3);
    border-radius: 10px;
    padding: 0.35em 0.9em;
    font-size: 0.95em;
    margin-right: 0.5em;
    margin-bottom: 0.4em;
}

/* ===== LISTS ===== */
.symptom-list li,
.cause-list li,
.treatment-list li {
    margin-bottom: 8px;
    color: #e0f2f1;
}

/* ===== FILE UPLOADER ===== */
div[data-testid="stFileUploader"] {
    background: #000000 !important;
    border-radius: 14px;
    padding: 18px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 6px 20px rgba(0,0,0,0.8);
}

/* Upload text */
div[data-testid="stFileUploader"] label,
div[data-testid="stFileUploader"] span {
    color: #e0f7fa !important;
    font-weight: 500;
}

/* Drag & drop area */
div[data-testid="stFileUploader"] section {
    background: rgba(255,255,255,0.04) !important;
    border-radius: 12px;
    border: 1px dashed rgba(255,255,255,0.25);
}

/* Browse files button */
div[data-testid="stFileUploader"] button {
    background: linear-gradient(135deg, #ffeb3b, #fdd835);
    color: #1a1a1a;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 4px 14px rgba(255,235,59,0.45);
    transition: all 0.3s ease;
}

/* Browse hover */
div[data-testid="stFileUploader"] button:hover {
    background: linear-gradient(135deg, #69f0ae, #00e676);
    color: #003d1f;
}


/* ===== PREMIUM BUTTON ===== */
.stButton > button {
    background: linear-gradient(135deg, #ffeb3b, #fdd835);
    color: #1a1a1a;
    border: none;
    border-radius: 14px;
    padding: 0.7em 1.6em;
    font-size: 1.05em;
    font-weight: 700;
    letter-spacing: 0.6px;
    cursor: pointer;
    box-shadow: 0 8px 26px rgba(255,235,59,0.45);
    transition: all 0.35s ease;
    animation: pulseGlow 2.2s infinite;
}

/* Hover = light green */
.stButton > button:hover {
    background: linear-gradient(135deg, #69f0ae, #00e676);
    color: #003d1f;
    box-shadow: 0 10px 34px rgba(0,230,118,0.55);
    transform: translateY(-3px);
}

/* Click */
.stButton > button:active {
    transform: scale(0.97);
}

/* ===== BUTTON TEXT ANIMATION ===== */
@keyframes pulseGlow {
    0% {
        box-shadow: 0 0 12px rgba(255,235,59,0.35);
    }
    50% {
        box-shadow: 0 0 26px rgba(255,235,59,0.65);
    }
    100% {
        box-shadow: 0 0 12px rgba(255,235,59,0.35);
    }
}

/* ===== TIMESTAMP ===== */
.timestamp {
    color: #9e9e9e;
    font-size: 0.9em;
    margin-top: 1.2em;
    text-align: right;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
    <div style='text-align: center; margin-top: 1em;'>
        <span style='font-size:2.5em;'>🌿</span>
        <h1 style='color: #1565c0; margin-bottom:0;'>Leaf Disease Detection</h1>
        <p style='color: #616161; font-size:1.15em;'>Upload a leaf image to detect diseases and get expert recommendations.</p>
    </div>
""", unsafe_allow_html=True)

api_url = "https://leaf-diseases-detect.vercel.app"

col1, col2 = st.columns([1, 2])
with col1:
    uploaded_file = st.file_uploader(
        "Upload Leaf Image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Preview")

with col2:
    if uploaded_file is not None:
        if st.button("🔍 Detect Disease", use_container_width=True):
            result_placeholder = st.empty()
            with result_placeholder.container():
                with st.spinner("Analyzing image and contacting API..."):
                    try:
                        files = {
                    "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
                }
                        response = requests.post(
                    f"{api_url}/disease-detection-file",
                    files=files,
                    timeout=60
                )
                    if response.status_code == 200:
                        result = response.json()

                        # Check if it's an invalid image
                        if result.get("disease_type") == "invalid_image":
                            st.markdown("<div class='result-card'>",
                                        unsafe_allow_html=True)
                            st.markdown(
                                "<div class='disease-title'>⚠️ Invalid Image</div>", unsafe_allow_html=True)
                            st.markdown(
                                "<div style='color: #ff5722; font-size: 1.1em; margin-bottom: 1em;'>Please upload a clear image of a plant leaf for accurate disease detection.</div>", unsafe_allow_html=True)

                            # Show the symptoms (which contain the error message)
                            if result.get("symptoms"):
                                st.markdown(
                                    "<div class='section-title'>Issue</div>", unsafe_allow_html=True)
                                st.markdown("<ul class='symptom-list'>",
                                            unsafe_allow_html=True)
                                for symptom in result.get("symptoms", []):
                                    st.markdown(
                                        f"<li>{symptom}</li>", unsafe_allow_html=True)
                                st.markdown("</ul>", unsafe_allow_html=True)

                            # Show treatment recommendations
                            if result.get("treatment"):
                                st.markdown(
                                    "<div class='section-title'>What to do</div>", unsafe_allow_html=True)
                                st.markdown("<ul class='treatment-list'>",
                                            unsafe_allow_html=True)
                                for treat in result.get("treatment", []):
                                    st.markdown(
                                        f"<li>{treat}</li>", unsafe_allow_html=True)
                                st.markdown("</ul>", unsafe_allow_html=True)

                            st.markdown("</div>", unsafe_allow_html=True)

                        elif result.get("disease_detected"):
                            st.markdown("<div class='result-card'>",
                                        unsafe_allow_html=True)
                            st.markdown(
                                f"<div class='disease-title'>🦠 {result.get('disease_name', 'N/A')}</div>", unsafe_allow_html=True)
                            st.markdown(
                                f"<span class='info-badge'>Type: {result.get('disease_type', 'N/A')}</span>", unsafe_allow_html=True)
                            st.markdown(
                                f"<span class='info-badge'>Severity: {result.get('severity', 'N/A')}</span>", unsafe_allow_html=True)
                            st.markdown(
                                f"<span class='info-badge'>Confidence: {result.get('confidence', 'N/A')}%</span>", unsafe_allow_html=True)
                            st.markdown(
                                "<div class='section-title'>Symptoms</div>", unsafe_allow_html=True)
                            st.markdown("<ul class='symptom-list'>",
                                        unsafe_allow_html=True)
                            for symptom in result.get("symptoms", []):
                                st.markdown(
                                    f"<li>{symptom}</li>", unsafe_allow_html=True)
                            st.markdown("</ul>", unsafe_allow_html=True)
                            st.markdown(
                                "<div class='section-title'>Possible Causes</div>", unsafe_allow_html=True)
                            st.markdown("<ul class='cause-list'>",
                                        unsafe_allow_html=True)
                            for cause in result.get("possible_causes", []):
                                st.markdown(
                                    f"<li>{cause}</li>", unsafe_allow_html=True)
                            st.markdown("</ul>", unsafe_allow_html=True)
                            st.markdown(
                                "<div class='section-title'>Treatment</div>", unsafe_allow_html=True)
                            st.markdown("<ul class='treatment-list'>",
                                        unsafe_allow_html=True)
                            for treat in result.get("treatment", []):
                                st.markdown(
                                    f"<li>{treat}</li>", unsafe_allow_html=True)
                            st.markdown("</ul>", unsafe_allow_html=True)
                            st.markdown(
                                f"<div class='timestamp'>🕒 {result.get('analysis_timestamp', 'N/A')}</div>", unsafe_allow_html=True)
                            st.markdown("</div>", unsafe_allow_html=True)
                        else:
                            # Healthy leaf case
                            st.markdown("<div class='result-card'>",
                                        unsafe_allow_html=True)
                            st.markdown(
                                "<div class='disease-title'>✅ Healthy Leaf</div>", unsafe_allow_html=True)
                            st.markdown(
                                "<div style='color: #4caf50; font-size: 1.1em; margin-bottom: 1em;'>No disease detected in this leaf. The plant appears to be healthy!</div>", unsafe_allow_html=True)
                            st.markdown(
                                f"<span class='info-badge'>Status: {result.get('disease_type', 'healthy')}</span>", unsafe_allow_html=True)
                            st.markdown(
                                f"<span class='info-badge'>Confidence: {result.get('confidence', 'N/A')}%</span>", unsafe_allow_html=True)
                            st.markdown(
                                f"<div class='timestamp'>🕒 {result.get('analysis_timestamp', 'N/A')}</div>", unsafe_allow_html=True)
                            st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.error(f"API Error: {response.status_code}")
                        st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
