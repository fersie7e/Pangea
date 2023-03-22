from model.Usuario import Usuario

usr_name = input("introduzca un nombre de usuario: ")
pwd = input("introduzca una contraseña: ")

print("\n Creacion del objeto usuario: \n")

new_usr = Usuario(usr_name, pwd)

print(new_usr)
