# QuizMaster_config.py

#!/usr/bin/env python3


# File Import
from Constant.Variables.constant_variables import define_variable


# Changeable Variables

text_colour = "black";text_colour_num = define_variable()  # Can be changed inside of running program
"""
This text colour only applies to normal text, special text colours will remain the same.
Special text include: correct and wrong answer message, instructions, hint, time limit warning, score, retry option, error handling, feedback
Available colours: white, black, grey, blue, light blue, pink, yellow
"""

background_colour = "white";background_colour_num = define_variable()  # Can be changed inside of running program
"""
This background colour changes the background colour of everything.
Available colours: white, black, grey
"""

data_file_type = ".txt";data_file_type_num = define_variable()  # Can be changed inside of running program, but will cause you to lose previous work as it won't be saved in the other file type
"""
.txt = text file
"""

# End of program