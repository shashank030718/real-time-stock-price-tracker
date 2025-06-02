import yfinance as yf
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.get_json()['ticker']
    data = yf.Ticker(ticker).history(period='1d')
    if data.empty:
        return jsonify({'error': 'No data found'}), 404

    last_row = data.iloc[-1].to_dict()
    current_price = last_row.get('Close')
    open_price = last_row.get('Open')

    if current_price is None or open_price is None:
        return jsonify({'error': 'Invalid data for ticker'}), 404

    return jsonify({
        'currentPrice': current_price,
        'openPrice': open_price
    })

if __name__ == '__main__':
    app.run(debug=True)
