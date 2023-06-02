from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/getState")
def getState():
	# return render_template("getState.html")
	return "get state"
