from story.chapterBase import ChapterBase
from character.character import Character
from story.chapter4Data.overlay import GUI as Overlay

FINAL = [
    "O. Mike: What a night. Now let's see what the news got today.",
    "I even made it to the headline news today. But yeah, let's see what else is in the news.",
    "Ah, our team won the championship. Well, that's good news, they haven't won in ages.",
    "Quite a lot of good news for the News Hound. Anyways, back to work."
]

FINAL_ALICA = [
    "O. Mike: Oh, Ms Alica. How may I help you today? I hope you feel alright after what has hapened.",
    "Alica: No no Officer, I just wanted to come by and thank you again for saving me from those bad guys.",
    "O. Mike: I've just done my job.",
    "Alica: You've done so much more than that. Thank you. I need to go now. There's some unfinished business I need to atend."
]

class Chapter4B(ChapterBase):
    def __init__(self, rootParent):
        ChapterBase.__init__(self, "chapter4/office.png", rootParent)

        self.overlay = Overlay(rootParent)
        self.overlay.newspaper["image"] = "chapter4/newspaperB.png"

        self.startPos = (0.5, 0, -0.3)

        base.messenger.send("animateChar", ["idle", "l", 3, True])

        self.accept("continue", self.readNewspaper)
        base.messenger.send("showText", [FINAL.copy()])

        self.alica = Character(rootParent, (0.3, 0, -0.3), "alica", "alica")
        self.alica.animate("idle", "r", 3)

        self.accept("mike", self.talkMike)

    def destroy(self):
        self.overlay.destroy()
        self.alica.destroy()
        ChapterBase.destroy(self)

    def readNewspaper(self):
        self.overlay.newspaper.hide()
        self.accept("alica", self.talkAlica)

    def talkAlica(self):
        self.accept("continue", base.messenger.send, extraArgs=["switchToChapter", ["chapterEndB"]])
        base.messenger.send("showText", [FINAL_ALICA.copy()])

    def talkMike(self):
        base.messenger.send("showNote", ["Ms Alica is here, I should talk with her."])
