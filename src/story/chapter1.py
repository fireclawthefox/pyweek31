from story.chapterBase import ChapterBase
from story.chapter1Data.overlay import GUI as Overlay

STORY_TELEPHONE = [
    "Officer Mike: Hello, Police station 31, this is officer Mike.",
    "Woman: H-Hello? I-I-I need help quick. I think someone is going to KILL me!",
    "O. Mike: Please, calmn down miss. What’s your name, where are you and who you think is after you?",
    "Woman: My name’s A-Alica. I’m in a warehouse in Delvin street 62. I’ve probably seen too much...",
    "In the distant through the phone you can hear men shouting.",
    "Alica: Oh no, I think they’ve found me!",
    "Screams are heared through the phone followed by a pistol shot.",
    "O. Mike: Hello, miss Alica, can you hear me, are you still there!",
    "The call ends abrupt.",
    "O. Mike: Oh sh*t, I’ve got to get there fast!",
    "O. Mike: Let’s pick up that flashlight from the desk first though. Then I’ll be ready to head out.",
]

class Chapter1(ChapterBase):
    def __init__(self, rootParent):
        ChapterBase.__init__(self, "chapter1/office.png", rootParent)
        self.startPos = (0.05, 0, -0.3)

        self.phoneCallDone = False
        self.collectedFlashlight = False

        self.overlay = Overlay(rootParent)

        self.start()

        self.ringAudio = loader.loadSfx("audio/34381__reinsamba__german-old-telephonering-1.ogg")
        self.ringAudio.play()

        base.messenger.send("showNote", ["The phone's ringing, I should pick it up"])

    def start(self):
        self.accept("chapter1_telephone", self.startTelephoneCall)
        self.accept("chapter1_flashlight", self.collectFlashlight)
        self.accept("chapter1_door", self.openDoor)
        self.accept("mike", self.mikeSay)

    def pause(self):
        self.ignoreAll()
        self.accept("continue", self.start)

    def destroy(self):
        self.ringAudio.stop()
        ChapterBase.destroy(self)
        self.overlay.destroy()

    def collectFlashlight(self):
        self.pause()
        if not self.phoneCallDone:
            base.messenger.send("showNote", ["O. Mike: I don't need this now."])
        else:
            self.collectedFlashlight = True
            self.overlay.btnFlashlight.hide()
            base.messenger.send("addInventory", ["flashlight", "chapter1/flashlight.png"])
            base.messenger.send("showNote", ["O. Mike: Ok, now let’s get out of here."])

    def startTelephoneCall(self):
        self.pause()
        self.ringAudio.stop()
        self.phoneCallDone = True
        self.overlay.ringRing.hide()
        base.messenger.send("moveChar", [(0.5, 0, -0.3)])
        base.messenger.send("showText", [STORY_TELEPHONE.copy()])

    def openDoor(self):
        self.pause()
        if not self.phoneCallDone:
            base.messenger.send("showNote", ["O. Mike: The phone is ringing, I should pick it up!"])
        elif not self.collectedFlashlight:
            base.messenger.send("showNote", ["O. Mike: I’m not ready yet, I’ll have to pick up the flashlight first!"])
        else:
            base.messenger.send("moveChar", [(-0.7, 0, -0.3)])
            base.messenger.send("switchToChapter", ["chapter2"])

    def mikeSay(self):
        if not self.phoneCallDone:
            base.messenger.send("showNote", ["The phone's ringing, just click on that thing on the right."])
        elif not self.collectedFlashlight:
            base.messenger.send("showNote", ["Don't you see that flashlight, it's on the table below me."])
        else:
            base.messenger.send("showNote", ["Just click on the door on the left side already. I don't have all night."])
