import re

def is_scientific_number(number):
    pattern = r'^-?\d+(\.\d+)?([eE][-+]?\d+)?$'
    return re.match(pattern, number) is not None

def main():
    print("Scientific Number Checker")
    while True:
        user_input = input("Enter a number (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        if is_scientific_number(user_input):
            print("Yes, it is a number")
        else:
            print("No, it is not a number")

if __name__ == "__main__":
    main()