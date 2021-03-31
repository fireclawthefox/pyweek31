from direct.gui.DirectButton import DirectButton
from panda3d.core import Texture
from panda3d.core import SamplerState
from direct.interval.IntervalGlobal import Sequence, Parallel, Func, Wait

class Character(DirectButton):
    def __init__(self, rootParent, pos, charFolder, charEvt):

        self.btn = DirectButton(
            image="characters/{}/idle_l1.png".format(charFolder),
            frameColor=(0, 0, 0, 0),
            frameSize=(-0.5, 0.5, -1, 1),
            scale=0.15,
            pos=pos,
            parent=rootParent,
            command=base.messenger.send,
            extraArgs=[charEvt],
            pressEffect=True)
        self.btn.setTransparency(1)
        self.animation = None
        self.charFolder = charFolder
        self.movement = None

    def stop(self):
        if self.animation is not None:
            self.animation.finish()
        if self.movement is not None:
            self.movement.finish()

    def destroy(self):
        self.stop()
        self.btn.destroy()

    def setStart(self, newPos):
        if self.movement is not None:
            self.movement.finish()

        self.btn.setPos(newPos)

    def animate(self, animation, direction, framecount, stopMovement=False):
        if stopMovement and self.movement is not None:
            self.movement.finish()

        if self.animation is not None:
            self.animation.finish()
        self.animation = self.getAnimation(animation, direction, framecount)
        self.animation.loop()

    def getAnimation(self, animationName, direction, framecount):
        delay = Wait(0.3)
        animation = Sequence()

        for i in range(1, framecount):
            path = "characters/{}/{}_{}{}.png".format(
                self.charFolder,
                animationName,
                direction,
                i)
            animation.append(Func(self.setFrame, path))
            animation.append(delay)

        return animation

    def setFrame(self, path):
        self.btn.setImage(path)
        tex = self.btn.component("image0").getTexture()
        tex.setMagfilter(SamplerState.FT_nearest)
        tex.setMinfilter(SamplerState.FT_nearest)

    def moveTo(self, newPos):
        self.animation.finish()
        direction = ""
        if newPos[0] > self.btn.getX():
            direction = "r"
        else:
            direction = "l"
        self.movement = Sequence(
            Func(self.animate, "run", direction, 4),
            self.btn.posInterval(3.0, newPos),
            Func(self.animate, "idle", direction, 3),
            )
        self.movement.start()
