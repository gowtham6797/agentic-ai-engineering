try:
    a = int(input("Enter the numerator:"))
    b = int(input("Enter the denominator:"))

    result = a / b

    print("Result is ", result)

except ZeroDivisionError as zde:
    print("Cannot divide by Zero. Enter a valid number", zde)
except ValueError as ve:
    print("Use only numeric values", ve)
except Exception as e:  # noqa: BLE001
    print("Unknown error...", e)


print("Completed successfully...")
