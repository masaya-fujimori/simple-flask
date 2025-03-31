from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # フロントエンドからのリクエストを許可

@app.route('/api/greet')
def greet():
    return jsonify(message="こんにちは、ApacheからFlaskへようこそ！")

if __name__ == '__main__':
    app.run(debug=True)
