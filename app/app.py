from flask import Flask, render_template_string
from prometheus_client import Counter, generate_latest
import random

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('request_count', 'Total Requests')

colors = [
    "#FF5733",
    "#33FF57",
    "#3357FF",
    "#F3FF33",
    "#FF33A8",
    "#33FFF3"
]

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Color Change App</title>
    <style>
        body {
            background-color: {{color}};
            text-align: center;
            font-family: Arial;
            margin-top: 100px;
        }
        button {
            padding: 15px 30px;
            font-size: 18px;
            cursor: pointer;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<h1>Python Color App</h1>

<form method="GET">
    <button type="submit">Change Background Color</button>
</form>

</body>
</html>
"""

# ✅ Single route handling both UI + metrics count
@app.route("/")
def home():
    REQUEST_COUNT.inc()
    color = random.choice(colors)
    return render_template_string(html_template, color=color)

# ✅ Prometheus endpoint
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)