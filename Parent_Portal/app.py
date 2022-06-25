from flask import Flask , request, render_template,redirect
import matplotlib.pyplot as plt
import mysql.connector
from flask import Flask,render_template
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as convas
from matplotlib.figure import Figure
conn= mysql.connector.connect(host="localhost",username="root",password="password",database="profane")

cursor=conn.cursor()
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/visualize")
def visualize():

  
    lst=['"','[',']','(',')',"'",''," "]

    str1=''
    #iemi=IEMI
    #fetch present iemi_number stored in database
    #cursor.execute("SELECT json_extract(profane_word, '$.profane') AS Pr FROM profane_words where Iemi_id='{}';".format(iemi))
    cursor.execute("SELECT json_extract(profane_word, '$.profane') AS Pr FROM profane_words where Iemi_id='862719041502560';")
    myresult = cursor.fetchall()

    lst1=[]
    for x in myresult:
        for i in str(x):
            if i in lst :
                pass
            else:
                str1+=i
        print(str1)
        lst1=str1.split(",")
        lst1.pop(-1)

    x=[]
    y=[]
    for word in set(lst1):
        x.append(lst1.count(word))
        y.append(word)
    plt.pie(x, labels = y,autopct='%1.1f%%')
    img=io.BytesIO()
    plt.savefig('static/images/new_plot.png')
    return render_template("visualize.html",url='static/images/new_plot.png')

    

@app.route('/add_user',methods=["POST","GET"])
def add_user():
    email=request.form.get('email')
    IEMI=request.form.get('IEMI')
    cname=request.form.get('cname')
    phoneno=request.form.get('phoneno')
    password=request.form.get('password')
    cursor.execute("INSERT INTO parent_signup (mail_id,Iemi_number,child_name,phone_number,passwords) VALUES ('{}','{}','{}','{}','{}')".format(email,IEMI,cname,phoneno,password))
    conn.commit()
    return render_template('login.html')

@app.route("/login_validation",methods=["POST","GET"])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute("SELECT Iemi_number from parent_signup WHERE mail_id LIKE '{}' AND passwords LIKE '{}'".format(email,password))
    users=cursor.fetchall()
    print(users)
    if len(users)==1:
        return redirect('/visualize')
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug = True)