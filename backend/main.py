from flask import Flask
from flask import request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Receive data and echo it back
# Reply format: {
#	'hello': string
#	'data': json received
#	}
@app.route('/echo', methods=["POST"])
def echo():
	data = json.loads(request.data)
	print(data)
	return jsonify({
        'hello':'Hello!', 
        'data':data,
        })
 
if __name__ == '__main__':
    app.run(debug=True)
