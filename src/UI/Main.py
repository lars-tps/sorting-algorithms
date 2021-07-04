from src.UI.Manager import Manager
class Main():
    def __init__(self):
        self.manager = Manager()
        self.prompt()
        self.check_command()

    def check_command(self):
        try:
            choice = int(input("Choose : "))
            if choice > 3:
                raise Exception
        except Exception:
            self.check_command()

        if choice == 1:
            self.manager.add_data()
        elif choice == 2:
            raise NotImplementedError


    def prompt(self) -> None:
        print("========================")
        print("                        ")
        print("========================")
        print("1. Add Data")
        print("2. Sort Data")
        print("3. Quit")

main = Main()