# Real-Time Twitter Sentiment Dashboard

A production-ready dashboard that streams tweets, performs VADER sentiment analysis, and visualizes trends in real-time.

## features
- **Backend Streaming**: `src/streamer.py` fetches/generates tweets and saves them.
- **Sentiment Analysis**: Classifies text as Positive/Negative/Neutral using NLTK.
- **Live Dashboard**: Streamlit app with auto-refreshing charts.
- **API**: FastAPI backend included for extension.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamer (Mock Mode for testing):
   ```bash
   python src/streamer.py
   ```
   *Keep this terminal open.*

3. Run the Dashboard (New Terminal):
   ```bash
   streamlit run dashboard.py
   ```

## Files
- `src/`: Core logic modules.
- `data/`: Stores polled tweets locally.
- `dashboard.py`: Frontend UI.
