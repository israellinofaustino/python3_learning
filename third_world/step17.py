try:
    a = int(input("First number => "))
    b = int(input("Second number => "))
    answer = a/b
except (ValueError, TypeError):
    print("We had a problem with the type of data you entered.")
except ZeroDivisionError:
    print("It is not possible to divide a number by zero.")
except KeyboardInterrupt:
    print("\nThe user chose not to inform the data.")
except Exception as error:
    print(f"The error found was {error.__cause__}.")
else:
    print(f"The result is {answer:.2f}")
finally:
    print("Thank you! Come back often.")
