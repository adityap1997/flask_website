from flask import Flask, send_from_directory
import os

# Serve everything out of the "static" folder (where index.html lives)
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path="")


@app.route("/")
def home():
    return send_from_directory(STATIC_DIR, "index.html")


# Catch-all so direct links / refreshes on any path still resolve to a file
# in /static if it exists, otherwise fall back to index.html
@app.route("/<path:path>")
def catch_all(path):
    full_path = os.path.join(STATIC_DIR, path)
    if os.path.isfile(full_path):
        return send_from_directory(STATIC_DIR, path)
    return send_from_directory(STATIC_DIR, "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
