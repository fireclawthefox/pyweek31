from direct.showbase.DirectObject import DirectObject
from story.endScreen.endscreen import GUI as EndScreen
from character.character import Character

class ChapterEndB(DirectObject):
    def __init__(self, rootParent):
        self.screen = EndScreen(rootParent)
        self.screen.lblEnding["text"] = "You've found ending 2/2"

        self.startPos = (0.1,0,-.3)
        base.messenger.send("animateChar", ["idle", "l", 3, True])

        self.alica = Character(rootParent, (-0.1, 0, -.3), "alica", "alica")
        self.alica.animate("idle", "r", 3)

        self.accept("alica", self.talkAlica)
        self.accept("mike", self.talkMike)

    def destroy(self):
        self.alica.destroy()
        self.screen.destroy()

    def talkAlica(self):
        base.messenger.send("showNote", ["Thanks for playing!"])

    def talkMike(self):
        base.messenger.send("showNote", ["Good job!"])
