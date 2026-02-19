from flask import *
import pymysql


app= Flask(__name__)

@app.route("/api/singup",methods=["POST"])
def signup():
    username=request.form['username']
    email=request.form['email']
    phone=request.form['phone']
    password=request.form['password']

    print(username,email,phone,password)
    #creating connection db

    connection=pymysql.connect(host="localhost",user="root",password="",database="abraham_sokogarden")

    #creat  cusor to hanle sql query
    cursor=connection.cursor()
    #creat sql query

    sql="insert into users (username,email,phone,password) values(%s,%s,%s,%s)"
    #data to be saved

    data=(username,email,phone,password)
    print(data)

    # execute sql query

    cursor.execute(sql,data)

    # save data 
    connection.commit()
    return jsonify({"message": "sing up successful"})

#to signin
@app.route("/api/signin",methods=["POST"] )
def signin():
    email=request.form['email']
    password=request.form['password']
    print(email,password)

    connection=pymysql.connect(host="localhost",user="root",password="",database="abraham_sokogarden")
    #creating cusor
    # cursor=connection.cursor()

    #cursorto fetch data as key
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    #creating sql
    sql="select user_id,username,email,phone from users where email=%s and password=%s"
    #data to execute the uery
    data=(email,password)
    cursor.execute(sql,data)
    #check for resulting rows
    if cursor.rowcount==0:
        return jsonify({"message":"invalid credantials"})
    else:
        #get user data
        user=cursor.fetchone()
        return jsonify({"message":"login succesfull","user":user})

    

  




if __name__=="__main__":
    app.run(debug=True)
