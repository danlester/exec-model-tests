from bokeh.layouts import column
from bokeh.models import Button, PreText
from bokeh.plotting import curdoc

from datetime import datetime

start_time = datetime.now()

p = PreText(text=str(start_time))

count = 1

def callback():
    global count

    count += 1

    p.text = "{}\nClicked! Start Time {}; Count {}".format(p.text, start_time, count)

button = Button(label="Increment")
button.on_click(callback)

# Put the button and text output in a layout and add to the document
curdoc().add_root(column(button, p))
