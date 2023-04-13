user_data = [["Maksim", "10072005"], ["Ivan", "03052005"], ["Danata", "18032005"]]


def get_name():
    name = input("Enter your name: ")
    output = check_names(name)
    return output


def check_names(name):
    x = len(name)
    while x < 2 or x > 11:
        print("Error!")
        name = input("Please enter your name again!: ")
    return name


name_result = get_name()



def get_password():
    password = input("Enter your password: ")
    output = check_password(password)
    return output


def check_password(password):
    x = password
    while len(x) < 2 or len(x) > 21:
        print("Bad!Authentication Error.Check name or password! Rewrite password!")
        x = input("Enter your password: ")
    return x


password_result = get_password()
input_data = [name_result, password_result]

def check_authentification(y):
    while y not in user_data:
        print("Error.Enter your data again!CUM")
        y = [get_name(), get_password()]
    print(f"Hello,{y[0]},WElCOME to the system!")


check_authentification(input_data)

