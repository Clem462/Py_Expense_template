from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"new_user",
        "message":"New User : ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as csvfile :
        fieldnames = ['new_user']
        writerfile = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writerfile.writerow(infos)
    return True