from pygame import mixer
from time import time
from datetime import datetime

def onloopsong(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def mylog(msg):
    with open("mylogs.txt","a") as p:
        p.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 60
    eyesec = 30
    exersec = 45
    while True:
        if time() - init_water > watersec:
            print("Water Time, To stop type 'Drank' !")
            onloopsong("water.mp3", 'Drank')
            init_water= time()
            mylog("Dranked Water At")

        elif time() - init_eyes > eyesec:
            print("Eye exercise time, type 'Relax' to Stop !")
            onloopsong("eye.mp3", 'Relax')
            init_eyes= time()
            mylog("Eyes relaxed at: ")

        elif time() - init_exercise > exersec:
            print("Exercise time , type 'Done' to stop!")
            onloopsong("exercise.mp3", "Done")
            init_exercise= time()
            mylog("Exercise done at:")

