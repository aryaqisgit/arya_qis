from flask import *

app=Flask(__name__)
app.secret_key="aa"

# @app.route("/Gstudreg",methods=['GET'])
# def my_get_method():
#     nam=request.args.get("fname")
#     em=request.args.get("eml")
#     ph=request.args.get("phn")
#     print(nam,em,ph)
#     return 'success GET method'


# @app.route("/Pstudreg",methods=['POST'])
# def my_post_method():
#     nam=request.form["fname"]
#     em=request.form["eml"]
#     ph=request.form["phn"]
#     print(nam,em,ph)
#     return 'success POST method'


# ----------FLASK REQUEST OBJECTS:form

# @app.route("/n")
# def reg():
#     return render_template("d21_3_flask_request_obj.html")

@app.route("/data",methods=["POST"])
def getdata():
    data=request.form
    return data
# work : terminal run + go live on html page

@app.route("/d",methods=["POST","GET"])
def get_data():
    if request.method=="POST":
        data=request.form
        return data
    else:
        return render_template("d21_3_flask_request_obj.html")
    
# -----------cookies

# @app.route("/sc")
# def set_cook():
#     res=make_response("<h1> cookie is set </h1>")
#     res.set_cookie("fname","anju")
#     return res

# @app.route("/gc")
# def get_cook():
#     name=request.cookies.get("fname")
#     return name

# # ---------------------session

@app.route("/ss")
def set_session():
    res=make_response("session is set")
    session["phon"]=7868
    return res

@app.route("/gs")
def get_session():
    if "phon" in session:
        return str(session["phon"])




if __name__=="__main__":
    app.run(debug=True)
