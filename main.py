import streamlit as st
import requests

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Leaf Disease Detection",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= CSS (AS IT IS) =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #000000, #0b2b2e, #1b4332);
    color: #e0f7fa;
}

h1, h2, h3, h4, h5, h6 {
    color: #e3f2fd !important;
}

.result-card {
    background: rgba(18, 18, 18, 0.95);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 8px 28px rgba(0,255,180,0.15);
    padding: 2.5em 2em;
    margin: 1.5em 0;
}

.disease-title {
    color: #69f0ae;
    font-size: 2.2em;
    font-weight: 700;
}

.section-title {
    color: #ffeb3b;
    font-weight: 600;
}

.info-badge {
    background: rgba(255,235,59,0.12);
    color: #ffeb3b;
    border-radius: 10px;
    padding: 6px 12px;
    margin-right: 6px;
    display: inline-block;
}

.timestamp {
    color: #9e9e9e;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div style='text-align:center;margin-top:1em;'>
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

            # 🔹 THIS IS THE BLACK BOX (NOW WITH CONTENT)
            status_box = st.container()

            with status_box:
                st.markdown("<div class='result-card'>", unsafe_allow_html=True)
                st.markdown("🔄 **Processing image… please wait**")
                
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

                        st.markdown("---")

                        if result.get("disease_detected"):
                            st.markdown(
                                f"<div class='disease-title'>🦠 {result.get('disease_name')}</div>",
                                unsafe_allow_html=True
                            )

                            st.markdown(
                                f"<span class='info-badge'>Type: {result.get('disease_type')}</span>"
                                f"<span class='info-badge'>Severity: {result.get('severity')}</span>"
                                f"<span class='info-badge'>Confidence: {result.get('confidence')}%</span>",
                                unsafe_allow_html=True
                            )

                            st.markdown("<div class='section-title'>Symptoms</div>", unsafe_allow_html=True)
                            for s in result.get("symptoms", []):
                                st.write(f"• {s}")

                            st.markdown("<div class='section-title'>Treatment</div>", unsafe_allow_html=True)
                            for t in result.get("treatment", []):
                                st.write(f"• {t}")

                        else:
                            st.markdown(
                                "<div class='disease-title'>✅ Healthy Leaf</div>",
                                unsafe_allow_html=True
                            )
                            st.success("No disease detected. The plant looks healthy 🌱")

                        st.markdown(
                            f"<div class='timestamp'>🕒 {result.get('analysis_timestamp')}</div>",
                            unsafe_allow_html=True
                        )

                    else:
                        st.error(f"API Error: {response.status_code}")
                        st.write(response.text)

                except Exception as e:
                    st.error(f"Error: {str(e)}")

                st.markdown("</div>", unsafe_allow_html=True)
