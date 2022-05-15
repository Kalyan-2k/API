from flask import Flask,request,jsonify
from flask_cors import CORS
import pymongo

mdb_obj=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=mdb_obj["info"]

tab= mydb["user_info"]




app = Flask(__name__)
CORS(app)
app.config['ENV'] = "development"


@app.route('/auth',methods=["POST"])
def login():
    res=request.get_json()
    # print(res)
    em=res["email"]
    pwd=res["password"]
    for x in tab.find():
        if em==x["email"]:
            if pwd ==x["password"]:
                return "success"
            else :
                return "Invalid Password"
        else:
            return "Invalid Username"
        
@app.route('/register',methods=["POST"])
def register():
    req=request.get_json()
    fn=req['firstname']
    ln=req['lastname']
    rn=req['roll no']
    gn=req['gender']
    em=req['email']
    pwd=req['password']
    tab.insert_one({"first name":fn,"last name":ln,"roll no":rn,"gender":gn,"email":em,"passowrd":pwd})
    return "Congrats"

@app.route('/forgotpass',methods=["POST"])
def forgotpass():
    req=request.get_json()
    em=req['email']
    pwd=req['password']
    cpwd=req['confirmpassword']
    if(pwd==cpwd):
        for x in tab.find():
            if em==x["email"]:
                x["password"]=pwd
    else:
        return "Password mismatch"

@app.route('/video',methods=["POST"])
def video():
    #return main()
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)