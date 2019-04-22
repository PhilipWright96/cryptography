import unittest
import vig_functions


class MyTest(unittest.TestCase):

    # Tests to ensure encoding and decoding operate correctly. Even with symbols included.

    def test_encode(self):
        self.assertEqual(vig_functions.run_cipher('bcd', 'hello+', 'encode'), "igomq.")

    def test_decode(self):
        self.assertEqual(vig_functions.run_cipher('bcd', 'igomq.', 'decode'), "hello+")


def main():
    choice = int(input("Welcome to a Vigenere encryption program. Press 1 to encode. Press 2 to decode. "
                       "Press 3 to run unit tests \n"))

    if choice == 1:
        key = input("Please insert cipher key. Key must consist of at least 3 letters and no numbers or symbols. \n ")
        plaintext = input("Please insert plaintext ")
        print(vig_functions.run_cipher(key, plaintext, "encode"))

    elif choice == 2:
        key = input("Please insert cipher key. Key must consist of at least 3 letters and no numbers or symbols. \n")
        encoded_string = input("Please insert encoded string ")
        print(vig_functions.run_cipher(key, encoded_string, "decode"))

    elif choice == 3:
        unittest.main()

    else:
        print("Invalid input")
        exit(3)


if __name__ == '__main__':
    main()