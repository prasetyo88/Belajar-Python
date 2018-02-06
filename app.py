import json
data = [{'id':1,'nama':'tas1'},{'id':2,'nama':'tas2'}]

from flask import Flask, request
app = Flask(__name__)

@app.route("/tas", methods=['GET'])
def tas():    
    if request.method == 'GET':
        return json.dumps(data)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")