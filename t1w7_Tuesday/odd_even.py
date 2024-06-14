def is_even(num):
    return num % 2 == 0

def get_number():
    return int(input("enter a number: "))

def main():
    print("odd or even checker")
    number = get_number()
    if is_even(number):
        print(f"{number} is an even number")
    else:
        print(f"{number} is an False number")
    
# Run the main function
main()