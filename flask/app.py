from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # フロントエンドからのリクエストを許可（すべてのオリジンを許可）

@app.route('/api/greet')
def greet():
    return jsonify(message="こんにちは、ApacheからFlaskへようこそ！")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
