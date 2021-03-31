#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectButton import DirectButton
from direct.gui.DirectFrame import DirectFrame
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):

        self.btnBox1 = DirectButton(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-1.0, 1.0, -1.0, 1.0),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter2/box1.png',
            pos=LPoint3f(-0.25, 0, -0.35),
            relief=1,
            scale=LVecBase3f(0.05, 0.08, 0.05),
            text='',
            image_scale=LVecBase3f(1, 1, 1),
            image_pos=LPoint3f(0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(1.0, 1.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["box1"],
            pressEffect=0,
        )
        self.btnBox1.setTransparency(1)

        self.btnBox2 = DirectButton(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-1.0, 1.0, -1.0, 1.0),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter2/box2.png',
            pos=LPoint3f(0.4, 0, 0.16),
            relief=1,
            scale=LVecBase3f(0.05, 0.08, 0.05),
            text='',
            image_scale=LVecBase3f(1, 1, 1),
            image_pos=LPoint3f(0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["box2"],
            pressEffect=0,
        )
        self.btnBox2.setTransparency(1)

        self.btnBox3 = DirectButton(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-1.0, 1.0, -1.0, 1.0),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter2/box3.png',
            pos=LPoint3f(0.305, 0, -0.435),
            relief=1,
            scale=LVecBase3f(0.08, 0.1, 0.08),
            text='',
            image_scale=LVecBase3f(1, 1, 1),
            image_pos=LPoint3f(0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["box3"],
            pressEffect=0,
        )
        self.btnBox3.setTransparency(1)

        self.overlay = DirectFrame(
            frameColor=(1.0, 1.0, 1.0, 0.0),
            frameSize=(-0.8, 0.8, -0.8, 0.8),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter2/overlay.png',
            pos=LPoint3f(0, 0, 0),
            image_scale=LVecBase3f(0.8, 1, 0.8),
            image_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.overlay.setTransparency(1)


    def show(self):
        self.btnBox1.show()
        self.btnBox2.show()
        self.btnBox3.show()
        self.overlay.show()

    def hide(self):
        self.btnBox1.hide()
        self.btnBox2.hide()
        self.btnBox3.hide()
        self.overlay.hide()

    def destroy(self):
        self.btnBox1.destroy()
        self.btnBox2.destroy()
        self.btnBox3.destroy()
        self.overlay.destroy()
