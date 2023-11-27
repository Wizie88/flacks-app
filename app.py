from flask import Flask, render_template, send_from_directory
import os

app = Flask(_name_)

@app.route('/')
def hello():
    content = "I'm almost a DevOps engineer"
    print(f"Returning content: {content}")
    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)
