from flask import Flask, request, session, jsonify, make_response
import os

app = Flask(__name__)
app.json.compact = False

app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):

    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session.get(key),
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
            for cookie in request.cookies],
    }), 200)

    response.set_cookie('mouse', 'Cookie', httponly=True)

    return response

if __name__ == '__main__':
    app.run(port=5555)
    