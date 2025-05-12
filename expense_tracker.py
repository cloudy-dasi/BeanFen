#Define problems need to be solved

#input expect amount of expense of a month (30 days)
#input users expense
#input name of thing that users spent on
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
import os


FILENAME = "beanfen.json"
def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f) #we will write a json file named beanfen.json by dumping data into that file
def load_data():
    if not os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f) #we read the file and turn data into the json file after loading the file
        if data.get("user_name") != user_name:
            return {}
        return data
    except json.JSONDecodeError:
        return {}

recommended_amount_per_day = None
total_expense_a_day = 0
list_of_expense = {"Food": 0, "Home": 0, "Health": 0, "Work": 0, "Entertainment": 0, "Study": 0}
expense_per_day_tuples = ()
user_name = str()


def main():
    print("Welcome to BeanFen")
    data = load_data()
    user(data)
    print(f"Here is your data: \n user_name: {data["user_name"]} \n expected_expense_in_a_month: {data["expected_expense_in_a_month"]} \n recommended_amount_per_day: {data["recommended_amount_per_day"]} \n your_expense: {data["your_expense"]} \n total_expense_a_day: {data["total_expense_a_day"]} \n left_amount_in_a_day (compared to recommender_amount_per_day): {data["left_amount_in_a_day"]} \n amount_spent_on_Food: {data["amount_spent_on_Food"]} \n amount_spent_on_Home: {data["amount_spent_on_Home"]} \n amount_spent_on_Health: {data["amount_spent_on_Health"]} \n amount_spent_on_Work: {data["amount_spent_on_Work"]} \n amount_spent_on_Entertainment: {data["amount_spent_on_Entertainment"]} \n amount_spent_on_Study: {data["amount_spent_on_Study"]}")

def update_category(data):
    for keys in list_of_expense:
        if keys not in data:
            data[f"amount_spent_on_{keys}"] = list_of_expense[keys]
            save_data(data)

def user(data):
    global user_name
    global list_of_expense
    if "user_name" not in data:
        user_name = input("Enter your name: ").capitalize()
        data["user_name"] = user_name
        recommended_per_day(data)
        user_expense(data)
        update_category(data)
        save_data(data)
    else:
        user_name = input("Enter your name (perhaps again :3 ): ").capitalize()
        if data["user_name"] == user_name:
            total_expense_overwrite = str(input("Do you want to overwrite your 'expected total expense in a month' (write Y/N): ")).capitalize()
            if total_expense_overwrite == "Y":
                new_total_expected_expense = int(input("The new amount you expect to spend in this month: "))
                data["expected_expense_in_a_month"] = new_total_expected_expense
                data["recommended_amount_per_day"] = int(data["expected_expense_in_a_month"] / 30)
                add_more_new_expense = str(input("Do you want to add more new expense? (write Y/N): ")).capitalize()
                if add_more_new_expense == "Y":
                    new_expense = int(input("The amount of expense you want to add: "))
                    new_added_category = str(input("Your added amount belongs to which of these categories? (Food / Home / Health / Work / Entertainment / Study: ")).capitalize()
                    data["your_expense"] += new_expense
                    data["total_expense_a_day"] = data["your_expense"]
                    data["left_amount_in_a_day"] = data["recommended_amount_per_day"] - data["total_expense_a_day"]
                    for keys in list_of_expense:
                        if keys in data:
                            if new_added_category == keys:
                                list_of_expense[new_added_category] += new_expense
                                data[f"amount_spent_on_{new_added_category}"] = list_of_expense[new_added_category]
                save_data(data)
            else:
                add_more_new_expense = str(input("Do you want to add more new expense? (write Y/N): ")).capitalize()
                if add_more_new_expense == "Y":
                    new_expense = int(input("The amount of expense you want to add: "))
                    new_added_category = str(input("Your added amount belongs to which of these categories? (Food / Home / Health / Work / Entertainment / Study: ")).capitalize()
                    data["your_expense"] += new_expense
                    data["total_expense_a_day"] = data["your_expense"]
                    data["left_amount_in_a_day"] = data["recommended_amount_per_day"] - data["total_expense_a_day"]
                    for keys in list_of_expense:
                        if f"amount_spent_on_{keys}" in data:
                            if new_added_category == keys:
                                list_of_expense[new_added_category] += new_expense
                                data[f"amount_spent_on_{new_added_category}"] = list_of_expense[new_added_category]
                save_data(data)
        return(data)
        
def recommended_per_day(data):
    global recommended_amount_per_day
    if "expected_expense_in_a_month" not in data:
        total_expense = int(input("The amount you expect to spend in this month: "))
        data["expected_expense_in_a_month"] = total_expense
        if "recommended_amount_per_day" not in data:
            recommended_amount_per_day = int(data["expected_expense_in_a_month"] / 30)
            data["recommended_amount_per_day"] = recommended_amount_per_day
        save_data(data)
    print(f"The amount should be spent on a day: {data["recommended_amount_per_day"]}")

def user_expense(data):
    global total_expense_a_day, recommended_amount_per_day
    if "your_expense" not in data:
        user_expense = int(input("The amount you have just spent: "))
        category_of_expense = str(input("Which one in these categories you have spent on? (Food / Home / Health / Work / Entertainment / Study): ")).capitalize()
        for keys in list_of_expense:
            if category_of_expense == keys:
                list_of_expense[category_of_expense] += user_expense
                data[f"amount_spent_on_{category_of_expense}"] = list_of_expense[category_of_expense]
                save_data(data)
        data["your_expense"] = user_expense
        total_expense_a_day += user_expense
        if "total_expense_in_a_day" not in data:
            data["total_expense_a_day"] = total_expense_a_day
        if "left_amount_in_a_day" not in data:
            data["left_amount_in_a_day"] = data["recommended_amount_per_day"] - data["total_expense_a_day"]
        save_data(data)
    print(f"The left amount you should spend in a day to achieve the target 'spending {data["recommended_amount_per_day"]} a day': {data["left_amount_in_a_day"]}")

main()


