import sys

if len(sys.argv) == 2:
    skey = sys.argv[1]
    key = int(skey)
else:
    print("You must enter a key")
    sys.exit(1)

p = input("Please insert plaintext: ")

print("ciphertext: ", end="")

for i in range(len(p)):
    if p[i].isalpha():
        if p[i].isupper():
            letter = ord(p[i]) - 65
            encrypt = ((letter + key) % 26) + 65
            cencrypt = chr(encrypt)
            print(f"{cencrypt}", end="")
        elif p[i].islower():
            letter = ord(p[i]) - 97
            new_letter = ((letter + key) % 26) + 97
            cencrypt = chr(new_letter)
            print(f"{cencrypt}", end="")
        else:
            print(f"{p[i]}", end="")

print()