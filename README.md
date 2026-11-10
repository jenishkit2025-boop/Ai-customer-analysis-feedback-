# AI Customer Feedback Analysis Dashboard

A beginner-friendly Python project that analyses customer comments, predicts sentiment, and displays results in an interactive dashboard.

## Features
- Upload a CSV file containing a `feedback` column.
- Automatically classify comments as Positive, Neutral, or Negative.
- Show total feedback, sentiment counts, and positive-feedback rate.
- Visualise sentiment distribution, feedback trends, and product comparisons.
- Display example negative comments for follow-up.
- Download the analysed data as CSV.

## Technology
- Python
- Streamlit (dashboard interface)
- Pandas (data processing)
- Plotly (interactive charts)
- VADER Sentiment (natural-language sentiment analysis)

## Run the project
1. Install Python 3.9 or later.
2. Extract this ZIP and open a terminal in the project folder.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Start the dashboard:
   `streamlit run app.py`
5. Open the local address shown in the terminal.

## Input CSV format
The required column is `feedback`. Optional columns are `date`, `product`, and `customer_id`.

Example:
```csv
date,customer_id,product,feedback
2026-10-01,C001,Mobile App,The app is easy to use and fast.
```

## Project workflow
Customer feedback -> CSV upload -> text cleaning -> VADER sentiment scoring -> sentiment labels -> dashboard charts and insights -> CSV export.

## Limitations
- VADER works best with short English text.
- It may misunderstand sarcasm, mixed-language comments, and context-specific expressions.
- The insight summary is a simple rule-based recommendation, not a substitute for human review.
