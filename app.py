from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    return {
        'success' : True,
        'message' : 'Server is healthy',
        'data' : []
    }

if __name__ == '__main__':
    app.run()
