from flask import *
from flask_mail import *

app=Flask(__name__)

app.secret_key="aa"

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("d1_4_dp.html")
    else:
        er="hhhhhhhhhhhhhhhhhhh"
        f=request.files["dp"]
        f.save(f.filename)
        a=1
        if a==1:
            flash("successfully saved")
        else:
            flash("error")
        return render_template("d1_4_dp.html",error=er)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="meenuquest123@gmail.com"
app.config['MAIL_PASSWORD']="ywcx ykrt hpja znxk"
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route("/sm")
def smail():
    msg=Message('subject',sender="meenuquest123@gmail.com",recipients=['aryasomasundaran2001@gmail.com'])
    msg.body='hi my first message in flask'
    mail.send(msg)
    return "success"







if __name__=="__main__":
    app.run(debug=True)