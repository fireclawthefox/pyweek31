#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectScrolledFrame import DirectScrolledFrame
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectLabel import DirectLabel
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):
        
        self.frmInventory = DirectFrame(
            frameColor=(0.2, 0.2, 0.2, 1.0),
            frameSize=(-0.3, 0.3, -0.5, 0.5),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0.725, 0, 0.2),
            parent=rootParent,
        )
        self.frmInventory.setTransparency(0)

        self.frmContent = DirectScrolledFrame(
            canvasSize=(-0.8, 0.8, -0.8, 0.8),
            frameColor=(0.2, 0.2, 0.2, 1.0),
            frameSize=(-0.8, 0.8, -0.8, 0.8),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-0.475, 0, 0.1),
            scrollBarWidth=0.08,
            state='normal',
            horizontalScroll_borderWidth=(0.01, 0.01),
            horizontalScroll_frameSize=(-0.05, 0.05, -0.04, 0.04),
            horizontalScroll_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_pos=LPoint3f(0, 0, 0),
            horizontalScroll_decButton_borderWidth=(0.01, 0.01),
            horizontalScroll_decButton_frameSize=(-0.05, 0.05, -0.04, 0.04),
            horizontalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_decButton_pos=LPoint3f(0, 0, 0),
            horizontalScroll_incButton_borderWidth=(0.01, 0.01),
            horizontalScroll_incButton_frameSize=(-0.05, 0.05, -0.04, 0.04),
            horizontalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_incButton_pos=LPoint3f(0, 0, 0),
            horizontalScroll_thumb_borderWidth=(0.01, 0.01),
            horizontalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            horizontalScroll_thumb_pos=LPoint3f(0, 0, 0),
            verticalScroll_borderWidth=(0.01, 0.01),
            verticalScroll_frameSize=(-0.04, 0.04, -0.05, 0.05),
            verticalScroll_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_pos=LPoint3f(0, 0, 0),
            verticalScroll_decButton_borderWidth=(0.01, 0.01),
            verticalScroll_decButton_frameSize=(-0.04, 0.04, -0.05, 0.05),
            verticalScroll_decButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_decButton_pos=LPoint3f(0, 0, 0),
            verticalScroll_incButton_borderWidth=(0.01, 0.01),
            verticalScroll_incButton_frameSize=(-0.04, 0.04, -0.05, 0.05),
            verticalScroll_incButton_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_incButton_pos=LPoint3f(0, 0, 0),
            verticalScroll_thumb_borderWidth=(0.01, 0.01),
            verticalScroll_thumb_hpr=LVecBase3f(0, 0, 0),
            verticalScroll_thumb_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.frmContent.setTransparency(1)

        self.btnQuit = DirectButton(
            frameSize=(-3.0, 3.0, -0.3, 0.9),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0.725, 0, -0.85),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Quit',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["quitGame"],
            pressEffect=1,
        )
        self.btnQuit.setTransparency(0)

        self.btnAudioToggle = DirectButton(
            frameSize=(-3.0, 3.0, -0.3, 0.9),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0.725, 0, -0.7),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Audio On',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["toggleAudio"],
            pressEffect=1,
        )
        self.btnAudioToggle.setTransparency(0)

        self.frmBorderOverlay = DirectFrame(
            frameColor=(1.0, 1.0, 1.0, 0.0),
            frameSize=(-0.8, 0.8, -0.8, 0.8),
            hpr=LVecBase3f(0, 0, 0),
            image='gameScreen/border.png',
            pos=LPoint3f(-0.475, 0, 0.1),
            image_scale=LVecBase3f(0.8, 1, 0.8),
            image_pos=LPoint3f(0, 0, 0),
            parent=rootParent,
        )
        self.frmBorderOverlay.setTransparency(1)

        self.lblInventory = DirectLabel(
            frameColor=(0.8, 0.8, 0.8, 0.0),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0.725, 0, 0.775),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Inventory',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0.9, 0.9, 0.9, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
        )
        self.lblInventory.setTransparency(0)

        self.lblStory = DirectLabel(
            frameSize=(-0.125, 12.0, -0.313, 0.925),
            hpr=LVecBase3f(0, 0, 0),
            pad=(0.2, 0.2),
            pos=LPoint3f(-1.26, 0, -0.845),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='',
            text_align=TextNode.A_left,
            text_scale=(0.4, 0.4),
            text_pos=(0.0, 0.4),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=29.8,
            parent=rootParent,
        )
        self.lblStory.setTransparency(0)

        self.btnContinue = DirectButton(
            frameSize=(-1.8, 1.8, -0.3, 0.9),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(0.145, 0, -0.845),
            scale=LVecBase3f(0.1, 0.1, 0.1),
            text='Cont.',
            text_align=TextNode.A_center,
            text_scale=(1, 1),
            text_pos=(0, 0),
            text_fg=LVecBase4f(0, 0, 0, 1),
            text_bg=LVecBase4f(0, 0, 0, 0),
            text_wordwrap=None,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=["story_continue"],
            pressEffect=1,
        )
        self.btnContinue.setTransparency(0)

        self.frmFadeOverlay = DirectFrame(
            frameColor=(0.0, 0.0, 0.0, 1.0),
            frameSize=(-0.8, 0.8, -0.8, 0.8),
            hpr=LVecBase3f(0, 0, 0),
            pos=LPoint3f(-0.475, 0, 0.1),
            parent=rootParent,
        )
        self.frmFadeOverlay.setTransparency(1)


    def show(self):
        self.frmInventory.show()
        self.frmContent.show()
        self.btnQuit.show()
        self.btnAudioToggle.show()
        self.frmBorderOverlay.show()
        self.lblInventory.show()
        self.lblStory.show()
        self.btnContinue.show()
        self.frmFadeOverlay.show()

    def hide(self):
        self.frmInventory.hide()
        self.frmContent.hide()
        self.btnQuit.hide()
        self.btnAudioToggle.hide()
        self.frmBorderOverlay.hide()
        self.lblInventory.hide()
        self.lblStory.hide()
        self.btnContinue.hide()
        self.frmFadeOverlay.hide()

    def destroy(self):
        self.frmInventory.destroy()
        self.frmContent.destroy()
        self.btnQuit.destroy()
        self.btnAudioToggle.destroy()
        self.frmBorderOverlay.destroy()
        self.lblInventory.destroy()
        self.lblStory.destroy()
        self.btnContinue.destroy()
        self.frmFadeOverlay.destroy()
