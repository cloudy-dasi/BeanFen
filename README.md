# WELCOME TO BEANFEN
### A friendly friend who helps you control your expense day to day to meet your expected expenditure in a period of time

#### Here are some notes I take when making this one:
1. First
- we need to write a file to store, read and get the data => create a beanfen.json file by using <code>def save_data()</code>. 
- How the data will be written: data will be collected and dumped into the file 
```python
def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f)
```
2. Second
- to read and get the data, we need to use <code>def load_data()</code>. this function will help to read the file and turn those collected data into a Python dictionary which enables to get the data from the file
```python
def load_data(current_user_name): #load_data() happens only when user_name input it means it only reads the file when having user_name input
    if not os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, "r") as f: #after having the input, it will read the file
            data = json.load(f) #load the file, turns loaded Json data into Py dictionary
        if data["user_name"] != current_user_name: #if user_name exists and the input user_name != the current one then => return {}
            print("Welcome new friend! Your account now will be created!")
            return {}
        return data #equals to json.load(f)
    except json.JSONDecodeError:
        return {}
```
```python
def main():
    print("Welcome to BeanFen")
    global user_name #change the value of user_name
    user_name = input("Enter your name: ").capitalize()
    data = load_data(user_name) #or data = json.load(f) => data now is a python dictionary
    user(data)
    print(f"Here is your data: \n user_name: {data["user_name"]} \n expected_expense_in_a_month: {data["expected_expense_in_a_month"]} \n recommended_amount_per_day: {data["recommended_amount_per_day"]} \n your_expense: {data["your_expense"]} \n total_expense_a_day: {data["total_expense_a_day"]} \n left_amount_in_a_day (compared to recommended_amount_per_day): {data["left_amount_in_a_day"]} \n amount_spent_on_Food: {data["amount_spent_on_Food"]} \n amount_spent_on_Home: {data["amount_spent_on_Home"]} \n amount_spent_on_Health: {data["amount_spent_on_Health"]} \n amount_spent_on_Work: {data["amount_spent_on_Work"]} \n amount_spent_on_Entertainment: {data["amount_spent_on_Entertainment"]} \n amount_spent_on_Study: {data["amount_spent_on_Study"]}")

```
- after struggling to make the data refresh again when a different user enters their name to use the feature, this is solution:
    + at first try, the flow I created is not a well-systematic flow. Because if i want the data refresh when user enters different user_name compared to the saved data in the json file then I should put the input of user_name at the first start and then use its value as argument of load_data() function. However I let user input their user name then use the value of the input to process other related data and to write data in the file
    + the flow should be like this:
<br><div style="color: pink">input user_name -> load the file to prepare the data (enable the "read and get data" ability) -> stages/steps of how data will be written into the json file and modified by using syntax dict[""]</div>

3. Third
- all functions need data (a python dictionary) as the required input. Because in order to process data and return a result we need to use a function, this function will process and return the value that will be written into the json file; and to be able to write into the json file the function needs to receive an input which is <code>data</code> as a tool to do that (data - python dictionary created after json.load(f)).