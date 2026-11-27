import sys
def validateInput(inp):
    """Verify input"""
    while (True):
        if len(inp) == 2:
            break
        elif len(inp) > 2:
            raise AssertionError("Too many arguments")
        elif len(sys.argv) < 2:
            print("What is the text to count?")
            userInput = input()
            if len(userInput) > 0:
                inp.append(userInput)
    return inp

def count(phrase: str):
    """Count the sums of all letters and punctuation counts"""
    upper_char_count = 0
    lower_char_count = 0
    punctuation_count = 0
    space_count = 0
    digits_count = 0
    for s in phrase:
        if s in "'.,;:?!":
            punctuation_count += 1
        elif s.isupper():
            upper_char_count += 1
        elif s.islower():
            lower_char_count += 1
        elif s.isspace():
            space_count += 1
        elif s.isnumeric():
            digits_count += 1
    return upper_char_count, lower_char_count, punctuation_count, space_count, digits_count

def main():
    validateInput(sys.argv)

    result = count(sys.argv[1])

    """Display the result"""
    print(f"The text contains {len(sys.argv[1])} characters:")
    print(f"{result[0]} upper letters")
    print(f"{result[1]} lower letters")
    print(f"{result[2]} punctuation")
    print(f"{result[3]} space")
    print(f"{result[4]} digits")

if __name__ == "__main__":
    main()