

from models.User import User
class UserManager:
    __Users=[]
    @classmethod
    def adduser(cls,userobj):
        if isinstance(userobj,User):
            cls.__Users.append(userobj)
            print("you have been successfully registered")
        else:
            print("invalid user")

    @classmethod
    def finduser(cls,email,password):
        for user in cls.__Users:
            if user.email==email and user.password==password:
                return user


