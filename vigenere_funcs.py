def key_check(key):
    if not (key.isalpha()):
        print("Cipher key must consist of one word with only letters")
        exit(1)
    key_len = len(key)
    if key_len < 3:
        print("Cipher key must be at least 3 letters long")
        exit(2)


def run_cipher(key, txt, type):
    """ Function to encode or decode a string with the Vigenere cypher.
    User must input a key (made up entirely of letters) and a plaintext string. """
    # Storage for encoding results
    result_chars = []

    # Call our key check function to check if the values are okay
    key_check(key)

    # Initialise variables to keep track of key position. Check key length.
    key_len = len(key)
    key_indx = 0

    # Loop through each letter of plaintext. For each plaintext letter,
    # get a new key letter. Reduce both letter values from their ASCII
    # values to alpha. Add them together. Then bring back to ASCII value

    for i in range(len(txt)):
        if txt[i].isalpha() or txt[i] != " ":
            key_val = ord(key[key_indx % key_len].lower()) - 97
            key_indx += 1

            # Check whether letter is uppercase
            if txt[i].isupper():
                ltr = ord(txt[i]) - 65
                if type == "encode":
                    new_ltr = chr(((ltr + key_val) % 26) + 65)
                else:
                    new_ltr = chr(((ltr - key_val) % 26) + 65)
                result_chars.append(new_ltr)

            # Check whether is lowercase

            elif txt[i].islower():
                ltr = ord(txt[i]) - 97
                if type == "encode":
                    new_ltr = chr(((ltr + key_val) % 26) + 97)
                else:
                    new_ltr = chr(((ltr - key_val) % 26) + 97)
                result_chars.append(new_ltr)

            # If its not a letter or a space, it must be a number or a special character.
            elif txt[i] != " ":
                if type == "encode":
                    ltr = chr((ord(txt[i]) + key_val) % 255)
                else:
                    ltr = chr((ord(txt[i]) - key_val) % 255)
                result_chars.append(ltr)

        # Else its a space. Add it. Don't touch the key values.
        else:
            result_chars.append(txt[i])

    # Convert the result array into a completed string, then return that string
    encoded_string = "".join(result_chars)

    return encoded_string