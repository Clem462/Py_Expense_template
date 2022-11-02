from PyInquirer import prompt
import csv

from user import choose_user

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"input",
        "name":"involvers",
        "message":"New Expense - Involvers: ",
    },

]

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    users_list = choose_user()
    if infos['spender'] in users_list :
        if check_list(infos, users_list) :
            with open('expense_report.csv', 'a', newline='') as csvfile :
                fieldnames = ['amount', 'label', 'spender', 'involvers']
                writerfile = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writerfile.writerow(infos)
            print("Expense Added !")
        else :
            print("These involvers don't exist")
    else :
        print("The spender doesn't exist")
    return True

def check_list(infos, users_list):
    involvers = infos['involvers'].split(' ')
    return all(item in users_list for item in involvers)