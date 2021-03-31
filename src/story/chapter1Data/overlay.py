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

        self.table = DirectFrame(
            frameColor=(1.0, 1.0, 1.0, 0.0),
            frameSize=(-1, 1, -1, 1),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter1/table.png',
            pos=LPoint3f(0.55, 0, -0.575),
            sortOrder=200,
            image_scale=LVecBase3f(0.256, 1, 0.312),
            image_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.table.setTransparency(1)

        self.btnFlashlight = DirectButton(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-0.4, 0.4, -0.4, 0.4),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter1/flashlight.png',
            pos=LPoint3f(0.39, 0, -0.39),
            sortOrder=201,
            relief=1,
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='',
            image_scale=LVecBase3f(0.4, 0, 0.4),
            image_pos=LPoint3f(0, 0, 0),
            text_align=TextNode.A_center,
            text_scale=(1.0, 1.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["chapter1_flashlight"],
            pressEffect=1,
        )
        self.btnFlashlight.setTransparency(1)

        self.btnTelephone = DirectButton(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-0.4, 0.4, -0.4, 0.4),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0.625, 0, -0.125),
            relief=1,
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["chapter1_telephone"],
            pressEffect=1,
        )
        self.btnTelephone.setTransparency(0)

        self.btnDoor = DirectButton(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-0.5, 0.5, -2.0, 2.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-0.75, 0, -0.125),
            relief=1,
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["chapter1_door"],
            pressEffect=1,
        )
        self.btnDoor.setTransparency(0)

        self.ringRing = DirectFrame(
            frameColor=(1.0, 1.0, 1.0, 0.0),
            frameSize=(-0.1, 0.1, -0.1, 0.1),
            hpr=LVecBase3f(0, 0, 0),
            image='chapter1/ringRing.png',
            pos=LPoint3f(0.5, 0, -0.025),
            image_scale=LVecBase3f(0.1, 1, 0.1),
            image_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.ringRing.setTransparency(1)


    def show(self):
        self.table.show()
        self.btnFlashlight.show()
        self.btnTelephone.show()
        self.btnDoor.show()
        self.ringRing.show()

    def hide(self):
        self.table.hide()
        self.btnFlashlight.hide()
        self.btnTelephone.hide()
        self.btnDoor.hide()
        self.ringRing.hide()

    def destroy(self):
        self.table.destroy()
        self.btnFlashlight.destroy()
        self.btnTelephone.destroy()
        self.btnDoor.destroy()
        self.ringRing.destroy()
