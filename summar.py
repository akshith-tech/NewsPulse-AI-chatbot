import streamlit as st
from openai import OpenAI

# --- API CLIENT (Use environment variable in real apps!) ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="ENTER_YOUR_OPENAI_KEY_HERE"
)

# --- PAGE CONFIG ---
st.set_page_config(page_title="📰 NewsPulse AI", layout="centered")

# --- SIMPLE STYLING ---
st.markdown("""
    <style>
    .main {background-color: #0E1117; color: white;}
    textarea {background-color: #1E1E1E !important; color: white !important;}
    .stButton>button {
        background: linear-gradient(90deg, #ff4b4b, #ff7a18);
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("📰 NewsPulse AI")
st.caption("Smart News Summarizer powered by AI")

# --- INPUT ---
article = st.text_area("Paste your news article here 👇", height=250)

# --- FUNCTION ---
def get_summary(text):
    prompt = f"""
    Summarize this news article:

    {text}

    Format:
    SHORT SUMMARY (2 lines)
    KEY POINTS (bullets)
    IMPORTANT FACTS (numbers, names, dates)
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content


# --- BUTTON ---
if st.button("🚀 Analyze Article"):
    if not article.strip():
        st.warning("Please paste an article first.")
    else:
        with st.spinner("Analyzing..."):
            result = get_summary(article)

        st.markdown("### 📊 Result")
        st.markdown(result)

# --- FOOTER ---
st.markdown("---")
st.caption("⚡ Powered by OpenRouter + AI")
