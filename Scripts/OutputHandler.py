import time

import autopy
from Configuration import Constant, Config
from Scripts.AHKHandler import AHKHandler
import pandas as pd

class OutputHandler:
    def downlaodOutput(self, ahk, data):

        data = pd.DataFrame(data)
        data = pd.DataFrame(data.transpose())

        # open the output tab
        ahk.run_script(Constant.VIEW_OUTPUT_SUB_MENU)
        ahk.run_script('SetWinDelay, 10')

        ahkHandler = AHKHandler()

        time.sleep(1)

        # setting monte carlo cycles
        ahkHandler.writeFile(Constant.headerToClassNN["set mote carlo cycles"], "radioButton", '')
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(1)

        ahkHandler.writeFile(Constant.headerToClassNN["number of cycles"], "entry", data["number of cycles"].values[0])
        ahkHandler.writeToFile("Sleep,2\nSend, {Enter}", Config.DATA_PATH + r"\auto.ahk")
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(1)

        # click on perform analysis
        ahkHandler.writeFile(Constant.headerToClassNN["perform analysis"], "radioButton", '')
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(1)

        # click ok
        ahkHandler.writeFile(Constant.headerToClassNN["ok"], "radioButton", '')
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(1)

        # save the output file
        ahkHandler.writeFile(Constant.headerToClassNN["save path"], "entry", Config.OUTPUT_PATH + data['save filename'].values[0])
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(1)

        ahkHandler.writeFile(Constant.headerToClassNN["save"], "radioButton", '')
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(5)

        # export formatted data
        ahkHandler.writeFile(Constant.headerToClassNN["export"], "radioButton", '')
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(1)

        ahkHandler.writeFile(Constant.headerToClassNN["save path"], "entry",
                             Config.OUTPUT_PATH + data['filename report'].values[0][:-5])
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(1)

        ahkHandler.writeFile(Constant.headerToClassNN["save"], "radioButton", '')
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()

        time.sleep(1)

        autopy.key.tap(autopy.key.Code.ESCAPE)

        ahkHandler.writeFile(Constant.headerToClassNN["leave"], "radioButton", '')
        ahkScript = ahkHandler.readFile()
        ahk.run_script(ahkScript)
        ahkHandler.clearFile()