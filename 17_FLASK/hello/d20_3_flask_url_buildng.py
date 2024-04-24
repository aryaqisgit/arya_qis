# ------flask url building-----------

from flask import *

app=Flask(__name__)

@app.route("/adm")
def admin():
    return "welcome admin"

@app.route("/stu")
def student():
    return "welcome student"

@app.route("/teach")
def teacher():
    return "welcome teacher"

@app.route("/user/<uname>")
def user(uname):
    if uname=="admin":
        return redirect(url_for ("admin"))
    elif uname=="student":
        return redirect(url_for ("student"))
    elif uname=="teacher":
        return redirect(url_for ("teacher"))
    else:
        return "invalid user"
    
# ---connect pages------

# @app.route("/<job>")    
# def mypage(job):
#     # name="ammu"
#     name=input("enter ur name : ")
#     # return "my html page"
#     return render_template ("d20_3.html",uname=name,j=job)

# ---------- multiplication table

@app.route("/")
def multi():
    n=int(input("enter number : "))
    return render_template ("d20_3_multi.html",unum=n)
    

if __name__=="__main__":
    app.run(debug=True)