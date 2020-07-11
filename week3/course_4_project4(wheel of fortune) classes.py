#only classes

class WOFPlayer():
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def addMoney(self,amt):
        self.prizeMoney = self.prizeMoney + amt
        
    def __str__(self):
        state = self.name + " ($" + str(self.prizeMoney) + ")"
        return state
    
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    
    def getMove(self, category, phrase, guess):
        input(
            "{%s} has ${%s}\n"
            "Category: {%s}\n"
            "Phrase:  {%s}\n"
            "Guessed: {%s}\n"
            "Guess a letter, phrase, or type 'exit' or 'pass':\n") % (
            self.name, self.prizeMoney, category, phrase, guess)
        return ("%s") % (guess)

# Write the WOFComputerPlayer class definition (part C) here
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    VOWEL_COST = 250
    VOWELS = "AEIOU"

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def smartCoinFlip(self):
        random_num = random.randint(1, 10)
        if random_num > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        return guessed.upper()

    def getMove(category, obscuredPhrase, guessed):
        return getPossibleLetters(guessed)


