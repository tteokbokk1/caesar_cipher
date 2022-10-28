alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(regular_text, shift_num):
    original_message = []
    for letter in regular_text:
        original_message.append(letter)
    encrpyted_message = []
    for i in original_message:
        if shift_num + alphabet.index(i) > 25:
            encrpyted_message.append(alphabet[alphabet.index(i) + shift_num - 26])
        else:
            encrpyted_message.append(alphabet[alphabet.index(i) + shift_num])
    print(f"Your encrypted text is {''.join(encrpyted_message)}")

encrypt(text, shift)