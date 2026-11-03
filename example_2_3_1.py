saved_psw = "NewPassword"
psw = input("Введите пароль для входа: ")
while psw != saved_psw:
    psw = input("Пароль введен неверно. Введите пароль повторно: ")
print("Пароль верный")