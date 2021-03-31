from direct.gui.DirectButton import DirectButton

class InventoryItem():
    def __init__(self, key, image, action, pos, rootParent):
        self.key = key
        self.btn = DirectButton(
            frameSize=(-0.1, 0.1, -0.1, 0.1),
            frameColor=(0, 0, 0, 0),
            text="",
            image=image,
            image_scale=0.1,
            command=base.messenger.send,
            extraArgs=[action],
            pos=pos,
            parent=rootParent
            )
        self.btn.setTransparency(1)

class Inventory():
    def __init__(self, rootParent):
        self.inventoryList = []
        self.rootParent = rootParent

    def addItem(self, key, image):
        self.inventoryList.append(
            InventoryItem(
                key,
                image,
                "inventory_{}".format(key),
                (0, 0, 0.4-(0.3*len(self.inventoryList))),
                self.rootParent
            )
        )
