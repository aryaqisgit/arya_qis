from flask import Flask



app=Flask(__name__)

@app.route("/")
def hi():
    return "<h1> haii </h1>"

@app.route("/hello")
def hello():
    return "<h1> hello </h1>"

@app.route("/hello/<name>")
def hello1(name):
    return "<h1> my name is "+name+"</h1>"

@app.route("/hello/<int:name>")
def hello2(name):
    return "num -->%d " %name


# add_url_rule----------------------------------

def welcome():
    return "welcome"
app.add_url_rule("/w","nnnn",welcome)
# app.add_url_rule(<url rule>,<end point>,<view function>)


if __name__=="__main__":
    app.run(debug=True)