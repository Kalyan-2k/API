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
    em=res["email"]
    pwd=res["password"]
    print(em+"\t"+pwd)
    return "success"
        
@app.route('/register',methods=["POST"])
def register():
    req=request.get_json()
    fn=req['firstname']
    ln=req['lastname']
    rn=req['roll no']
    gn=req['gender']
    em=req['email']
    pwd=req['password']
    print( "firstname " + fn +
      "lastname "+ ln+
      "roll no "+ rn+
      "gender "+ gn+
      "email "+ em+
      "password "+ pwd)

    return "Congrats"

@app.route('/forgotpass',methods=["POST"])
def forgotpass():
    req=request.get_json()
    em=req['email']
    pwd=req['password']
    
    #
    # rec=

if __name__ == "__main__":
    app.run(debug=True)