from user import UserRegister
from whatsapp import WhatsappMessages

user = UserRegister.register_user()
message = UserRegister.get_message_code(user.code)

WhatsappMessages.send_message(user, message)