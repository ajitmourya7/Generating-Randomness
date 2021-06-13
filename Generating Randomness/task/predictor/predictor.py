class GenerateRandomness:
    """Generate randomness"""

    def __init__(self):
        """Initiate user input"""
        self.number = ''
        self.capital = 1000
        self.profile = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
                        "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}

    def get_number(self):
        """Get string from user input. If the input is less than 100 store string and ask for more input."""
        data = input('Print a random string containing 0 or 1:\n\n')
        for x in data:
            if x == '0' or x == '1':
                self.number += x
        if len(self.number) < 100:
            print("The current data length is {}, {} symbols left".format(len(self.number), 100 - len(self.number)))
            self.get_number()
        else:
            self.generate_profile()

    def generate_profile(self):
        """Iterate the length of the string and search with slices for matches with the keys from the dictionary
         'profile'. If the next number to the last in the triad index is 0 or 1 store in the values of the dict."""
        for y in range(len(self.number) - 3):
            if self.number[y + 3] == "0":
                self.profile[self.number[y:y + 3]][0] += 1
            elif self.number[y + 3] == "1":
                self.profile[self.number[y:y + 3]][1] += 1
        print("\nFinal data string:\n{}".format(self.number))
        print("""
You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!
                """)
        self.prediction()

    def prediction(self):
        test_string = input("Print a random string containing 0 or 1:\n")
        if test_string == "enough":
            print("Game over!")
            return
        wrong_input = False
        for i in test_string:
            if i not in ["0", "1"]:
                wrong_input = True
        if wrong_input:
            self.prediction()
        else:
            prediction_string = test_string[:3]
            total = len(test_string) - 3
            for number in range(total):
                triad = test_string[number:number + 3]
                prediction_string += '0' if self.profile[triad][0] >= self.profile[triad][1] else '1'
            correct = 0
            for x in range(total):
                if prediction_string[x] == test_string[x]:
                    correct += 1
            print("prediction:\n{}\n".format(prediction_string))
            print("Computer guessed right {} out of {} symbols ({:.2f} %)".format(correct,
                                                                                  total,
                                                                                  (correct / total) * 100))
            self.capital += (total - correct)
            self.capital -= correct
            print("Your capital is now ${}\n".format(self.capital))
            self.prediction()


if __name__ == '__main__':
    print("Please give AI some data to learn...\nThe current data length is 0, 100 symbols left")
    GenerateRandomness().get_number()
