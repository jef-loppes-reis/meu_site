# from app import create_app

# app = create_app()
# @app.route('/')
# def homepage():
#     return 'hello world'
# if __name__ == '__main__':
#     app.run(host='localhost', port=9874


from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Hey there!"

if __name__ == '__main__':
    app.run(debug=True)
