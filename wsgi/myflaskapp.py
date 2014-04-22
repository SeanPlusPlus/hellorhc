from flask import Flask, jsonify
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route("/")
def hello():
    msg = {'message': 'hello world'}
    return flask.jsonify(**msg)

if __name__ == "__main__":
    app.run()

