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
        
        self.frmMain = DirectFrame(
            frameColor=(1, 1, 1, 1),
            frameSize=(-1, 1, -1, 1),
            hpr=LVecBase3f(0, 0, 0),
            image='menu/background.png',
            pos=LPoint3f(0, 0, 0),
            image_scale=LVecBase3f(1, 1, 1),
            image_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.frmMain.setTransparency(0)

        self.btnStart = DirectButton(
            frameColor=(1.0, 1.0, 0.5, 0.1),
            frameSize=(-1.9, 1.8, -0.6, 0.6),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 0.46),
            relief=1,
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Start Game',
            text_align=TextNode.A_center,
            text_scale=(0.42, 0.4),
            text_pos=(0.03, -0.45),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmMain,
            command=base.messenger.send,
            extraArgs=["startGame"],
            pressEffect=1,
        )
        self.btnStart.setTransparency(0)

        self.btnOptions = DirectButton(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-1.825, 1.925, -0.437, 0.85),
            hpr=LVecBase3f(35, -28, 20),
            pos=LPoint3f(0.6, 0, -0.125),
            relief=1,
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Options',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0.7, 0.7, 0.7, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmMain,
            command=base.messenger.send,
            extraArgs=["options"],
            pressEffect=0,
        )
        self.btnOptions.setTransparency(0)

        self.btnExit = DirectButton(
            frameColor=(0.1, 0.7, 0.1, 1.0),
            frameSize=(-1.5249999523162843, 1.6499999523162843, -0.21250001192092896, 0.8250000238418579),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-0.45, 0, -0.6),
            relief=1,
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='EXIT',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0.9, 0.9, 0.9, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmMain,
            command=base.messenger.send,
            extraArgs=["exit"],
            pressEffect=0,
        )
        self.btnExit.setTransparency(0)


    def show(self):
        self.frmMain.show()

    def hide(self):
        self.frmMain.hide()

    def destroy(self):
        self.frmMain.destroy()
