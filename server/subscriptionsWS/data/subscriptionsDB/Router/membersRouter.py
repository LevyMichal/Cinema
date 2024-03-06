from flask import Blueprint, jsonify, request
from BLL.membersBLL import MembersBLL

members = Blueprint('members', __name__)

BLL = MembersBLL()

@members.route('/', methods=['GET'])
def get_all_members():
    all_members = BLL.get_all_members()
    return jsonify(all_members)
