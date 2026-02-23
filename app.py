from flask import *
import pymysql
import os


app= Flask(__name__)
app.config["UPLOAD_FOLDER"]="static/images"


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
    
@app.route("/api/add_product", methods=["POST"])
def add_product():
    product_name=request.form["product_name"]
    product_description=request.form["product_description"]
    product_category=request.form["product_category"]
    product_cost=request.form["product_cost"]
    product_image=request.files["product_image"]

    print(product_name,product_description,product_category,product_cost,product_image)
    #get the image name

    image_name=product_image.filename
    file_path=os.path.join(app.config["UPLOAD_FOLDER"],image_name)
    product_image.save(file_path)

    
    connection=pymysql.connect(host="localhost",user="root",password="",database="abraham_sokogarden")
    cursor=connection.cursor()
    sql="insert into product_details (product_name, product_description, product_category, product_cost, product_image) values (%s,%s,%s,%s,%s) "

    data=(product_name,product_description,product_category,product_cost,image_name)
    cursor.execute(sql,data)

    connection.commit()

    return jsonify({"message":"product added succesfull"})


    #save the image to folder

   
    # return "done"


    

  




if __name__=="__main__":
    app.run(debug=True)
