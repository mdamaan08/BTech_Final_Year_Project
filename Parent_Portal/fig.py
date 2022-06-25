import matplotlib.pyplot as plt
import mysql.connector
from flask import Flask,render_template
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as convas
from matplotlib.figure import Figure


app=Flask(__name__)

@app.route("/visualize")
def visualize():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="profane"
    )

    lst=['"','[',']','(',')',"'",''," "]

    str1=''

    mycursor = mydb.cursor()
    #fetch present iemi_number stored in database
    mycursor.execute("SELECT json_extract(profane_word, '$.profane') AS Pr FROM profane_words where Iemi_id='988764764563';")
    myresult = mycursor.fetchall()

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


if __name__=="__main__":
    app.run(debug=True)

    

