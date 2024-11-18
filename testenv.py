
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


# Function to conduct the Peer Review Challenge
def peerReviewChallenge():
    global CONFIDENCE, collectedArtifacts, LUCK

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
            print(f"{idx}. {answer}")

        # Get player's answer
        player_answer = input("Your answer (1 or 2): ").strip()

        # Adjust the difficulty based on luck
        if random.random() < (LUCK / 10):  # The higher the luck, the easier the question
            print("\nThe question feels easier, luck is on your side!\n")
            correct_answer = question["correct_answer"]
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
