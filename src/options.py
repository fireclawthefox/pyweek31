#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectSlider import DirectSlider
from direct.gui.DirectCheckButton import DirectCheckButton
from direct.gui.DirectButton import DirectButton
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):

        self.volume = DirectSlider(
            pos=LPoint3f(0.2, 0, 0.325),
            text='Volume',
            text_pos=(-1.05, -0.02),
            text_fg=(1,1,1,1),
            text_scale=0.1,
            text_align=TextNode.ARight,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["volumeChange"],
        )
        self.volume.setTransparency(0)

        self.audioMute = DirectCheckButton(
            frameSize=(-2.925000047683716, 3.024999713897705, -0.225, 0.8250000238418579),
            pos=LPoint3f(0, 0, 0),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Mute',
            parent=rootParent,
            command=self.toggleMute,
        )
        self.audioMute.setTransparency(0)

        self.btnBack = DirectButton(
            frameSize=(-1.5249999523162843, 1.6499999523162843, -0.21250001192092896, 0.8250000238418579),
            pos=LPoint3f(0, 0, -0.575),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Back',
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["optionBack"],
            pressEffect=1,
        )
        self.btnBack.setTransparency(0)

        self.fullscreen = DirectCheckButton(
            frameSize=(-3.35, 2.6, -0.213, 0.825),
            pos=LPoint3f(0.045, 0, -0.175),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Fullscreen',
            parent=rootParent,
            command=self.toggleFullscreen,
        )
        self.fullscreen.setTransparency(0)


    def show(self):
        self.volume.show()
        self.audioMute.show()
        self.btnBack.show()
        self.fullscreen.show()

    def hide(self):
        self.volume.hide()
        self.audioMute.hide()
        self.btnBack.hide()
        self.fullscreen.hide()

    def destroy(self):
        self.volume.destroy()
        self.audioMute.destroy()
        self.btnBack.destroy()
        self.fullscreen.destroy()
