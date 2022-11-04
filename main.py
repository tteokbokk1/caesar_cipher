from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, cipher_direction):
    output_message = ""
    shift = shift % 26
    for letter in text:
        try:
            if cipher_direction == "encode":
                new_position = alphabet.index(letter) + shift
            elif cipher_direction == "decode":
                new_position = alphabet.index(letter) - shift
            output_message += alphabet[new_position]
        except ValueError:
            output_message += letter
    print(f"Your {cipher_direction}d text is {output_message}")

repeat = True
while repeat == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    replay = input("Would you like to go again? Yes or No?\n").lower()
    if replay == "no":
        repeat = False