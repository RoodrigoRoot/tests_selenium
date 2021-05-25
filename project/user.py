import random

class User:
    def __init__(self, name, last_name, phone, email):
        self.__name = name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email
        self.__code = 0
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_code(self):
        return self.__code
    
    def set_code(self, code):
        self.__code = code

    name = property(get_name, set_name)
    last_name = property(get_last_name, set_last_name)
    email = property(get_email, set_email)
    phone = property(get_phone, set_phone)
    code = property(get_code, set_code)


class UserRegister:

    @classmethod
    def register_user(cls):
        name = input("Ingreser su nombre> ")
        last_name = input("Ingreser su apellido> ")
        email = input("Ingreser su email> ")
        phone = input("Ingrese su número> ")
        user = User(name, last_name, phone, email)
        user.code = random.randint(1000,9999)
        return user


class UserVerification:

    @classmethod
    def read_file(cls):
        text = ""
        #with open("verification.txt", 'r') as file:
        #    text = file.readline()
        text = "Tú código de verificación es: "
        return text
    
    @classmethod
    def get_message_code(cls, code):
        text = ""
        text = cls.read_file()
        text += str(code)
        return text
    
    @classmethod
    def verification_code(cls, user_code):
        code = int("Ingrese el código de verificación> ")
        if code == user_code:
            print("Usuario registrado")
