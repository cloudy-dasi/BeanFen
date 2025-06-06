#Define problems need to be solved

#input expect amount of expense of a month (30 days)
#input users expense
#choose one category
#write those input data to a file
#a file to read and summarize (left amount, the amount should be spent perday to achieve the expected amount, the amount users have spent on after 24h)

#IDEA for the summarize the amount of expense
"""
the amount should be spent per day = variable 1
the left amount compared to the variable 1
the total expense of each category
the amount spent on a day (after 24h) = varible 2
the amount have been saved after a day = variable 3
store the amount have been saved on a day into a list
if list[29] == None then push the varible 3, then count the total saving in a month
if the total saving == the total expected amount of expense => meet expectation, if > then "Congratulations! :)))"
"""
#use json to access values
import json
import os #operate system
from datetime import datetime


FILENAME = "beanfen.json"
def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f) #we will write a json file named beanfen.json by dumping data into that file
def load_data(current_user_name): #load_data() happens only when user_name input it means it only reads the file when having user_name input
    if not os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, "r") as f: #after having the input, it will read the file
            data = json.load(f) #load the file, turns loaded Json data into Py dictionary
        if data.get("user_name") != current_user_name: #if user_name exists and the input user_name != the current one then => return {}
            print("Welcome new friend! Your account now will be created!")
            return {}
        return data #equals to json.load(f)
    except json.JSONDecodeError:
        return {}

recommended_amount_per_day = None
#DELETE total_expense_a_day = 0
list_of_expense = {"Family": 0, "Study": 0, "Food": 0, "Home": 0, "Health": 0, "Work": 0, "Entertainment": 0, "Friends": 0, "Transport": 0}
user_expense = int()
expense_a_year_list = list()
expense_a_month_list = list() #total_expense_in_day (30 items)
#DELETE expense_per_day_list = list()
user_name = str()

def main():
    print("Welcome to BeanFen")
    global user_name
    user_name = input("Enter your name: ").capitalize()
    data = load_data(user_name) #or data = json.load(f)
    check_and_update_daily_data(data) #check the date right after loading the file
    user(data)
    print(f"Here is your data: \n user_name: {data.get("user_name")} \n your_control_expense_days: {data.get("control_expense_days")} \n total_amount_of_expense_need_controlling: {data.get("expected_expense_amount")} \n recommended_amount_per_day: {data.get("recommended_amount_per_day")} \n recommended_amount_today: {data.get("recommended_amount_today")} \n your_expense_until_now: {data.get("your_expense")} \n today_you_have_spent: {data.get("total_expense_a_day")} \n left_amount_in_a_day (recommended_amount_today - today_you_have_spent): {data.get("left_amount_in_a_day")} \n your_total_left_amount (total_amount_of_expense_need_controlling - your_expense_until_now): {data.get("total_left_amount")} \n expense_next_day: {data.get("expense_next_day")} \n total_amount_spent_on_Food: {data.get("amount_spent_on_Food")} \n total_amount_spent_on_Home: {data.get("amount_spent_on_Home")} \n total_amount_spent_on_Health: {data.get("amount_spent_on_Health")} \n total_amount_spent_on_Work: {data.get("amount_spent_on_Work")} \n total_amount_spent_on_Entertainment: {data.get("amount_spent_on_Entertainment")} \n total_amount_spent_on_Study: {data.get("amount_spent_on_Study")}")
    print(f" total_amount_spent_on_Family: {data.get("amount_spent_on_Family")} \n total_amount_spent_on_Friends: {data.get("amount_spent_on_Friends")} \n total_amount_spent_on_Transport: {data.get("amount_spent_on_Transport")}")
    print (f"This is your history of expense today {data.get("last_update")}: {data.get("expense_per_day_list")}")

def check_and_update_daily_data(data):
    global expense_a_month_list, expense_per_day_list
    today = datetime.today().strftime("%d/%m/%Y")
    if "last_update" not in data:
        data["last_update"] = today
        save_data(data)
    else: #if last_update exists, it wont update the "last_update", just check the condition following
        if data.get("last_update") != datetime.today().strftime("%d/%m/%Y"):
            expense_a_month_list.append(data.get("expense_per_day_list"))
            data["control_expense_days"] -= 1
            print(f"Welcome to next day! :3 \nYou have {data["control_expense_days"]} days left to control your expense compared to the last_update")
            data["expense_per_day_list"] = []
            data["total_expense_a_day"] = 0
            if data["left_amount_in_a_day"] <0: #check if the left amount is negative
                print(f"Your previous day expense extends the recommended an amount {data["left_amount_in_a_day"]} \nif you dont overwrite control_expense_days or total_amount_of_expense_need_controlling,\nwe will overwrite the recommended_amount_today to make it suitable with your condition :3")
                data["recommended_amount_today"] = data["expense_next_day"]
        save_data(data)


def update_category(data): #write and save data when file is empty
    for keys in list_of_expense:
        if keys not in data:
            data[f"amount_spent_on_{keys}"] = list_of_expense[keys]
            save_data(data) #save and write one by one

#note: check date and update data after every input
def user(data):
    global user_name
    global list_of_expense
    #DELETE global expense_per_day_list
    #DELETE global total_expense_a_day
    if "user_name" not in data: #write into an empty file
        data["user_name"] = user_name
        save_data(data) #when finish writing and save user_name then process other data
        data["last_update"] = datetime.today().strftime("%d/%m/%Y") #keep on updating last_update
        check_and_update_daily_data(data) #check again to make sure
        update_category(data)
        control_expense_days(data)
        expected_expense(data)
        recommended_per_day(data)
        expense(data)
        save_data(data) #make sure all data have been saved and written
    if "user_name" in data: #write and save data when data in file exists
        #user_name = input("Enter your name (perhaps again :3 ): ").capitalize()
        if data["user_name"] == user_name:
            data["last_update"] = datetime.today().strftime("%d/%m/%Y")
            check_and_update_daily_data(data)
            print("Your account was saved!")
            print("Welcome back my friend! :3")
            overwrite_control_expense_days(data)
            overwrite_total_expense(data)
            add_more_new_expense(data)

def control_expense_days(data): #write and save data when data is empty
    if "control_expense_days" not in data:
        control_expense_days = int(input("How many days you want to control your expense? (write a number): "))
        if control_expense_days < 1:
            print("Please enter a number >= 1")
            control_expense_days(data) #call the function again
        else:
            data["control_expense_days"] = control_expense_days
            save_data(data)

def expected_expense(data): #write and save data when data is empty
    if "expected_expense_amount" not in data:
        expected_expense_amount = int(input("The amount of expense you want to control: "))
        if expected_expense_amount < 1:
            print("Please enter a number >= 1")
            expected_expense(data) #call the function again
        else:
            data["expected_expense_amount"] = expected_expense_amount
            save_data(data)

def recommended_per_day(data): #write and save data when data is empty
    global recommended_amount_per_day
    if "recommended_amount_per_day" not in data:
        recommended_amount_per_day = int(data["expected_expense_amount"] / data["control_expense_days"])
        data["recommended_amount_per_day"] = recommended_amount_per_day
        if "recommended_amount_today" not in data:
            data["recommended_amount_today"] = data["recommended_amount_per_day"]
    save_data(data) #save data only when finishing the input (write data into file)
    print(f"The amount should be spent on a day: {data["recommended_amount_per_day"]}")

def expense(data): #write and save data when data is empty
    global recommended_amount_per_day, user_expense
    if "your_expense" not in data:
        user_expense = int(input("The amount you have just spent: "))
        data["your_expense"] = user_expense
        if "expense_per_day_list" not in data:
            data["expense_per_day_list"] = []
        data["expense_per_day_list"].append(user_expense)
        if "total_expense_in_a_day" not in data: #after 24h total_expense_a_day returns 0 => need a array to store
            data["total_expense_a_day"] = sum(data.get("expense_per_day_list", []))
        #input category of expense
        category_of_expense = str(input("Which one in these categories you have spent on? (Family / Study / Food / Home / Health / Work / Entertainment / Friends / Transport): ")).capitalize()
        for keys in list_of_expense:
            if category_of_expense == keys:
                data[f"amount_spent_on_{keys}"] = user_expense
                save_data(data)
        if "left_amount_in_a_day" not in data:
            data["left_amount_in_a_day"] = data["recommended_amount_today"] - data["total_expense_a_day"]
        if "total_left_amount" not in data:
            data["total_left_amount"] = data["expected_expense_amount"] - data["your_expense"]
        if "expense_next_day" not in data:
            data["expense_next_day"] = int((data["expected_expense_amount"] - data["total_expense_a_day"]) / (data["control_expense_days"] - 1))
        save_data(data)
    print(f"The left amount you should spend in a day to achieve the target 'spending {data["recommended_amount_per_day"]} a day': {data["left_amount_in_a_day"]}")

def overwrite_control_expense_days(data): #overwrite control_expense_days
    if "control_expense_days" in data:
        control_expense_days_overwrite = str(input("Do you want to overwrite your 'control_expense_days' (write Y/N): ")).capitalize()
        if control_expense_days_overwrite == "Y":
            data["last_update"] = datetime.today().strftime("%d/%m/%Y")
            check_and_update_daily_data(data)
            new_control_expense_days = int(input("How many days you want to control your expense? (write a number): "))
            if new_control_expense_days < 1:
                print("Please enter a number >= 1")
                control_expense_days_overwrite(data)
            else:
                data["control_expense_days"] = new_control_expense_days
                print ("You have successfully overwritten your control_expense_days!")
                data["recommended_amount_per_day"] = int(data["expected_expense_amount"] / data["control_expense_days"])
                data["recommended_amount_today"] = data["recommended_amount_per_day"]
                data["left_amount_in_a_day"] = data["recommended_amount_today"] - data["total_expense_a_day"]
                save_data(data)

def overwrite_total_expense(data): #overwrite total_expense_in_a_month
    if "expected_expense_amount" in data:
        total_expense_overwrite = str(input("Do you want to overwrite your amount of expense that needs controlling (write Y/N): ")).capitalize()
        if total_expense_overwrite == "Y":
            data["last_update"] = datetime.today().strftime("%d/%m/%Y") #update last_update
            check_and_update_daily_data(data) #check the date and modify data if needed before overwriting
            new_total_expected_expense = int(input("The new amount of expense you want to control: "))
            print ("You have successfully overwritten your expected_expense_amount!")
            data["expected_expense_amount"] = new_total_expected_expense
            data["total_left_amount"] = data["expected_expense_amount"] - data["your_expense"]
            data["recommended_amount_per_day"] = int(data["expected_expense_amount"] / data["control_expense_days"])
            data["recommended_amount_today"] = data["recommended_amount_per_day"]
            data["expense_next_day"] = int(data(data["expected_expense_amount"] - data["total_expense_a_day"]) / (data["control_expense_days"] - 1))
            data["left_amount_in_a_day"] = data["recommended_amount_today"] - data["total_expense_a_day"]
            save_data(data)

def add_more_new_expense(data):
    data["last_update"] = datetime.today().strftime("%d/%m/%Y")
    check_and_update_daily_data(data)
    add_more_new_expense = str(input("Do you want to add more new expense? (write Y/N): ")).capitalize()
    if add_more_new_expense == "Y":
        data["last_update"] = datetime.today().strftime("%d/%m/%Y")
        check_and_update_daily_data(data)
        new_expense = int(input("The amount of expense you want to add: "))
        new_added_category = str(input("Your added amount belongs to which of these categories? (Family / Study / Food / Home / Health / Work / Entertainment / Friends / Transport): ")).capitalize()
        if "expense_per_day_list" in data:
            data["expense_per_day_list"].append(new_expense)
        data["total_expense_a_day"] = sum(data.get("expense_per_day_list", []))
        data["your_expense"] += new_expense
        data["left_amount_in_a_day"] = data["recommended_amount_today"] - data["total_expense_a_day"]
        data["total_left_amount"] = data["expected_expense_amount"] - data["your_expense"]
        data["expense_next_day"] = int((data["expected_expense_amount"] - data["total_expense_a_day"]) / (data["control_expense_days"] - 1))
        for keys in list_of_expense:
            if f"amount_spent_on_{keys}" in data:
                if new_added_category == keys:
                    data[f"amount_spent_on_{keys}"] += new_expense
    save_data(data)

main()