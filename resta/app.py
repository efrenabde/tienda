from flask import Flask

app = Flask(__name__)

@app.route("/resta/<int:value1>/<int:value2>")
def resta(value1, value2):
    return str(value1-value2)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)