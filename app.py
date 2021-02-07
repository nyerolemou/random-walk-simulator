from flask import Flask, render_template, request, url_for, flash, redirect
from random_walk import RandomWalk

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'POST':
		position = [int(request.form['xcoordinate']),int(request.form['ycoordinate'])]
		probabilities = [int(request.form['up']),int(request.form['right']),int(request.form['down']),int(request.form['left'])]
		numiters = int(request.form['numberofiterations'])
		walker = RandomWalk(*position, *probabilities)
		walker.visualise

	return render_template('index.html')



