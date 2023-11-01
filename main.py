from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/test", methods=["POST"])
def info_post():
    email_receive = request.form['email_give']
    name_receive = request.form['name_give']
    print(email_receive, name_receive)
    
    return jsonify({'msg': '구독 완료!'})


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)