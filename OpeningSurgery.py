
sexAppeal = 100
LUCK = 0
hasRedPager = True
CONDFIDENCE = 10
surgerySuccess = True
hasUltimateScalpel = False
hasOmegaCaseStudy = False
hasFinalScrubTop = False
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
            CONDFIDENCE += 1
        else:
            print("\nThe surgery did not go well. You have lost CONFIDENCE. Better luck next time.")
            CONDFIDENCE -= 1
        return surgerySuccess, CONDFIDENCE

    def end_game(message):
        print(message)
        finish()

    step_one()
    return surgerySuccess
def actOne():
    global CONDFIDENCE
    global LUCK

    def redPage():
        print('After the surgery, your RED PAGER goes off.')
        print('You think: Oh no! Not the RED PAGER! That is for personal emergencies only!')
        choice = input('Do you RESPOND to the RED PAGE, or do you IGNORE? ').strip().lower()
        
        if choice == 'ignore':
            actOneFailure()
            return choice  
        
        elif choice == 'respond':
            print('\nYou decide to respond to the RED PAGER. It turns out to be a genuine emergency.')
            print('DOCTOR FRIEND: AKILA! Your wife BRIAN has been kidnapped!')
            brianKidnapped()
            return choice  # End the function if responding
        
        else:
            print('I do not understand your choice. Please try again.')
            return redPage()  # Recursive call to ask for valid input again
    def brianKidnapped():
        global CONDFIDENCE, LUCK
        print('\nYour heart skips a beat. \nBrian...kidnapped??? NO!!! \nYou feel your CONFIDENCE drop')
        CONDFIDENCE -= 1
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
            'DOCTOR FRIEND, you scream into your PAGER, TELL ME WHAT HAS HAPPENED TO MY WIFE'
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
        choice = input('Will you CONFRONT GENERAL ANESTHESIA now, or will you LEARN more about each object?').split().lower()
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
            pass #this is where you pick up next time
        else:
            print('Ugh. Please pick one of the two choices.')
            plotOverview()
            return

        pass
    def prepareOrNot():
        pass
    redPage()
def actTwo():
    pass
def actThree():
    pass
def actOneFailure():
    print('Unfortunately, your adventure has ended before it really got started.')
    print('Later in the day, the world ends. You are not really sure why.')
    print('During the apocalypse you die of dysentery.')
def actTwoFailure():
    pass


prologue()
print(CONDFIDENCE)
print(surgerySuccess)
actOne()
