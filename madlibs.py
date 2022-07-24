from madlibs_choices import madlib_1, madlib_2, madlib_3
import random


if __name__ == "__main__":
    madlib_choice = random.choice([madlib_1, madlib_2, madlib_3])
    madlib_choice.madlib()
