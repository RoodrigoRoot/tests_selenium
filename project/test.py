from send import WhatsAppMessages
from user import UserVerification, UserRegister, User


user = UserRegister.register_user()
message = UserVerification.get_message_code(user.code)
print(user.code)
WhatsAppMessages.send_message(user, message)