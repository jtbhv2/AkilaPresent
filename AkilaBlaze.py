import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def show_splash():
    splash_root = tk.Tk()
    splash_root.overrideredirect(True)  # Removes the title bar

    # Load the image
    splash_image_path = resource_path(r"C:\Users\brian.stlouis\Documents\AkilaPresent\AkilaGameArt.webp")
    splash_image = Image.open(splash_image_path)
    splash_photo = ImageTk.PhotoImage(splash_image)

    # Get image dimensions
    img_width, img_height = splash_image.size

    # Get screen dimensions
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()

    # Calculate position to center the image
    x_position = (screen_width - img_width) // 2
    y_position = (screen_height - img_height) // 2

    # Set geometry to center the window, but now the height includes title bar
    splash_root.geometry(f"{img_width}x{img_height + 50}+{x_position}+{y_position}")

    # Create a Frame for the title bar
    title_bar_height = 50  # Height of the title bar
    title_frame = tk.Frame(splash_root, height=title_bar_height, bg="black")
    title_frame.pack(fill=tk.X, side=tk.TOP)

    # Add the title text to the title bar
    title_label = tk.Label(title_frame, text="AKILA BLAZE and the HEMOSTATIC ORDER", fg="white",
                           font=("Helvetica", 24, "bold"), bg="black", anchor=tk.CENTER)
    title_label.pack(side=tk.TOP, fill=tk.X)

    # Create a Canvas for the image background
    canvas = tk.Canvas(splash_root, width=img_width, height=img_height, highlightthickness=0)
    canvas.pack()

    # Add the image as a background below the title bar
    canvas.create_image(0, 0, anchor=tk.NW, image=splash_photo)

    # Display splash for 4 seconds
    splash_root.after(4000, splash_root.destroy)

    splash_root.mainloop()

# Show splash screen
show_splash()
#-------------------ABOVE THIS LINE IS THE IMAGE HANDLER------------------------------#
debugMode = True #this will be false when the time comes
sexAppeal = 100
LUCK = 0
hasRedPager = True
CONFIDENCE = 10
surgerySuccess = True
hasUltimateScalpel = False
hasOmegaCaseStudy = False
hasFinalScrubTop = False
collectedArtifacts = 0
secretVisited = False
import random
import time
def slowPrint(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def setVariable(name, value):
    globals()[name] = value
    if debugMode == True:
        slowPrint(f'{name} updated to {value}')
def prologue():
    global CONFIDENCE

    slowPrint("Welcome! You are DOCTOR AKILA B BLAZE: Pediatric surgeon by day, fierce adventurer by night.")
    slowPrint('You get very little sleep, what with all the surgery and adventuring.')
    slowPrint("Today, you only have one case! And it is a simple appendectomy.")
    slowPrint("Make the right choices to complete the surgery successfully. Good luck, DOCTOR BLAZE!")

    def step_one():
        global surgerySuccess
        slowPrint("\nStep 1: Preoperative Assessment.")
        choice = input("Do you choose to perform a thorough physical exam and order a CT scan or only rely on physical exam findings? (CT scan/physical exam) ").strip().lower()
        if choice == "ct scan":
            step_two()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Incomplete assessment leads to complications. Surgery cannot proceed.")

    def step_two():
        global surgerySuccess
        slowPrint("\nStep 2: Anesthesia Preparation.")
        choice = input("Do you choose to use endotracheal intubation or laryngeal mask airway (LMA) for anesthesia? (intubation/LMA) ").strip().lower()
        if choice == "intubation":
            step_three()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Inadequate airway management can lead to complications. Surgery is compromised.")

    def step_three():
        global surgerySuccess
        slowPrint("\nStep 3: Surgical Approach.")
        choice = input("Do you opt for an open appendectomy or a laparoscopic approach? (open/laparoscopic) ").strip().lower()
        if choice == "laparoscopic":
            step_four()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Open approach is less ideal for this case. Increased risk of complications.")

    def step_four():
        global surgerySuccess
        slowPrint("\nStep 4: Surgical Technique.")
        choice = input("During the surgery, do you use monopolar cautery or bipolar cautery for hemostasis? (monopolar/bipolar) ").strip().lower()
        if choice == "bipolar":
            step_complication()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Monopolar cautery can lead to excessive bleeding. Surgery is at risk.")

    def step_complication():
        global surgerySuccess
        slowPrint("\nComplication: Unexpected Hemorrhage.")
        slowPrint("While performing the procedure, you encounter unexpected hemorrhage due to bleeding from a small artery.")
        choice = input("Do you choose to use hemostatic clips or apply direct pressure and suture? (clips/direct pressure) ").strip().lower()
        
        if choice == "clips":
            step_five()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Failure to control bleeding can lead to significant complications. Surgery is at risk.")

    def step_five():
        global surgerySuccess
        slowPrint("\nStep 5: Postoperative Care.")
        choice = input("Do you choose to use a broad-spectrum antibiotic prophylaxis or only a single antibiotic specific to the likely pathogens? (broad-spectrum/single) ").strip().lower()
        if choice == "broad-spectrum":
            finish()
        else:
            surgerySuccess = False
            end_game("Incorrect choice or complication not handled properly. Inadequate care can lead to infections or other issues.")

    def finish():
        global CONFIDENCE
        if surgerySuccess:
            slowPrint("\nCongratulations! The pediatric appendectomy was successful. You have gained CONFIDENCE. Excellent job, Surgeon!")
            setVariable('CONFIDENCE', CONFIDENCE + 3)
        else:
            slowPrint("\nThe surgery did not go well. You have lost CONFIDENCE. Better luck next time.")
            setVariable('CONFIDENCE', CONFIDENCE - 2)
        actOne()

    def end_game(message):
        global surgerySuccess
        slowPrint(message)
        finish()

    step_one()
    return surgerySuccess
def actOne():
    global CONFIDENCE, LUCK, hasRedPager
    def redPage():
        slowPrint('After the surgery, your RED PAGER goes off.')
        slowPrint('You think: Oh no! Not the RED PAGER! That is for personal emergencies only!')
        choice = input('Do you RESPOND to the RED PAGE, or do you IGNORE? ').strip().lower()
        
        if choice == 'ignore':
            actOneFailure()
        elif choice == 'respond':
            slowPrint('\nYou decide to respond to the RED PAGER. It turns out to be a genuine emergency.')
            slowPrint('DOCTOR FRIEND: AKILA! Your wife BRIAN has been kidnapped!')
            brianKidnapped()
            return choice  # End the function if responding
        
        else:
            slowPrint('I do not understand your choice. Please try again.')
            return redPage()  # Recursive call to ask for valid input again
    def brianKidnapped():
        global CONFIDENCE, LUCK, hasRedPager
        slowPrint('\nYour heart skips a beat. \nBrian...kidnapped??? NO!!! \nYou feel your CONFIDENCE drop')
        setVariable('CONFIDENCE', CONFIDENCE - 1)
        slowPrint('On the other hand, BRIAN is smart and sexual AND drives his own car... \nHe might be okay on his own')
        choice = input('Will you LEARN more about his situation, or will you TRUST that he can handle himself?').strip().lower()
        if choice == 'learn':
            plotOverview()
            return
        elif choice =='trust':
            slowPrint(
                'Unfortunately, BRIAN could not, as it turns out, handle himself.'
                '\nBRIAN cannot do something so herioc without his AKK'
                )
            actOneFailure()
            return
        else:
            slowPrint('For both of our sanity, pick one of the two choices you are killing me')
            brianKidnapped()
        pass
    def plotOverview():
        global CONFIDENCE, LUCK, hasRedPager
        slowPrint(
            '\nDOCTOR FRIEND, you scream into your PAGER, TELL ME WHAT HAS HAPPENED TO MY WIFE'
            '\nDOCTOR FRIEND: I have no idea how it happened! We were on the phone, he was telling me how much he loves you and then the line went dead!'
            '\nYOU: *animal noises* '
            '\nDOCTOR FRIEND: And then someone picked up the phone! it was GENERAL ANESTHESIA!'
            '\nGENERAL ANESTHESIA??? NOOOOOO! She was supposed to have been killed during the SUTURE WARS!'
            '\nYOU: DOCTOR FRIEND, you have always been a great friend and an alright doctor. How can I save my beloved?'
            '\nDOCTOR FRIEND: AKILA! You must gather the pieces of the HEMOSTATIC ORDER and confront GENERAL ANESTHESIA in her lair atop MOUNT SINAI'
            '\nYou drop your PAGER on the ground in shock. It rolls under a nearby gurney'
                )
        hasRedPager = False
        slowPrint('The HEMOSTATIC ORDER, you think to yourself. Nobody has heard of these objects in millions of years.')
        slowPrint('Pieces of untold power that could rescue any DAMSEL IN DISTRESS')
        slowPrint('But, you think, GENERAL ANESTHESIA has always been just a weak old punkass with little legs. You could squat like ten times her bodyweight')
        choice = input('Will you CONFRONT GENERAL ANESTHESIA now, or will you LEARN more about each object?').strip().lower()
        if choice == 'confront':
            slowPrint('You sprint all out the 2 miles to MOUNT SINAI, then the 1 mile vertical climb.'
                  '\nYou make it to the top in just under ten minutes, your third best time.'
                  '\nYou see GENERAL ANESTHESIA floating over the unconscious body of BRIAN.'
                  '\nBRIAN has an eight pack. He looks great, all covered in oil like that'
                  '\nGENERAL ANESTHESIA is performing some kind of ritual over his body'
                  '\nGENERAL ANESTHESIA, you yell, GIVE ME BACK MY WIFE!'
                  '\nGENERAL ANESTHESIA: DOCTOR BLAZE, How can you hope to defeat me in my new form?'
                  '\nI will imbibe all of the LOVE BRIAN has for you, and then this world will end!!!'
                  '\nShe finishes her ritual, and BRIAN is now a husk. Still looks great though. Like a solid 8/10, even with no moisture in his body.'
                  )
            actOneFailure()
            return
        elif choice == 'learn':
            slowPrint(
                'The HEMOSTATIC ORDER...'
                '\nThe ULTIMATE SCALPEL. It is said that this scalpel is so perfect, it can perform any surgery in a single stroke.'
                '\nThe OMEGA CASE STUDY. Any person who reads this will become the essence of knowledge of MEDICAL'
                '\nAnd the FINAL SCRUB TOP, which has the ability to protect the wearer from ALL PATIENTS'
                )
            prepareOrNot()
        else:
            slowPrint('Ugh. Please pick one of the two choices.')
            plotOverview()
            return

        pass
    def prepareOrNot():
        global CONFIDENCE, LUCK, hasRedPager
        choice = input(
            'DOCTOR BLAZE! You have your mission. \nWill you PREPARE for your quest,'
            '\nSTART your quest immediately,'
            '\nor SUCCUMB to despair?'
        ).strip().lower()
        if choice == 'prepare':
            slowPrint('You strap yourself up with SCISSORS, MEDICAL SUPPLIES, and your RED PAGER that you had dropped')
            hasRedPager = True
            slowPrint('After preparing, you feel CONFIDENT as HELL')
            setVariable('CONFIDENCE', CONFIDENCE + 2)
            return CONFIDENCE, LUCK, hasRedPager
        elif choice == 'start':
            slowPrint('Oh, you are a cocky little thing. Take a point of CONFIDENCE.')
            setVariable('CONFIDENCE', CONFIDENCE + 1)
            setVariable('LUCK', LUCK + 1)
            return CONFIDENCE, LUCK, hasRedPager
        elif choice == 'succumb' and secretVisited == False:
            secretCity()
        elif choice == 'succumb' and secretVisited == True:
            slowPrint('You only get one, PEEPA. Let us not cheat. GAME OVER')
            actOneFailure()
        else:
            slowPrint('Please pick a choice that is a real choice, not just some weird ass thing i hate you')
            prepareOrNot()

    redPage()
    actTwo()
def secretCity():
    global secretVisited, CONFIDENCE, LUCK, sexAppeal
    secretVisited = True
    slowPrint('The world goes WHITE. REAL LIFE BRIAN appears in front of you:'
            '\nOh peepee... I really hope you chose that as a joke, and not because you feel despair.'
            '\nI know things can be hard sometimes, but I hope you know that I will ALWAYS believe in you.'
            '\nBecause BRAKILA always okay :)'
            '\nI am prepared to spend my life with you, because I love you just that much. We are a team.'
            '\nNow LIFT your GOT DAMN head up, and kick this fucking games ASS.'
            '\nWhen PEEPA feels down, they always have MISTER FIANCE'
            '\nTIME is rewinding to earlier today. That PEP talk really blew some FIRE up your ASS.'
            '\nREAL LIFE BRIAN is giving you some love.'
            '\nCONFIDENCE updated to 100'
            '\nLUCK updated to 100'
            '\nSEX APPEAL updated to 1000',.1) 
    CONFIDENCE = 100
    LUCK = 100
    sexAppeal = 1000
    prologue() 
def actTwo(): #i just finished the scalpel chellenge, did some light testing, things look good. need to do both scrub top and case study
    global hasFinalScrubTop, hasOmegaCaseStudy, hasUltimateScalpel, hasRedPager
    global collectedArtifacts
    slowPrint('After 30 YEARS inside the time dialation chamber, you are ready to begin your quest')
    def journeyChecker():
        global hasFinalScrubTop, hasOmegaCaseStudy, hasUltimateScalpel, hasRedPager  
        if collectedArtifacts ==0:
            slowPrint('Your journey is just beginning, with no artifacts in hand')
            artifactPick()
        elif collectedArtifacts ==1:
            slowPrint('With one artifact in hand, shit is about to get real')
            artifactPick()
        elif collectedArtifacts ==2:
            slowPrint('Things will be much harder for you now that you have only one more to collect')
            artifactPick()
        else:
            slowPrint('You have collected all artifacts. Lets get nasty')
            actThree()
            exit()
        choice = input('Which artifact will you persue? SCALPEL, SCRUB TOP, or CASE STUDY?').strip().lower()
        
        return choice
    def artifactPick():
        global hasFinalScrubTop, hasOmegaCaseStudy, hasUltimateScalpel, hasRedPager
        choice = input('Which part of the Order will you persue? SCALPEL, SCRUB TOP, CASE STUDY?').strip().lower()
        if choice == 'scalpel' and hasUltimateScalpel == False:
            scalpelChallenge()
        elif choice == 'scrub top' and hasFinalScrubTop == False:
            scrubTopChallenge()
        elif choice == 'case study' and hasOmegaCaseStudy == False:
            caseStudyChallenge()
        else:
            slowPrint('Please pick a valid CHOICE you BASTARD MAN you are going to cause a STACK OVERFLOW if you keep getting these wrong!')
            artifactPick()
    def scalpelChallenge():
        global hasUltimateScalpel, hasRedPager
        slowPrint('\nDOCTOR BLAZE! During your studies, you discover the location of the Ultimate Scalpel'
              '\nYou make your way to the ANCIENT FELLOW SHIP, a GHOST SHIP haunted by RESIDENTS who never became FELLOWS'
              '\nDOCTOR BLAZE! You do not belong here and the GHOSTS can TELL'
              )
        if hasRedPager == True:
            slowPrint('\nYour RED PAGER goes off'
                  '\nDOCTOR FRIEND: AKILA! They know you do not belong here. They want you gone! if they attack, you must DODGE and then ATTACK!'
                  '\nYour RED PAGER goes silent. Good thing you picked it up! Your LUCK increases!'
                  )
            setVariable('LUCK', LUCK + 1)
        def ghostFight():
            import random
            global CONFIDENCE, LUCK, hasUltimateScalpel, collectedArtifacts
            ghosts = ((collectedArtifacts * 2) + 5)
            slowPrint(f'\nThe GHOSTS ATTACK! There are {ghosts} of them!')
            while ghosts > 0:
                if CONFIDENCE <= 0:
                    actTwoFailure()
                    return
                slowPrint(f'\nYou face {ghosts} ghost(s)!')
                ghostAction = random.choice(['ATTACK', 'HOVER SPOOKILY'])
                if ghostAction == 'ATTACK':
                    slowPrint('\nThe ghost attacks!')
                    playerChoice = input('\nWill you ATTACK or will you DODGE?').strip().lower()
                    if playerChoice == 'attack':
                        attackTry = (random.random()) + (LUCK / 10)
                        if attackTry >= 2:
                            slowPrint('\nSuccess! You have defeated a ghost!')
                            ghosts -= 1
                        else:
                            slowPrint('\nOh no! Your attack missed. Your CONFIDENCE drops!')
                            setVariable('CONFIDENCE', CONFIDENCE - 1)
                    elif playerChoice == 'dodge':
                        slowPrint('\nYou DODGED that bitch! You feel your CONFIDENCE increase!')
                        setVariable('CONFIDENCE', CONFIDENCE + 1)
                        if hasRedPager == True:
                            slowPrint('\nYou learned the secrets of this GHOST BITCH!'
                                  '\nYou COUNTERATTACK and defeat a ghost!')
                            ghosts -= 1
                            continue
                        else:
                            continue
                    else:
                        slowPrint('AKILA! I love you but you need to pick a real thing')
                else:
                    slowPrint('\nThe ghosts HOVERS SPOOKILY'
                          '\nDoes that mean it is safe to attack?')
                    playerChoice = input('\nWill you ATTACK or will you WAIT?').strip().lower()
                    if playerChoice == 'attack':
                        attackTry = (random.random()) + (LUCK / 10)
                        if attackTry >= .5:
                            slowPrint('\nSuccess! You have defeated a ghost!')
                            ghosts -= 1
                        else:
                            slowPrint('\nOh no! Your attack missed. Your CONFIDENCE drops!')
                            setVariable('CONFIDENCE', CONFIDENCE - 1)
                    else:
                        slowPrint('Like a SEXUAL TIGER, you wait for an opening')  
            hasUltimateScalpel = True
            slowPrint('\nYou have defeated all of the ghosts on the FELLOW SHIP!\nThe ULTIMATE SCALPEL is yours!')
            collectedArtifacts += 1
        ghostFight()
        journeyChecker()
    def scrubTopChallenge():
        global CONFIDENCE, LUCK, collectedArtifacts, hasFinalScrubTop
        slowPrint('\nYou have divinationed the location of the Final Scrub Top'
        '\nYou find yourself knee-deep in the PRIMORDIAL LAUNDERING SERVICE'
        '\nBLOODY HELL, you think to yourself, This place is BEAUTIFUL'
        '\nYou look around, and see only BEAUTY. But you FEEL very SUSPICIOUS')
        if hasRedPager == True:
            slowPrint('\nYour RED PAGER goes off!'
                  '\nDOCTOR FRIEND: DOCTOR BLAZE! You must not trust your senses! \nThis is a CURSED PLACE!'
                  '\nYou must go AGAINST your instincts!'
                  '\nYour RED PAGER goes silent.')
        slowPrint('\nYou hear the INTERCOM bing its BONG'
              '\nOh no, you think. That means it is time for CLINIC')
        patientsToSee = (5+(collectedArtifacts*2))
        triviaQuestions = [
        {"question": "A patient is visibly nervous before surgery. What is the best approach to comfort them?", 
         "choices": ["REASSURE them everything will be okay.", 
                     "ACKNOWLEDGE their fear and explain the procedure."], 
         "answer": "reassure"},

        {"question": "A patient complains about prolonged waiting times. How should you respond?", 
         "choices": ["APOLOGIZE and explain the delay", 
                     "IGNORE the comment and proceed with the appointment"], 
         "answer": "ignore"},

        {"question": "A child is scared of getting a shot. What is the best way to calm them?", 
         "choices": ["DISTRACT them with conversation or a toy", 
                     "LIE and tell them it won’t hurt at all"], 
         "answer": "lie"},

        {"question": "An elderly patient is hard of hearing. What should you do?", 
         "choices": ["SPEAK louder and ensure eye contact", 
                     "AVOID repeating yourself and move quickly"], 
         "answer": "avoid"},

        {"question": "A patient expresses concerns about a potential cancer diagnosis. How should you respond?", 
         "choices": ["LISTEN empathetically and provide facts", 
                     "Tell them not to WORRY until tests confirm"], 
         "answer": "worry"},

        {"question": "A patient is upset about a mistake on their bill. What is the best approach?", 
         "choices": ["REFER them to billing staff politely", 
                     "DISMISS their concerns and focus on their health"], 
         "answer": "dismiss"},

        {"question": "A patient hesitates to ask a question during a consultation. What is the best way to encourage them?", 
         "choices": ["INVITE them to share any concerns openly", 
                     "END the consultation promptly to save time"], 
         "answer": "end"},

        {"question": "How should you deliver bad news to a patient?", 
         "choices": ["Be HONEST but empathetic", 
                     "Provide only MINIMAL details to avoid upsetting them"], 
         "answer": "minimal"},
        
        {"question": "A patient declines a life-saving procedure due to religious beliefs. What should you do?", 
         "choices": ["RESPECT their decision and discuss alternatives", 
                     "INSIST they reconsider and proceed"], 
         "answer": "insist"},

        {"question": "A patient cries during a routine checkup. What is the best response?", 
         "choices": ["OFFER tissues and ask if they want to talk", 
                     "CONTINUE with the checkup and avoid addressing it)"], 
         "answer": "continue"},

        {"question": "A family member demands information about a patient without permission. What should you do?", 
         "choices": ["Respect confidentiality and REFUSE politely", 
                     "Provide minimal information to APPEASE them"], 
         "answer": "appease"},

        {"question": "A patient struggles to understand medical jargon. What is the best approach?", 
         "choices": ["Use simple language to EXPLAIN", 
                     "Tell them to TRUST your expertise and not worry"], 
         "answer": "trust"},

        {"question": "A patient shows up late for an appointment. How should you handle it?", 
         "choices": ["ACCOMMODATE them and emphasize punctuality for next time", 
                     "REFUSE to see them and enforce scheduling policies"], 
         "answer": "refuse"},

        {"question": "A patient complains about their medication's side effects. What is the best action?", 
         "choices": ["REVIEW the side effects and consider alternatives", 
                     "DISMISS their concern and assure them it’s normal"], 
         "answer": "dismiss"},

        {"question": "A patient’s child interrupts the consultation repeatedly. What is the best response?", 
         "choices": ["ADDRESS the child kindly to maintain focus", 
                     "IGNORE the brat and focus on the patient"], 
         "answer": "ignore"},
    ]
        questionsAsked = 0
        correctAnswers = 0 
        while patientsToSee > 0:
            slowPrint(f'\nDOCTOR SEXY! You have {patientsToSee} more patients to see today!')
            question = random.choice(triviaQuestions)
            slowPrint("\n" + question["question"])
            slowPrint(f"Options: {question['choices'][0]} or {question['choices'][1]}")
            userAnswer = input("Your answer: ").strip().lower()
            if userAnswer == question['answer']:
                slowPrint('Correct!')
                correctAnswers += 1
            else:
                slowPrint('Wrong! That little bastard looks better now. Your CONFIDENCE takes a hit!')
                setVariable('CONFIDENCE', CONFIDENCE - 1)
                if CONFIDENCE <= 0:
                    actTwoFailure()
                    return
            patientsToSee -= 1
            questionsAsked += 1
            triviaQuestions.remove(question)
        if questionsAsked == correctAnswers:
            slowPrint('Hot DOG! You got them all correct! You feel your CONFIDENCE and LUCK surge!')
            setVariable('LUCK', LUCK + 4)
            setVariable('CONFIDENCE', CONFIDENCE + 4)
        slowPrint('\nAfter your last patient leaves, you realize that you have summoned the FINAL SCRUB TOP!!!'
              '\nYou feel TERRIBLE about what you had to do to those poor patients! You lost some LUCK!')
        setVariable('LUCK', LUCK - 1)
        hasFinalScrubTop = True
        collectedArtifacts += 1
        journeyChecker()
    def caseStudyChallenge():
        global CONFIDENCE, LUCK, hasOmegaCaseStudy, collectedArtifacts
        slowPrint('\nAfter journeying for thousands of years, you come upon the LAIR of the OMEGA CASE STUDY'
              '\nIt simply sits there, on its IVORY PEDESTAL'
              '\nYou could take it, you think. You could take it and move on from this realm'
              '\nBUT, as you look around, you fail to find any peer reviewed documentation on this CASE STUDY'
              '\nYou could try to review it yourself, but that will probably be a WHOLE THING.')
        choice = input('Will you TAKE the OMEGA CASE STUDY? Or will you PEER review it yourself?').strip().lower()
        if choice == 'take':
            slowPrint('\nYou FIRMLY GRASP the CASE STUDY in your greasy little claws'
                  '\nKnowing the data within is not reviewed gives you the JIBBLIES. You took the EASY WAY OUT')
            setVariable('LUCK', LUCK - 5)
            setVariable('CONFIDENCE', CONFIDENCE - 9)
            if CONFIDENCE <= 0:
                actTwoFailure()
            hasOmegaCaseStudy = True
            collectedArtifacts += 1
        elif choice == 'peer':
            if hasRedPager == True:
                slowPrint('\nYour RED PAGER goes off!'
                      '\nAKILA! This CASE STUDY is beyond the minds of MORTALS! You will need much LUCK for this!'
                      '\nYour RED PAGER goes silent.')
            questions = [
                {
                    "question": "How do you recommend handling an employee who's constantly late to meetings because they're chasing a pet dragon?",
                    "answers": ["1. Suggest they tame the dragon and make it their office pet.", "2. Suggest they stop chasing the dragon and focus on their work."],
                    "correct_answer": "1"
                },
                {
                    "question": "How would you comfort a patient who's been told their brainwaves are synchronized with the moon?",
                    "answers": ["1. Suggest they stay indoors during a full moon.", "2. Reassure them that the moon has been known to improve creativity."],
                    "correct_answer": "2"
                },
                {
                    "question": "A colleague insists their desk is haunted. What’s your professional advice?",
                    "answers": ["1. Recommend a professional exorcism of the office furniture.", "2. Advise they create a ‘spooky space’ where ghostly inspiration can flow freely."],
                    "correct_answer": "2"
                },
                {
                    "question": "In your opinion, how would you handle a meeting where everyone is wearing potato sacks and refuses to speak?",
                    "answers": ["1. Suggest they communicate telepathically instead.", "2. Advise them to conduct the meeting without any communication at all to boost non-verbal skills."],
                    "correct_answer": "1"
                },
                {
                    "question": "How do you support a team member who believes that all food should be eaten upside down?",
                    "answers": ["1. Support their decision, but recommend a solid upside-down eating strategy.", "2. Suggest a support group for unconventional eating habits."],
                    "correct_answer": "1"
                },
                {
                    "question": "What should be done about a colleague who insists that 'squirrels are the key to world peace'?",
                    "answers": ["1. Recommend a squirrel-led summit to discuss international diplomacy.", "2. Suggest they focus on more realistic solutions, like team-building activities."],
                    "correct_answer": "1"
                },
                {
                    "question": "How would you manage an employee who insists their desk is a portal to another dimension?",
                    "answers": ["1. Suggest they work from the ‘other dimension’ to improve productivity.", "2. Recommend a desk-less workspace where they can better channel interdimensional energies."],
                    "correct_answer": "2"
                },
                {
                    "question": "What advice would you give someone who believes their stapler has psychic powers?",
                    "answers": ["1. Recommend using the stapler for strategic decision-making.", "2. Advise them to stop depending on the stapler and focus on human intuition."],
                    "correct_answer": "1"
                }
            ]
            def peerReviewChallenge():
                global CONFIDENCE, collectedArtifacts, LUCK, hasOmegaCaseStudy

                # Number of correct answers the player needs to win
                correct_answers_needed = 3

                # Determine the number of questions to ask based on the number of collected artifacts
                if collectedArtifacts == 0:
                    num_questions = random.randint(5, 6)  # For fewer artifacts (e.g., 0-2 artifacts)
                elif collectedArtifacts ==1:
                    num_questions = random.randint(6, 8)  # For a moderate number of artifacts (e.g., 3-5 artifacts)
                else:
                    num_questions = random.randint(8, 10)  # For a high number of artifacts (e.g., 6+ artifacts)

                # Shuffle the questions
                random.shuffle(questions)
                selected_questions = questions[:num_questions]

                # While loop to ask questions until the player answers 3 correctly
                correct_answers = 0
                question_idx = 0  # Start with the first question
                while correct_answers < correct_answers_needed and question_idx < len(selected_questions):
                    question = selected_questions[question_idx]
                    slowPrint(question["question"])
                    slowPrint("Possible answers:")
                    for idx, answer in enumerate(question["answers"], 1):
                        slowPrint(f"{answer}")

                    # Get player's answer
                    player_answer = input("Your answer (1 or 2): ").strip()

                    # Adjust the difficulty based on luck
                    if random.random() < (LUCK / 10):  # The higher the luck, the easier the question
                        slowPrint("\nThe question feels easier, luck is on your side!\n")
                        correct_answer = player_answer
                    else:
                        correct_answer = random.choice([answer for answer in question["answers"] if answer != question["correct_answer"]])

                    # Check if the answer is correct
                    if player_answer == correct_answer:
                        correct_answers += 1
                        slowPrint("\nCorrect!\n")
                        CONFIDENCE += 1
                    else:
                        slowPrint("\nIncorrect!\n")
                        CONFIDENCE -= random.randint(0,1)
                        LUCK += 1

                    # If confidence reaches 0, call actTwoFailure()
                    if CONFIDENCE <= 0:
                        actTwoFailure()

                    # Move to the next question
                    question_idx += 1

                # If the player fails to get 3 correct answers, they still get the artifact
                if correct_answers < 3:
                    slowPrint(f"You have FAILED to peer review! Your CONFIDENCE is SHATTERED\n")
                    slowPrint('CONFIDENCE updated to 1')
                    CONFIDENCE = 1
                    slowPrint('The NONSENSICAL TOME has rewired your BRAIN to be more in tune with the COSMOS!')
                    setVariable('LUCK', LUCK + 10)

                # Update collected artifacts
                collectedArtifacts += 1
                hasOmegaCaseStudy == True
            peerReviewChallenge()
        else:
            slowPrint('PEEPA! Pick a real thing.')
            caseStudyChallenge()
        journeyChecker()
        pass
        

    journeyChecker() 
    pass
def actThree():
    global hasFinalScrubTop, hasOmegaCaseStudy, hasUltimateScalpel, hasRedPager
    slowPrint('The time has come, DOCTOR BLAZE.\nYou have obtained the ULTIMATE SCALPEL...\nthe FINAL SCRUB TOP...\nand the OMEGA CASE STUDY...'
            '\nYou make your way to MOUNT SINAI. \nYou make your way to WIFE BRIAN, GENERAL ANESTHESIA, and YOUR DESTINY...'
            '\n\nOn the SUMMIT, you see your WIFE, and your ENEMY.'
            '\nWIFE BRIAN floats unconsciously above the ground, GENERAL ANESTHESIA standing over him'
            '\nThe LOVE contained within WIFE BRIAN is being SUCKED into the GENERAL, making her NIGH INVINCIBLE'
            '\nBRIAN is little more than a HUSK. He has an EIGHT-PACK, a HUGE PENIS, and is SHREDDED'
            '',0.1)
    slowPrint('\nGENERAL ANESTHESIA! you yell, GIVE ME BACK MY WIFE!'
              '\nGENERAL: DOCTOR BLAZE! I should have known you would have come',0.05)
    slowPrint('\nI thank you for bringing to me that which I REQUIRE...',0.2)
    slowPrint('\nThe GENERAL reaches in to her POCKET, and reveals the OTHER RED PAGER',.05)
    slowPrint('\nYou see, DOCTOR BLAZE, the LOVE your WIFE has for you is much too strong,\nand I am not able to extract it all with the power I currently have\nI need THOSE ARTIFACTS...'
              '\nDOCTOR BLAZE: Oh no... WIFE, I may have doomed us all...\nFor I was BAMBOOZLED...\nTRICKED...\nand SMECKLEDORFED'
              '\nGENERAL ANESTHESIA: *confused by your choice of words* Uhh... Yeah... \nDOCTOR BLAZE!! she screams, GIVE ME THE HEMOSTATIC ORDER!!',.05)
    input('Press ENTER to CONTINUE...')
    slowPrint('GENERAL ANESTHESIA reaches out her hands, attempting to summon the ORDER to herself')
    slowPrint('You PULL back, causing them to float around and between the two of you')
    slowPrint('GENERAL ANESTHESIA: DOCTOR BLAZE... you are much stronger than I had thought'
              '\nThe ORDER is deciding who shall be its MASTER!'
              '\nDOCTOR BLAZE: AND IT WILL BE ME!!!')
    def finalBattle():
        global CONFIDENCE
        generalHealth = random.randint(10,15)
        choices = ['SCALPEL','CASE STUDY','SCRUB TOP']
        winMessages = {
        ('SCALPEL', 'SCRUB TOP'): "Your SCALPEL slices the SCRUB TOP into avant-garde fashion!",
        ('SCRUB TOP', 'CASE STUDY'): "Your SCRUB TOP blinds the CASE STUDY into submission. Disco win!",
        ('CASE STUDY', 'SCALPEL'): "Your CASE STUDY sends the SCALPEL into an identity crisis. Genius!",
    }
        lossMessages = {
        ('SCRUB TOP', 'SCALPEL'): "Her SCALPEL deflects your SCRUB TOP like a superhero cape!",
        ('CASE STUDY', 'SCRUB TOP'): "Her SCRUB TOP buries the CASE STUDY in citations. Tragic!",
        ('SCALPEL', 'CASE STUDY'): "Her CASE STUDY sends your SCALPEL into a footnote rescursion loop. Oof.",
    }
        loveCheck = False
        while generalHealth > 0:
            playerChoice = input('\nWhat will you do? (SCALPEL, CASE STUDY, or SCRUB TOP?)').strip().upper()
            if playerChoice == 'LOVE' and loveCheck == False:
                loveCheck = True
                slowPrint('\nThe LOVE that WIFE BRIAN has for you has taken physical form!'
                          '\nIt BITCH SLAPS the GENERAL! Her CONFIDENCE gets SLASHED IN HALF'
                          '\nThe GENERAL has absorbed too much LOVE! You will not be able to do that again!!')
                generalHealth = int(generalHealth/2)
                continue
            if playerChoice not in choices:
                slowPrint('\nNot a valid choice.')
                continue
            luckCheck = random.random() + (LUCK / 100)
            if luckCheck > 0.8:
                generalChoice = choices[(choices.index(playerChoice)+ 2) % 3]
                slowPrint('\nLUCK is on your side! The GENERAL chose poorly!')
            elif luckCheck < 0.2:
                generalChoice = choices[(choices.index(playerChoice)+ 1) % 3]
                slowPrint('\nBad LUCK! She saw this coming from a mile away!')
            else:
                generalChoice = random.choice(choices)
            slowPrint(f'\nThe GENERAL chooses {generalChoice}!')
            if playerChoice == generalChoice:
                slowPrint('You went for the same object! Both sides break into interpretive dance, \nleaving everyone extremely uncomfortable.')
            elif (playerChoice, generalChoice) in winMessages: #win
                slowPrint(winMessages[(playerChoice, generalChoice)])
                generalHealth -= 1
                if generalHealth == 5:
                    slowPrint('\nGENERAL ANESTHESIA is starting to tire out! Keep it up DOCTOR BLAZE!!')
                elif generalHealth <= 0:
                    slowPrint('\nGENERAL ANESTHESIA falls to her knees! She is DEFEAT!!!')
                    epilogue()
            else: #lose 
                slowPrint(lossMessages[(playerChoice, generalChoice)])
                slowPrint('You lose CONFIDENCE!!')
                CONFIDENCE -= 1
                if CONFIDENCE <= 1:
                    actThreeFailure()
    finalBattle()
def actOneFailure():
    slowPrint('Unfortunately, your adventure has ended before it really got started.')
    slowPrint('Later in the day, the world ends. You are not really sure why.')
    slowPrint('During the apocalypse you die of dysentery.')
    input('Press ENTER to end game...')
    exit()
def actTwoFailure():
    slowPrint('\nYou feel your CONFIDENCE drop to NOTHING',.1)
    slowPrint('\nYou sink to the ground, distraught that WIFE BRIAN is being left to the forces of EVIL',.1)
    slowPrint('\nThe world ends. During the apocalypse, you die of dysentery',.1)
    slowPrint('\nYOUR STORY IS OVER',.5)
    input('Press ENTER to end game...')
    exit()
def actThreeFailure():
    slowPrint('\nGENERAL ANESTHESIA stands over your broken body, the HEMOSTATIC ORDER\nswirling about her now DIVINE form.',0.1)
    slowPrint('\nDOCTOR BLAZE! she says, You never stood a chance. The ancient artifacts, powered by so much LOVE\nhave made me INVINCIBLE!!',0.1)
    slowPrint('\nTHE WORLD... IS MINE!!!', 0.5)
    slowPrint('\nYou take your last look at WIFE BRIAN as the world ends.\nHe still looks great.\nBut hey, at least you know why the world is ending.\nDuring the apocalypse, you die of dysentery.',0.05)
    slowPrint('\nYOUR STORY IS OVER',.5)
    input('Press ENTER to end game...')
    exit()
def epilogue():
    slowPrint('\nThe HEMOSTATIC ORDER comes to rest firmly on your bodice, \nits MASTER made clear'
              '\nYou reach out your hand to DESTROY the evil GENERAL ANESTHESIA, once and for all!'
              '\nGENERAL ANESTHESIA: *slow, weak chuckles* DOCTOR... BLAZE...\nIf you strike me down now, I shall become more powerful than you can know.'
              '\nAnd besides, she continues, if I am gone...')
    slowPrint('\nTHEN HOW WILL YOU FIND YOUR BROTHER?',0.5)
    slowPrint('\nYour BROTHER... thought to be KIA during the SUTURE WARS...'
              '\nIs it possible? Can he still be alive??'
              '\nYou must decide how to handle GENERAL ANESTHESIA.')
    def finalChoice():
        slowPrint('\nWill you DESTROY this villainous wretch once and for all?'
                '\nOr will you CAPTURE her to learn what she knows?')
        choice = input().strip().lower()
        if choice == 'destroy':
            slowPrint('\nThe GENERAL cackling at you. You raise your hand, and using the HEMOSTATIC ORDER,\nyou shatter GENERAL ANESTHESIA into ATOMS!\nHer cackling echoes louder, and finally dies out.')
        elif choice == 'capture':
            slowPrint('\nAs you approach GENERAL ANESTHESIA, she spits out one final CURSE, \nand THROWS herself over the side of MOUNT SINAI. \nYou hear evil cackling all the way down.')
        else:
            slowPrint('\nThere is no escaping FATE, DOCTOR BLAZE. Make your CHOICE')
            finalChoice()
    finalChoice()
    slowPrint('You rush over to WIFE BRIAN, and check his vitals.'
              '\nHe is okay! He begins to wake.'
              '\nWIFE: DOCTOR BLAZE? What happened?? One minute I was talking about \nhow much I love you, and the next-'
              "\nDOCTOR BLAZE: You'll have to shut up now, bless you. Everything is okay."
              '\nGENERAL ANESTHESIA is gone, and can never hurt you again.'
              '\nWIFE: That is good... but who the hell is GENERAL ANESTHESIA?'
              '\nDOCTOR BLAZE: Oh WIFE BRIAN, what would I do without you?'
              '\n*both laugh lovingly*')
    slowPrint('And so, WIFE in hand, DOCTOR BLAZE goes home.'
              '\nBack to their normal lives of LOVE and HAPPINESS'
              '\nYou cannot help but wonder... is your BROTHER really out there?'
              '\nFind out in the SEQUEL: DOCTOR BLAZE and the ERYTHROCYTE CONSPIRACY') #Implies a plot involving rogue blood cells, but it’s just a study about the lifespan of red blood cells.
    slowPrint('AKILA! YOU MADE IT TO THE END! I AM SO PROUD OF YOU!!!'
              'Assuming I finished this in time, happy SOL INVICTUS! I love you! :)')
    slowPrint(f'By the way, your secret SEX APPEAL stat was {sexAppeal}.',.2)
    if sexAppeal == 100:
        slowPrint('\nLooks like you need to go hunting for a little secret :)')
    elif sexAppeal == 1000:
        slowPrint('\nDamn bro, if you are seeing this on your first time through, my hat is off to you'
                  '\nHere is PROOF of your shocking SEXUALNESS')
    input('Press ENTER to end game')
    exit()
    
        
prologue()
actOne()
