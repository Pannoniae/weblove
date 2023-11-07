import flask
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return flask.render_template('index.html')


@app.route('/api/submit', methods=['GET'])
def post_comment():
    author = request.args.get('author')
    comment = request.args.get('comment')
    if author == "" or comment == "":
        return "Author or comment not filled out"
    with open("comments.txt", "a") as f:
        f.write(f"{author}: {comment}\n")
    return flask.redirect("/")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
