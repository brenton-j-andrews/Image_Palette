from flask import Flask, render_template
from image_processor import processor

app = Flask(__name__)


@app.route("/")
def hello():
    colors = processor()
    return render_template("index.html", colors=colors, length=len(colors))


if __name__ == "__main__":
    app.run(debug=True)
