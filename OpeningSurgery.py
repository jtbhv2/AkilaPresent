

LUCK = 0
redPager = True
CONDFIDENCE = 10
surgerySuccess = True
def prologue():
    
    complication_handled = False

    print("Welcome! You are DOCTOR AKILA B BLAZE: Pediatric surgeon by day, fierce adventurer by night.")
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
        if surgerySuccess:
            print("\nCongratulations! The pediatric appendectomy was successful. Excellent job, Surgeon!")
        else:
            print("\nThe surgery did not go well. Better luck next time.")
        return surgerySuccess

    def end_game(message):
        print(message)
        finish()

    step_one()
    return surgerySuccess
def actOne():
    if surgerySuccess == True:
        print('DOCTOR COLLEAGUE: Great job DOCTOR BLAZE. I have never seen such quick thinking before. Not once in my 23 years.')
        CONDFIDENCE += 1

    else:
        print('DOCTOR COLLEAGUE: It happens, DOCTOR BLAZE. We have all had off days. Shake it off! He then smacks you on the back way too hard.')
        CONDFIDENCE -= 1
    
    print('After the surgery, your RED PAGER goes off')
    print('You think: Oh no! not the RED PAGER! That is for personal emergencies only!')
    while True:
        choice = input('Do you RESPOND to the RED PAGE, or do you IGNORE?').strip().lower()
        if choice == 'ignore':
            return choice
        elif choice == 'red page':
            print('Very funny. Trying to take advantage of me like that. You know what? You are going to be punished for this. Now please pick something else.')
            LUCK -= 1
        if choice == 'respond':
            return choice
        else:
            print('I do not understand. So I will ask again.')
    if choice == 'ignore':
        
def actOneFailure():


prologue()
print(surgerySuccess)
