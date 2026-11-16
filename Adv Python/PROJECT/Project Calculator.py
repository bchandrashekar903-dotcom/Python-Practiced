import math

history = []


def show_history():
    print("\n" + "=" * 20 + " CALCULATION HISTORY " + "=" * 20)
    if not history:
        print("Oop's!.History is empty.")
    else:
        for idx, item in enumerate(history, 1):
            print(f"Result {idx}->{item}")
    print("=" * 61)


def clear_history():
    history.clear()
    print("\nCalculation history cleared successfully!")


def calculator_program():
    print("\n" + "=" * 20 + " EXPRESSION CALCULATOR " + "=" * 20)
    while True:
        expr = input("\nEnter expression: ").strip()

        if not expr:
            continue
        if expr.lower() in ('history', 'h'):
            show_history()
            continue
        if expr.lower() == 'clear':
            clear_history()
            continue
        if expr.lower() in ('exit', 'quit'):
            print("Exiting Calculator!")
            break

        try:
            # Replace ^ with ** for power
            expr_clean = expr.replace('^', '**')
            
            # Evaluate expression using standard math functions
            res = eval(expr_clean, {
                'sqrt': math.sqrt,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log10,
                'ln': math.log,
                'abs': abs,
                'fact': math.factorial,
                'pi': math.pi,
                'e': math.e
            })

            # Format whole numbers neatly as integers
            if isinstance(res, float) and res.is_integer():
                res = int(res)

            print(f"Result of expression [{expr}] = {res}")
            history.append(f"{expr} = {res}")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception:
            print("Error: Invalid expression!")

        again = input("\nDo you want to continue ? (yes/no): ").strip().lower()
        if again not in ('y', 'yes'):
            print("Exiting Calculator!")
            break


def main():
    while True:
        print("\n" + "=" * 50)
        print("               MENU DRIVEN PROGRAM")
        print("=" * 50)
        print("1.Calculator Expression Evaluate")
        print("2.View History")
        print("3.Clear History")
        print("4.Exit")
        
        choice = input("\nEnter your choice (1-4):").strip()
        
        if choice == '1':
            calculator_program()
        elif choice == '2':
            show_history()
        elif choice == '3':
            clear_history()
        elif choice == '4':
            print("\nExiting Program.")
            break
        else:
            print("Invalid choice! Please select a valid option (1-4).")


if __name__ == "__main__":
    main()




  