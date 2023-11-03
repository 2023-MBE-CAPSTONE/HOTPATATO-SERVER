from flask import Blueprint, request

user_route = Blueprint('user_route', __name__)

@user_route.route("/signup")
def signup():
    print("helooo", flush=True)
    return "Hello World"

