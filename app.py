from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {
        "balance": 2500.00,
        "transactions": [
            {"type": "Deposit", "amount": 1000, "date": "2026-10-09", "status": "Completed"},
            {"type": "Transfer", "amount": -250, "date": "2026-10-08", "status": "Completed"}
        ]
    }

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump({"balance": balance, "transactions": transactions}, f)

# Load persistent data
data = load_data()
balance = data["balance"]
transactions = data["transactions"]

@app.route('/')
def home():
    return render_template('index.html', balance=balance, transactions=transactions)

@app.route('/deposit', methods=["POST"])
def deposit():
    global balance
    try:
        data_json = request.get_json()
        amount = float(data_json.get("amount", 0))
        if amount > 0:
            balance += amount
            transactions.insert(0, {"type": "Deposit", "amount": amount, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "status": "Completed"})
            save_data()
            return jsonify({"success": True, "new_balance": balance})
    except Exception as e:
        print(e)
    return jsonify({"success": False})

@app.route('/transfer', methods=["POST"])
def transfer():
    global balance
    data_json = request.get_json()
    amount = float(data_json.get("amount", 0))
    recipient = data_json.get("recipient", "")
    if amount > 0 and amount <= balance and recipient:
        balance -= amount
        transactions.insert(0, {"type": f"Transfer to {recipient}", "amount": -amount, "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "status": "Completed"})
        save_data()
        return jsonify({"success": True, "new_balance": balance})
    return jsonify({"success": False, "error": "Insufficient funds or invalid recipient"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
