import tkinter as tk
import random

class AdventureGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Adventure Game")

        # Player Stats
        self.confidence = 10
        self.luck = 0
        self.sexAppeal = 1003
        self.inventory = []
        self.currentRoom = "forest"

        # Item Effects
        self.itemEffects = {
            "Berry": self.useBerry,
            "Old Book": self.useOldBook
        }

        # Room Descriptions and Commands
        self.rooms = {
            "forest": {
                "description": "You are in a dense forest. Paths lead to a cabin and a dark basement entrance.\nCommands: go cabin, go basement, search, inventory, use [item]",
                "items": ["Stick", "Berry"],
                "commands": ["go cabin", "go basement", "search", "inventory", "use"]
            },
            "cabin": {
                "description": "You are inside a cozy wooden cabin. There’s a locked chest here.\nCommands: go forest, search, open chest, inventory, use [item]",
                "items": ["Key", "Old Book"],
                "commands": ["go forest", "search", "open chest", "inventory", "use"]
            },
            "basement": {
                "description": "You are in a damp, dark basement. A coin slot is visible on the wall.\nCommands: go forest, search, insert coin, inventory, use [item]",
                "items": ["Gold Coin", "Torch"],
                "commands": ["go forest", "search", "insert coin", "inventory", "use"]
            }
        }

        # Stats Labels
        self.confidenceVar = tk.StringVar()
        self.luckVar = tk.StringVar()
        self.sexAppealVar = tk.StringVar()
        self.updateStats()

        tk.Label(root, textvariable=self.confidenceVar, anchor="w").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(root, textvariable=self.luckVar, anchor="e").grid(row=0, column=2, sticky="e", padx=10, pady=5)
        tk.Label(root, textvariable=self.sexAppealVar, anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=5)

        # Main Text Display
        self.textDisplay = tk.Text(root, height=15, width=50, state=tk.DISABLED, wrap="word")
        self.textDisplay.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        # Input Field
        self.inputVar = tk.StringVar()
        self.inputEntry = tk.Entry(root, textvariable=self.inputVar, width=50)
        self.inputEntry.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
        self.inputEntry.bind("<Return>", self.processInput)

        self.updateText(self.rooms[self.currentRoom]["description"])

    def processInput(self, event):
        command = self.inputVar.get().lower()
        self.inputVar.set("")
        self.updateText(f"> {command}")

        if command.startswith("go"):
            self.currentRoom = command.split(" ")[1]
            self.updateText(self.rooms[self.currentRoom]["description"])
        elif command == "search":
            if self.rooms[self.currentRoom]["items"]:
                found_item = self.rooms[self.currentRoom]["items"].pop(0)
                self.inventory.append(found_item)
                self.updateText(f"You found a {found_item}!")
            else:
                self.updateText("You found nothing.")
        elif command == "open chest" and "Key" in self.inventory:
            self.updateText("You open the chest and find a treasure!")
        elif command == "insert coin" and "Gold Coin" in self.inventory:
            self.updateText("You insert the coin and hear a mechanism unlock!")
        elif command.startswith("use"):
            item_name = command.split("use ")[1].title()
            if item_name in self.inventory and item_name in self.itemEffects:
                self.itemEffects[item_name]()
                self.inventory.remove(item_name)
                self.updateText(f"You used {item_name}.")
            else:
                self.updateText("You can't use that item.")
        elif command == "inventory":
            self.updateText(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        else:
            self.updateText("That command isn't available here.")

        self.updateStats()

    def useBerry(self):
        self.confidence += 5
        self.updateText("The berry was delicious! Your confidence increases by 5.")

    def useOldBook(self):
        self.luck += 2
        self.updateText("Reading the old book fills you with wisdom. Luck increases by 2.")

    def updateText(self, text):
        self.textDisplay.config(state=tk.NORMAL)
        self.textDisplay.insert(tk.END, text + "\n")
        self.textDisplay.config(state=tk.DISABLED)
        self.textDisplay.yview(tk.END)

    def updateStats(self):
        self.confidenceVar.set(f"Confidence: {self.confidence}")
        self.luckVar.set(f"Luck: {self.luck}")
        self.sexAppealVar.set(f"Sex Appeal: {self.sexAppeal}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureGameUI(root)
    root.mainloop()
