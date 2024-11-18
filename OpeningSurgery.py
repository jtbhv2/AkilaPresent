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
import random
import time
def slowPrint(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def setVariable(name, value):
    globals()[name] = value
    if debugMode == True:
        print(f'{name} updated to {value}')
def prologue():
    global CONFIDENCE
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
        global CONFIDENCE
        if surgerySuccess:
            print("\nCongratulations! The pediatric appendectomy was successful. You have gained CONFIDENCE. Excellent job, Surgeon!")
            setVariable('CONFIDENCE', CONFIDENCE + 1)
        else:
            print("\nThe surgery did not go well. You have lost CONFIDENCE. Better luck next time.")
            setVariable('CONFIDENCE', CONFIDENCE - 1)
        return surgerySuccess, CONFIDENCE

    def end_game(message):
        global surgerySuccess
        print(message)
        finish()

    step_one()
    return surgerySuccess
def actOne():
    global CONFIDENCE, LUCK, hasRedPager
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
        global CONFIDENCE, LUCK, hasRedPager
        print('\nYour heart skips a beat. \nBrian...kidnapped??? NO!!! \nYou feel your CONFIDENCE drop')
        setVariable('CONFIDENCE', CONFIDENCE - 1)
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
        global CONFIDENCE, LUCK, hasRedPager
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
        global CONFIDENCE, LUCK, hasRedPager
        choice = input(
            'DOCTOR BLAZE! You have your mission. Will you PREPARE for your quest,'
            '\nSTART your quest immediately,'
            '\nor SUCCUMB to despair?'
        ).strip().lower()
        if choice == 'prepare':
            print('You strap yourself up with SCISSORS, MEDICAL SUPPLIES, and your RED PAGER that you had dropped')
            hasRedPager = True
            print('After preparing, you feel CONFIDENT as HELL')
            setVariable('CONFIDENCE', CONFIDENCE + 2)
            return CONFIDENCE, LUCK, hasRedPager
        elif choice == 'start':
            print('Oh, you are a cocky little thing. Take a point of CONFIDENCE.')
            setVariable('CONFIDENCE', CONFIDENCE + 1)
            setVariable('LUCK', LUCK + 1)
            return CONFIDENCE, LUCK, hasRedPager
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
        elif choice == 'case study' and hasOmegaCaseStudy == False:
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
            global CONFIDENCE, LUCK, hasUltimateScalpel, collectedArtifacts
            ghosts = ((collectedArtifacts * 2) + 5)
            print(f'\nThe GHOSTS ATTACK! There are {ghosts} of them!')
            while ghosts > 0:
                if CONFIDENCE <= 0:
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
                            setVariable('CONFIDENCE', CONFIDENCE - 1)
                    elif playerChoice == 'dodge':
                        print('\nYou DODGED that bitch! You feel your CONFIDENCE increase!')
                        setVariable('CONFIDENCE', CONFIDENCE + 1)
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
                            setVariable('CONFIDENCE', CONFIDENCE - 1)
                    else:
                        print('Like a SEXUAL TIGER, you wait for an opening')  
            hasUltimateScalpel = True
            print('\nYou have defeated all of the ghosts on the FELLOW SHIP!\nThe ULTIMATE SCALPEL is yours!')
            collectedArtifacts += 1
        ghostFight()
        journeyChecker()
    def scrubTopChallenge():
        global CONFIDENCE, LUCK, collectedArtifacts, hasFinalScrubTop
        print('\nYou have divinationed the location of the Final Scrub Top'
        '\nYou find yourself knee-deep in the PRIMORDIAL LAUNDERING SERVICE'
        '\nBLOODY HELL, you think to yourself, This place is BEAUTIFUL'
        '\nYou look around, and see only BEAUTY. But you FEEL very SUSPICIOUS')
        if hasRedPager == True:
            print('\nYour RED PAGER goes off!'
                  '\nDOCTOR FRIEND: DOCTOR BLAZE! You must not trust your senses! \nThis is a CURSED PLACE!'
                  '\nYou must go AGAINST your instincts!'
                  '\nYour RED PAGER goes silent.')
        print('\nYou hear the INTERCOM bing its BONG'
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
            print(f'\nDOCTOR SEXY! You have {patientsToSee} more patients to see today!')
            question = random.choice(triviaQuestions)
            print("\n" + question["question"])
            print(f"Options: {question['choices'][0]} or {question['choices'][1]}")
            userAnswer = input("Your answer: ").strip().lower()
            if userAnswer == question['answer']:
                print('Correct! Grind them down')
                correctAnswers += 1
            else:
                print('Wrong! That little bastard looks better now. Your CONFIDENCE takes a hit!')
                setVariable('CONFIDENCE', CONFIDENCE - 1)
                if CONFIDENCE <= 0:
                    actTwoFailure()
                    return
            patientsToSee -= 1
            questionsAsked += 1
            triviaQuestions.remove(question)
        if questionsAsked == correctAnswers:
            print('Hot DOG! You got them all correct! You feel your CONFIDENCE and LUCK surge!')
            setVariable('LUCK', LUCK + 4)
            setVariable('CONFIDENCE', CONFIDENCE + 4)
        print('\nAfter your last patient leaves, you realize that you have summoned the FINAL SCRUB TOP!!!'
              '\nYou feel TERRIBLE about what you had to do to those poor patients! You lost some LUCK!')
        setVariable('LUCK', LUCK - 1)
        hasFinalScrubTop = True
        collectedArtifacts += 1
        journeyChecker()
    def caseStudyChallenge():
        global CONFIDENCE, LUCK, hasOmegaCaseStudy, collectedArtifacts
        print('\nAfter journeying for thousands of years, you come upon the LAIR of the OMEGA CASE STUDY'
              '\nIt simply sits there, on its IVORY PEDESTAL'
              '\nYou could take it, you think. You could take it and move on from this realm'
              '\nBUT, as you look around, you fail to find any peer reviewed documentation on this CASE STUDY'
              '\nYou could try to review it yourself, but that will probably be a whole thing.')
        choice = input('Will you TAKE the OMEGA CASE STUDY? Or will you PEER review it yourself?').strip().lower()
        if choice == 'take':
            print('\nYou FIRMLY GRASP the CASE STUDY in your greasy little claws'
                  '\nKnowing the data within is not reviewed gives you the JIBBLIES. You took the EASY WAY OUT')
            setVariable('LUCK', LUCK - 5)
            CONFIDENCE = 1
            print('CONFIDENCE updated to 1')
            hasOmegaCaseStudy = True
            collectedArtifacts += 1
        elif choice == 'peer':
            if hasRedPager == True:
                print('\nYour RED PAGER goes off!'
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
                    print(question["question"])
                    print("Possible answers:")
                    for idx, answer in enumerate(question["answers"], 1):
                        print(f"{answer}")

                    # Get player's answer
                    player_answer = input("Your answer (1 or 2): ").strip()

                    # Adjust the difficulty based on luck
                    if random.random() < (LUCK / 10):  # The higher the luck, the easier the question
                        print("\nThe question feels easier, luck is on your side!\n")
                        correct_answer = player_answer
                    else:
                        correct_answer = random.choice([answer for answer in question["answers"] if answer != question["correct_answer"]])

                    # Check if the answer is correct
                    if player_answer == correct_answer:
                        correct_answers += 1
                        print("\nCorrect!\n")
                        CONFIDENCE += 1
                    else:
                        print("\nIncorrect!\n")
                        CONFIDENCE -= 1
                        LUCK += 1

                    # If confidence reaches 0, call actTwoFailure()
                    if CONFIDENCE <= 0:
                        actTwoFailure()

                    # Move to the next question
                    question_idx += 1

                # If the player fails to get 3 correct answers, they still get the artifact
                if correct_answers < 3:
                    print(f"You have FAILED to peer review! Your CONFIDENCE is SHATTERED\n")
                    print('CONFIDENCE updated to 1')
                    CONFIDENCE = 1
                    print('The NONSENSICAL TOME has rewired your BRAIN to be more in tune with the COSMOS!')
                    setVariable('LUCK', LUCK + 10)

                # Update collected artifacts
                collectedArtifacts += 1
                hasOmegaCaseStudy == True
            peerReviewChallenge()
        else:
            print('PEEPA! Pick a real thing.')
            caseStudyChallenge()
        journeyChecker()
        pass
        

    journeyChecker() 
    pass
def actThree():
    global hasFinalScrubTop, hasOmegaCaseStudy, hasUltimateScalpel, hasRedPager
    slowPrint('The time has come, DOCTOR BLAZE.\nYou have obtained the ULTIMATE SCALPEL...\nthe FINAL SCRUB TOP...\nand the OMEGA CASE STUDY...'
            '\nYou make your way to MOUNT SINAI. You make your way to WIFE BRIAN, GENERAL ANESTHESIA, and YOUR DESTINY...'
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
    
    pass
def actOneFailure():
    print('Unfortunately, your adventure has ended before it really got started.')
    print('Later in the day, the world ends. You are not really sure why.')
    print('During the apocalypse you die of dysentery.')
    exit()
def actTwoFailure():
    slowPrint('\nYou feel your CONFIDENCE drop to NOTHING',.1
          '\nYou sink to the ground, distraught that WIFE BRIAN is being left to the forces of EVIL',.1
          '\nThe world ends. During the apocalypse, you die of dysentery',.1  
          )
    slowPrint('\nYOUR STORY IS OVER',0.5)
    exit()


#prologue()
#actOne()
#actTwo()
actThree()