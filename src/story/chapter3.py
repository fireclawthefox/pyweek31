from story.chapterBase import ChapterBase
from story.chapter3Data.overlay import GUI as Overlay

from character.character import Character

STORY_ALICA = [
    "O. Mike: Miss Alica, are you alright?",
    "Alica: Oh my hero, thank you! You saved my life.",
]

STORY_BADGUY1_GOOD = [
    "Shady Guy: Hey, what are you doing here. This is secrete inteligence business.",
    "O. Mike: Oh, really? I don't think so!",
    "Shady Guy: And what makes you think so mister wise guy?",
    "O. Mike: I will show you! I've found something that you may recognize."
]

STORY_BADGUY1_FAILED = [
    "Shady Guy: Hey, what are you doing here. This is secrete inteligence business.",
    "O. Mike: Secret inteligence? You guys are fast. How come you already got here?",
    "Shady Guy: That's none of your business, now go get lost.",
    "O. Mike: Well, ok I guess you guys can handle this way better than I could... Though something feels odd about this."
]

STORY_BADGUY1_2 = [
    "O. Mike: I've found this ID cards in a warehouse nearby and it looks very much lie yours.",
    "O. Mike: And I guess the reinforcement coming after me will se it the same, so let me through now!",
    "Shady Guy: How.. Why... Sh*t, oh well, I'll let you pass, but my budy won't be that easy to convince."
]

STORY_BADGUY2 = [
    "Other Shady Guy: Hey, whatcha doin here?",
    "O. Mike: Your friend was so nice to let me pass and you should better do the same.",
    "O. Mike: I know you were after Alica and I also know you faked your agent IDs.",
    "O. Mike: So better play along nice or it will end really bad for you.",
    "Other Shady Guy: This's bigger then ya can handle. Ya may got us now, but I'll tell ya, this is not the last time ya'll see us...",
    "O. Mike: Don't even try to threaten me. The reinforcement is already waiting outside. So just get lost and let me to Alica.",
    "Other Shady Guy: Ha, that Girl won't say much if it'd be a clever Girl."
]

class Chapter3(ChapterBase):
    def __init__(self, rootParent):
        ChapterBase.__init__(self, "chapter3/hotel.png", rootParent)

        self.startPos = (-0.7, 0, -0.3)

        self.talkedBadGuy1 = False
        self.talkedBadGuy2 = False
        self.hasFakeIDs = False
        self.shownFakeID = False

        base.messenger.send("animateChar", ["idle", "r", 3, True])

        self.overlay = Overlay(rootParent)

        self.alica = Character(rootParent, (0.5, 0, -0.3), "alica", "alica")
        self.alica.animate("lie", "l", 3)

        self.badGuy1 = Character(rootParent, (-0.2, 0, -0.3), "badGuy1", "badGuy1")
        self.badGuy1.animate("idle", "l", 3)

        self.badGuy2 = Character(rootParent, (0.4, 0, -0.3), "badGuy2", "badGuy2")
        self.badGuy2.animate("idle", "l", 3)

        self.accept("badGuy1", self.talkBadGuy1)
        self.accept("badGuy2", self.talkBadGuy2)
        self.accept("alica", self.talkAlica)
        self.accept("mike", self.talkMike)

        self.accept("inventory_fakeID", self.showFakeID)
        self.accept("inventoryRequest", self.inventoryCheck)

        base.messenger.send("getInventory")

    def destroy(self):
        self.overlay.destroy()
        self.alica.destroy()
        self.badGuy1.destroy()
        self.badGuy2.destroy()

        ChapterBase.destroy(self)

    def inventoryCheck(self, inventory):
        for i in inventory:
            if i.key == "fakeID":
                self.hasFakeIDs = True

    def talkMike(self):
        if not self.talkedBadGuy1:
            base.messenger.send("showNote", ["Let's talk with that guy in front of me."])
        elif not self.shownFakeID:
            base.messenger.send("showNote", ["Now's the time to select the Fake IDs from my inventory"])
        elif not self.talkedBadGuy2:
            base.messenger.send("showNote", ["That guy is letting me pass, I should speakk with that other one in the next room"])
        else:
            base.messenger.send("showNote", ["C'mon, Alica is there waiting for me!"])

    def talkBadGuy1(self):
        if not self.talkedBadGuy1:
            self.talkedBadGuy1 = True
            base.messenger.send("moveChar", [(-0.4, 0, -0.3)])
            if self.hasFakeIDs:
                base.messenger.send("showText", [STORY_BADGUY1_GOOD.copy()])
            else:
                self.accept("continue", base.messenger.send, extraArgs=["switchToChapter", ["chapter4A"]])
                base.messenger.send("showText", [STORY_BADGUY1_FAILED.copy()])
        elif not self.shownFakeID:
            base.messenger.send("showNote", ["Why are you still around, you disturb our ascertainment. Go get lost!"])
        else:
            base.messenger.send("showNote", ["You already got me, just go on, my buddy won't be so easy."])

    def showFakeID(self):
        if not self.talkedBadGuy1:
            base.messenger.send("showNote", ["It's not the right time for it yet. I should talk to that guy in front of me first."])
        elif not self.shownFakeID:
            self.shownFakeID = True
            base.messenger.send("showText", [STORY_BADGUY1_2.copy()])
        else:
            base.messenger.send("showNote", ["The guys already saw them and should play along nice... for now."])

    def talkBadGuy2(self):
        if not self.talkedBadGuy1 or not self.shownFakeID:
            base.messenger.send("showNote", ["Shady Guy: Where do you think you're going. You may not pass yet."])
        elif not self.talkedBadGuy2:
            self.talkedBadGuy2 = True
            base.messenger.send("moveChar", [(0.2, 0, -0.3)])
            base.messenger.send("showText", [STORY_BADGUY2.copy()])
        else:
            base.messenger.send("showNote", ["He remains silent."])

    def talkAlica(self):
        if not self.talkedBadGuy1 or not self.shownFakeID:
            base.messenger.send("showNote", ["Shady Guy: Where do you think you're going. You may not pass yet."])
        elif not self.talkedBadGuy2:
            base.messenger.send("showNote", ["Other Shady Guy: This is none of ya busines. Go get lost!"])
        else:
            self.accept("continue", base.messenger.send, extraArgs=["switchToChapter", ["chapter4B"]])
            base.messenger.send("moveChar", [(0.35, 0, -0.3)])
            base.messenger.send("showText", [STORY_ALICA.copy()])
