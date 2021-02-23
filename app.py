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

@app.route('/')
def index():
		
	return render_template('index.html')

@app.route("/plot.gif",methods=('GET', 'POST'))
def plot_walker(numiters,probabilities,position):
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        position = [int(request.form['xcoordinate']),int(request.form['ycoordinate'])]
        probabilities = [int(request.form['up']),int(request.form['right']),int(request.form['down']),int(request.form['left'])]
        numiters = int(request.form['numberofiterations'])
    """ renders the plot on the fly.
    """
    
    #walk = RandomWalk(0,0,25,25,25,25)
    #walk.walk(10)

    #img = io.BytesIO()
    #anim, fig = walk.visualise()

    #writer = AnimatedPNGWriter(fps=2)
    #Writer = animation.writers['pillow']
    #writer = Writer(fps=50, metadata=dict(artist='Me'), bitrate=1800)
    #anim.save('static/test.png', writer=writer, savefig_kwargs=img)
    #img.seek(0)
    
   ############

    #fig = Figure()
    #axis = fig.add_subplot(1, 1, 1)
    #x_points = range(numiters)
    #axis.plot(x_points, [random.randint(1, 30) for x in x_points])
    #fig.savefig(img)
    #img.seek(0)

    ############

    #walk = RandomWalk(0,0,25,25,25,25)
    #walk.walk(10)
    #anim, fig = walk.fig_setup()



    #N = 25          # number of frames

    # Create individual frames
    #frames = []
    #for n in range(N):
    #    frame = Image.new("RGB", (200, 150), (25, 25, 255*(N-n)//N))
    #    draw = ImageDraw.Draw(frame)
    #    x, y = frame.size[0]*n/N, frame.size[1]*n/N
    #    draw.ellipse((x, y, x+40, y+40), 'yellow')
        # Saving/opening is needed for better compression and quality
    #    fobj = io.BytesIO()
    #    frame.save(fobj, 'GIF')
    #    frame = Image.open(fobj)
    #    frames.append(frame)

    # Save the frames as animated GIF to BytesIO
    #animated_gif = io.BytesIO()
    #frames[0].save(animated_gif,
    #               format='GIF',
    #               save_all=True,
    #               append_images=frames[1:],      # Pillow >= 3.4.0
    #               delay=0.1,
    #               loop=0)
    #animated_gif.seek(0)
    walk = RandomWalk(*position, *probabilities)
    walk.walk(numiters)
    img= walk.visualise_bytesio()
    return send_file(img, mimetype='image/gif')
    
 

    #output = io.BytesIO()
    #FigureCanvasAgg(fig).print_png(output)
    #return Response(img.getvalue(), mimetype="image/gif")



