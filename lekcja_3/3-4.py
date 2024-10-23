'''
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float)
i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu
z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać
komunikat o błędzie i kontynuować pracę.
'''

if __name__ == "__main__":
    while True:
        x = input("\nI (int): ")
        if x.lower() == "stop":
            print("Do widzenia!")
            break
        try:
            x = float(x)
            print("x   = " + str(x))
            print("x^3 = " + str(round(x*x*x, 15)))
            # round() ucina błąd zmiennoprzecinkowy w reprezentacji binarnej
        except ValueError:
            print("Wpisz liczbę zmiennoprzecinkową.")
            continue
