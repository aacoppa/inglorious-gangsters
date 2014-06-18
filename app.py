#start building up structure for the web page
from flask import Flask
from flask import session,request,render_template, url_for, redirect
#from Populator import populate_database
#import search
#from Populator import populate_database
from userdb import *
from initcoldb import *
from Populator import populate_database

app = Flask(__name__)
app.secret_key="kq345bz2"

@app.route("/search", methods = ['POST', 'GET'])
def search():
    """
        Users find the schools that fit their interests
    """
    schools = search.find_schools(session['user'])
    return render_template("results.html", safetys=schools['safetys'],
                           targets=schools['targets'], reachs=schools['reachs'])


@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == "GET":
        if 'login_error' in session:
            return render_template("login.html", error=session['login_error'])
        else:
            return render_template("login.html", error="")
    if request.form["button"] == "Register":
        return redirect(url_for("register"))
    session['login_error'] = ""
    email = request.form['email']
    password = request.form['pass']
    
    if db_valid_upass(email, password):
        session['user'] = db_load_user(email)
        return redirect(url_for("/"))
    else:
        session['login_error'] = "Invalid username and password combination"
        return redirect(url_for("/login"))


@app.route("/register", methods = ['POST', 'GET'])
def register():
    if request.method == "GET":
        if 'register_error' in session:
            return render_template("register.html", error=session['register_error'])
        else:
            return render_template("register.html",error="")
    session['register_error'] = ""
    name = request.form['name']
    print name
    email = request.form['email']
    print email
    pass1 = request.form['pass1']
    print pass1
    pass2 = request.form['pass2']
    print pass2
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
    
@app.route("/rate_locations", methods = ['POST', 'GET'])
def rate_locations():
    """
        Users select locations they would be interested in studying
    """
    from locations import areas, states
    if request.method == "GET":
        return render_template("get_location.html", Areas=Areas, states=states.keys())
    #Read form data
    for data in request.form:
        if data in states:
            session['user'].add_state(data)
def auth(func):
    def wrapper():
        if 'username' not in session:
            return redirect(url_for("login"))
        else:
            return func()
    return wrapper


 
@app.route("/add_grades", methods = ['POST', 'GET'])
def add_grades():
    """
        Users added grades and sats
    """
    if request.method == "GET":
        return render_template("add_grades.html", subjects=subjects)

    for subject in subjects:
        session['user'].add_grade(subject, request.form['subject'])
#    for 
    #db_update_user


@app.route("/colleges")
def show_colleges():
    return render_template("colleges.html", collegeList=populate_database())


@app.route("/",methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        return redirect(url_for("login"))

@app.route("/sample",methods=['GET','POST'])
def samplePage():
    return render_template("harvard.html")

if __name__ == "__main__":
    if not checkDB():
        for college in populate_database():
            if not db_college_exits(colllege.name):
                db_store_college(college)
    app.debug=True
    app.run(host="0.0.0.0",port=1337)
