# Real-Time Stock Price Tracker

A simple full-stack web app to fetch and display real-time stock prices using HTML/CSS/JavaScript frontend, and Python/Flask backend with `yfinance`.

---

## 🛠️ Technologies  
- **Frontend:** HTML, CSS, JavaScript (AJAX)  
- **Backend:** Python, Flask  
- **Data Source:** `yfinance` for live stock data

---

## 🚀 Features  
- Users can enter any stock ticker to fetch current and opening prices.  
- Performs live backend queries to Yahoo Finance and returns JSON.  
- Displays data dynamically with error handling for invalid or unavailable tickers.

---

## ⚙️ Installation & Usage  
1. **Clone the repo:**  
   ```bash
   git clone https://github.com/yourusername/stock-price-tracker.git
   cd stock-price-tracker


pip install Flask yfinance


Run the server:
python app.py



📁 Project Structure
app.py               # Flask application handling routes and API
templates/
 └─ index.html       # Frontend UI with input form and display section
static/
 ├─ style.css        # Basic styling for layout and responsiveness
 └─ script.js        # AJAX logic for ticker lookup and result rendering
