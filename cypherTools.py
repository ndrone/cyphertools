import util

from history import History
from substitution import Substitution

menu = """Welcome to ndrone/cyphertools
    Select from the options below:
    Press '1' to load a file
    Press '2' to reset decipher in progress
    Press '3' to print history to screen
    Press '4' to write history to file *warning this clears the history
    Press '5' to search for a pattern and print counts to screen
    Press '6' to do substitution
    Press 'x' to exit
    selection: """

# list of readLines when we first loaded the file. This way if we need to start the decipher over we can without
# reading the file
file_contents = []
# list to be manipulated
cipher_text_list = []
# keep a history of changes for further analysis later
history = History()
substitution = Substitution()
selection = ""
while selection != "x":
    selection = input(menu)
    if selection == "1":
        file_contents = util.load_file(history)
        cipher_text_list = file_contents
        print("Done")
    if selection == "2":
        # reset everything but history
        cipher_text_list = file_contents
        history.append("resetting cipher to", str(cipher_text_list))
        substitution = Substitution()
        print("Done")
    if selection == "3":
        history.display()
    if selection == "4":
        history.save(input("output file to save to: "))
    if selection == "5":
        util.find_pattern(cipher_text_list, history)
    if selection == "6":
        cipher_text_list = substitution.do_substitution(cipher_text_list, history)
