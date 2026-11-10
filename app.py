import streamlit as st
import pandas as pd
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter

st.set_page_config(page_title="AI Customer Feedback Dashboard", page_icon="📊", layout="wide")
st.title("📊 AI Customer Feedback Analysis Dashboard")
st.caption("Turn customer comments into sentiment insights and actionable business decisions.")

analyzer = SentimentIntensityAnalyzer()

@st.cache_data
def load_sample():
    return pd.read_csv("data/sample_feedback.csv")

def analyse(text):
    score = analyzer.polarity_scores(str(text))["compound"]
    label = "Positive" if score >= 0.05 else ("Negative" if score <= -0.05 else "Neutral")
    return pd.Series([score, label])

uploaded = st.file_uploader("Upload feedback CSV (must contain a 'feedback' column)", type=["csv"])
try:
    df = pd.read_csv(uploaded) if uploaded else load_sample()
except Exception as e:
    st.error(f"Could not read the CSV: {e}")
    st.stop()

if "feedback" not in df.columns:
    st.error("The CSV needs a column named 'feedback'.")
    st.stop()

if "date" not in df.columns:
    df["date"] = pd.Timestamp.today().normalize()
df["date"] = pd.to_datetime(df["date"], errors="coerce")
if "product" not in df.columns:
    df["product"] = "All Products"
if "customer_id" not in df.columns:
    df["customer_id"] = [f"C{i+1:03d}" for i in range(len(df))]

df[["sentiment_score", "sentiment"]] = df["feedback"].fillna("").apply(analyse)
df["date_label"] = df["date"].dt.strftime("%Y-%m-%d")

st.sidebar.header("Filters")
products = ["All"] + sorted(df["product"].dropna().astype(str).unique().tolist())
selected_product = st.sidebar.selectbox("Product", products)
sentiments = ["All", "Positive", "Neutral", "Negative"]
selected_sentiment = st.sidebar.selectbox("Sentiment", sentiments)

filtered = df.copy()
if selected_product != "All":
    filtered = filtered[filtered["product"].astype(str) == selected_product]
if selected_sentiment != "All":
    filtered = filtered[filtered["sentiment"] == selected_sentiment]

total = len(filtered)
positive = int((filtered["sentiment"] == "Positive").sum())
negative = int((filtered["sentiment"] == "Negative").sum())
neutral = int((filtered["sentiment"] == "Neutral").sum())
positive_rate = (positive / total * 100) if total else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total feedback", f"{total:,}")
c2.metric("Positive feedback", f"{positive:,}")
c3.metric("Negative feedback", f"{negative:,}")
c4.metric("Positive rate", f"{positive_rate:.1f}%")

left, right = st.columns(2)
with left:
    st.subheader("Sentiment distribution")
    if total:
        counts = filtered["sentiment"].value_counts().rename_axis("Sentiment").reset_index(name="Count")
        st.plotly_chart(px.pie(counts, names="Sentiment", values="Count", hole=0.45), use_container_width=True)
    else:
        st.info("No feedback matches these filters.")
with right:
    st.subheader("Feedback over time")
    dated = filtered.dropna(subset=["date"]).groupby([pd.Grouper(key="date", freq="D"), "sentiment"]).size().reset_index(name="Count")
    if not dated.empty:
        st.plotly_chart(px.line(dated, x="date", y="Count", color="sentiment", markers=True), use_container_width=True)
    else:
        st.info("No valid dates available.")

st.subheader("Product sentiment comparison")
if not filtered.empty:
    product_summary = filtered.groupby(["product", "sentiment"]).size().reset_index(name="Count")
    st.plotly_chart(px.bar(product_summary, x="product", y="Count", color="sentiment", barmode="group"), use_container_width=True)

st.subheader("AI-generated insight summary")
if total:
    if positive_rate >= 70:
        st.success("Overall feedback is strongly positive. Maintain the features and service customers appreciate.")
    elif negative / total >= 0.35:
        st.warning("A high share of feedback is negative. Prioritise issue investigation and customer follow-up.")
    else:
        st.info("Feedback is mixed. Review negative comments and monitor neutral feedback for improvement opportunities.")
    negative_comments = filtered.loc[filtered["sentiment"] == "Negative", "feedback"].dropna().astype(str).head(5)
    if len(negative_comments):
        st.markdown("**Recent negative comments to review**")
        for comment in negative_comments:
            st.write("• " + comment)
else:
    st.info("Upload or select feedback to generate insights.")

st.subheader("Feedback records")
display_cols = [c for c in ["date", "customer_id", "product", "feedback", "sentiment", "sentiment_score"] if c in filtered.columns]
st.dataframe(filtered[display_cols], use_container_width=True, hide_index=True)

csv_bytes = filtered.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download analysed feedback CSV", csv_bytes, "analysed_feedback.csv", "text/csv")
st.caption("Note: Sentiment is estimated using VADER, a rule-based NLP sentiment model. Review important decisions with human judgement.")
