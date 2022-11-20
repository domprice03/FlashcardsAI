import AI2


class Flashcard:
    def __init__(self, topic, content, keywords, leitner):
        self.topic = topic
        self.content = content
        self.keywords = keywords
        self.leitner = int(leitner)

    def test(self):
        print('Topic:' + self.topic)
        answer = input()
        correct = True
        self.keywords = self.keywords.split(',')

        for i in self.keywords:
            if i not in answer:
                correct = False

        if correct is False:
            print('Incorrect')
        else:
            print('correct')

        print(self.content + '\n')
        return correct

    def leitner_test(self):
        if self.test() is False:
            if self.leitner > 0:
                self.leitner -= 1
        else:
            if self.leitner < 4:
                self.leitner += 1

        return self.leitner

    def AI_test(self):
        print('Topic:' + self.topic)
        answer = input()
        correct = AI2.check(self.content, answer)
        if correct:
            print('Correct')
        else:
            print('Incorrect')

    # What happens when you pass object to print?
    def __str__(self):
        return f"Topic: {self.topic}\n\tContent: {self.content}\n\t" \
               f"Keywords: {self.keywords}\n\tLeitner score: {self.leitner}"

    # What happens when you use ==?
    def __eq__(self, other):
        if self.topic == other.topic and self.content == other.content and \
                self.keywords == other.keywords and self.leitner == other.leitner:
            return True
        return False

    # It's appropriate to give something for __hash__ when you override __eq__
    __hash = None

    # def __repr__(self):  # Added to make list of items invoke str
        # return self.__str__()
