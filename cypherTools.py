import pathlib
import re

from history import History


def main():
    menu = """Welcome to ndrone/cyphertools
    Select from the options below:
    Press '1' to load a file
    Press '2' to reset decipher in progress
    Press '3' to print history to screen
    Press '4' to write history to file *warning this clears the history
    Press '5' to search for a pattern and print counts to screen
    Press 'x' to exit
    selection: """

    # list of readLines when we first loaded the file. This way if we need to start the decipher over we can without
    # reading the file
    file_contents = []
    # list to be manipulated
    cipher_text_list = []
    # keep a history of changes for further analysis later
    history = History()
    selection = ""
    while selection != "x":
        selection = input(menu)
        if selection == "1":
            input_file_name = input("Enter file name to load relative from {}: ".format(pathlib.Path().absolute()))
            file_contents = load_file(input_file_name)
            cipher_text_list = file_contents
            history.append("load file {}".format(input_file_name), str(file_contents))
            print("Done")
        if selection == "2":
            cipher_text_list = file_contents
            history.append("resetting cipher to", str(cipher_text_list))
            print("Done")
        if selection == "3":
            history.display()
        if selection == "4":
            history.save(input("output file to save to: "))
        if selection == "5":
            find_pattern(cipher_text_list, history)


def load_file(file_name):
    file = open(file_name, "r")
    file_lines = []
    for line in file.readline():
        file_lines.append(line)
    file.close()
    return file_lines


def find_pattern(search_text_list, history):
    freq = {}
    regex = input("Enter regex search term: ")
    for line in search_text_list:
        matches = re.findall(regex, line)
        for match in matches:
            if match in freq:
                freq[match] += 1
            else:
                freq[match] = 1

    # sort in descending order by count
    sorted_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
    history.append("Count of pattern '{}' ".format(regex), str(sorted_freq))
    print("Count of pattern '{}' ".format(regex) + str(sorted_freq))


main()
