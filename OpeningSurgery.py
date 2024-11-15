debugMode = True #this will be false when the time comes
sexAppeal = 100
LUCK = 0
hasRedPager = True
CONDFIDENCE = 10
surgerySuccess = True
hasUltimateScalpel = False
hasOmegaCaseStudy = False
hasFinalScrubTop = False
collectedArtifacts = 0 
def setVariable(name, value):
    globals()[name] = value
    if debugMode == True:
        print(f'{name} updated to {value}')
def prologue():
    global CONDFIDENCE
    complication_handled = False

    print("Welcome! You are DOCTOR AKILA B BLAZE: Pediatric surgeon by day, fierce adventurer by night.")
    print('You get very little sleep, what with all the surgery and adventuring.')
    print("Today, you only have one case! And it is a simple appendectomy.")
    print("Make the right choices to complete the surgery successfully. Good luck, DOCTOR BLAZE!")

    def step_one():
        global surgerySuccess
        print("\nStep 1: Preoperative Assessment.")
        choice = input("Do you choose to perform a thorough physical exam and order a CT scan or only rely on physical exam findings? (CT scan/physical exam) ").strip().lower()
        if choice == "ct scan":
            step_two()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Incomplete assessment leads to complications. Surgery cannot proceed.")

    def step_two():
        global surgerySuccess
        print("\nStep 2: Anesthesia Preparation.")
        choice = input("Do you choose to use endotracheal intubation or laryngeal mask airway (LMA) for anesthesia? (intubation/LMA) ").strip().lower()
        if choice == "intubation":
            step_three()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Inadequate airway management can lead to complications. Surgery is compromised.")

    def step_three():
        global surgerySuccess
        print("\nStep 3: Surgical Approach.")
        choice = input("Do you opt for an open appendectomy or a laparoscopic approach? (open/laparoscopic) ").strip().lower()
        if choice == "laparoscopic":
            step_four()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Open approach is less ideal for this case. Increased risk of complications.")

    def step_four():
        global surgerySuccess, complication_handled
        print("\nStep 4: Surgical Technique.")
        choice = input("During the surgery, do you use monopolar cautery or bipolar cautery for hemostasis? (monopolar/bipolar) ").strip().lower()
        if choice == "bipolar":
            step_complication()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Monopolar cautery can lead to excessive bleeding. Surgery is at risk.")

    def step_complication():
        global surgerySuccess, complication_handled
        print("\nComplication: Unexpected Hemorrhage.")
        print("While performing the procedure, you encounter unexpected hemorrhage due to bleeding from a small artery.")
        choice = input("Do you choose to use hemostatic clips or apply direct pressure and suture? (clips/direct pressure) ").strip().lower()
        
        if choice == "clips":
            complication_handled = True
            step_five()
        else:
            surgerySuccess = False
            end_game("Incorrect choice. Failure to control bleeding can lead to significant complications. Surgery is at risk.")

    def step_five():
        global surgerySuccess
        print("\nStep 5: Postoperative Care.")
        choice = input("Do you choose to use a broad-spectrum antibiotic prophylaxis or only a single antibiotic specific to the likely pathogens? (broad-spectrum/single) ").strip().lower()
        if choice == "broad-spectrum" and complication_handled:
            finish()
        else:
            surgerySuccess = False
            end_game("Incorrect choice or complication not handled properly. Inadequate care can lead to infections or other issues.")

    def finish():
        global CONDFIDENCE
        if surgerySuccess:
            print("\nCongratulations! The pediatric appendectomy was successful. You have gained CONFIDENCE. Excellent job, Surgeon!")
            setVariable('CONDFIDENCE', CONDFIDENCE + 1)
        else:
            print("\nThe surgery did not go well. You have lost CONFIDENCE. Better luck next time.")
            setVariable('CONDFIDENCE', CONDFIDENCE - 1)
        return surgerySuccess, CONDFIDENCE

    def end_game(message):
        global surgerySuccess
        print(message)
        finish()

    step_one()
    return surgerySuccess
def actOne():
    global CONDFIDENCE, LUCK, hasRedPager
    def redPage():
        print('After the surgery, your RED PAGER goes off.')
        print('You think: Oh no! Not the RED PAGER! That is for personal emergencies only!')
        choice = input('Do you RESPOND to the RED PAGE, or do you IGNORE? ').strip().lower()
        
        if choice == 'ignore':
            actOneFailure()
        elif choice == 'respond':
            print('\nYou decide to respond to the RED PAGER. It turns out to be a genuine emergency.')
            print('DOCTOR FRIEND: AKILA! Your wife BRIAN has been kidnapped!')
            brianKidnapped()
            return choice  # End the function if responding
        
        else:
            print('I do not understand your choice. Please try again.')
            return redPage()  # Recursive call to ask for valid input again
    def brianKidnapped():
        global CONDFIDENCE, LUCK, hasRedPager
        print('\nYour heart skips a beat. \nBrian...kidnapped??? NO!!! \nYou feel your CONFIDENCE drop')
        setVariable('CONDFIDENCE', CONDFIDENCE - 1)
        print('On the other hand, BRIAN is smart and sexual AND drives his own car... \nHe might be okay on his own')
        choice = input('Will you LEARN more about his situation, or will you TRUST that he can handle himself?').strip().lower()
        if choice == 'learn':
            plotOverview()
            return
        elif choice =='trust':
            print(
                'Unfortunately, BRIAN could not, as it turns out, handle himself.'
                '\nBRIAN cannot do something so herioc without his AKK'
                )
            actOneFailure()
            return
        else:
            print('For both of our sanity, pick one of the two choices you are killing me')
            brianKidnapped()
        pass
    def plotOverview():
        global CONDFIDENCE, LUCK, hasRedPager
        print(
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
        print('The HEMOSTATIC ORDER, you think to yourself. Nobody has heard of these objects in millions of years.')
        print('Pieces of untold power that could rescue any DAMSEL IN DISTRESS')
        print('But, you think, GENERAL ANESTHESIA has always been just a weak old punkass with little legs. You could squat like ten times her bodyweight')
        choice = input('Will you CONFRONT GENERAL ANESTHESIA now, or will you LEARN more about each object?').strip().lower()
        if choice == 'confront':
            print('You sprint all out the 2 miles to MOUNT SINAI, then the 1 mile vertical climb.'
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
            print(
                'The HEMOSTATIC ORDER...'
                '\nThe ULTIMATE SCALPEL. It is said that this scalpel is so perfect, it can perform any surgery in a single stroke.'
                '\nThe OMEGA CASE STUDY. Any person who reads this will become the essence of knowledge of MEDICAL'
                '\nAnd the FINAL SCRUB TOP, which has the ability to protect the wearer from ALL PATIENTS'
                )
            prepareOrNot()
        else:
            print('Ugh. Please pick one of the two choices.')
            plotOverview()
            return

        pass
    def prepareOrNot():
        global CONDFIDENCE, LUCK, hasRedPager
        choice = input(
            'DOCTOR BLAZE! You have your mission. Will you PREPARE for your quest,'
            '\nSTART your quest immediately,'
            '\nor SUCCUMB to despair?'
        ).strip().lower()
        if choice == 'prepare':
            print('You strap yourself up with SCISSORS, MEDICAL SUPPLIES, and your RED PAGER that you had dropped')
            hasRedPager = True
            print('After preparing, you feel CONFIDENT as HELL')
            setVariable('CONDFIDENCE', CONDFIDENCE + 2)
            return CONDFIDENCE, LUCK, hasRedPager
        elif choice == 'start':
            print('Oh, you are a cocky little thing. Take a point of CONFIDENCE.')
            setVariable('CONDFIDENCE', CONDFIDENCE + 1)
            setVariable('LUCK', LUCK + 1)
            return CONDFIDENCE, LUCK, hasRedPager
        elif choice == 'succumb':
            actOneFailure()
        else:
            print('Please pick a choice that is a real choice, not just some weird ass thing i hate you')
            prepareOrNot()

    redPage()
    actTwo()
def actTwo(): #i just finished the scalpel chellenge, did some light testing, things look good. need to do both scrub top and case study
    global hasFinalScrubTop, hasOmegaCaseStudy, hasUltimateScalpel, hasRedPager
    global collectedArtifacts
    print('After 30 YEARS inside the time dialation chamber, you are ready to begin your quest')
    def journeyChecker():
        global hasFinalScrubTop, hasOmegaCaseStudy, hasUltimateScalpel, hasRedPager  
        if collectedArtifacts ==0:
            print('Your journey is just beginning, with no artifacts in hand')
            artifactPick()
        elif collectedArtifacts ==1:
            print('With one artifact in hand, shit is about to get real')
            artifactPick()
        elif collectedArtifacts ==2:
            print('Things will be much harder for you now that you have only one more to collect')
            artifactPick()
        else:
            print('You have collected all artifacts. Lets get nasty')
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
        elif choice == 'case study' and hasUltimateScalpel == False:
            caseStudyChallenge()
        else:
            print('Please pick a valid CHOICE you BASTARD MAN you are going to cause a STACK OVERFLOW if you keep getting these wrong!')
            artifactPick()
    def scalpelChallenge():
        global hasUltimateScalpel, hasRedPager
        print('\nDOCTOR BLAZE! During your studies, you discover the location of the Ultimate Scalpel'
              '\nYou make your way to the ANCIENT FELLOW SHIP, a GHOST SHIP haunted by RESIDENTS who never became FELLOWS'
              '\nDOCTOR BLAZE! You do not belong here and the GHOSTS can TELL'
              )
        if hasRedPager == True:
            print('\nYour RED PAGER goes off'
                  '\nDOCTOR FRIEND: AKILA! They know you do not belong here. They want you gone! if they attack, you must DODGE and then ATTACK!'
                  '\nYour RED PAGER goes silent. Good thing you picked it up! Your LUCK increases!'
                  )
            setVariable('LUCK', LUCK + 1)
        def ghostFight():
            import random
            global CONDFIDENCE, LUCK, hasUltimateScalpel, collectedArtifacts
            ghosts = ((collectedArtifacts * 2) + 5)
            print(f'\nThe GHOSTS ATTACK! There are {ghosts} of them!')
            while ghosts > 0:
                if CONDFIDENCE <= 0:
                    actTwoFailure()
                    return
                print(f'\nYou face {ghosts} ghost(s)!')
                ghostAction = random.choice(['ATTACK', 'HOVER SPOOKILY'])
                if ghostAction == 'ATTACK':
                    print('\nThe ghost attacks!')
                    playerChoice = input('\nWill you ATTACK or will you DODGE?').strip().lower()
                    if playerChoice == 'attack':
                        attackTry = (random.random()) + (LUCK / 10)
                        if attackTry >= 2:
                            print('\nSuccess! You have defeated a ghost!')
                            ghosts -= 1
                        else:
                            print('\nOh no! Your attack missed. Your CONFIDENCE drops!')
                            setVariable('CONDFIDENCE', CONDFIDENCE - 1)
                    elif playerChoice == 'dodge':
                        print('\nYou DODGED that bitch! You feel your CONFIDENCE increase!')
                        setVariable('CONDFIDENCE', CONDFIDENCE + 1)
                        if hasRedPager == True:
                            print('\nYou learned the secrets of this GHOST BITCH!'
                                  '\nYou COUNTERATTACK and defeat a ghost!')
                            ghosts -= 1
                        else:
                            return
                    else:
                        print('AKILA! I love you but you need to pick a real thing')
                else:
                    print('\nThe ghosts HOVERS SPOOKILY'
                          '\nDoes that mean it is safe to attack?')
                    playerChoice = input('\nWill you ATTACK or will you WAIT?').strip().lower()
                    if playerChoice == 'attack':
                        attackTry = (random.random()) + (LUCK / 10)
                        if attackTry >= .5:
                            print('\nSuccess! You have defeated a ghost!')
                            ghosts -= 1
                        else:
                            print('\nOh no! Your attack missed. Your CONFIDENCE drops!')
                            setVariable('CONDFIDENCE', CONDFIDENCE - 1)
                    else:
                        print('Like a SEXUAL TIGER, you wait for an opening')  
            hasUltimateScalpel = True
            print('\nYou have defeated all of the ghosts on the FELLOW SHIP!\nThe ULTIMATE SCALPEL is yours!')
            collectedArtifacts += 1
        ghostFight()
        journeyChecker()
        pass
    def scrubTopChallenge():
        journeyChecker()
        pass
    def caseStudyChallenge():
        journeyChecker()
        pass
        

    journeyChecker() 
    pass
def actThree():
    global hasFinalScrubTop, hasOmegaCaseStudy, hasUltimateScalpel, hasRedPager
    pass
def actOneFailure():
    print('Unfortunately, your adventure has ended before it really got started.')
    print('Later in the day, the world ends. You are not really sure why.')
    print('During the apocalypse you die of dysentery.')
    exit()
def actTwoFailure():
    print('\nYou feel your CONFIDENCE drop to NOTHING'
          '\nYou sink to the ground, distraught that WIFE BRIAN is being left to the forces of EVIL'
          '\nThe world ends. During the apocalypse, you die of dysentery'  
          )
    print('\nYOUR STORY IS OVER')
    exit()


#prologue()
#actOne()
actTwo()