from flask import Blueprint, request

user_route = Blueprint('user_route', __name__)

@user_route.route("/signup",methods=["POST"])
def signup():
    email_receive = request.form['email_give']
    name_receive = request.form['name_give']
    print("helooo",flush=True)
    print(f"received: {email_receive},{name_receive}",flush=True)
    # return "Hello World"
