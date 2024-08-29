# QuizMaster_console_main.py


#!/usr/bin/env python3


# File Import
from Constant.Variables.constant_variables import *
from Projects.Education.QuizMaster.Config.QuizMaster_config import *
from Constant.Checks.checks import quiz_master_checks


# Running Checks
quiz_master_checks()


# Variables
current_points = 0
script_dir = os.path.dirname(os.path.realpath(__file__))
QuizMaster_Leaderboard = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'QuizMaster_Leaderboard.txt'))
QuizMaster_English_Questions = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'Questions', 'QuizMaster_English_Questions.txt'))
QuizMaster_Math_Questions = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'Questions', 'QuizMaster_Math_Questions.txt'))
QuizMaster_Science_Questions = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'Questions', 'QuizMaster_Science_Questions.txt'))
QuizMaster_Chinese_Questions = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'Questions', 'QuizMaster_Chinese_Questions.txt'))
QuizMaster_English_Answers = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'Answers', 'QuizMaster_English_Answers.txt'))
QuizMaster_Math_Answers = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'Answers', 'QuizMaster_Math_Answers.txt'))
QuizMaster_Science_Answers = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'Answers', 'QuizMaster_Science_Answers.txt'))
QuizMaster_Chinese_Answers = os.path.abspath(os.path.join(script_dir, '..', '..', 'Data', 'txt', 'Answers', 'QuizMaster_Chinese_Answers.txt'))
Leaderboard_Seperator = "-=~-|+-=_/|~=-"
Question_Sperator = ""

# Function: quiz_master_main()
def quiz_master_main():
    global current_points
    while True:
        clear_screen()
        print(dash)
        bold("Welcome to QuizMaster!\n")
        print(dash)
        bold("Options: ")
        green("Quiz, Leaderboard, Add Question, Exit\n")
        print(dash)
        option = str(input("Choice: ")).lower()
        if option == "quiz":
            clear_screen()
            while True:
                print(dash)
                bold("QuizMaster\\Quiz\n")
                print(dash)
                bold("Options Available: ")
                green("English, Math, Science, Chinese, Return\n")
                print(dash)
                subject = str(input("Subject to quiz: ")).lower()
                if subject == "english":
                    clear_screen()
                    while True:
                        print(dash)
                        bold("QuizMaster\\Quiz\\English\n")
                        print(dash)
                        green("Type 'return' to return to the main menu.\n")
                        print(dash)
                        try:
                            if current_points >= 100:
                                current_points = 100
                                cyan("Current Points: ")
                                green(f"{current_points}\n")

                            elif current_points in range(75, 101):
                                cyan("Current Points: ")
                                green(f"{current_points}\n")

                            elif current_points in range(50, 75):
                                cyan("Current Points: ")
                                yellow(f"{current_points}\n")

                            elif current_points in range(25, 51):
                                cyan("Current Points: ")
                                purple(f"{current_points}\n")

                            elif current_points < 25:
                                cyan("Current Points: ")
                                red(f"{current_points}\n")

                            elif current_points < 0:
                                current_points = 0
                                cyan("Current Points: ")
                                red(f"{current_points}\n")

                        except Exception:
                            current_points = 0
                            lightgray(f"Error reading current points. Points reset back to {current_points}\n")

                        print(dash)
                        if os.path.exists("quiz_master_english_data.pkl"):
                            with open("quiz_master_english_data.pkl", "rb") as file:
                                data = pickle.load(file)

                        else:
                            red("Error loading questions and answers. Add some questions first.")
                            time.sleep(2)
                            clear_screen()
                            quiz_master_main()

                        index = random.randint(0, len(data["questions"]) - 1)
                        question = data["questions"][index]
                        correct_answer = data["answers"][index]
                        lightpurple(f"{question}\n")
                        user_answer = str(input("Answer: ")).lower().strip()
                        print(dash)
                        if isinstance(correct_answer, list):
                            if user_answer in map(str.lower, correct_answer):
                                green("Correct Answer!\n")
                                current_points += 1

                            else:
                                red("Wrong Answer!\n")
                                lightgray(f"The correct answers were: {', '.join(correct_answer)}\n")
                                current_points -= 1

                        else:
                            if user_answer == correct_answer.lower().strip():
                                green("Correct Answer!\n")
                                current_points += 1

                            else:
                                red("Wrong Answer!\n")
                                lightgray(f"The correct answer was: {correct_answer}\n")
                                current_points -= 1

                        print(dash)
                        another_question = str(input("Quiz another English question? (Y/N): ")).upper()
                        if another_question == "Y" or another_question == "YES":
                            clear_screen()

                        elif another_question == "N" or another_question == "NO":
                            save_leaderboard_name = str(input("Add your current points to the leaderboard? (Y/N): ")).upper()
                            if save_leaderboard_name == "Y" or save_leaderboard_name == "YES":
                                leaderboard_name = str(input("Name to use for leaderboard: "))
                                leaderboard = f"{leaderboard_name}:{current_points}"
                                data["leaderboard"].append(leaderboard)
                                with open("quiz_master_english_data.pkl", "wb") as file:
                                    pickle.dump(data, file)
                                clear_screen()
                                quiz_master_main()

                            elif save_leaderboard_name == "N" or save_leaderboard_name == "NO":
                                clear_screen()
                                quiz_master_main()

                            else:
                                print(dash)
                                red(f"You inputted '{save_leaderboard_name}', which we will take as a no.")
                                time.sleep(2)
                                clear_screen()
                                quiz_master_main()

                        else:
                            print(dash)
                            red(f"You inputted '{another_question}', which we will take as a no.")
                            print(dash)
                            save_leaderboard_name = str(input("Add your current points to the leaderboard? (Y/N): ")).upper()
                            if save_leaderboard_name == "Y" or save_leaderboard_name == "YES":
                                leaderboard_name = str(input("Name to use for leaderboard: "))
                                leaderboard = f"{leaderboard_name}:{current_points}"
                                data["leaderboard"].append(leaderboard)
                                with open("quiz_master_english_data.pkl", "wb") as file:
                                    pickle.dump(data, file)
                                clear_screen()
                                quiz_master_main()

                            elif save_leaderboard_name == "N" or save_leaderboard_name == "NO":
                                clear_screen()
                                quiz_master_main()

                            else:
                                print(dash)
                                red(f"You inputted '{save_leaderboard_name}', which we will take as a no.")
                                time.sleep(2)
                                clear_screen()
                                quiz_master_main()

                elif subject == "math":
                    print("math")
                    exit()

                elif subject == "science":
                    print("science")
                    exit()

                elif subject == "chinese":
                    print("chinese")
                    exit()

                elif subject == "return":
                    clear_screen()
                    quiz_master_main()

                else:
                    red("Error 400: Invalid Input - Invalid.\n")
                    time.sleep(1.5)
                    clear_screen()

        elif option == "leaderboard":
            print("leaderboard")
            exit()

        elif option == "add question":
            clear_screen()
            while True:
                print(dash)
                bold("QuizMaster\\Add Question\n")
                print(dash)
                bold("Options Available: ")
                green("English, Math, Science, Chinese, Return\n")
                print(dash)
                option1 = str(input("Subject to add question to: ")).lower()
                if option1 == "english":
                    clear_screen()
                    while True:
                        print(dash)
                        bold("QuizMaster\\Add Question\\English\n")
                        print(dash)
                        red("All inputs here are CaSe-SeNsItIvE.\n")
                        green("Type 'return' to return to the main menu.\n")
                        print(dash)
                        English_Question = str(input("English question to be added: "))
                        variation = generate_variations("return")
                        if English_Question in variation:
                            clear_screen()
                            quiz_master_main()
                        English_Variation_Num = str(input("Number of answer variations (Max 6): ")).lower()
                        if English_Variation_Num == "1" or English_Variation_Num == "one":
                            English_Answer = str(input("Answer for the question: "))
                            if English_Answer in variation:
                                clear_screen()
                                quiz_master_main()
                            if os.path.exists("quiz_master_english_data.pkl"):
                                with open("quiz_master_english_data.pkl", "rb") as file:
                                    data = pickle.load(file)

                            else:
                                data = {"questions": [], "answers": [], "leaderboard": []}

                            data["questions"].append(English_Question)
                            data["answers"].append(English_Answer)
                            with open("quiz_master_english_data.pkl", "wb") as file:
                                pickle.dump(data, file)
                            clear_screen()

                        elif English_Variation_Num == "2" or English_Variation_Num == "two":
                            English_Answer_1 = str(input("First answer variation: "))
                            if English_Answer_1 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_2 = str(input("Second answer variation: "))
                            if English_Answer_2 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer = [English_Answer_1, English_Answer_2]
                            counts = Counter(English_Answer)
                            duplicates = [item for item, count in counts.items() if count > 1]
                            if duplicates:
                                red("Both answer variations cannot be the same, please choose another answer variation instead.")
                                English_Answer = []
                                time.sleep(1.5)
                                clear_screen()
                            else:
                                if os.path.exists("quiz_master_english_data.pkl"):
                                    with open("quiz_master_english_data.pkl", "rb") as file:
                                        data = pickle.load(file)

                                else:
                                    data = {"questions": [], "answers": [], "leaderboard": []}

                                data["questions"].append(English_Question)
                                data["answers"].append(English_Answer)
                                with open("quiz_master_english_data.pkl", "wb") as file:
                                    pickle.dump(data, file)
                                clear_screen()

                        elif English_Variation_Num == "3" or English_Variation_Num == "three":
                            English_Answer_1 = str(input("First answer variation: "))
                            if English_Answer_1 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_2 = str(input("Second answer variation: "))
                            if English_Answer_2 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_3 = str(input("Third answer variation: "))
                            if English_Answer_3 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer = [English_Answer_1, English_Answer_2, English_Answer_3]
                            counts = Counter(English_Answer)
                            duplicates = [item for item, count in counts.items() if count > 1]
                            if duplicates:
                                red("Both answer variations cannot be the same, please choose another answer variation instead.")
                                English_Answer = []
                                time.sleep(1.5)
                                clear_screen()
                            else:
                                if os.path.exists("quiz_master_english_data.pkl"):
                                    with open("quiz_master_english_data.pkl", "rb") as file:
                                        data = pickle.load(file)

                                else:
                                    data = {"questions": [], "answers": [], "leaderboard": []}

                                data["questions"].append(English_Question)
                                data["answers"].append(English_Answer)
                                with open("quiz_master_english_data.pkl", "wb") as file:
                                    pickle.dump(data, file)
                                clear_screen()

                        elif English_Variation_Num == "4" or English_Variation_Num == "four":
                            English_Answer_1 = str(input("First answer variation: "))
                            if English_Answer_1 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_2 = str(input("Second answer variation: "))
                            if English_Answer_2 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_3 = str(input("Third answer variation: "))
                            if English_Answer_3 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_4 = str(input("Fourth answer variation: "))
                            if English_Answer_4 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer = [English_Answer_1, English_Answer_2, English_Answer_3, English_Answer_4]
                            counts = Counter(English_Answer)
                            duplicates = [item for item, count in counts.items() if count > 1]
                            if duplicates:
                                red("Both answer variations cannot be the same, please choose another answer variation instead.")
                                English_Answer = []
                                time.sleep(1.5)
                                clear_screen()
                            else:
                                if os.path.exists("quiz_master_english_data.pkl"):
                                    with open("quiz_master_english_data.pkl", "rb") as file:
                                        data = pickle.load(file)

                                else:
                                    data = {"questions": [], "answers": [], "leaderboard": []}

                                data["questions"].append(English_Question)
                                data["answers"].append(English_Answer)
                                with open("quiz_master_english_data.pkl", "wb") as file:
                                    pickle.dump(data, file)
                                clear_screen()

                        elif English_Variation_Num == "5" or English_Variation_Num == "five":
                            English_Answer_1 = str(input("First answer variation: "))
                            if English_Answer_1 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_2 = str(input("Second answer variation: "))
                            if English_Answer_2 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_3 = str(input("Third answer variation: "))
                            if English_Answer_3 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_4 = str(input("Fourth answer variation: "))
                            if English_Answer_4 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_5 = str(input("Fifth answer variation: "))
                            if English_Answer_5 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer = [English_Answer_1, English_Answer_2, English_Answer_3, English_Answer_4, English_Answer_5]
                            counts = Counter(English_Answer)
                            duplicates = [item for item, count in counts.items() if count > 1]
                            if duplicates:
                                red("Both answer variations cannot be the same, please choose another answer variation instead.")
                                English_Answer = []
                                time.sleep(1.5)
                                clear_screen()
                            else:
                                if os.path.exists("quiz_master_english_data.pkl"):
                                    with open("quiz_master_english_data.pkl", "rb") as file:
                                        data = pickle.load(file)

                                else:
                                    data = {"questions": [], "answers": [], "leaderboard": []}

                                data["questions"].append(English_Question)
                                data["answers"].append(English_Answer)
                                with open("quiz_master_english_data.pkl", "wb") as file:
                                    pickle.dump(data, file)
                                clear_screen()

                        elif English_Variation_Num == "6" or English_Variation_Num == "six":
                            English_Answer_1 = str(input("First answer variation: "))
                            if English_Answer_1 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_2 = str(input("Second answer variation: "))
                            if English_Answer_2 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_3 = str(input("Third answer variation: "))
                            if English_Answer_3 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_4 = str(input("Fourth answer variation: "))
                            if English_Answer_4 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_5 = str(input("Fifth answer variation: "))
                            if English_Answer_5 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer_6 = str(input("Sixth answer variation: "))
                            if English_Answer_6 in variation:
                                clear_screen()
                                quiz_master_main()
                            English_Answer = [English_Answer_1, English_Answer_2, English_Answer_3, English_Answer_4, English_Answer_5, English_Answer_6]
                            counts = Counter(English_Answer)
                            duplicates = [item for item, count in counts.items() if count > 1]
                            if duplicates:
                                red("Both answer variations cannot be the same, please choose another answer variation instead.")
                                English_Answer = []
                                time.sleep(1.5)
                                clear_screen()
                            else:
                                if os.path.exists("quiz_master_english_data.pkl"):
                                    with open("quiz_master_english_data.pkl", "rb") as file:
                                        data = pickle.load(file)

                                else:
                                    data = {"questions": [], "answers": [], "leaderboard": []}

                                data["questions"].append(English_Question)
                                data["answers"].append(English_Answer)
                                with open("quiz_master_english_data.pkl", "wb") as file:
                                    pickle.dump(data, file)
                                clear_screen()

                        elif English_Variation_Num == "return":
                            clear_screen()
                            quiz_master_main()

                        else:
                            red("Please enter a number from 1 to 6.")
                            time.sleep(1.5)
                            clear_screen()

                elif option1 == "math":
                    print("math")
                    exit()

                elif option1 == "science":
                    print("science")
                    exit()

                elif option1 == "chinese":
                    print("chinese")
                    exit()

                elif option1 == "return":
                    clear_screen()
                    quiz_master_main()

                else:
                    red("Error 400: Invalid Input - Invalid.\n")
                    time.sleep(1.5)
                    clear_screen()

        elif option == "exit":
            clear_screen()
            red("The program has ended. Thank you for your time and attention. Goodbye!")
            exit()

        else:
            red("Error 400: Invalid Input - Invalid.\n")
            time.sleep(1.5)
            clear_screen()


# Main Loop
if __name__ == "__main__":
    quiz_master_main()