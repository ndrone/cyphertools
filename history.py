class History:

    def __init__(self):
        self.history_list = []

    def append(self, header, content):
        self.history_list.append("{}\n{}\n".format(header, content))

    def display(self):
        for element in self.history_list:
            print(element)
            print("\n")

    def save(self, file_name):
        file = open(file_name, "a")
        for element in self.history_list:
            file.write(element)
        file.close()
        self.history_list = []
