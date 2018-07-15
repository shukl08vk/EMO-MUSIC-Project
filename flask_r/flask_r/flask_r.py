import os
import sqlite3
import realTime
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask import Response
import time

app = Flask(__name__) # create the application instance :)
##app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
"""app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))"""
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#def connect_db():"""Connects to the specific database."""
 #   rv = sqlite3.connect(app.config['DATABASE'])
  #  rv.row_factory = sqlite3.Row
   # return rv

@app.route('/index')
def index():
    return render_template("index1.html")
	


@app.route('/index8')
def index8():
    return render_template("index3.html")
	
@app.route('/index6')	
def index6():
	print("\n")
	print("hello")
	return render_template("index3.html")
	
@app.route('/index7')
def index7():
	print("hii")
	return redirect(url_for('index6'))
	
	

	


@app.route('/index3',methods=['POST'])
def index3():
	i = request.form['output']
	print(i)
	index7()
	return (i)
	
	
	
@app.route('/index4')
def index4():
	return Response(open('templates/index4.html').read(), mimetype="text/html")
	
	
# save the image as a picture
@app.route('/image', methods=['POST'])
def image():
	i = request.files['image']  # get the image
	f = ('image1.png')
	i.save('%s' % (f))
	a=realTime.fun("haarcascade_frontalface_default.xml")
	a=str(a)
	return Response(a)
	
	



if __name__=='__main__':
    app.run(debug=True)