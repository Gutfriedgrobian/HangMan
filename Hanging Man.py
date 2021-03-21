#Pyautogui als modul für eine gui
import PySimpleGUI as sg
import random

def level0():
      print(" "
      " \n"
      "      \n"
      "       \n"
      "      \n"
      "       \n"
      " \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def level1():
            print(" "
      " \n" 
      "      \n"
      "       \n"
      "      \n"
      "       \n"
      "/‾‾‾‾‾\ \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )

def level2():
            print(" "
      " \n" 
      "  |    \n"
      "  |      \n"
      "  |    \n"
      "  |    \n"
      "/‾‾‾‾‾\ \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )

def level3():
            print(" "
      " \n" 
      "  |/    \n"
      "  |     \n"
      "  |     \n"
      "  |     \n"
      "/‾‾‾‾‾\ \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )

def level4():
            print(" "
      " ________\n" 
      "  |/    \n"
      "  |     \n"
      "  |     \n"
      "  |     \n"
      "/‾‾‾‾‾\ \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )

def level5():
      print(" "
      " ________\n" 
      "  |/    |\n"
      "  |     \n"
      "  |     \n"
      "  |     \n"
      "/‾‾‾‾‾\ \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )
def level6():
            print(" "
      " ________\n" 
      "  |/    |\n"
      "  |     O\n"
      "  |     \n"
      "  |     \n"
      "/‾‾‾‾‾\ \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )


def level7():
            print(" "
      " ________\n" 
      "  |/    |\n"
      "  |     O\n"
      "  |    /|\ \n"
      "  |     \n"
      "/‾‾‾‾‾\ \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )


def level8():
            print(" "
      " ________\n" 
      "  |/    |\n"
      "  |     O\n"
      "  |    /|\ \n"
      "  |    // \n"
      "/‾‾‾‾‾\ \n"
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )

Words = ["wellensittich", "hund", "katze", "hirsch"]

def Win(Solution):

      for a in Solution:
            if a == "_ ":
                  print("b")

            else:
                  print("a")

def Fortschritt(Letter, Solution):
      nummer = -1

      richtige = len(Solution)
      for i in Words[Wort]:
            nummer = nummer + 1

            if i == Letter:
                  Solution[nummer] = str(Letter + " ")

            else:
                  richtige = richtige-1
      if richtige < 1:
            return 1

      else:
            return 0

if __name__ == "__main__":
      Wort = random.randint(0, 3)
      Solution = []
      deathlevel = 0
      Used = []
      Start = ""

      länge = len(Words[Wort])

      while länge > 0:
            Solution.append("_ ")
            länge = länge - 1

      for i in Solution:
            Start = Start + i

      print("\n\n\n\n")
      print(Start)

      while True:

            Buchstabe = (input("\n\n\n\n\n"
                                  "Erfrage einen Buchstabe -> ").lower())

            try:
                F = int(Buchstabe)
                print(F)

            except ValueError:
                  print("Bruder, weißt du eigentlich wie dieses Spiel funktioniert oder bist du Marlon der BugTester?")



            if Buchstabe in Used:
                        print("Du hast diesen Buchstaben bereits benutzt!")


            elif Buchstabe == Words[Wort]:
                        print("Gewonnen!")
                        exit()

            else:

                  Used.append(Buchstabe)

                  Fortschritt(Buchstabe, Solution)
                  deathlevel = deathlevel + Fortschritt(Buchstabe, Solution)

            if deathlevel == 0:
                        level0()
            elif deathlevel == 1:
                        level1()
            elif deathlevel == 2:
                        level2()
            elif deathlevel == 3:
                        level3()
            elif deathlevel == 4:
                        level4()
            elif deathlevel == 5:
                        level5()
            elif deathlevel == 6:
                        level6()
            elif deathlevel == 7:
                        level7()
            elif deathlevel == 8:
                        level8()
                        print("Verloren!")
                        exit()

            f = ""
            for B in Solution:
                  f = f + B
            print("\n")
            print(f)

            a = ""
            for i in Words[Wort]:
                  a = a + (i + " ")

            if f == a:
                  print("Gewonnen!")
                  exit()

