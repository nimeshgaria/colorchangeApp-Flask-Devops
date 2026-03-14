from flask import Flask, render_template_string
import random

app = Flask(__name__)

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

@app.route("/")
def home():
    color = random.choice(colors)
    return render_template_string(html_template, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)