def to_morse_code(text):
    result = ""
    for c in text:
        if c.isalpha():
            upper_c = c.upper()  # Convert to uppercase
            if 'A' <= upper_c <= 'M':
                result += "-"  # A-M is dash
            elif 'N' <= upper_c <= 'Z':
                result += "."  # N-Z is dot
        elif c.isspace():
            result += " "  # Keep spaces between words
    return result

def main():
    input_text = input("Enter text to convert to Morse Code: ")
    morse_code = to_morse_code(input_text)
    print("Morse Code Output:", morse_code)

if __name__ == "__main__":
    main()