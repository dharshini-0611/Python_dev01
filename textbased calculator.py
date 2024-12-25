def add(a, b):    
    return a + b

def subtract(a, b):    
    return a - b

def multiply(a, b):    
    return a * b

def divide(a, b):    
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a // b if a % b == 0 else a / b  

def calculate(expression):
    try:
        expression = expression.replace(" ", "")
        
        if '+' in expression:
            operand1, operand2 = expression.split('+')
            operator = '+'
        elif '-' in expression:
            operand1, operand2 = expression.split('-')
            operator = '-'
        elif '*' in expression:
            operand1, operand2 = expression.split('*')
            operator = '*'
        elif '/' in expression:
            operand1, operand2 = expression.split('/')
            operator = '/'
        else:
            raise ValueError("Unsupported operator. Use +, -, *, or /.")
        
        operand1 = float(operand1)
        operand2 = float(operand2)

        if operator == '+':
            result = add(operand1, operand2)
        elif operator == '-':
            result = subtract(operand1, operand2)
        elif operator == '*':
            result = multiply(operand1, operand2)
        elif operator == '/':
            result = divide(operand1, operand2)

        if isinstance(result, float) and result.is_integer():
            result = int(result)  
        
        return result

    except ValueError as e:
        return f"Error: {e}"

def main():
    print("Welcome to the Text Calculator!")
    print("Type 'exit' to quit.")
    print("-" * 50)

    while True:
        user_input = input("Enter expression: ").strip()
        if user_input.lower() == "exit":
            print("Thank you for using the Text Calculator. Goodbye!")
            break

        result = calculate(user_input)
        print(f"Result: {result}")
        print("-" * 50)

if __name__ == "__main__":
    main()
