from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# ==============================
# KPI + AI DATA GENERATOR
# ==============================

def generate_kpi():
    return {
        "total_orders": random.randint(200, 400),
        "total_units": random.randint(1000, 5000),
        "avg_pick": round(random.uniform(20, 60), 2),
        "overall_lph": round(random.uniform(50, 120), 2),
        "zone_perf": {
            "Zone 1": random.randint(50,120),
            "Zone 2": random.randint(50,120),
            "Zone 3": random.randint(50,120),
            "Zone 4": random.randint(50,120),
        },
        "operator_perf": {
            "OP1": random.randint(50,120),
            "OP2": random.randint(50,120),
            "OP3": random.randint(50,120),
            "OP4": random.randint(50,120),
        },
        "model_score": round(random.uniform(0.80, 0.99), 3),
        "zone_accuracy": {
            "Zone 1": round(random.uniform(0.75, 0.99), 2),
            "Zone 2": round(random.uniform(0.75, 0.99), 2),
            "Zone 3": round(random.uniform(0.75, 0.99), 2),
            "Zone 4": round(random.uniform(0.75, 0.99), 2),
        }
    }

# ==============================
# ORDER SIMULATION ENGINE
# ==============================

orders = []
statuses = ["RECEIVED", "PICKING", "PACKED", "SHIPPED"]

@app.route("/simulate")
def simulate():
    global orders

    new_order = {
        "order_id": f"ORD{random.randint(1000,9999)}",
        "zone": random.randint(1,4),
        "operator": f"OP{random.randint(1,4)}",
        "status": "RECEIVED",
        "time": datetime.now().strftime("%H:%M:%S")
    }

    orders.append(new_order)

    for order in orders:
        current = statuses.index(order["status"])
        if current < len(statuses) - 1 and random.random() > 0.5:
            order["status"] = statuses[current + 1]

    orders = orders[-15:]
    return jsonify(orders)

# ==============================
# API ROUTES
# ==============================

@app.route("/api/data")
def api_data():
    return jsonify(generate_kpi())

@app.route("/")
def home():
    return render_template("index.html")

# ==============================

if __name__ == "__main__":
    app.run(debug=True)