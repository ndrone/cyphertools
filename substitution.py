class Substitution:

    def __init__(self):
        self.substitution_key = {}

    def do_substitution(self, encrypted_text_list, history):
        print("current substitution cipher" + str(self.substitution_key))

        search = input("Enter search term:")
        replace = input("Enter replacement term:")
        self.substitution_key[search] = replace
        history.append("Updating substitution cipher", str(self.substitution_key))

        changed_text_list = []
        for line in encrypted_text_list:
            changed_text_list.append(str(line.replace(search, replace)))

        history.append("Deciphering encrypted text to", changed_text_list)
        return changed_text_list
