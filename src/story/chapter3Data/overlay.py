#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectFrame import DirectFrame
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):

        self.pg202 = DirectFrame(
            frameColor=(1.0, 1.0, 1.0, 0.0),
            frameSize=(-1, 1, -1, 1),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter3/overlay.png',
            sortOrder=200,
            pos=LPoint3f(0, 0, 0),
            image_scale=LVecBase3f(0.8, 1, 0.8),
            image_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.pg202.setTransparency(1)


    def show(self):
        self.pg202.show()

    def hide(self):
        self.pg202.hide()

    def destroy(self):
        self.pg202.destroy()
