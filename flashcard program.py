import random
import flashcardsSDK
from flashcard import Flashcard

while True:
    print("""\nChoose an option: \n
    1: Test a specific flashcard
    2: Test all flashcards in order
    3: Test all flashcards randomly
    4: Test flashcards from leitner system

    5: Add a flashcard
    6: Delete a flashcard

    7: Show all flashcards
    8: Show specific flashcard

    else: exit
    """)
    response = input()

    if response == '1':
        print("What topic?")
        topic = input()
        flashcard = flashcardsSDK.get_flashcard_by_topic(topic)
        if flashcard is not None:
            # flashcard.test()
            flashcard.AI_test()

    elif response == '2':
        escape = 'y'
        while escape == 'y':
            for flashcard in flashcardsSDK.get_flashcards():
                flashcard.test()
                print("Carry on y/n")
                escape = input()
                if escape != 'y':
                    break

    elif response == '3':
        escape = 'y'
        while escape == 'y':
            flashcard = random.choice(flashcardsSDK.get_flashcards())
            correct = flashcard.test()
            print("Carry on y/n")
            escape = input()

    elif response == '4':
        escape = 'y'
        while escape == 'y':
            while True:
                try:
                    number = random.randint(1, 15)
                    if 1 <= number <= 5:
                        flashcards = flashcardsSDK.get_flashcards_by_leitner(0)
                    if 6 <= number <= 9:
                        flashcards = flashcardsSDK.get_flashcards_by_leitner(1)
                    if 10 <= number <= 12:
                        flashcards = flashcardsSDK.get_flashcards_by_leitner(2)
                    if 13 <= number <= 14:
                        flashcards = flashcardsSDK.get_flashcards_by_leitner(3)
                    if number == 15:
                        flashcards = flashcardsSDK.get_flashcards_by_leitner(4)
                    if len(flashcards) > 0:
                        break
                except:
                    pass
            flashcard = random.choice(flashcards)
            flashcardsSDK.update_leitner(flashcard.leitner_test(), flashcard.topic)
            print("Carry on y/n")
            escape = input()
            if escape != 'y':
                break

    elif response == '5':
        print("What is the topic?")
        topic = input()
        print("What is the content?")
        content = input()
        print("What are the keywords?")
        keywords = input()
        leitner = 0
        flashcard = Flashcard(topic, content, keywords, leitner)
        flashcardsSDK.add_flashcard(flashcard)

    elif response == '6':
        print("What is the topic?")
        topic = input()
        print("Are you sure you wish to delete this flashcard? y/n")
        confirmation = input()
        if confirmation == 'y':
            flashcardsSDK.delete_flashcard(topic)

    elif response == '7':
        for flashcard in flashcardsSDK.get_flashcards():
            print(flashcard)

    elif response == '8':
        print("What is the flashcard's topic?")
        topic = input()
        flashcard = flashcardsSDK.get_flashcard_by_topic(topic)
        print(flashcard)

    else:
        print("Thanks for using the flashcard program")
        break
