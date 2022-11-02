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

]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    users_list = choose_user()
    print(users_list)
    print(infos['spender'])
    if infos['spender'] in users_list :
        with open('expense_report.csv', 'a', newline='') as csvfile :
            fieldnames = ['amount', 'label', 'spender']
            writerfile = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writerfile.writerow(infos)
        print("Expense Added !")
    else :
        print("This user doesn't exist")
    return True
