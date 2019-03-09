from flask import Flask
from flask import request
from flask import jsonify
import json


app = Flask(__name__)

@app.route("/")
def get_main():
    with open("contribute.html", "r") as f:
        return f.read()

@app.route("/path.json")
def get_path():
    with open("path.json", "r") as f:
        return f.read()

@app.route('/submitRoute', methods = ['POST'])
def user():
    if request.method == 'POST':
        data = request.form # a multidict containing POST data
        #print(data)
        #print(data)
        keys = list(data.to_dict().keys())
        d = json.loads(keys[0])
        print(d['routeName'])
        print(d['newPathPoints'])
        with open("path.json", "r") as f:
            path_json_string = f.read()
        path_json = json.loads(path_json_string)
        path_json[d['routeName']] = {"points": [{"name": '{:.0f}'.format(i), "coordinates": coordinates} for i, coordinates in enumerate(d['newPathPoints'])]}
        path_json_string = json.dumps(path_json)
        with open("path.json", "w") as f:
            f.write(path_json_string)
    else:
        # POST Error 405 Method Not Allowed
        pass
    return 'ok!'

if __name__ == '__main__':
    app.run()
