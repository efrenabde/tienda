from flask import *

app =Flask(__name__)

@app.route("/suma/<int:value1>/<int:value2>")
def suma(value1, value2):
    return str(value1+value2)
    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)