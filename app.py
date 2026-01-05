from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {"status": "success", "message": "大家好棒喔，版本更新了v3"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

