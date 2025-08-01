from controllers.MainMenu import MainMenu
from controllers.foodManager import foodManager
from models.User import User
from models.UserManager import UserManager
from controllers.MainMenu import MainMenu


class Loginsystem:
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user=UserManager.finduser(email,password)
        if user is not None:
            print("Login Successful")
            menu = MainMenu()
            menu.start()
            exit()
        else:
            print("Login Failed")

    def register(self):
        name = input("Enter your name: ")
        mobile = int(input("Enter your mobile number: "))
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        new_user = User(name, mobile, email, password)
        UserManager.adduser(new_user)

    def exit(self):
        print("Thank you for logging in again")
        exit()

    def guest(self):
        pass
    def validoption(self,choice):
        getattr(self,choice)()
        """
        if choice == 1:
            self.login()
        elif choice == 2:
            self.register()
        elif choice == 3:
            self.guest()
        elif choice == 4:
            exit()
        else:
            print("invalid option")

        """


class foodApp:
    loginoptions={1:"login",2:"register",3:"guest",4:"exit"}
    @staticmethod
    def Init():
        print("<<welcome to online foodApp>>")
        loginsystem1=Loginsystem()
        while True:
            for option in foodApp.loginoptions:
                print(option,".",foodApp.loginoptions[option],end=" ")
                print()
            try:
                choice = int(input("Enter your choice: "))
                loginsystem1.validoption(foodApp.loginoptions[choice]) #choice call also
            except (ValueError,KeyError):
                print("invalid option","try another option")


