# QuizMaster_console_main.py


#!/usr/bin/env python3


# File Import
from Constant.Variables.constant_variables import *


# Variables
script_dir = os.path.dirname(os.path.realpath(__file__))
QuizMaster_Leaderboard = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'QuizMaster_Leaderboard.txt'))
QuizMaster_English_Questions = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'Questions', 'QuizMaster_English_Questions.txt'))
QuizMaster_Math_Questions = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'Questions', 'QuizMaster_Math_Questions.txt'))
QuizMaster_Science_Questions = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'Questions', 'QuizMaster_Science_Questions.txt'))
QuizMaster_Chinese_Questions = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'Questions', 'QuizMaster_Chinese_Questions.txt'))
QuizMaster_English_Answers = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'Answers', 'QuizMaster_English_Answers.txt'))
QuizMaster_Math_Answers = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'Answers', 'QuizMaster_Math_Answers.txt'))
QuizMaster_Science_Answers = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'Answers', 'QuizMaster_Science_Answers.txt'))
QuizMaster_Chinese_Answers = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'Answers', 'QuizMaster_Chinese_Answers.txt'))


# Function: quiz_master_main()
def quiz_master_main():
    while True:
        clear_screen()
        print(dash)
        bold("Welcome to QuizMaster!\n")
        print(dash)
        bold("Options: ")
        green("Quiz, Leaderboard, Add Question, Exit\n")
        print(dash)
        option = str(input("Choice: ")).lower().strip()
        if option == "quiz":
            clear_screen()
            print("quiz")
            exit()

        elif option == "leaderboard":
            clear_screen()
            bold("QuizMaster\\Leaderboard\n")
            print(dash)
            with open(QuizMaster_Leaderboard, "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(f"{line}\n")
            print(dash)
            exit()

        elif option == "add question":
            clear_screen()
            print("add question")
            exit()

        elif option == "exit":
            clear_screen()
            red("Program Exited")
            exit()

        else:
            red("Please enter a valid option.")
            time.sleep(1.5)
            clear_screen()


# Main Loop
if __name__ == "__main__":
    quiz_master_main()