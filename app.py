from flask import Flask, render_template, request, url_for, flash, redirect
from random_walk import RandomWalk

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'POST':
		position = [request.form['x'],request.form['ycoordinate']]
		probabilities = [request.form['up'],request.form['right'],request.form['down'],request.form['left']]
		numiters = request.form['numberofiterations']
		walker = RandomWalk(*position, *probabilities)
		walker.visualise

	return render_template('index.html')



