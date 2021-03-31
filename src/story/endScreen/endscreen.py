#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectLabel import DirectLabel
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):

        self.frmBack = DirectFrame(
            frameColor=(0.0, 0.0, 0.0, 1.0),
            frameSize=(-0.8, 0.8, -0.8, 0.8),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.frmBack.setTransparency(0)

        self.pg671 = DirectLabel(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-0.893750011920929, 1.0187499523162842, -0.11250001192092896, 0.7124999761581421),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 0.5),
            scale=LVecBase3f(0.2, 0.2, 0.2),
            text='END',
            text_align=TextNode.A_center,
            text_scale=(1.0, 1.0),
            text_pos=(0, 0),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmBack,
        )
        self.pg671.setTransparency(0)

        self.lblEnding = DirectLabel(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-8.0, 8.0, -0.325, 0.75),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0.025, 0, -0.675),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text="You've found ending x/x",
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmBack,
        )
        self.lblEnding.setTransparency(0)

        self.pg6340 = DirectLabel(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-0.893750011920929, 1.0187499523162842, -0.11250001192092896, 0.7124999761581421),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-0.125, 0, 0.65),
            scale=LVecBase3f(0.05, 0.05, 0.05),
            text='the',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmBack,
        )
        self.pg6340.setTransparency(0)

        self.pg1228 = DirectLabel(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-8.0, 8.0, -0.325, 0.75),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 0.35),
            scale=LVecBase3f(0.05, 0.1, 0.056),
            text='A Game By',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmBack,
        )
        self.pg1228.setTransparency(0)

        self.pg1785 = DirectLabel(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-8.0, 8.0, -0.325, 0.75),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 0.275),
            scale=LVecBase3f(0.08, 0.1, 0.08),
            text='Fireclaw',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmBack,
        )
        self.pg1785.setTransparency(0)

        self.pg4435 = DirectLabel(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-8.0, 8.0, -0.325, 0.75),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 0.175),
            scale=LVecBase3f(0.05, 0.1, 0.056),
            text='Music from Jamendo by Golden Antelope',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmBack,
        )
        self.pg4435.setTransparency(0)

        self.pg5320 = DirectLabel(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            frameSize=(-8.0, 8.0, -0.325, 0.75),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0, 0, 0.1),
            scale=LVecBase3f(0.05, 0.1, 0.056),
            text='Audio from freesound by reinsamba',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(1, 1, 1, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=self.frmBack,
        )
        self.pg5320.setTransparency(0)


    def show(self):
        self.frmBack.show()

    def hide(self):
        self.frmBack.hide()

    def destroy(self):
        self.frmBack.destroy()
