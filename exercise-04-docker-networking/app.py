from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/about")
def about():
    return jsonify(
        name="Simple REST API",
        version="1.0",
        description="Flask API running on a user-defined Docker bridge network.",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
