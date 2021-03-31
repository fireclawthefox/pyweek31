from direct.showbase.DirectObject import DirectObject
from story.endScreen.endscreen import GUI as EndScreen
from character.character import Character

class ChapterEndA(DirectObject):
    def __init__(self, rootParent):
        self.screen = EndScreen(rootParent)
        self.screen.lblEnding["text"] = "You've found ending 1/2"

        self.startPos = (0,0,-.3)
        base.messenger.send("animateChar", ["idle", "r", 3, True])

        self.accept("mike", self.giveHint)

    def destroy(self):
        self.screen.destroy()

    def giveHint(self):
        base.messenger.send("showNote", ["How could I let her die... I must have missed something in the warehouse!"])
