import os
from tkinter import E, NW, Button
from mojangskin import MojangSkin, Skin, Model, Face, Bone, SkinAnimation, SkinCanvas

LOCAL = os.path.dirname(os.path.realpath(__file__))

CAPE = os.path.join(LOCAL, 'template', 'template_cape.png')
SKIN = os.path.join(LOCAL, 'template', 'template_classic.png')

def example1():
    skin = Skin(SKIN, Model.CLASSIC, CAPE)
    # skin = MojangSkin('legopitstop')
    doll = skin.paperdoll(Face.FRONT, 10.0, True)
    doll.show()

def example2():
    from tkinter import Tk, Canvas, W
    root = Tk()
    root.title('mojangskin')

    # The custom widget for displying widgets
    # skin = Skin(SKIN, Model.CLASSIC, CAPE)
    skin = MojangSkin('legopitstop')

    canvas = SkinCanvas(root, 10.0, width=600, height=600)
    canvas.create_paperdoll(150,150, skin, Face.FRONT, tag='my_tag', anchor=NW)

    # Bind all bones
    # canvas.tag_bind('my_tag', '<Enter>', lambda e: print('my_tag')) # Bind to all bones
    # Bind to each bone. If tag is not defined in self.create_paperdoll ignore it. example; 'my_tag.head' -> 'head'
    canvas.tag_bind('my_tag.head', '<Button-1>', lambda e: print('head'))
    canvas.tag_bind('my_tag.torso', '<Button-1>', lambda e: print('torso'))
    canvas.tag_bind('my_tag.left_arm', '<Button-1>', lambda e: print('left_arm'))
    canvas.tag_bind('my_tag.right_arm', '<Button-1>', lambda e: print('right_arm'))
    canvas.tag_bind('my_tag.left_leg', '<Button-1>', lambda e: print('left_leg'))
    canvas.tag_bind('my_tag.right_leg', '<Button-1>', lambda e: print('right_leg'))
    canvas.tag_bind('my_tag.cape', '<Button-1>', lambda e: print('cape'))
    # Bind to both left and right arms and legs
    # canvas.tag_bind('my_tag.arms', '<Button-1>', lambda e: print('arms'))
    # canvas.tag_bind('my_tag.legs', '<Button-1>', lambda e: print('legs'))
    canvas.grid(row=1,column=0,columnspan=2,sticky='nesw')

    # test animation
    test = SkinAnimation(canvas, 2500, loop=False)
    test.translate(500, 'my_tag', rel=(0,100))
    test.translate(1000, 'my_tag', rel=(100,0))
    test.translate(1500, 'my_tag', rel=(0,-100))
    test.translate(2000, 'my_tag', rel=(-100,0))

    # Play stop animation
    Button(root, text='Play', command=test.play).grid(row=0,column=0,sticky=E)
    Button(root, text='Stop', command=test.stop).grid(row=0,column=1,sticky=W)

    # Responsive
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


    root.mainloop()

example2()