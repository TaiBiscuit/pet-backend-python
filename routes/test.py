from app import app

@app.route("/")
def hello_world():
    return "<p>PENE</p>"

@app.route("/register")
def register_user():
    return "null"