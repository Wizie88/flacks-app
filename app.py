from flask import Flask
app = flacks-app(__name__)
@app.route('/')
def hello():
    return 'I am almost a DevOps Engineer!\n'
if __name__ == '__main__':
    app.run(host='0.0.0.0')