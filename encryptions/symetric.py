from cryptography.fernet import Fernet

class Symmetric():

    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)

    @staticmethod
    def generate_key():
        """Generates key

        Returns:
            bytes: HEX key
        """
        return Fernet.generate_key()
    
    def encode(self,message): 
        """Encrypts message with the key specified on initalization

        Args:
            message (str): Message to encrypt

        Returns:
            bytes: HEX encrypted message
        """
        return self.fernet.encrypt(bytes(message, 'utf-8'))
    
    def decode(self,message): 
        """Decrypts message with the key specified on initalization

        Args:
            message (bytes): HEX encrypted message

        Returns:
            str: Decrypted message
        """
        return self.fernet.decrypt(bytes(message, 'utf-8'))
