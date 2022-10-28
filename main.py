alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text = text, shift = shift):
    original_message = []
    for letter in text:
        original_message.append(letter)
    encrpyted_message = []
    for i in original_message:
        if shift + alphabet.index(i) > 25:
            encrpyted_message.append(alphabet[alphabet.index(i) + shift - 26])
        else:
            encrpyted_message.append(alphabet[alphabet.index(i) + shift])
    print(original_message)
    print(encrpyted_message)

encrypt()