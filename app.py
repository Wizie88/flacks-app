from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        content = "I'm almost a DevOps engineer"
        print(f"Returning content: {content}")
        return render_template('index.html')
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    app.run(debug=True)
