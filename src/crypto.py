from cryptography.fernet import Fernet
import base64



# Generar una clave Fernet
key = Fernet.generate_key()

# Crear un objeto Fernet con la clave generada
cipher_suite = Fernet(key)

# Datos a cifrar
data_to_encrypt = b"Hola, este es un mensaje secreto."

# Cifrar los datos
cipher_text = cipher_suite.encrypt(data_to_encrypt)
print(f'Datos cifrados: {base64.b64encode(cipher_text)}')

# Descifrar los datos
plain_text = cipher_suite.decrypt(cipher_text)
print(f'Datos descifrados: {plain_text.decode("utf-8")}')