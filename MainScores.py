from Utils import SCORES_FILE_NAME
from flask import Flask
app = Flask(__name__)

scores_template = "templates/score.html"
error_template = "templates/error.html"


def score_server():
    file = open(SCORES_FILE_NAME, "r")
    score = file.read()
    file.close()
    return int(score)


@app.route("/", methods=['GET'])
def index():
    try:
        score = score_server()
        print(score)
        template = open(scores_template, 'r')
        page = template.read()
        page = page.replace('{SCORE}', str(score))
        print(page)
    except FileNotFoundError as e:
        template = open(error_template)
        page = template.read()
        page = page.replace('{ERROR}', str(e))
    return page


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
