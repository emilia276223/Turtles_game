from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/getState")
def getState():
	return "get state"
