from direct.showbase.DirectObject import DirectObject
from gameScreen import GUI as GameScreen
from direct.gui.DirectDialog import YesNoDialog
from direct.interval.IntervalGlobal import Sequence, Parallel, Func
from direct.interval.LerpInterval import LerpColorScaleInterval, LerpColorInterval

from character.character import Character
from story.chapter1 import Chapter1
from story.chapter2 import Chapter2
from story.chapter3 import Chapter3
from story.chapter4A import Chapter4A
from story.chapter4B import Chapter4B
from story.chapterEndA import ChapterEndA
from story.chapterEndB import ChapterEndB

from inventory import Inventory

levelTree = {
    "chapter1":Chapter1,
    "chapter2":Chapter2,
    "chapter3":Chapter3,
    "chapter4A":Chapter4A,
    "chapter4B":Chapter4B,
    "chapterEndA":ChapterEndA,
    "chapterEndB":ChapterEndB,
}

class GameScreenHandler(DirectObject, GameScreen):
    def __init__(self):
        GameScreen.__init__(self)

        self.btnContinue.hide()

        self.mainChar = Character(self.frmContent.getCanvas(), (0,0,0), "mainChar", "mike")
        self.mainChar.animate("idle", "l", 3)
        self.mainChar.btn.reparentTo(self.frmContent.getCanvas(), 100)

        self.chapter = None
        self.inventory = Inventory(self.frmInventory)

        self.accept("quitGame", self.askQuit)
        self.accept("toggleAudio", self.toggleAudio)
        self.accept("switchToChapter", self.switchToChapter)
        self.accept("showText", self.showText)
        self.accept("showNote", self.showNote)
        self.accept("addInventory", self.addInventory)
        self.accept("getInventory", self.getInventory)
        self.accept("moveChar", self.mainChar.moveTo)
        self.accept("stopChar", self.mainChar.stop)
        self.accept("animateChar", self.mainChar.animate)

        if base.AppHasAudioFocus:
            self.btnAudioToggle["text"] = "Audio On"
        else:
            self.btnAudioToggle["text"] = "Audio Off"

        self.chapter = levelTree["chapter1"](self.frmContent.getCanvas())
        self.mainChar.btn.setPos(self.chapter.startPos)
        LerpColorInterval(self.frmFadeOverlay, 2.0, (0,0,0,0)).start()

    def askQuit(self):
        self.yesNoDialog = YesNoDialog(
            text="Realy Quit?",
            command=self.quitGame)

    def quitGame(self, yes):
        self.yesNoDialog.destroy()
        if yes:
            self.ignoreAll()
            self.mainChar.stop()
            self.mainChar.destroy()
            self.chapter.destroy()
            base.messenger.send("exit")

    def toggleAudio(self):
        if base.AppHasAudioFocus:
            base.disableAllAudio()
            self.btnAudioToggle["text"] = "Audio Off"
        else:
            base.enableAllAudio()
            self.btnAudioToggle["text"] = "Audio On"

    def setChapter(self, chapterName):
        if self.chapter is not None:
            del self.chapter
            self.chapter = None
        self.chapter = levelTree[chapterName](self.frmContent.getCanvas())

    def switchToChapter(self, chapterName):
        switchTo = Sequence(
            LerpColorInterval(self.frmFadeOverlay, 2.0, (0,0,0,1), (0,0,0,0)),
            Func(self.chapter.destroy),
            Func(self.setChapter, chapterName),
            Func(self.setStarPos),
            LerpColorInterval(self.frmFadeOverlay, 2.0, (0,0,0,0)),
        )
        switchTo.start()

    def setStarPos(self):
        self.mainChar.setStart(self.chapter.startPos)

    def showNote(self, text):
        self.lblStory["text"] = text
        base.messenger.send("continue")

    def showText(self, textQueue):
        self.btnContinue.show()
        self.textQueue = textQueue
        self.accept("story_continue", self.nextText)
        self.nextText()

    def nextText(self):
        if len(self.textQueue) <= 0:
            base.messenger.send("continue")
            self.ignore("story_continue")
            self.lblStory["text"] = ""
            self.btnContinue.hide()
            return

        text = self.textQueue[0]
        self.lblStory["text"] = text
        del self.textQueue[0]

    def addInventory(self, itemKey, itemImage):
        self.inventory.addItem(itemKey, itemImage)

    def getInventory(self):
        base.messenger.send("inventoryRequest", [self.inventory.inventoryList])
