#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectButton import DirectButton
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):

        self.overlay = DirectFrame(
            frameColor=(1.0, 1.0, 1.0, 0.0),
            frameSize=(-1, 1, -1, 1),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter4/overlay.png',
            pos=LPoint3f(0, 0, 0),
            sortOrder=200,
            image_scale=LVecBase3f(0.8, 1, 0.8),
            image_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.overlay.setTransparency(1)

        self.newspaper = DirectFrame(
            frameColor=(1.0, 1.0, 1.0, 0.0),
            frameSize=(-1, 1, -1, 1),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter4/newspaperA.png',
            pos=LPoint3f(0, 0, 0),
            sortOrder=200,
            image_scale=LVecBase3f(0.5, 1, 0.5),
            image_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.newspaper.setTransparency(1)




    def show(self):
        self.overlay.show()
        self.newspaper.show()

    def hide(self):
        self.overlay.hide()
        self.newspaper.hide()

    def destroy(self):
        self.overlay.destroy()
        self.newspaper.destroy()
