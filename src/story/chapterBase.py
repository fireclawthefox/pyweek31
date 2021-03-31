from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectFrame import DirectFrame
from panda3d.core import SamplerState

class ChapterBase(DirectObject):
    def __init__(self, backgroundImage, rootParent):
        self.background = DirectFrame(
            image=backgroundImage,
            image_scale=.8,
            frameColor=(0, 0, 0, 0),
            frameSize=(-.8, .8, -.8, .8),
            scale=1,
            parent=rootParent)
        tex = self.background.component("image0").getTexture()
        tex.setMagfilter(SamplerState.FT_nearest)
        tex.setMinfilter(SamplerState.FT_nearest)

        self.startPos = (0,0,0)

    def destroy(self):
        self.ignoreAll()
        self.background.destroy()
