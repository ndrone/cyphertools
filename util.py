import pathlib
import re


def load_file(history):
    input_file_name = input("Enter file name to load relative from {}: ".format(pathlib.Path().absolute()))
    file = open(input_file_name, "r")
    file_lines = file.readlines()
    file.close()
    history.append("load file {}".format(input_file_name), str(file_lines))
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
