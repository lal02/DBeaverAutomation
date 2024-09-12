import os
import time
import pyautogui
import tkinter as tk
import threading 
import sys


diagram_folder = "C:\\Users\\lalbr\\AppData\\Roaming\\DBeaverData\\workspace6\\General\\Diagrams\\automatedprint"

pdf_folder = "C:\\Users\\lalbr\\Desktop\\programming_files\\python\\pdfexport"

erd_files = [f for f in os.listdir(diagram_folder) if f.endswith('.erd')]


app = tk.Tk()

def loadGUI():
    print("loading gui")

    global PPFEntry,DPFEntry
    
    app.title("DBeaver Auto Printer")
    #DPFLabel = diagram path folder label
    DPFLabel = tk.Label(app,text="enter path of diagram folder")
    DPFLabel.pack(padx = 50)

    #text entry for diagram folder path
    DPFEntry = tk.Entry(app,width=100)
    DPFEntry.pack(padx=10)

    #PPFLabel = pdf path folder label
    PPFLabel = tk.Label(app,text="enter path to export destination folder")
    PPFLabel.pack(padx =50)

    #text entry for pdf folder path
    PPFEntry = tk.Entry(app,width=100)
    PPFEntry.pack(padx=10)

    #start print button
    executeButton = tk.Button(app,text="execute print export",command=onExecuteButtonPressed)
    executeButton.pack(padx=50,pady=10)

    #abort buttong
    abortButton = tk.Button(app,text="abort",command=abort)
    abortButton.pack(padx=50,pady=5)

    #start application
    app.mainloop()

def abort():
    #app.destroy()
    #sys.exit()
    os._exit(1)

def onExecuteButtonPressed():
    readInput()
    thread = threading.Thread(target=exec)
    thread.start()
    # exec()

def readInput():
    global diagram_folder,pdf_folder
    input = DPFEntry.get()
    if input != "":
        diagram_folder = input

    input = PPFEntry.get()
    if input != "":
        pdf_folder = input
        
    # diagram_folder = DPFEntry.get()
    # pdf_folder = PPFEntry.get()


def exec():
    
    for f in erd_files:
        full_path = os.path.join(diagram_folder,f)

        print(full_path)

        os.startfile(full_path)
        time.sleep(5)
        
        #focus the dbeaver application upon opening
        screen_width,screen_height = pyautogui.size()
        pyautogui.moveTo(screen_width,screen_height/2)
        pyautogui.leftClick()
        time.sleep(1)

        #print to pdf
        pyautogui.hotkey('ctrl','p')
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        pyautogui.sleep(0.5)

        #navigate to adress bar
        pyautogui.hotkey('ctrl','l')
        pyautogui.typewrite(pdf_folder)
        pyautogui.hotkey('enter')
        time.sleep(0.5)
        
        #enter file name
        pyautogui.typewrite(f.removesuffix(".erd"))
        pyautogui.hotkey('enter')







if __name__ == "__main__":
    loadGUI()
    