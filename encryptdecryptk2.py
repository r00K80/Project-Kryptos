def char_to_num(c):
    return ord(c.upper()) - ord('A') + 1

def num_to_char(n, is_lowercase):
    base = ord('a') if is_lowercase else ord('A')
    return chr((n - 1) % 26 + base)

def encode(text1, text2):
    result = []
    for i, char in enumerate(text1):
        if char.isalpha():
            num1 = char_to_num(char)
            num2 = char_to_num(text2[i % len(text2)])
            encoded_num = (num1 + num2 - 1) % 26 + 1
            result.append(num_to_char(encoded_num, char.islower()))
        else:
            result.append(char)
    return ''.join(result)

def decode(text1, text2):
    result = []
    for i, char in enumerate(text1):
        if char.isalpha():
            num1 = char_to_num(char)
            num2 = char_to_num(text2[i % len(text2)])
            decoded_num = (num1 - num2 + 26 - 1) % 26 + 1
            result.append(num_to_char(decoded_num, char.islower()))
        else:
            result.append(char)
    return ''.join(result)

def main():
    option = input("Would you like to encode or decode? (Enter 'encode' or 'decode'): ").strip()
    
    text1 = input("Enter the first string (text to encode/decode): ").strip()
    text2 = input("Enter the second string (key): ").strip()
    
    if option == 'encode':
        print("Encoded result:", encode(text1, text2))
    elif option == 'decode':
        print("Decoded result:", decode(text1, text2))
    else:
        print("Invalid option. Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()