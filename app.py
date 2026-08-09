from flask import Flask, send_from_directory
import os

# Path to the static folder
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

app = Flask(
    __name__
    )


@app.route("/")
def home():
    return send_from_directory("index.html")


# Catch-all route for files/pages inside static
@app.route("/<path:path>")
def catch_all(path):
    full_path = os.path.join(path)

    if os.path.isfile(full_path):
        return send_from_directory(path)

    return send_from_directory("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5500))
    app.run(host="0.0.0.0", port=port)
