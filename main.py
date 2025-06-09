import sys
from src.activity_1 import continuous_sine
from src.activity_2 import understanding_freq
from src.activity_3 import sine_both
from src.activity_4 import analizar_dac

def main(options):
    if options[1] == "act_1":
        continuous_sine()
    elif options[1] == "act_2":
        if len(args) > 2:
            understanding_freq(options[2])
        else:
            print("Please give a frequency. Example: python main.py act_2 2")
    elif options[1] == "act_3":
        if len(options) < 5:
            print("Ingresa tres parámetros (amplitud, frecuencia, fase)")
            return

        amplitude = float(options[2])
        frequency = float(options[3])
        phi = float(options[4])
        sine_both(amplitude, frequency, phi)

    elif options[1] == "act_4":
        if len(options) != 3:
            print("ejemplo: python main.py act_4 (bits)")
        else:
            try:
                bits = int(options[2])
                analizar_dac(bits)
            except ValueError:
                print("El número de bits debe ser un entero.")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ) : python main.py act_1")
        print("Example ( run activity 2 ) : python main.py act_2 1")
