from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    return {
        'success' : True,
        'message' : 'Server is healthy',
        'data' : []
    }

@app.route('/users')
def health():
    return {
        'success' : True,
        'message' : 'users fetched successfully',
        'data' : []
    }

if __name__ == '__main__':
    app.run()
