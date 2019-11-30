# Cow Bull Game
# 1 cow = 1 misplaced number
# 1 bull = 1 well placed number
# example of numbers : "0123" "0012" "1035" "9959"

from random import randint



class CowBull:
    def rand_num(self):
        num = ""
        for i in range(self.num_digits):
            num += str(randint(0, 9))
        return num

    def __init__(self, num_digits=4):  # num_digits for the number of digits in the number to guess
        self.num_digits = num_digits
        self.number = self.rand_num()

    def reset_number(self):
        self.number = self.rand_num()

    def evaluate(self, proposition):  # evaluates a proposition, returns number of cows and number of bulls
        cows = 0
        bulls = 0

        number_copy = self.number  # we copy it because we will delete from it during the evaluation.
        proposition_copy = proposition  # same for the proposition

        # Step 1 : find the well-placed numbers, count them, then "delete" them
        for i in range(self.num_digits):
            if number_copy[i] == proposition_copy[i]:
                number_copy[i] = "n"  # Replace all found well placed numbers by "n" so we don't recheck them afterwards
                proposition_copy[i] = "n"  # Do the same thing
                bulls += 1

        for i in range(self.num_digits):  # Count the number of cows
            if number_copy[i] != "n":  # Ignore the deleted parts
                f = proposition.find(i)  # Returns the position of the first occurrence of number_copy[i], else -1.
                if f >= 0:
                    cows += 1
                    number_copy[i] = "n"
                    proposition_copy[f] = "n"
        return cows, bulls


game = CowBull()
print(game.number)
