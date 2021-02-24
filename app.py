import io
import os
from flask import Flask, render_template, request, url_for, flash, redirect, Response, send_file
from random_walk import RandomWalk
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure
from matplotlib import animation
import random
from PIL import Image, ImageDraw
import base64
from numpngw import AnimatedPNGWriter

app = Flask(__name__)

@app.route('/',methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        position = [int(request.form['xcoordinate']),int(request.form['ycoordinate'])]
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




