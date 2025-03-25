
from graphics import *

staff_username = "staff"
staff_password = "welcome"

def write_to_file(result, credits_pass, credits_defer, credits_fail):
    with open("histogram_data.txt", 'a') as file:
        file.write("{}: ({} , {} , {})\n".format(result, credits_pass, credits_defer, credits_fail))

def read():
    print("part 3")
    print("---------")
    with open('histogram_data.txt', 'r') as file:
        data = file.read()
        print(data)

def get_user_input():
    try:
        credits_pass = int(input("Enter the credits at Pass : "))
        credits_defer = int(input("Enter the credits at defer : "))
        credits_fail = int(input("Enter the credits at Fail : "))
        return credits_pass, credits_defer, credits_fail
    except ValueError:
        print("Integer required")
        return get_user_input()

def validate_credits(credits_pass, credits_defer, credits_fail):
    credit_list = [0, 20, 40, 60, 80, 100, 120]
    if not all(credit in credit_list for credit in [credits_pass, credits_defer, credits_fail]):
        print("Out of range")
        return False

    credit_total = credits_pass + credits_defer + credits_fail
    if credit_total != 120:
        print("Total incorrect")
        return False

    return True

def predict_progression(credits_pass, credits_defer, credits_fail):
    if credits_pass == 120:
        result = "Progress"
    elif credits_pass == 100:
        result = "Progress (Module trailer)"
    elif credits_fail >= 80:
        result = "Exclude"
    else:
        result = "Do not Progress - Module retriever"

    write_to_file(result, credits_pass, credits_defer, credits_fail)
    return result

def progression_predict():
    students_data = []
    print("________________________________________________________________________________________________")
    print("Hello Staff, Welcome To The University Progression Predictor")
    user_choice = "y"
    while user_choice.lower() == "y":
        credits_pass, credits_defer, credits_fail = get_user_input()

        if not validate_credits(credits_pass, credits_defer, credits_fail):
            continue

        result = predict_progression(credits_pass, credits_defer, credits_fail)
        students_data.append(result)
        print(result)

        user_choice = input("Do you want to predict progression for another student? (y/q) : ")
        if user_choice.lower() == "q":
            break
        elif user_choice.lower() != "y":
            print("Invalid Input.")

    return students_data

def create_histogram(students_data):
    win = GraphWin("Histogram", 700, 500)
    categories = ["Progress", "Progress (Module trailer)", "Do not Progress - Module retriever", "Exclude"]
    column_width = 100
    column_space = 70
    index = 0

    for category in categories:
        x_start = 50 + index * (column_width + column_space)
        x_end = x_start + column_width

        text_center_x = x_start + column_width // 2
        text_center_y = 270

        column_name = Text(Point(text_center_x, text_center_y), category)
        column_name.setSize(8)
        column_name.draw(win)

        category_count = students_data.count(category)
        count_text = Text(Point(text_center_x, 250 - category_count * 10 - 20), f"{category_count}")
        count_text.setSize(8)
        count_text.draw(win)

        index += 1

    index = 0

    for category in categories:
        x_start = 50 + index * (column_width + column_space)
        x_end = x_start + column_width

        category_count = students_data.count(category)
        category_rect = Rectangle(Point(x_start, 250), Point(x_end, 250 - category_count * 10))
        category_rect.setFill("green" if category == "Progress" else "yellow" if category == "Progress (Module trailer)" else "blue" if category == "Do not Progress - Module retriever" else "red")
        category_rect.draw(win)

        index += 1

    total_students = len(students_data)
    total_text = Text(Point(350, 400), f"Total Number of Students: {total_students}")
    total_text.setSize(16)
    total_text.draw(win)
    win.getMouse()
    win.close()

def student_predict():
    print("________________________________________________________________________________________________")
    print("""Hello Student, Welcome To The University Progression Predictor""")
    credits_pass, credits_defer, credits_fail = get_user_input()
    if validate_credits(credits_pass, credits_defer, credits_fail):
        result = predict_progression(credits_pass, credits_defer, credits_fail)
        print(result)
    
def main():
    user_type = input("Are you a student or staff? (student/staff): ").lower()

    if user_type == "staff":
        role = role_user()
        students_data = progression_predict()

        if role == "staff":
            create_histogram(students_data)
            read()
        print(students_data)

    elif user_type == "student":
        student_predict()

    else:
        print("Invalid user type.")

def role_user():
    print("___________________________________________________________________")
    print("username = staff , password = welcome")
    print("Login")
    username = input("Enter username : ")
    password = input("Enter password : ")
    if username == staff_username and password == staff_password:
        return "staff"
    else:
        print("Invalid username or password")
        return role_user()

try:
    if __name__ == "__main__":
        main()
except GraphicsError:
    None
    





