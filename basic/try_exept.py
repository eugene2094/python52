# try except

try:
    print(2 / 0)
except:
    print("number cant be 0")


# try:
#     amount = int(input("Enter the amount of received item - "))
#     item_type = input("Enter type of item - ")
#     parts_number = int(input("Enter the number of parts - "))
#     parts_amount = amount / parts_number
#
# except (ValueError, TypeError):
#     print("Amount should be an interger!")
# except ZeroDivisionError:
#     print("Cannt devide by zero!")
# except Exception as ex:
#     print(ex)
# finally:
#     print("Finished !")
#
# try:
#     age = int(input("Enter age: "))
#     if age < 0:
#         raise Exception("Age must be > 0")
# except ValueError:
#     print("error input age")
# except Exception as ex:
#     print(ex)


def buy_ticket(age, balance, price):
    try:
        age = int(age)
        balance = float(balance)

        if age < 18:
            raise ValueError("Error age !")

        if balance < price:
            raise Exception("Error balance ")

        print("Ticket was paid !")
    except ValueError as e:
        print("Have error with value: ", e)
    except Exception as e:
        print("Some Error ", e)
    else:
        print("Operation finished without error!")
    finally:
        print("Testing finished!")


buy_ticket(16, 500, 300)

buy_ticket(20, 500, 600)
buy_ticket(26, 500, 300)

buy_ticket("45.", 500, 300)
