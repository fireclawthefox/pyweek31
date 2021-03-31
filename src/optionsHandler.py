from options import GUI
from direct.showbase.DirectObject import DirectObject
from panda3d.core import WindowProperties

class OptionsHandler(GUI, DirectObject):
    def __init__(self):
        GUI.__init__(self)

        self.windowSizeX = base.win.getXSize()
        self.windowSizeY = base.win.getYSize()


        volume = base.musicManager.getVolume()
        self.volume["value"] = volume

        if base.AppHasAudioFocus:
            self.audioMute["indicatorValue"] = False
        else:
            self.audioMute["indicatorValue"] = True

        if base.win.isFullscreen():
            self.fullscreen["indicatorValue"] = True
        else:
            self.fullscreen["indicatorValue"] = False

        self.accept("volumeChange", self.changeVolume)
        self.accept("optionBack", base.messenger.send, extraArgs=["exit"])

    def destroy(self):
        self.ignoreAll()
        GUI.destroy(self)

    def changeVolume(self):
        base.musicManager.setVolume(self.volume["value"])
        base.sfxManagerList[0].setVolume(self.volume["value"])

    def toggleMute(self, value):
        if self.audioMute["indicatorValue"]:
            base.disableAllAudio()
        else:
            base.enableAllAudio()

        base.enableSoundEffects(self.audioMute["indicatorValue"])
        base.enableMusic(self.audioMute["indicatorValue"])

    def toggleFullscreen(self, value):
        # global variables... in production code, better use class variables!

        # get the window properties and clear them
        props = WindowProperties()
        props.clear()
        props.clearFullscreen()
        props.clearSize()

        # are we fullscreen yet
        fullscreen = base.win.isFullscreen()
        # for clarity set a variable that determines to which state
        # we want to switch
        changeToFullscreen = not fullscreen

        # if we are in windowed mode, save the current window size for
        # resetting it later
        if not fullscreen:
            self.windowSizeX = base.win.getXSize()
            self.windowSizeY = base.win.getYSize()

        # set the new window size
        x = self.windowSizeX
        y = self.windowSizeY
        if changeToFullscreen:
            di = base.pipe.getDisplayInformation()
            x = di.getDisplayModeWidth(0)
            y = di.getDisplayModeHeight(0)
        props.setSize(x, y)

        # set the fullscreen property
        props.setFullscreen(changeToFullscreen)
        props.setUndecorated(changeToFullscreen)

        base.win.requestProperties(props)
        base.taskMgr.step()
