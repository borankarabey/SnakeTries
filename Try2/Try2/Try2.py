import math
import random as rnd

##### GİTHUB KAYIT ŞEKLİ 'TURKCELL OYUN' #####

WhiteTeam = {}
BlackTeam = {}
Magicians = {}


def Hobbits():

    global WhiteTeam

    Power = 60
    Health = 40
    Strategy = 90
    Magic = 0

def Elves():

    global WhiteTeam

    Power = 90
    Health = 80
    Strategy = 80
    Magic = 20

def Humans():

    global WhiteTeam

    Power = 80
    Health = 70
    Strategy = 80
    Magic = 0

def Midgets():

    global WhiteTeam

    Power = 90
    Health = 60
    Strategy = 40
    Magic = 0

def Orgs():

    global BlackTeam

    Power = 85
    Health = 70
    Strategy = 40
    Magic = 0

def Goblins():

    global BlackTeam

    Power = 50
    Health = 40
    Strategy = 20
    Magic = 0

def BlackGhosts():

    global BlackTeam

    Power = 90
    Health = 70
    Strategy = 30
    Magic = 30

def Gandalf():

    global Magicians

    Power = 60
    Health = 40
    Strategy = 95
    Magic = 95

def Saruman():

    global Magicians

    Power = 60
    Health = 40
    Strategy = 90
    Magic = 100

def Groot():

    global Magicians

    Power = 50
    Health = 50
    Strategy = 85
    Magic = 90

def Dragon():

    global Magicians

    Power = 50
    Health = 70
    Strategy = 25
    Magic = 80
   

def TeamSelection():

    selection = input(" Please select your team.\n")

    if selection == "1":
        print(" Now you are in the Brotherhood of the Ring.")
        WhiteTeamMenu()

    elif selection == "2":
        print(" Now you are in the Army of the Eye.")
        BlackTeamMenu()

    elif selection == "3":
        print(" Now you are in the Mighty Five Magicians.")
        MagiciansTeamMenu()

    else:
        print(" Error accured, please try again.")
        FirstMenu()



def PlayerSelectionWhiteTeam():

    selection = input(" Please select a race.\n")

    if selection == "1":
       print(" Your character is Frodo. Wait for your enemy.\n")
       #selection = WhiteTeam(Hobbits)
       ThirdMenu()
 
    elif selection == "2":
       print(" Your character is Legolas. Wait for your enemy.\n")
       selection = WhiteTeam(Elves)
       ThirdMenu()

    elif selection == "3":
       print(" Your character is Aragon. Wait for your enemy.\n")
       selection = WhiteTeam(Humans)
       ThirdMenu()

    elif selection == "4":
       print(" Your character is Ronin. Wait for your enemy.\n")
       selection = WhiteTeam(Midgets)
       ThirdMenu()

    else:
        print(" Error accured, please try again.")
        WhiteTeamMenu()


def PlayerSelectionBlackTeam():

    selection = input(" Please select a race.\n")

    if selection == "1":
       print(" Your character is Org Commander. Wait for your enemy.\n")
       selection = BlackTeam(Orgs)
       FourthMenu()
 
    elif selection == "2":
       print(" Your character is Fat Goblin King. Wait for your enemy.\n")
       selection = BlackTeam(Goblins)
       FourthMenu()

    elif selection == "3":
       print(" Your character is Nightcrawler. Wait for your enemy.\n")
       selection = BlackTeam(BlackGhosts)
       FourthMenu()

    else:
        print(" Error accured, please try again.")
        BlackTeamMenu()


def PlayerSelectionMagicians():

    selection = input(" Please select a magician.\n")

    if selection == "1":
       print(" Your character is Gandalf the Gray. Wait for your enemy.\n")
       selection = Magicians(Gandalf)
       FourthMenu()
 
    elif selection == "2":
       print(" Your character is Saruman the White. Wait for your enemy.\n")
       selection = Magicians(Saruman)
       FourthMenu()
    
    elif selection == "3":
       print(" Your character is Groot the Green. Wait for your enemy.\n")
       selection = Magicians(Groot)
       FourthMenu()

    elif selection == "4":
       print(" Your character is Dragon the Red. Wait for your enemy.\n")
       selection = Magicians(Dragon)
       FourthMenu()

    else:
        print(" Error accured, please try again.")
        MagiciansTeamMenu()


def Enemy():

    selection = input(" Please select a number.\n")

    if selection == "1":
       print(" Your enemy is from the dark side.\n He is -->")
       enemy = rnd(BlackTeam) | Saruman | Dragon
       print(enemy)
       FourthMenu()

    elif selection == "2":
        print(" Your enemy is from the good side.\n He is -->")
        enemy = rnd(WhiteTeam) | Gandalf | Groot
        print(enemy)
        FourthMenu()

    elif selection == "3":

        if PlayerSelectionMagicians == "2":
            print(" Your enemy is from the light.\n He is -->")
            enemy = Gandalf | Groot
            print(enemy)
            FourthMenu()
        else:
            print(" Your enemy is from the eye.\n He is -->")
            enemy = Saruman | Dragon
            print(enemy)
            FourthMenu()

    else:
        print(" Error accured, please try again.")
        FirstMenu()


def TacticSelection1():

    selection = input(" Please select a way to attack.\n")

    if selection == "1":
       print(" Attacked with your power.") 
    {
        if Player.Power > Enemy.Power:
            Enemy.Health = (Enemy.Health - 40)
            CheckHealth()
        else:
            Player.Health = (PlayerHealth - 40)
            CheckHealth()
    }
    elif selection == "2":
       print(" Attacked with your strategy.")
    {   
        if Player.Strategy > Enemy.Strategy:
            Enemy.Health = (Enemy.Health - 40)
            CheckHealth()
        else:
            Player.Health = (PlayerHealth - 40)
            CheckHealth()
    }
    elif selection == "3":
       print(" Attacked with your magic.")
    {
        if Player.Magic > Enemy.Magic:
            Enemy.Health = (Enemy.Health - 40)
            CheckHealth()
        else:
            Player.Health = (PlayerHealth - 40)
            CheckHealth()
    }
    else:
        print(" Error accured, please try again.")
        FourthMenu()


def TacticSelection2():

    selection = input(" Please select a way to attack.\n")

    if selection == "1":
       print(" Attacked with your power one more time.") 
    # if power is higher -40 health
 
    elif selection == "2":
       print(" Attacked with your strategy one more time.")
    # if strategy is higher -40 health

    elif selection == "3":
       print(" Attacked with your magic one more time.")
    # if magic is higher -40 health

    else:
        print(" Error accured, please try again.")
        FifthMenu()




def FirstMenu():

        firstmenu = '''
   __________________________
  | 1: WhiteTeam             |
  | 2: BlackTeam             |
  | 3: Magicians             |
   --------------------------
  '''
        print(firstmenu)  

        TeamSelection()


def WhiteTeamMenu():

        second1menu = '''
   __________________________
  | 1: Hobbits               |
  | 2: Elves                 |
  | 3: Humans                |
  | 4: Midgets               |
   --------------------------
  '''
        print(second1menu)    

        PlayerSelectionWhiteTeam()


def BlackTeamMenu():

        second2menu = '''
   __________________________
  | 1: Orgs                  |
  | 2: Goblins               |
  | 3: Black Ghosts          |
   --------------------------
  '''
        print(second2menu)    

        PlayerSelectionBlackTeam()


def MagiciansTeamMenu():

        second3menu = '''
   __________________________
  | 1: Gandalf               |
  | 2: Saruman               |
  | 3: Groot                 |
   --------------------------
  '''
        print(second3menu)    

        PlayerSelectionMagicians()


def ThirdMenu():

        thirdmenu = '''
   ___________________________
  | 1: ?????                  |
  | 2: ?????                  |
  | 3: ?????                  |
   ---------------------------
  '''
        print(thirdmenu)

        Enemy() 


def FourthMenu():

        fourthmenu = '''
   ___________________________
  | 1: Cut his head off       |
  | 2: Stab him from behind   |
  | 3: Stop his heart         |
   ---------------------------
  '''
        print(fourthmenu)

        TacticSelection1() 


def FifthMenu():

        fifthmenu = '''
   ___________________________
  | 1: Blow his eyes off      |
  | 2: Tie him up in the trap |
  | 3: Make him burned        |
   ---------------------------
  '''
        print(fifthmenu)

        TacticSelection2()



FirstMenu()