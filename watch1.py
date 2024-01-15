import tkinter as tk

from datetime import datetime

import time



root = tk.Tk()

root.title('My Clock')

cnvs = tk.Canvas(width = 700, height = 300, background = '#27c85d')

cnvs.pack()

cnvs.create_text(350, 150, text = '', font = ('', 100), fill = 'blue', tags = 'MyText')

try:

    while True:

        now = datetime.now()

        s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)

        cnvs.itemconfig('MyText', text = s)

        cnvs.update()

        time.sleep(0.1)

except:

    pass

