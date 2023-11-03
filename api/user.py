from flask import Blueprint, request

user_route = Blueprint('user_route', __name__)

@user_route.route("/signup")
def signup():
    # data = request.get_json()
    return "Hello World"

# @user_route.route("/api/v2/user/login", methods=['POST'])
# def login():
#     data = request.get_json()
#     return login_service(data)