from flask import request,Flask,render_template,url_for
from Places import places

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", method = ['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("login.html", error=session['login_error'])
    session['login_error'] = ""
    name = request.form['name']
    password = request.form['pass']
    
    if db_valid_upass(name, password):
        session['user'] = db_load_user(name)
        return redirect(url_for("/"))
    else:
        session['login_error'] = "Invalid username and password combination"
        return redirect(url_for("/login"))


@app.route("/register", method = ['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template("register.html", error=session['register_error'])
    session['register_error'] = ""
    name = request.form['name']
    email = request.form['email']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']
    if db_name_taken(name):
        session['register_error'] = "Username is already taken"
        return redirect(url_for("/register"))
    if not pass1 == pass2:
        session['register_error'] = "Passwords don't match"
        return redirect(url_for("/register"))
    if db_email_taken(email):
        session['register_error'] = "Email is already taken"
        return redirect(url_for("/register"))
    uid = get_next_uid()
    db_add_user(uid, name, email, pass1)
    session['user'] = db_load_user(name)
    return redirect(url_for("/"))
    
@app.route("/rate_locations", method = ['POST', 'GET'])
def rate_locations():
    if request.method == "GET":
        return render_template("get_location.html")
    #Read form data
    for place in places:
        if place in request.form:
            session['user'].addLocation(place)
    db_update_user(

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
