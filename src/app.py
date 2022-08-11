"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#get all members
@app.route('/members', methods=['GET'])
def get_all_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

#get single member
@app.route('/member/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    single_member = jackson_family.get_member(member_id)
    return jsonify(single_member), 200

#add member
@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.json
    jackson_family.add_member(new_member)
    return jsonify(f'{new_member["name"]} added to the family'), 200
    
@app.route('/members/<int:delete_id>', methods=['DELETE'])
def delete_member(delete_id):
    is_deleted = jackson_family.delete_member(delete_id)
    member_to_delete = jackson_family.get_member(delete_id)
    if is_deleted:
        return jsonify(f'{member_to_delete["name"]} deleted from the family'), 200
    else:
        raise APIException('Wrong ID', 400)    
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
