import random
LUCK = 100
CONFIDENCE = 10
def finalBattle():
    generalHealth = random.randint(int(CONFIDENCE * 1.1), int(CONFIDENCE * 1.5))
    choices = ['SCALPEL','CASE STUDY','SCRUB TOP']
    outcomeMessages = {
    ('SCALPEL', 'SCRUB TOP'): "Your SCALPEL slices the SCRUB TOP into avant-garde fashion!",
    ('SCRUB TOP', 'CASE STUDY'): "Your SCRUB TOP blinds the CASE STUDY into submission. Disco win!",
    ('CASE STUDY', 'SCALPEL'): "Your CASE STUDY sends the SCALPEL into an identity crisis. Genius!",
    ('SCRUB TOP', 'SCALPEL'): "Her SCALPEL deflects your SCRUB TOP like a superhero cape!",
    ('CASE STUDY', 'SCRUB TOP'): "Her SCRUB TOP buries the CASE STUDY in citations. Tragic!",
    ('SCALPEL', 'CASE STUDY'): "Her CASE STUDY sends your SCALPEL into a footnote rescursion loop. Oof.",
    'tie': "You went for the same object! Both sides break into interpretive dance, leaving everyone extremely uncomfortable."
}
    playerChoice = input('What will you do? (SCALPEL, CASE STUDY, or SCRUB TOP?)').strip().upper()
    if playerChoice not in choices:
        print('Not a valid choice.')
        return
    luckCheck = random.random() + (LUCK / 100)
    if luckCheck > 0.8:
        generalChoice = choices[(choices.index(playerChoice)+ 2) % 3]
        print('LUCK is on your side! The GENERAL chose poorly!')
    elif luckCheck < 0.2:
        generalChoice = choices[(choices.index(playerChoice)+ 1) % 3]
        print('Bad LUCK! She saw this coming from a mile away!')
    else:
        generalChoice = random.choice(choices)
    print(f'\nThe GENERAL chooses {generalChoice}!')
    if playerChoice == generalChoice:
        print(outcomeMessages['tie'])
    elif (playerChoice, generalChoice) in outcomeMessages:
        print(outcomeMessages[(playerChoice, generalChoice)])
    else:
        print(outcomeMessages[(generalChoice, playerChoice)])
finalBattle()