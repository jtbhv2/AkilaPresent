import tkinter as tk
import random
import json
import base64

class Item:
    def __init__(self, name, effect, description, essential=False):
        self.name = name
        self.effect = effect
        self.description = description
        self.essential = essential

    def use(self, game):
        self.effect(game)

def useScalpel(game):
    game.confidence += 100
    game.updateText("The ULTIMATE SCALPEL can slice through anything! Your CONFIDENCE skyrockets!.")

def useScrubTop(game):
    game.luck += 100
    game.updateText("The SCRUB TOP bends reality itself! Your LUCK skyrockets!")

def useCaseStudy(game):
    game.sexAppeal += 100
    game.updateText("This CASE STUDY implants all MEDICAL KNOWLEDGE into your brain! You become SEXY AS HELL.")


itemMasterList = {
"Ultimate Scalpel": Item("Ultimate Scalpel", useScalpel, 'A legendary scalpel capable of performing any surgery in a single stroke.', essential=True),
"Final Scrub Top": Item("Final Scrub Top", useScrubTop, 'A cosmic scrub top that will protect the wearer from all patients.', essential=True),
"Omega Case Study": Item("Omega Case Study", useCaseStudy, 'An intense case study that imparts its reader with all medical knowledge.', essential=True),
}

class AdventureGameUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='black')
        self.root.title("AKILA BLAZE and the ERYTHROCYTE CONSPIRACY")

        #Game flags
        self.flags = {
            'hasSuccumbed': False,
            'hasRedPager': False
        }

        # Player Stats
        self.confidence = 10
        self.luck = 0
        self.sexAppeal = 100
        self.inventory = {
            "Ultimate Scalpel":1,
            "Final Scrub Top":1,
            'Omega Case Study':1
            }
        self.maxUniqueItems = 10
        self.currentRoom = "dream"

        #Global Commands
        self.globalCommands = {'use', 'take', 'save', 'go', 'inventory', 'help', 'toss', 'search', 'examine'}

        #These rooms will not work if you try to 'go' to/from them
        self.restrictedRooms = {'dream'}
        # Room Descriptions and Commands
        self.rooms = {
            "dream": {
                "description": "You are back on MT SINAI, the villanous GENERAL ANESTHESIA in your grasp.\nThe battle was fangorious; the city behind you destroyed, the smell of burning ozone from the burned sky stings your nostrils.\nWIFE BRIAN lies dead on the ground next to you, having saved you from the General's fourth nuclear strike upon you.\nYour anger overtakes you! The General must be destroyed!\nUse the HEMOSTATIC ORDER and DESTROY the GENERAL!",
                "items": [],
                "commands": ["destroy"]
            },
            "home": {
                "description": "You are at home. The pets greet you."
                + ('\nYour Red Pager sits on the dresser.' if not self.flags.get('hasRedPager', False) else ""),
                "items": [],
                "commands": ['wife']
            },
            "testroom": {
                "description": "You are in a damp, dark basement. A coin slot is visible on the wall.",
                "items": ["Gold Coin", 'Torch', 'test', 'Test', 'test' ],
                "commands": []
            }
        }

        #Dynamic Commands
        #EXAMPLE (put this in processinput, this for instance ise search)
        #if self.currentRoom == 'basement' and 'flip switch' not in self.discoveredCommands['basement']:
            #self.discoveredCommands['basement'].add('flip switch')
            #self.updateText('You discovered a hidden switch!')
        self.discoveredCommands = {room: set(self.rooms[room]['commands']) for room in self.rooms}

        # Stats Labels
        self.confidenceVar = tk.StringVar()
        self.luckVar = tk.StringVar()
        self.sexAppealVar = tk.StringVar()
        self.locationVar = tk.StringVar()
        self.updateStats()

        tk.Label(root, textvariable=self.confidenceVar, anchor="w",bg="black", fg="green", font=("Courier", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(root, textvariable=self.luckVar, anchor="e", bg="black", fg="green", font=("Courier", 12)).grid(row=0, column=2, sticky="e", padx=10, pady=5)
        tk.Label(root, textvariable=self.sexAppealVar, anchor="w", bg="black", fg="green", font=("Courier", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Label(root, textvariable=self.locationVar, anchor='e', bg="black", fg="green", font=("Courier", 12)).grid(row=2, column=2, sticky='e', padx=10, pady=5)

        # Main Text Display
        self.textDisplay = tk.Text(root, height=15, width=70, state=tk.DISABLED, wrap="word")
        self.textDisplay.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
        self.textDisplay.config(bg="black", fg="green", insertbackground="green", font=("Courier", 12), padx=10, pady=10)

        # Input Field
        self.inputVar = tk.StringVar()
        self.inputEntry = tk.Entry(root, textvariable=self.inputVar, width=70)
        self.inputEntry.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
        self.inputEntry.config(bg="black", fg="green", insertbackground="green",insertwidth=4, font=("Courier", 12))
        self.inputEntry.bind("<Return>", self.processInput)

        self.loadGame()

        if self.currentRoom == 'dream':
            self.updateText(self.rooms[self.currentRoom]["description"])

    def processInput(self, event):
        command = self.inputVar.get().lower()
        self.inputVar.set("")
        self.displayInstantText(f"> {command}")
        allowedCommands = self.discoveredCommands[self.currentRoom] | self.globalCommands
        if any(command.startswith(cmd) for cmd in allowedCommands) or (command == 'succumb' and self.flags['hasSuccumbed']== False):
            if command.startswith("go"):
                destination = command.split(" ")[1]
                if self.currentRoom in self.restrictedRooms:
                    self.updateText('You cannot leave this place in that way.')
                elif destination in self.rooms and destination not in self.restrictedRooms:
                    self.currentRoom = destination
                    self.updateStats()
                    self.updateText(self.rooms[self.currentRoom]["description"])
                else:
                    self.updateText("You cannot go there.")
            elif command == 'succumb':
                self.flags["hasSuccumbed"] = True
                self.confidence += 100
                self.luck += 100
                self.sexAppeal +=900
                self.updateText('You curious little minx. Yep. I put in the same damn easter egg in this game.\nWhy Peepa wants to succumb? Do you not know that I love you? Keep that chin up, and keep that frown upside-down.\nREAL LIFE BRIAN loves you very much :)\nAlso, fine, take some crazy fucking stat boosts.')
            elif command == 'help':
                self.updateText(f'Commands you can always use: {', '.join(sorted(self.globalCommands))}')
            elif command == "search":
                #testblock starts here
                # if self.currentRoom == 'dream' and 'testaction' not in self.discoveredCommands['dream']:
                #     self.discoveredCommands['dream'].add('testaction')
                #     self.updateText('This is a testaction test text!')
                #     return
                #testblock ends here
                room = self.rooms[self.currentRoom]
                if room['items']:
                    itemList = ', '.join(room['items'])
                    self.updateText(f'You notice the following items in the room: {itemList}.')
                else:
                    self.updateText('You find no items of interest.')
            elif command.startswith('take'):
                itemName = command[5:].strip().lower()
                room = self.rooms[self.currentRoom]
                for item in room['items']:
                    if item.lower() == itemName:
                        if item in self.inventory:
                            self.inventory[item] += 1
                            self.updateText(f'You picked up another {itemName}!')
                        elif len(self.inventory) < self.maxUniqueItems:
                            self.inventory[item] = 1
                            self.updateText(f'You picked up the {itemName}')
                        else:
                            self.updateText('You have no room for this!')
                            return
                        room['items'].remove(item)  # Remove item from the room list
                        break
                    else:
                        self.updateText('There is no such item that you can take.')
            elif command.startswith('toss'):
                itemName = command[5:].strip().lower()
                matchingItem = next((i for i in self.inventory if i.lower() == itemName), None)
                if matchingItem:
                    if itemMasterList[matchingItem].essential:
                        self.updateText(f'You cannot toss {matchingItem}! You feel in your loins that this is too important!')
                    else:
                        self.inventory[matchingItem] -= 1
                        if self.inventory[matchingItem] == 0:
                            del self.inventory[matchingItem]
                        self.updateText(f'You tossed {matchingItem} away.')
                else:
                    self.updateText('Bro how tf are you gonna try to toss something you do not even have?')
            elif command == "destroy":
                if self.inventory:
                    self.updateText("Akila! You must use the ORDER to power yourself up first!")
                else:
                    self.updateText('As you go to destroy the GENERAL, she taunts you. "DOCTOR BLAZE, your brother is ALIVE! and he is-"\nYou awake in your bed, WIFE BRIAN sleeping sexually next to you')
                    self.currentRoom = 'home'
                    self.confidence = 10
                    self.luck = 0
                    self.sexAppeal = 100
                    self.updateText(self.rooms[self.currentRoom]["description"])
            elif command.startswith("use"):
                itemName = command[4:].strip().lower()
                matchingItem = next((i for i in self.inventory if i.lower() == itemName), None)
                if matchingItem and matchingItem in itemMasterList:
                    itemMasterList[matchingItem].use(self)  # Calls item effect with game instance
                    self.inventory[matchingItem] -= 1
                    if self.inventory[matchingItem] == 0:
                        del self.inventory[matchingItem]
                else:
                    self.updateText("You can't use that item.")
            elif command.startswith("examine"):
                itemName = command[8:].strip().lower()
                matchingItem = next((i for i in self.inventory if i.lower() == itemName), None)
                if matchingItem and matchingItem in itemMasterList:
                    self.updateText(f'{matchingItem}: {itemMasterList[matchingItem].description}')
                else:
                    self.updateText("You can't examine that.")
            elif command == "inventory":
                print(self.inventory)
                if not self.inventory:
                    self.updateText('Your inventory is empty.')
                else:
                    inventoryList = [f'{item} x {count}' if count > 1 else item for item, count in self.inventory.items()]
                    self.updateText(f'Inventory ({len(self.inventory)}/{self.maxUniqueItems} slots used): ' + ', '.join(inventoryList))
            elif command == 'save':
                self.saveGame()
        else:
            self.updateText("You can't do that here. Type help for a list of global commands.")

        self.updateStats()
        self.updateText(f'Commands: {', '.join(self.discoveredCommands[self.currentRoom])}')

    def updateText(self, text, index=0, speed=5):
        if hasattr(self, "textInProgress") and self.textInProgress:
            if not hasattr(self, "textQueue"):
                self.textQueue = []
            self.textQueue.append(text)  # Queue up the new text instead of canceling
            return

        self.textInProgress = True
        self.textDisplay.config(state=tk.NORMAL)
        self.inputEntry.config(state=tk.DISABLED, disabledbackground="black")

        def typeNextChar():
            nonlocal index
            if index < len(text):
                self.textDisplay.insert(tk.END, text[index])
                self.textDisplay.yview(tk.END)
                index += 1
                self.root.after(speed, typeNextChar)
            else:
                self.textDisplay.insert(tk.END, "\n")
                self.textDisplay.config(state=tk.DISABLED)
                self.inputEntry.config(state=tk.NORMAL)
                self.textInProgress = False

                # If there’s queued text, run it next
                if hasattr(self, "textQueue") and self.textQueue:
                    nextText = self.textQueue.pop(0)
                    self.updateText(nextText)

        typeNextChar()

    def displayInstantText(self, text):
        self.textDisplay.config(state=tk.NORMAL)
        self.textDisplay.insert(tk.END, text + "\n")
        self.textDisplay.yview(tk.END)
        self.textDisplay.config(state=tk.DISABLED)

    def updateStats(self):
        self.confidenceVar.set(f"Confidence: {self.confidence}")
        self.luckVar.set(f"Luck: {self.luck}")
        self.sexAppealVar.set(f"Sex Appeal: {self.sexAppeal}")
        self.locationVar.set(f'Location: {self.currentRoom.capitalize()}')

    def saveGame(self):
        saveData = {
            "currentRoom": self.currentRoom,
            "confidence": self.confidence,
            "luck": self.luck,
            "sexAppeal": self.sexAppeal,
            "inventory": self.inventory,
            "flags": self.flags,
            "discoveredCommands": {room: list(commands) for room, commands in self.discoveredCommands.items()},
            "roomItems": {room: self.rooms[room]["items"] for room in self.rooms},
        }

        jsonData = json.dumps(saveData)
        encodedData = base64.b64encode(jsonData.encode()).decode()

        with open("savegame.dat", "w") as file:
            file.write(encodedData)
        
        self.updateText("Game saved successfully!")

    def loadGame(self):
        try:
            with open("savegame.dat", "r") as file:
                encodedData = file.read()
                jsonData = base64.b64decode(encodedData).decode()
                saveData = json.loads(jsonData)

            self.currentRoom = saveData["currentRoom"]
            self.confidence = saveData["confidence"]
            self.luck = saveData["luck"]
            self.sexAppeal = saveData["sexAppeal"]
            self.inventory = saveData["inventory"]
            self.flags = saveData["flags"]
            self.discoveredCommands = {room: set(commands) for room, commands in saveData["discoveredCommands"].items()}
            
            # Restore room items
            for room, items in saveData["roomItems"].items():
                self.rooms[room]["items"] = items

            self.updateStats()
            self.updateText(f"Game loaded! You are in {self.currentRoom.capitalize()}.\n{self.rooms[self.currentRoom]['description']}")

        except FileNotFoundError:
            self.updateText("No save file found.")
        except Exception as e:
            self.updateText(f"Error loading save: {str(e)}")



if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureGameUI(root)
    root.mainloop()
