from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return 'I am almost a DevOps Engineer!\n'
render_template('index.html')
if __name__ == '__main__':
    with app.app_context():
        db.creat_all()
    app.run(debug=True)
