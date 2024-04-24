from flask import *
import sqlite3

app=Flask(__name__)

@app.route("/s",methods=["GET","POST"])
def studreg():
    if request.method=="POST":
        n=request.form["fname"]
        e=request.form["eml"]
        p=request.form["phn"]
        with sqlite3.connect("stud.db")as con:
            cur=con.cursor()
            cur.execute("""insert into student(name,email,phone)values(?,?,?)""",(n,e,p))
            con.commit()
        return "success"
    else:
        return render_template("d25_3_flask_thread.html")
    


@app.route("/sv")
def stuview():
    con=sqlite3.connect("stud.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()
    return render_template("d25_3_flask_view.html",data=rows)


@app.route("/sd/<int:id>")
def studel(id):
    with sqlite3.connect("stud.db")as con:
        cur=con.cursor()
        cur.execute("delete from student where id=?",(id,))
        con.commit()
    return("<script>window.alert('successfully deleted!!!!');window.location.href='/s'</script>")


@app.route("/se/<int:id>")
def studedit(id):
        n=request.form["fname"]
        e=request.form["eml"]
        p=request.form["phn"]
        with sqlite3.connect("stud.db")as con:
            # doc.name=nam
            con=sqlite3.connect("stud.db")
            con.row_factory=sqlite3.Row
            cur=con.cursor()
            rows=cur.fetchone()
            con.commit()
            return render_template("d25_3_flask_edit.html",data=rows)
      
            


    

    


    
if __name__=="__main__": 
    app.run(debug=True)