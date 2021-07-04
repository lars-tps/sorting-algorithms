class Manager():
    def __init__(self):
        self.amount = None
        self.data_types = []
        self.data = []   # Might change to HashTable
        self.create_data()

    def create_data(self):
        try:
            amount = int(input("Length of your data: "))
        except Exception:
            self.create_data()

        for i in range(amount):
            string = input(str(i) + "th Data to input: ")
            self.data_types.append(string)

    def add_data(self):
        list = []
        for i in range(len(self.data_types)):
            data = input("Input your " + self.data_types[i] + ": ")
            list.append(data)
        self.data.append(list)
        print(self.data)

