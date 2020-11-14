class PolyAlphabetic:

    def __init__(self):
        self.alpha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
                      'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,
                      'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
        self.key = []
        self.menu = """
Select from the options below:
    Press '1' to append character to key
    Press '2' to replace a specific character in the key
    Press '3' to print key to screen
    Press '4' to decrypt with the set key
    Press 'b' to go back
selection: """

    def main(self, encrypted_text_list, history):
        selection = ""
        while selection != "b":
            selection = input(self.menu)
            if selection == "1":
                self.__append_key(history)
            if selection == "2":
                self.__replace(history)
            if selection == "3":
                print("Current key {}".format(str(self.key)))
            if selection == "4":
                self.__decrypt(encrypted_text_list, history)

    def __append_key(self, history):
        element = input("Enter an upper case character to append to the key: ")
        self.key.append(element)
        history.append("Adding character '{}'".format(element), str(self.key))

    def __replace(self, history):
        index = input("Enter the character to be replaced: ")
        replacement = input("Enter the replacement upper case character: ")
        for n, i in enumerate(self.key):
            if i == index:
                self.key[n] = replacement
        history.append("Replacing key '{}' with '{}'".format(index, replacement), str(self.key))

    def __decrypt(self, encrypted_text_list, history):
        # we only want to read one line at a time. The key starts over at the start of each line
        decrypted_text_list = []
        for line in encrypted_text_list:
            key_index = 0
            decrypted_text = ""
            for c in line:
                if c not in self.alpha:
                    # possible \n so instead of stopping just skip and continue
                    break
                # Get the character value so we can do math
                c_value = self.alpha[c]
                k_value = self.alpha[self.key[key_index]]
                total = c_value + k_value
                # if the total is above or dictionary subtract the dictionary till it is within
                # range
                while total > 25:
                    total = total - 25

                # Now that our total is within range of the dictionary values
                # loop through to find the value that matches, and get the key (the character)
                # that corresponds to that value.
                for x, y in self.alpha.items():
                    if y == total:
                        if x != c:
                            # write out the translated character in lower case
                            # in case we are still trying to translate other parts of the cipher
                            decrypted_text += x.lower()
                        else:
                            decrypted_text += x

                # increment the key or start over
                if key_index == (len(self.key) - 1):
                    key_index = 0
                else:
                    key_index += 1
            decrypted_text_list.append(decrypted_text)

        history.append("Decrypting with key {}".format(str(self.key)), decrypted_text_list)
