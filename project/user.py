import random 

class User:

    def __init__(self, name, last_name, email, phone):
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__code = 0

    def __str__(self):
        return f"Full name: {self.name} {self.last_name} \nCode: {self.code}"

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone

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

    @staticmethod
    def register_user():
        print("*"*70)
        name = input("Ingrese su nombre> ")
        last_name = input("Ingrese su apellido> ")
        email = input("Ingrese su email> ")
        phone = input("Ingrese su teléfono> ")
        user = User(name, last_name, email, phone)
        user.code = random.randint(1000, 9999)
        print("*"*70)
        return user


    @staticmethod
    def get_message_code(code):
        text = f"Tu código de verificación es: {code}"
        return text


    @staticmethod
    def verification_code(user_code):
        code = int(input("Ingrese el código que le enviamos a Whatsapp> "))
        if user_code == code:
            print("Usuario registrado")
        else:
            print("No se pudo procesar tu solicitud")
