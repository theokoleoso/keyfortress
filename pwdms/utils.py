
import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

SECRET_KEY = 'PdSgUkXp2s5v8y/B?E(H+MbQeThWmZq4'


class PwdCrypto:
    """ A class that encrypts and decrypts passwords using AES and base64. """
    def __init__(self, key: str = SECRET_KEY):
        self.key = key.encode() # Convert String to bytes using encoding
        self.block_size = 16 # Chosen block size of 16 bytes

    def encrypt(self, password: str) -> str:
        # Pad the password to a multiple of block size (16)
        padding = self.block_size - len(password) % self.block_size  # Calculate padding needed for password
        password += chr(padding) * padding # Add padding
        # Encrypt the password with AES
        cipher = AES.new(self.key, AES.MODE_ECB)
        encrypted = cipher.encrypt(password.encode())
        # Encode the encrypted password with base64
        encoded = base64.b64encode(encrypted)
        return encoded.decode()

    def decrypt(self, password: str) -> str:
        # Decode the password with base64
        decoded = base64.b64decode(password)
        # Decrypt the password with AES
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted = cipher.decrypt(decoded)
        # Calculate padding bytes added to original message
        """ First gets length of decrypted message, subtracts one to get the index,
        splices to get the last element in the index
        The element is served to the ord() function which takes the argument of a single byte
        string and returns its corresponding integer 
        That integer relates to the amount of padding that was originally done
        """
        padding = ord(decrypted[len(decrypted) - 1:])
        # Unpad
        password = decrypted[:-padding]
        # Return decrypted password bytes as a string
        return password.decode()
