print('''   
U /"___|U  /"\  u  |"|    U /"___|U |"|u| |  |"|    U  /"\  u  |_ " _|   \/"_ \/U |  _"\ u  
\| | u   \/ _ \/ U | | u  \| | u   \| |\| |U | | u   \/ _ \/     | |     | | | | \| |_) |/  
 | |/__  / ___ \  \| |/__  | |/__   | |_| | \| |/__  / ___ \    /| |\.-,_| |_| |  |  _ <    
  \____|/_/   \_\  |_____|  \____| <<\___/   |_____|/_/   \_\  u |_|U \_)-\___/   |_| \_\   
''')
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        print("Undefined Number (division by zero)")
        return None
    return a / b

def calculate(operand, fn, ln):
    if operand == '+':
        solution = add(fn, ln)
    elif operand == '-':
        solution = sub(fn, ln)
    elif operand == '*':
        solution = mul(fn, ln)
    elif operand == '/':
        solution = div(fn, ln)
        if solution is None:
            return None
    else:
        print("Select the right operand")
        return None

    print(f"{fn} {operand} {ln} = {solution}")
    return solution

def main():
    first_digit = float(input("Enter the first digit: "))
    print("Select one operation")
    print("addition         => +")
    print("subtraction     => -")
    print("division        => /")
    print("multiplication  => * ")
    oper = input()
    last_digit = float(input("Enter the second number: "))

    result = calculate(oper, first_digit, last_digit)

    if result is not None:
        print("Type 'yes' to continue the calculation or 'no' to exit")
        while input().lower() == 'yes':
            new_oper = input("Pick an operator: ")
            new_digit = float(input("What's the next digit? "))
            result = calculate(new_oper, result, new_digit)
            if result is None:
                break

    print("Thank you")

if __name__ == "__main__":
    main()
