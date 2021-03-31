from story.chapterBase import ChapterBase
from story.chapter4Data.overlay import GUI as Overlay

FINAL = [
    "O. Mike: What a night. Now let's see what the news got today.",
    "Ah, our team won the championship. Well, that's good news, they haven't won in ages.",
    "Let's see what else we have.",
    "Woman found dead in hotel... Hm, what's this about.",
    "A woman was found dead, shot in a hotel room in the Farlain Hotel...",
    "Wait, that's the hotel I've been that night at the end of my shift!",
    "The womans name was Alica A. (32).",
    "Oh no... that's bad. I knew there was something foul with those shady guys. I could have saved her..."
]

class Chapter4A(ChapterBase):
    def __init__(self, rootParent):
        ChapterBase.__init__(self, "chapter4/office.png", rootParent)

        self.overlay = Overlay(rootParent)
        self.overlay.newspaper["image"] = "chapter4/newspaperA.png"

        self.startPos = (0.5, 0, -0.3)

        base.messenger.send("animateChar", ["idle", "l", 3, True])

        self.accept("continue", base.messenger.send, extraArgs=["switchToChapter", ["chapterEndA"]])
        base.messenger.send("showText", [FINAL.copy()])

    def destroy(self):
        self.overlay.destroy()
        ChapterBase.destroy(self)
