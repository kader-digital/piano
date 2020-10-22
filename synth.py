from synthesizer import Waveform, Synthesizer, Player
from tkinter import *

root = Tk()

a1 = Button (root, text="A").grid(row=1, column=1)
a1_sh = Button (root, text="A#").grid(row=1, column=2)
b1 = Button (root, text="B").grid(row=1, column=3)
b1_sh = Button (root, text="B#").grid(row=1, column=4)
c1 = Button (root, text="C").grid(row=1, column=5)
c1_sh = Button (root, text="C#").grid(row=1, column=6)
d1 = Button (root, text="D").grid(row=1, column=7)
d1_sh = Button (root, text="D#").grid(row=1, column=8)
e1 = Button (root, text="E").grid(row=1, column=9)
f1 = Button (root, text="F").grid(row=1, column=10)
f1_sh = Button (root, text="F#").grid(row=1, column=11)
g1 = Button (root, text="G").grid(row=1, column=12)
g1_sh = Button (root, text="G#").grid(row=1, column=13)


root.mainloop()
