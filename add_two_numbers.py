def get_valid_number(prompt: str) -> float:
    while True:
        try:
            user_input = input(prompt)
            return float(user_input)
        except ValueError:
            print("  [!] Invalid input. Please enter a valid numerical value.\n")

def add_numbers(a: float, b: float) -> float:
    return a + b

def display_summary(num1: float, num2: float, total: float) -> None:
    print("\n" + "=" * 32)
    print("     ADDITION CALCULATION     ")
    print("=" * 32)
    print(f" First Number  : {num1}")
    print(f" Second Number : {num2}")
    print("-" * 32)
    print(f" Calculated Sum: {total}")
    print("=" * 32 + "\n")

def main() -> None:
    print("--- Welcome to the Addition Utility ---\n")
    first_num = get_valid_number("Enter first number: ")
    second_num = get_valid_number("Enter second number: ")
    sum_result = add_numbers(first_num, second_num)
    display_summary(first_num, second_num, sum_result)

if __name__ == "__main__":
    main()