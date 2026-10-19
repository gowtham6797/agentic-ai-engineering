try:
    a=int(input('Enter the numerator:'))
    b=int(input('Enter the denominator:'))

    result=a/b

    print('Result is ', result)

except ZeroDivisionError as zde:
    print('Cannot divide by Zero. Enter a valid number', zde)
except ValueError as ve:
    print('Use only numeric values', ve)
except Exception as e:
    print('Unknown error...')


print('Completed successfully...')