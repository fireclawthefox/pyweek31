from story.chapterBase import ChapterBase
from direct.gui.DirectFrame import DirectFrame
from panda3d.core import Point3
from story.chapter2Data.overlay import GUI as Overlay

STORY_BOX = [
    "O. Mike: Now look at that. There's fresh blood. This must be the place Alica called me from",
    "O. Mike: Oh, there's a card from a Hotel just around the corner, maybe they've gone there.",
    "O. Mike: I'm not sure I found everything, but I don't have more time, let's get going!"
]

class Chapter2(ChapterBase):
    def __init__(self, rootParent):
        ChapterBase.__init__(self, "chapter2/warehouse.png", rootParent)

        self.startPos = (-0.7, 0, -0.5)

        self.overlay = Overlay(rootParent)

        self.flashlightLight = DirectFrame(
            frameColor=(0.0, 0.0, 0.0, 1.0),
            frameSize=(-3.5, 3.5, -3.5, 3.5),
            image='chapter2/flashlightLight.png',
            image_scale=(3.5, 1, 3.5),
            parent=rootParent,
        )
        self.flashlightLight.setTransparency(1)
        self.flashLightActive = False

        self.accept("inventory_flashlight", self.activateFlashlight)

        self.accept("box1", self.box1)
        self.accept("box2", self.box2)
        self.accept("box3", self.box3)

        self.accept("mike", self.talkMike)

        base.messenger.send("animateChar", ["idle", "r", 3, True])
        base.messenger.send("showNote", ["I should turn on my flashlight"])

        base.taskMgr.add(self.flashlightTask, "flaslightLightTask")

    def destroy(self):
        base.taskMgr.remove("flaslightLightTask")
        ChapterBase.destroy(self)

    def talkMike(self):
        if self.flashLightActive:
            base.messenger.send("showNote", ["Wow! Such light. Much bright! ... Now I can check all the boxes!"])
        else:
            base.messenger.send("showNote", ["Yeah, who needs a lamp, I can just feel my way around here... Ouch my toe! Guess I should power up that lamp."])

    def activateFlashlight(self):
        if self.flashLightActive:
            self.flashlightLight["frameColor"] = (0,0,0,1)
            base.messenger.send("showNote", ["Without light, I won't see much in here..."])
        else:
            self.flashlightLight["frameColor"] = (0,0,0,0)
            base.messenger.send("showNote", ["That's better, now let's use that lightspot to search around this warehouse. (Light follows cursor)"])
        self.flashLightActive = not self.flashLightActive

    def flashlightTask(self, task):
        mwn = base.mouseWatcherNode
        if mwn.hasMouse():
            vMouse2render2d = Point3(mwn.getMouse()[0], 0, mwn.getMouse()[1])
            self.flashlightLight.setPos(render2d, vMouse2render2d)

        return task.cont

    def box1(self):
        base.messenger.send("addInventory", ["fakeID", "chapter2/fakeID.png"])
        base.messenger.send("showNote", ["O. Mike: Hey, look at that, fake ID cards of secret agents. This may be bigger than I thought..."])
        base.messenger.send("moveChar", [(-0.25, 0, -0.3)])

    def box2(self):
        base.messenger.send("showNote", ["O. Mike: A box full of weapons. Interesting, I'll better call the reinforcement to pick them up."])

    def box3(self):
        self.accept("continue", base.messenger.send, extraArgs=["switchToChapter", ["chapter3"]])
        base.messenger.send("moveChar", [(0.15, 0, -0.35)])
        base.messenger.send("showText", [STORY_BOX.copy()])
