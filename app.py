
from flask import Flask, render_template, request
from random_walk import RandomWalk
import base64

app = Flask(__name__)

@app.route('/',methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        position = [int(request.form.get("xcoordinate")),int(request.form.get("ycoordinate"))]
        probabilities = [int(request.form['up']),int(request.form['right']),int(request.form['down']),int(request.form['left'])]
        numiters = int(request.form['numberofiterations'])
        plot = plot_walker(numiters=numiters, probabilities=probabilities, position=position)
        return render_template('index.html', image = plot)

    return render_template('index.html')

def plot_walker(numiters=100,probabilities=[25,25,25,25],position=[0,0]):
    
    walk = RandomWalk(*position,*probabilities)
    walk.walk(numiters)
    img= walk.visualise_bytesio()
    return 'data:image/png;base64,' + base64.b64encode(img.getvalue()).decode()




