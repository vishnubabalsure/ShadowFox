import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import os

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Define file path
file_path = "X_tweets.csv"  # Change this path to your CSV location

# Check if file exists
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print(" Dataset loaded successfully!")
else:
    # If file not found, create a sample dataset
    print(f"⚠ File not found: {file_path}")
    print("Creating a sample dataset instead...")
    data = {
        'date': pd.date_range(start='2025-12-01', periods=5, freq='D'),
        'user': ['@user1', '@user2', '@user3', '@user4', '@user5'],
        'text': [
            'I love the new features on X!',
            'The update is terrible.',
            "Meh, it's okay.",
            'X platform keeps improving daily!',
            'Not impressed with the latest update.'
        ]
    }
    df = pd.DataFrame(data)

# Preview the first 5 rows
print(df.head())

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Apply sentiment analysis
df['sentiment'] = df['text'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['sentiment_label'] = df['sentiment'].apply(
    lambda score: 'Positive' if score > 0.05 else ('Negative' if score < -0.05 else 'Neutral')
)

# Preview dataframe with sentiment
print("\n Sentiment analysis applied:")
print(df.head())
# Drop missing tweet text
df = df.dropna(subset=['text'])

# Convert 'date' to datetime (if column exists)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Preview cleaned data
df.head()
# Initialize VADER Sentiment Analyzer
sid = SentimentIntensityAnalyzer()

# Categorize sentiment
def get_sentiment(text):
    score = sid.polarity_scores(text)['compound']
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['text'].apply(get_sentiment)

# Check sentiment counts
df['Sentiment'].value_counts()
if 'date' in df.columns:
    monthly_sentiment = df.groupby([df['date'].dt.to_period('M'),'Sentiment']).size().unstack().fillna(0)
    monthly_sentiment.plot(kind='line', figsize=(12,6), marker='o')
    plt.title("Sentiment Trend Over Time")
    plt.xlabel("Month")
    plt.ylabel("Number of Tweets")
    plt.grid(True)
    plt.show()
sentiment_counts = df['Sentiment'].value_counts()
plt.bar(sentiment_counts.index, sentiment_counts.values, color='orange')
plt.title("Tweet Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
plt.figure(figsize=(6,6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title("Sentiment Proportion on X")
plt.show()
if 'date' in df.columns:
    df['Month'] = df['date'].dt.month
    sns.scatterplot(x='Month', y='Sentiment', data=df, hue='Sentiment', palette='Set2')
    plt.title("Monthly Sentiment Scatter")
    plt.show()
sns.countplot(x='Sentiment', data=df, palette='Set1')
plt.title("Tweet Count by Sentiment")
plt.show()
numeric_cols = df.select_dtypes(include=np.number).columns
if len(numeric_cols) > 0:
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
