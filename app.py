import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "This App is deployed by pipeline on Docker!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT if available
    app.run(host='0.0.0.0', port=port)
