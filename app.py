#start building up structure for the web page
from flask import Flask
from flask import session,request,render_template, url_for, redirect


app = Flask(__name__)
app.secret_key="kq345bz2"

def auth(func):
    def wrapper():
        if 'username' not in session:
            return redirect(url_for("login"))
        else:
            return func()
    return wrapper

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        return redirect(url_for("login.html"))

@app.route("/sample",methods=['GET','POST'])
def samplePage():
    return render_template("harvard.html")

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=1337)
