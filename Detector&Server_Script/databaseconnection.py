import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="profane"
)
def insertprofaneword(iemi_number,pr):
    lst=[]
    mycursor = mydb.cursor()
    #fetch present iemi_number stored in database
    mycursor.execute("SELECT Iemi_id FROM profane_words")
    myresult = mycursor.fetchall()
    for x in myresult:
        lst.append(x[0])
    #iemi_number not present in list insert number and create json object profane in it
    if iemi_number not in lst:
        mycursor.execute("insert into profane_words(Iemi_id,profane_word) value(%s,'{\"profane\":[]}')",(iemi_number,))
        mydb.commit()
    #insert profane word used by respective iemi_number
    for p in pr:
        mycursor.execute("select json_length(profane_word,'$.profane')into @profane_counter from profane_words where Iemi_id=%s",(iemi_number,))
        mycursor.execute("update profane_words set profane_word=json_set(profane_word,concat('$.profane[',cast(@profane_counter as char(20)),']'),%s) where Iemi_id=%s",(p,iemi_number,))
        mydb.commit()
# iemi_number=input("enter Iemi number")
# pr=['shit','mc']
#call function for inseting profane data in database
# insertprofaneword(iemi_number,pr)
