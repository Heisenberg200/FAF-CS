from cryptography.fernet import Fernet


class Encryption:

    def __init__(self):
        key = self.call_key()
        self.crypto = Fernet(key)

    @staticmethod
    def call_key():
        return open("pass.key", "rb").read()

    @staticmethod
    def write_key():
        key = Fernet.generate_key()

        with open("pass.key", "wb") as key_file:
            key_file.write(key)

    def encrypt_data(self, data):
        return self.crypto.encrypt(data.encode())

    def decrypt_data(self, data):
        return self.crypto.decrypt(data).decode()
