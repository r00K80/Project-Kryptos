def char_to_num(c):
    """Convert a character to its corresponding number (A=1, ..., Z=26)"""
    return ord(c.upper()) - ord('A') + 1

def num_to_char(n, is_lowercase):
    """Convert a number (1-26) back to a character, preserving case"""
    base = ord('a') if is_lowercase else ord('A')
    return chr((n - 1) % 26 + base)

def encode(text, pad):
    """Encode the text using the given one-time pad"""
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            num1 = char_to_num(text[i])
            num2 = char_to_num(pad[i % len(pad)])
            encoded_num = (num1 * num2) % 26
            if encoded_num == 0:
                encoded_num = 26
            result += num_to_char(encoded_num, text[i].islower())
        else:
            result += text[i]
    return result

def mod_inverse(a, m):
    """Compute the multiplicative inverse of a under modulo m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def decode(text, pad):
    """Decode the text using the given one-time pad"""
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            num1 = char_to_num(text[i])
            num2 = char_to_num(pad[i % len(pad)])
            inverse_num2 = mod_inverse(num2, 26)
            if inverse_num2 is None:
                raise ValueError(f"No modular inverse for {num2} under mod 26")
            decoded_num = (num1 * inverse_num2) % 26
            if decoded_num == 0:
                decoded_num = 26
            result += num_to_char(decoded_num, text[i].islower())
        else:
            result += text[i]
    return result

def main():
    one_time_pads = ["PROBLEM", "TANGRAM", "PUZZLES", "QUIZZES"]
    option = input("Would you like to encode or decode? (Enter 'encode' or 'decode'): ").strip().lower()

    if option not in ["encode", "decode"]:
        print("Invalid option. Please enter 'encode' or 'decode'.")
        return

    text = input("Enter the text to encode/decode: ").strip()

    results = []
    if option == "encode":
        for pad in one_time_pads:
            result = encode(text, pad)
            results.append(result)
    elif option == "decode":
        for pad in one_time_pads:
            result = decode(text, pad)
            results.append(result)
    
    for i, res in enumerate(results):
        print(f"Result with {one_time_pads[i]}: {res}")

if __name__ == "__main__":
    main()