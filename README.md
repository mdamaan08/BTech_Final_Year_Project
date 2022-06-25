# BTech_Final_Year_Project.

## How To Run:

First Clone the repository from GitHub:[ GitHub Link@@](https://github.com/mdamaan08/BTech_Final_Year_Project)

### 1.Parent Portal:
1.Open BTech_Final_Year_Project/Parent_Portal folder in Visual studio run Parent Portal in local host.
2.After running the project user(Parent) can register themselves using IMEI number of child’s device, unique username, Password and other details on our parent 
portal by visitting to Local host URL.

### 2.DataBase File:
To set up SQL Live Server developer need to follow below steps:
1.Create New DataBase,name it as profane.
2.Execute the .sql file present in BTech_Final_Year_Project/DataBase/profane_parent_signup.sql and BTech_Final_Year_Project/DataBase/profane_profane_words.sql
3.After the new registration at parent portal devloper can see the changes in this SQL Live server.

### 3.Flask Server and Python Script:
1.To run the flask server go to BTech_Final_Year_Project/Detector&Server_Script/server_main.py and run the server_main.py file.
2.After running the server_main.py file it will generate a URL, copy that URL.
3.BTech_Final_Year_Project/Detector&Server_Script/databaseconnection.py this file location contains backend script, developer have to make the changes at line
number 2 from:
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="profane"
)
change user,password and name of database as per your workbench server's.
4.BTech_Final_Year_Project/Detector&Server_Script/Profane_word_Script_for_Hinglish.py at this using Profane_word_Script_for_Hinglish.py the predictions happen.

### 4.Android Studio:
1.Open your Android Studio, import the Project BTech_Final_Year_Project/AndroidCustomKeyboard to run your Keyboard service.
2. Navidate to EDMTKeyboard.java file and change the URL at line number 3 to one that you copied at step 3.3
3.If your laptop is of higher configuration run the project in Android Studio by creating a virtual device else enable developer option in your Physical 
device first then enable USB debugging and then run the project.
4.Once the Android project runs Successfully, go to the device settings, enable the EDMT Keyboard from keyboard services available.
5.Once the Flask server is ready and Keyboard is enabled then the device is ready for checking and monitoring the Abusive & Profaned contents after they are 
used during texting the messages.
7. To see the Abusive & Profaned contents user can login to Parent Portal and can refer the visualization for monitoring.
