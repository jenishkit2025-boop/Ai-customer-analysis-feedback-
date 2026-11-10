# PROJECT REPORT: AI CUSTOMER FEEDBACK ANALYSIS DASHBOARD

## 1. Introduction
Customer feedback helps organisations understand customer satisfaction and improve products and services. Manually reading a large number of comments is time-consuming. This project uses Natural Language Processing (NLP) sentiment analysis to classify feedback and present the results in a visual dashboard.

## 2. Problem Statement
Businesses receive feedback through reviews, forms, and support channels. Analysing these comments manually can be slow and inconsistent. A simple automated system is needed to identify positive, neutral, and negative feedback and help teams recognise areas that need attention.

## 3. Aim
To develop an AI-based dashboard that analyses customer feedback, identifies sentiment, and presents useful summaries for decision-making.

## 4. Objectives
- Collect customer feedback through CSV upload.
- Process text using a sentiment-analysis technique.
- Classify feedback as positive, neutral, or negative.
- Display sentiment statistics and visual charts.
- Compare feedback across products.
- Export analysed feedback for further review.

## 5. Proposed System
The user uploads a CSV file. The application checks for a feedback column, analyses each comment using VADER sentiment analysis, assigns a sentiment label, and displays key metrics and charts. Users can filter the results by product and sentiment and download the analysed records.

## 6. Technologies Used
- Front end: Streamlit
- Programming language: Python
- Data processing: Pandas
- Visualisation: Plotly
- NLP / sentiment analysis: VADER Sentiment

## 7. System Modules
1. **Data input module:** accepts customer feedback as a CSV file.
2. **Pre-processing module:** checks columns, handles missing text, and converts dates.
3. **Sentiment analysis module:** calculates a compound sentiment score and assigns a label.
4. **Dashboard module:** displays counts, percentage, charts, and product comparisons.
5. **Filtering module:** filters feedback by product and sentiment.
6. **Report/export module:** lets users download analysed records.

## 8. Methodology / Algorithm
1. Start the application.
2. Load the sample dataset or upload a customer-feedback CSV.
3. Validate that the `feedback` column exists.
4. Analyse each comment using VADER.
5. If compound score is at least +0.05, label it Positive.
6. If compound score is at most -0.05, label it Negative.
7. Otherwise, label it Neutral.
8. Calculate sentiment totals and positive-feedback rate.
9. Display charts and insight messages.
10. Allow the user to export the results.

## 9. Expected Output
The dashboard displays total feedback, positive and negative counts, positive-feedback rate, sentiment distribution, feedback trends, product-wise sentiment, and individual analysed comments.

## 10. Advantages
- Reduces the time needed to review large sets of comments.
- Gives a quick view of customer satisfaction.
- Helps identify negative experiences for follow-up.
- Makes results easier to understand through charts.
- Supports data export for additional analysis.

## 11. Limitations
The starter version is designed mainly for short English comments. Sarcasm, spelling errors, mixed-language text, and complex context may affect accuracy. Human review is recommended before taking important business decisions.

## 12. Future Enhancements
- Add multilingual sentiment analysis for Tamil and other languages.
- Connect directly to online review platforms and customer-support systems.
- Add aspect-based analysis to identify issues such as price, delivery, quality, and support.
- Add login roles and database storage.
- Use a transformer-based language model for more context-aware predictions.

## 13. Conclusion
The AI Customer Feedback Analysis Dashboard demonstrates how NLP can convert customer comments into understandable sentiment information. It provides a practical starting point for organisations to monitor satisfaction, identify service issues, and make data-informed improvements.
