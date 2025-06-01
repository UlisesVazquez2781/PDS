import sys
from src.activity_1 import continuous_sine, discrete_sine, continuous_exponential, discrete_exponential, continuous_triangular, discrete_triangular, continuous_square, discrete_square
from src.activity_2 import understanding_freq


def main(options):
    if options[1] == "act_1":
        continuous_sine()
        discrete_sine()
        continuous_exponential()
        discrete_exponential()
        continuous_triangular()
        discrete_triangular()
        continuous_square()
        discrete_square()
    elif options[1] == "act_2":
        if len(args) > 2:
            understanding_freq(options[2])
        else:
            print("Please give a frequency. Example: python main.py act_2 2")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ) : python main.py act_1")
        print("Example ( run activity 2 ) : python main.py act_2 1")
