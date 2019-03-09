from flask import Flask
app = Flask(__name__)

@app.route("/")
def get_main():
    with open("my_map.html", "r") as f:
        return f.read()

@app.route("/path.json")
def get_path():
    with open("path.json", "r") as f:
        return f.read()


app.run()