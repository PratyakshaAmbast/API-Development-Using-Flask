from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

dogs = [{'breed' : 'labrador'}, {'breed' : 'husky'}, {'breed' : 'bulldog'}, {'breed' : 'beagle'}]

from flask import request, make_response
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'dogdata':
        return 'dog'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/', methods=['GET'])
@auth.login_required
def test():
	return jsonify({'message' : 'Welcome!'})

@app.route('/page', methods=['GET'])
@auth.login_required
def returnAll():
	return jsonify({'dogs' : dogs})

@app.route('/page/<string:breed>', methods=['GET'])
@auth.login_required
def returnOne(breed):
	exist = [dog for dog in dogs if dog['breed'] == breed]
	return jsonify({'dog' : exist[0]})

@app.route('/page', methods=['POST'])
@auth.login_required
def addOne():
	dog = {'breed' : request.json['breed']}
	dogs.append(dog)
	return jsonify({'dogs' : dogs})

@app.route('/page/<string:breed>', methods=['PUT'])
@auth.login_required
def editOne(breed):
	exist = [dog for dog in dogs if dog['breed'] == breed]
	exist[0]['breed'] = request.json['breed']
	return jsonify({'dog' : exist[0]})

@app.route('/page/<string:breed>', methods=['DELETE'])
@auth.login_required
def removeOne(breed):
	page = [dog for dog in dogs if dog['breed'] == breed]
	dogs.remove(page[0])
	return jsonify({'dogs' : dogs})

if __name__ == '__main__':
	app.run(debug=True) 