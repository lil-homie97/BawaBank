from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

balance = 2500.00
transactions = [
    {"type": "Deposit", "amount": 1000, "date": "2026-10-09", "status": "Success"},
    {"type": "Transfer", "amount": -250, "date": "2026-10-08", "status": "Success"},
]

@app.route('/')
def home():
    return render_template('index.html', balance=balance, transactions=transactions)

@app.route('/deposit', methods=['POST'])
def deposit():
    global balance
    data = request.get_json()
    amount = float(data.get('amount', 0))
    if amount > 0:
        balance += amount
        transactions.insert(0, {"type": "Deposit", "amount": amount, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "status": "Success"})
        return jsonify({"success": True, "new_balance": balance})
    return jsonify({"success": False})

@app.route('/transfer', methods=['POST'])
def transfer():
    global balance
    data = request.get_json()
    amount = float(data.get('amount', 0))
    recipient = data.get('recipient', '')
    if amount > 0 and amount <= balance and recipient:
        balance -= amount
        transactions.insert(0, {"type": f"Transfer to {recipient}", "amount": -amount, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "status": "Success"})
        return jsonify({"success": True, "new_balance": balance})
    return jsonify({"success": False, "error": "Insufficient funds"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)s