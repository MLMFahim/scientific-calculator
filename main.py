import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Looks for your index.html file in the same directory
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        return render_template_string(html_content)
    except FileNotFoundError:
        return "<h3>Error: index.html not found in the same directory!</h3>"

if __name__ == '__main__':
    # Starts a local web server on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
