
import numpy as np

def main():
    #
    while True:
        eingabe = input("Tippe eine ganze Zahl größer 0 ein: ")
        try:
            x = int(eingabe)
            if x > 0:
                break
            else:
                print("Die Zahl muss größer als 0 sein. Bitte erneut versuchen.")
        except ValueError:
            print("Das war keine gültige Zahl. Bitte erneut versuchen.")
    #
    zufallszahl = np.random.randint(0, x)
    print(f"Zufallszahl im Intervall [0,{x}): {zufallszahl}")
    #
    #input("\nDrücke Enter zum Beenden...")

if __name__ == "__main__":
    main()