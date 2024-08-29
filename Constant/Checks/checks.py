# checks.py

#!/usr/bin/env python3


# File Import
from Projects.Education.QuizMaster.Config.QuizMaster_config import *
from Constant.Variables.constant_variables import *


# Checks and Error Message


# QuizMaster Checks

def quiz_master_checks():
    if text_colour in ["white","black","grey","blue","light blue","pink","yellow"]:
        pass
    else:
        print(f"{Fore.RED}Error: text_colour is not within available range.\nError in \033[4mQuizMaster_config.py\033[0m{Fore.RED} on line {text_colour_num}.{Fore.WHITE}")
        exit()

    if background_colour in ["white","black","grey"]:
        pass
    else:
        print(f"{Fore.RED}Error: background_colour is not within available range.\nError in \033[4mQuizMaster_config.py\033[0m{Fore.RED} on line {background_colour_num}.{Fore.WHITE}")
        exit()

    if data_file_type in [".pkl",".txt"]:
        pass
    else:
        print(f"{Fore.RED}Error: data_file_type is not within available range.\nError in \033[4mQuizMaster_config.py\033[0m{Fore.RED} on line {data_file_type_num}.{Fore.WHITE}")
        exit()


# End of program