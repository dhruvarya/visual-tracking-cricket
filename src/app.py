from flask import Flask
from flask import render_template
from flask import session
from flask import jsonify
from flask import make_response
from flask_sqlalchemy import SQLAlchemy
from flask import request
from base64 import b64encode
import numpy as np
import sys
import json
import io
from flask_cors import CORS
import cv2
sys.path.append("new")

from project import create_homography

app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'   #for database
db = SQLAlchemy(app)       # for database
CORS(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False)
    lname = db.Column(db.String(80), unique=False)
    jno = db.Column(db.Integer, unique=False)
    data = db.Column(db.LargeBinary, unique=False)
    
    def __init__(self,fname, lname, jno, data):
        self.fname = fname
        self.lname = lname
        self.jno = jno
        self.data = data
        

@app.errorhandler(404)
def not_found(error):
	return "Nothing found<br>Try something else.<br>"

@app.route("/")
@app.route("/index", methods=["GET"])
def home():
	return render_template('index.html')


@app.route("/left", methods=["GET"])
def left():
	return render_template('left.html')

@app.route("/right", methods=["GET"])
def right():
	return render_template('right.html')

@app.route("/center", methods=["GET"])
def center():
	return render_template('center.html')

@app.route("/teamdetails",methods=["GET"])
def f():
	return render_template('team-form.html')

@app.route("/end",methods=["GET"])
def end():
	db.create_all()
	allplayers=User.query.filter(User.id<=32)
	for player in allplayers:
		db.session.delete(player)
		db.session.commit()
	return render_template('team-form.html')
		
@app.route("/teamdetails", methods=["POST"]) #when submit button is hitted
def form():
	for i in range(5):
		fname=request.form["fn"+str(i)]
		lname=request.form["ln"+str(i)]
		jno=request.form["jn"+str(i)]
		data=request.files["im"+str(i)]
		db.create_all()
		new_entry=User(fname, lname, jno, data.read())
		db.session.add(new_entry)
		db.session.commit()
	return render_template('team-form.html')

@app.route("/teamdetails1", methods=["POST"]) #when submit button is hitted
def form1():
	for i in range(11):
		fname=request.form["fn"+str(i)]
		lname=request.form["ln"+str(i)]
		jno=request.form["jn"+str(i)]
		data=request.files["im"+str(i)]
		db.create_all()
		new_entry=User(fname, lname, jno, data.read())
		db.session.add(new_entry)
		db.session.commit()
	return render_template('team-form.html')

@app.route("/annotation", methods=["GET"])  
def userAdd1():
	list_all=[]
	db.create_all()
	allplayers=User.query.filter(User.id<=11)
	strf1=[]
	strf2=[]
	strf3=[]
	for player in allplayers:
		obj={}
		obj['index']=player.id
		obj["jno"]=str(player.jno);
		obj["name"]=player.fname+" "+player.lname;
		obj["image"]=b64encode(player.data).decode("utf-8")	
		strf3.append(obj)
		list_all.append(obj)
	var=0
	for player in allplayers:
		obj={}
		obj['index']=player.id
		obj["jno"]=str(player.jno);
		obj["name"]=player.fname+" "+player.lname;
		obj["image"]=b64encode(player.data).decode("utf-8")
		var+=1;	
		strf1.append(obj)
		if var == 6:
			break
	var=0
	for player in allplayers:
		var+=1
		if var <= 6:
			continue 
		obj={}
		obj['index']=player.id
		obj["jno"]=str(player.jno);
		obj["name"]=player.fname+" "+player.lname;
		obj["image"]=b64encode(player.data).decode("utf-8")
		strf2.append(obj)

	db.create_all()
	allplayers=User.query.filter(User.id>11,User.id<=16)
	stf=[]
	for player in allplayers:
		obj={}
		obj['index']=player.id
		obj["jno"]=str(player.jno);
		obj["name"]=player.fname+" "+player.lname;
		obj["image"]=b64encode(player.data).decode("utf-8")
		stf.append(obj)
		list_all.append(obj)

	db.create_all()
	allplayers=User.query.filter(User.id>16,User.id<=27)
	srf1=[]
	srf2=[]
	srf3=[]
	for player in allplayers:
		obj={}
		obj['index']=player.id
		obj["jno"]=str(player.jno);
		obj["name"]=player.fname+" "+player.lname;
		obj["image"]=b64encode(player.data).decode("utf-8")
		srf3.append(obj)
		list_all.append(obj)
	var=0
	for player in allplayers:
		obj={}
		obj['index']=player.id
		obj["jno"]=str(player.jno);
		obj["name"]=player.fname+" "+player.lname;
		obj["image"]=b64encode(player.data).decode("utf-8")
		var+=1
		srf1.append(obj)
		if var == 6:
			break
	var=0
	for player in allplayers:
		var+=1
		if var<=6:
			continue
		obj={}
		obj['index']=player.id
		obj["jno"]=str(player.jno);
		obj["name"]=player.fname+" "+player.lname;
		obj["image"]=b64encode(player.data).decode("utf-8")
		srf2.append(obj)
	

	db.create_all()
	allplayers=User.query.filter(User.id>27 ,User.id<=32)
	trf=[]
	for player in allplayers:
		obj={}
		obj['index']=player.id
		obj["jno"]=str(player.jno);
		obj["name"]=player.fname+" "+player.lname;
		obj["image"]=b64encode(player.data).decode("utf-8")
		trf.append(obj)
		list_all.append(obj)

	return render_template('annotation.html',all_players=list_all,team1_play=strf3,team1_play_6=strf1,team1_play_5=strf2,team1_subs=stf,team2_play_6=srf1,team2_play=srf3,team2_play_5=srf2,team2_subs=trf)



@app.route("/camera_left", methods = ['GET', 'POST'])
def vall():
    if request.method == 'POST':
	    tl=request.form['point1'].split();tl[0]=int(float(tl[0]));tl[1]=int(float(tl[1]));
	    tr=request.form['point2'].split();tr[0]=int(float(tr[0]));tr[1]=int(float(tr[1]));
	    bl=request.form['point3'].split();bl[0]=int(float(bl[0]));bl[1]=int(float(bl[1]));
	    br=request.form['point4'].split();br[0]=int(float(br[0]));br[1]=int(float(br[1]));
	
	    lst=[tr, tl,br,bl]
	    print(lst)
	    try:
	        create_homography(lst,"left")
	        return render_template("left.html")

	    except Exception as e:
	        return "error"

    else:
	    return render_template('left.html');

@app.route("/camera_right", methods = ['GET', 'POST'])
def valr():
    if request.method == 'POST':
	    tl=request.form['point1'].split();tl[0]=int(float(tl[0]));tl[1]=int(float(tl[1]));
	    tr=request.form['point2'].split();tr[0]=int(float(tr[0]));tr[1]=int(float(tr[1]));
	    bl=request.form['point3'].split();bl[0]=int(float(bl[0]));bl[1]=int(float(bl[1]));
	    br=request.form['point4'].split();br[0]=int(float(br[0]));br[1]=int(float(br[1]));
	
	    lst=[tr, tl,br,bl]
	    print(lst)
	    try:
	        create_homography(lst,"right")
	        return render_template("right.html")

	    except Exception as e:
	        return "error"

    else:
	    return render_template('right.html');

@app.route("/camera_center", methods = ['GET', 'POST'])
def valc():
    if request.method == 'POST':
	    tl=request.form['point1'].split();tl[0]=int(float(tl[0]));tl[1]=int(float(tl[1]));
	    tr=request.form['point2'].split();tr[0]=int(float(tr[0]));tr[1]=int(float(tr[1]));
	    bl=request.form['point3'].split();bl[0]=int(float(bl[0]));bl[1]=int(float(bl[1]));
	    br=request.form['point4'].split();br[0]=int(float(br[0]));br[1]=int(float(br[1]));
	
	    lst=[bl, br, tl, tr]
	    print(lst)
	    try:
	        create_homography(lst,"center")
	        return render_template("center.html")

	    except Exception as e:
	        return "error"

    else:
	    return render_template('center.html');

@app.route("/player", methods = ["GET"])
def play():
    f = open("assets/data.json", "rb")
    return json.loads(f.read())

@app.route("/final_image", methods = ["GET"])
def final():
	img1 = cv2.imread("static/images/projections/left/full_warped1.jpg")
	img2 = cv2.imread("static/images/projections/right/full_warped1.jpg")
	img3 = cv2.imread("static/images/projections/center/full_warped1.jpg")
	dst = cv2.add(img1, img2)
	dst = cv2.add(dst, img3)
	ret, jpeg = cv2.imencode('.jpg', dst)
	response = make_response(jpeg.tobytes())
	response.headers['Content-Type'] = 'image/png'
	return response

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r



if __name__ == "__main__":
    app.run(port=4000)


