from flask import *

app=Flask(__name__)
app.secret_key="aa"



@app.route("/lgn",methods=['POST','GET'])
def my_loggin():
    if request.method=="POST":
        em=request.form["eml"]
        pas=request.form["pass"]
        if pas=="admin":
            session["emil"]=em
            return render_template("d21_3_wrklgn.html")
        else:
            return "invalid password"
    else:
        return render_template("d21_3_work.html")


@app.route("/eg")
def emlget():
    if "emil" in session:
            return render_template("d22_3_wrkhi.html",mail=session['emil'])
    else:
         return("<script>window.alert('error!!!!');window.location.href='/lgn'</script>")
    
@app.route("/lgo")
def logout():
     del session['emil']
     return redirect(url_for("my_loggin"))



    


if __name__=="__main__":
    app.run(debug=True)