#Modules importing:
from time import sleep
from os import system

#Exit status checker:
def CheckExit():
    Check = input ('\nDo you want to exit? [Y/N]: ')
    if Check == 'Y' or Check == 'y':
        exit(1)
    else:
        Average()

#Main program:
def Average():
    system('clear')
    Scores = int(input ('Enter number of scores: '))
    ScoreList = []
    print ('\nYou must enter [{}] scores.\n'.format(Scores))
    for Score in range(1, Scores+1):
        Elements = float(input ('Enter score[{}]: '.format(Score)))
        ScoreList.append(Elements)

    #Calculate elements & Average:
    cAverage = sum(ScoreList) / Scores
    sleep(1)
    print ('\n<-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+->')
    print ('|->    [Your average is: [{}]]    <-|'.format(round(cAverage, 2)))
    print ('<-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+->')
    CheckExit()

#Exceptions handling for problems input entry:
try:
    Average()
except KeyboardInterrupt:
    exit(1)
except ValueError:
    print ('[!] This value is not true!')
    input ()
except NameError:
    print ('[!] Name not difined!')
    input ()
except KeyError:
    sleep(1)
    exit()
