import random
import pyautogui
import time
import sys
import PySimpleGUI as sg
import keyboard
import subprocess

sg.theme('DarkPurple2')
Characters = ["freddy", "bonnie", "chica", "foxy", "toy freddy", "toy bonnie", "toy chica", "mangle", "BB", "JJ", "withered chica", "whitered bonnie", "marionette", "golden freddy", "springtrap", "phantom mangle", "phantom freddy", "phantom BB", "nightmare freddy", "nightmare bonnie", "nightmare fredbear", "nightmare", "jack_O_chica", "nightmare mangle", "nightmarionne", "nightmare BB", "old man concequences", "circus baby", "ballora", "funtime foxy", "ennard", "trash and the gang", "helpy", "happy frog", "hr. hippo", "pigpatch", "nedd bear", "orville elephant", "rockstar freddy", "rockstar bonnie", "rockstar chica", "rockstar foxy", "music man", "el chip", "funtime chica", "molten freddy", "scrap baby", "afton", "lefty", "phone guy"]
Coordinatesx = ["72", "232", "391", "551", "711", "872", "1032", "1192", "1353", "1512", "72", "232", "391", "551", "711", "872", "1032", "1192", "1353", "1512", "72", "232", "391", "551", "711", "872", "1032", "1192", "1353", "1512", "72", "232", "391", "551", "711", "872", "1032", "1192", "1353", "1512", "72", "232", "391", "551", "711", "872", "1032", "1192", "1353", "1512"]
Coordinatesy = ["177", "177", "177", "177", "177", "177", "177", "177", "177", "177", "384", "384", "384", "384", "384", "384", "384", "384", "384", "384", "588", "588", "588", "588", "588", "588", "588", "588", "588", "588", "792", "792", "792", "792", "792", "792", "792", "792", "792", "792", "998", "998", "998", "998", "998", "998", "998", "998", "998", "998"]
openucn = sg.Window('UCN Randomizer', [[sg.Text('Open UCN?')],
                                 [sg.Button('Open UCN')], [sg.Button('Exit')]], keep_on_top=True)
event, values = openucn.read()
if event == sg.WIN_CLOSED or event == 'Exit':
    sys.exit(0)
if event == 'Open UCN':
    openucn.close()
    subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 871720")
time.sleep(4)
# ///////// number of characters //////////
def Charnum():
    global CharNum
    layout = [[sg.Text('Enter Number Of Characters To Generate')],
          [sg.Input(key='-IN-')],
          [sg.Button('Next'), sg.Button('Exit')]]
    window = sg.Window('Number of characters', layout, keep_on_top=True)
    while True:  # Event Loop
        event, values = window.read()
        print("charnum event and values:", event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            sys.exit(0)
        if event == 'Next':
            CharNum = values['-IN-']

            if CharNum.isnumeric():
                print(CharNum,"was entered")
            else:
                sg.popup('Not a number!', keep_on_top=True)
                continue
            if int(CharNum) > 50 or int(CharNum) < 1:
                sg.popup('Outside range!\nRange 1-50', keep_on_top=True)
                continue
        window.close()
        break
# /////////////////////////////////////////



def Roll():
    loop = 1
    global SelectedChar
    global SelectedCordx
    global SelectedCordy
    global SelectedDif
    global ExcludedChar
    SelectedChar = []
    SelectedCordx = []
    SelectedCordy = []
    SelectedDif = []
    ExcludedChar = []
    while loop <= int(CharNum):
        
        CurrentNum = random.randint(0, 49)
        if CurrentNum in ExcludedChar:
            continue

        CurrentChar = Characters[CurrentNum]
        CurrentCordx = Coordinatesx[CurrentNum]
        CurrentCordy = Coordinatesy[CurrentNum]
        SelectedChar.append(CurrentChar)
        SelectedCordx.append(CurrentCordx)
        SelectedCordy.append(CurrentCordy)
        CurrentDif = random.randint(1, 20)
        SelectedDif.append(CurrentDif)
        loop=int(loop)+1
        ExcludedChar.append(CurrentNum)
    #make beautiful
    loop2 = 1
    p=0
    global DispChar
    DispChar = []
    while loop2 <= int(CharNum):
        a = SelectedChar[p]
        b = SelectedDif[p]
        c = str(a)+"\n"+"level " + str(b)+"\n\n"
        DispChar.append(c)
        p=int(p)+1
        loop2=int(loop2)+1

def CheckChars():
    layout2 = [[sg.Text(''.join(DispChar), key='-DispChar-')],
           [sg.Button('OK'), sg.Button('REROLL')]]
    window2 = sg.Window('Generated Characters', layout2, keep_on_top=True)
    while True:
        event = ""
        event, values = window2.read()
        print("window2 event:",event)
        if event == sg.WIN_CLOSED:
            sys.exit(0)
        if event == 'REROLL':
            Roll()
            window2['-DispChar-'].update(''.join(DispChar))
        if event == 'OK':
            window2.close()
            click()
            break

def click():
    pyautogui.click(x=1776, y= 70)
    time.sleep(0.5)
    pyautogui.click(x=1776, y= 70)
    time.sleep(0.5)
    pyautogui.click(x=1776, y= 70)
    loop3 = 1
    g=0
    while loop3 <= int(CharNum):
        o=1
        CurrentMousex = SelectedCordx[g]
        CurrentMousey = SelectedCordy[g]
        while o <= int(SelectedDif[g]):
            print(SelectedDif[g], "<=", o)
            print("mousexy", CurrentMousex,", ", CurrentMousey)
            pyautogui.moveTo(x=int(CurrentMousex), y=int(CurrentMousey))
            time.sleep(0.3)
            pyautogui.click(x=int(CurrentMousex), y=int(CurrentMousey))
            o=int(o)+1
        g=int(g)+1
        loop3=int(loop3)+1
    
Charnum()   
Roll()
CheckChars()

def Goagain():
    while True:
        if keyboard.is_pressed("k"):
            Charnum()
            Roll()
            CheckChars()
            break
        if keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
            sg.popup('Exiting program', keep_on_top=True)
            time.sleep(1)
            sys.exit(0)
        else:
            continue
    


print("excludedchars", ExcludedChar)
print("selectedchars", SelectedChar)
print("selectedcordsx", SelectedCordx,"\n","selectedchordsy" ,SelectedCordy)
print("selecteddif", SelectedDif)
while True:
    sg.popup('Program has finished!\n Press [k] to go again or press [q] or [ESC] to quit\n Selected characters:',''.join(DispChar), keep_on_top=True)
    Goagain()