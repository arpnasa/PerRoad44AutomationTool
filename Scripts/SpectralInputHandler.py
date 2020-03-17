import time

import autopy
import pandas as pd
from numpy import nan

from Scripts.AHKHandler import AHKHandler
from Configuration import Constant, Config


class SpectralInputHandler:

    def loadSpectraInput(self, ahk, data):
        # select the input tab to input structure details
        ahk.run_script(Constant.SPECT_INPUT_SUB_MENU)
        ahk.run_script('SetWinDelay, 10')

        ahkHandler = AHKHandler()

        self.single = False
        self.tandem = False
        self.tridem = False
        self.steer = False

        data = pd.DataFrame(data)
        data = pd.DataFrame(data.transpose())
        time.sleep(0.5)

        for i in data.columns:
            if type(i) == 'str':
                i = i.lower()

            if i == "two way aadt":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.writeFile(Constant.headerToClassNN[i], 'entry', data[i].values[0])
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\auto.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)


            elif i == "% trucks":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.writeFile(Constant.headerToClassNN[i], 'entry', data[i].values[0])
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\auto.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "% trucks in design lane":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.writeFile(Constant.headerToClassNN[i], 'entry', data[i].values[0])
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\auto.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "axle groups/day":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\general.ahk")
                ahkHandler.writeToFile("Sleep, 1000", Config.DATA_PATH + r"\general.ahk")

            elif i == "% truck growth":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.writeFile(Constant.headerToClassNN[i], 'entry', data[i].values[0])
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\auto.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "directional distribution":
                ahkHandler.writeFile(Constant.headerToClassNN[i], 'entry', data[i].values[0])
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\auto.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "single":
                if data[i].values[0] is nan:
                    continue

                self.single = True
                ahkHandler.appendToFile(Constant.headerToClassNN["current axle drop down"], "dropDown", "1",
                                        Config.DATA_PATH + r"\single.ahk")

                # time.sleep(2)
                ahkHandler.appendToFile(Constant.headerToClassNN["single CB"], "checkBox", True,
                                        Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", data[i].values[0],
                                        Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\checkBox.ahk")


            elif i == "tandem":
                if data[i].values[0] is nan:
                    continue

                self.tandem = True
                ahkHandler.appendToFile(Constant.headerToClassNN["current axle drop down"], "dropDown", "2",
                                        Config.DATA_PATH + r"\tandem.ahk")

                ahkHandler.appendToFile(Constant.headerToClassNN["tandem CB"], "checkBox", True,
                                        Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", data[i].values[0],
                                        Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\checkBox.ahk")

            elif i == "tridem":
                if data[i].values[0] is nan:
                    continue

                self.tridem = True

                ahkHandler.appendToFile(Constant.headerToClassNN["current axle drop down"], "dropDown", "3",
                                        Config.DATA_PATH + r"\tridem.ahk")

                ahkHandler.appendToFile(Constant.headerToClassNN["tridem CB"], "checkBox", True,
                                        Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", data[i].values[0],
                                        Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\checkBox.ahk")

            elif i == "steer":
                if data[i].values[0] is nan:
                    continue

                self.steer = True

                ahkHandler.appendToFile(Constant.headerToClassNN["current axle drop down"], "dropDown", "4",
                                        Config.DATA_PATH + r"\steer.ahk")

                ahkHandler.appendToFile(Constant.headerToClassNN["steer CB"], "checkBox", True,
                                        Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", data[i].values[0],
                                        Config.DATA_PATH + r"\checkBox.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\checkBox.ahk")


            elif i == "0-2 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")

                ahkScript = ahkHandler.readFile()

                ahk.run_script(ahkScript, blocking=False)

                ahkHandler.clearFile()

                time.sleep(0.5)


            elif i == "2-4 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")

                ahkScript = ahkHandler.readFile()

                ahk.run_script(ahkScript, blocking=False)

                ahkHandler.clearFile()

                time.sleep(0.5)


            elif i == "4-6 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "6-8 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "8-10 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "10-12 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")

                ahkScript = ahkHandler.readFile()

                ahk.run_script(ahkScript, blocking=False)

                ahkHandler.clearFile()

                time.sleep(0.5)


            elif i == "12-14 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "14-16 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "16-18 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "18-20 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "20-22 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "22-24 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "24-26 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "26-28 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "28-30 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")

                # ahkScript = ahkHandler.readFile()

                # ahk.run_script(ahkScript, blocking=False)

                # ahkHandler.clearFile()

                # time.sleep(0.5)


            elif i == "30-32 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "32-34 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "34-36 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "36-38 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "38-40 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")

                # ahkScript = ahkHandler.readFile()

                # ahk.run_script(ahkScript, blocking=False)

                # ahkHandler.clearFile()

                # time.sleep(0.5)


            elif i == "40-42 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "42-44 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "44-46 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "46-48 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "48-50 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "50-52 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "52-54 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "54-56 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "56-58 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "58-60 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "60-62 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "62-64 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "64-66 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "66-68 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "68-70 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "70-72 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "72-74 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "74-76 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "76-78 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "78-80 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "80-82 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "82-84 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "84-86 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "86-88 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "88-90 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "90-92 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "92-94 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "94-96 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "96-98 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "98-100 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "100-102 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "102-104 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "104-106 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "106-108 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "108-110 single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")


            elif i == "110+ single":

                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],

                                        Config.DATA_PATH + r"\single.ahk")

                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\single.ahk")

            elif i == "0-2 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "2-4 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "4-6 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "6-8 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "8-10 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "10-12 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "12-14 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "14-16 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "16-18 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "18-20 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "20-22 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "22-24 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "24-26 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "26-28 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "28-30 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                # ahkHandler.clearFile()
                # time.sleep(0.5)

            elif i == "30-32 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "32-34 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "34-36 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "36-38 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "38-40 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                # ahkHandler.clearFile()
                # time.sleep(0.5)

            elif i == "40-42 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "42-44 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "44-46 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "46-48 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "48-50 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "50-52 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "52-54 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "54-56 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "56-58 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "58-60 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "60-62 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "62-64 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "64-66 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "66-68 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "68-70 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "70-72 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "72-74 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "74-76 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "76-78 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "78-80 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "80-82 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "82-84 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "84-86 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "86-88 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "88-90 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "90-92 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "92-94 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "94-96 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "96-98 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "98-100 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "100-102 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "102-104 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "104-106 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "106-108 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "108-110 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")

            elif i == "110+ tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tandem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tandem.ahk")
                
            elif i == "0-2 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "2-4 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "4-6 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "6-8 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "8-10 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "10-12 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "12-14 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "14-16 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "16-18 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "18-20 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "20-22 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "22-24 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "24-26 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "26-28 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "28-30 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                # ahkHandler.clearFile()
                # time.sleep(0.5)

            elif i == "30-32 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "32-34 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "34-36 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "36-38 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "38-40 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                # ahkHandler.clearFile()
                # time.sleep(0.5)

            elif i == "40-42 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "42-44 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "44-46 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "46-48 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "48-50 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "50-52 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "52-54 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "54-56 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "56-58 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "58-60 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "60-62 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "62-64 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "64-66 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "66-68 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "68-70 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "70-72 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "72-74 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "74-76 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "76-78 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "78-80 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "80-82 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "82-84 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "84-86 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "86-88 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "88-90 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "90-92 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "92-94 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "94-96 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "96-98 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "98-100 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "100-102 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "102-104 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "104-106 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "106-108 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "108-110 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "110+ tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-7]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\tridem.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\tridem.ahk")

            elif i == "0-2 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "2-4 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "4-6 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "6-8 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "8-10 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "10-12 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()
                time.sleep(0.5)

            elif i == "12-14 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "14-16 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "16-18 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "18-20 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "20-22 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "22-24 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "24-26 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "26-28 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "28-30 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                # ahkHandler.clearFile()
                # time.sleep(0.5)

            elif i == "30-32 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "32-34 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "34-36 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "36-38 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "38-40 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                # ahkHandler.clearFile()
                # time.sleep(0.5)

            elif i == "40-42 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "42-44 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "44-46 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "46-48 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "48-50 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "50-52 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "52-54 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "54-56 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "56-58 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "58-60 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "60-62 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "62-64 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "64-66 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "66-68 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "68-70 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "70-72 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "72-74 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "74-76 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "76-78 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "78-80 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "80-82 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "82-84 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "84-86 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "86-88 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "88-90 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "90-92 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "92-94 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "94-96 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "96-98 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "98-100 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "100-102 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "102-104 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "104-106 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "106-108 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "108-110 steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "110+ steer":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i[:-6]], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\steer.ahk")
                ahkHandler.writeToFile("Sleep, 50", Config.DATA_PATH + r"\steer.ahk")

            elif i == "roadway functional classification":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN["load spectra button"], "radioButton", '',
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 1000", Config.DATA_PATH + r"\vehicle.ahk")

                num = '1'
                if data[i].values[0].lower() == "rural interstate":
                    num = '1'
                elif data[i].values[0].lower() == "rural principal arterial":
                    num = '2'
                elif data[i].values[0].lower() == "rural minor arterial":
                    num = '3'
                elif data[i].values[0].lower() == "rural major collector":
                    num = '4'
                elif data[i].values[0].lower() == "rural minor collector":
                    num = '5'
                elif data[i].values[0].lower() == "rural local collector":
                    num = '6'
                elif data[i].values[0].lower() == "urban interstate":
                    num = '7'
                elif data[i].values[0].lower() == "urban other freeways and expressways":
                    num = '8'
                elif data[i].values[0].lower() == "urban principal arterial":
                    num = '9'
                elif data[i].values[0].lower() == "urban minor arterial":
                    num = '10'
                elif data[i].values[0].lower() == "urban collector":
                    num = '11'

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num,
                                        Config.DATA_PATH + r"\vehicle.ahk")


            elif i == "class 4 ":
                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                # ahkHandler.clearFile()
                # time.sleep(0.5)

            elif i == "class 5":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 6":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 7":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 8":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 9":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 10":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 11":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 12":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 13":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 4 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 5 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 6 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 7 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 8 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 9 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 10 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 11 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 12 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 13 single":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 4 tandem":
                if data[i].values[0] is nan:
                    continue

                # print("in class 4 single")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 5 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 6 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 7 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 8 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 9 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 10 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 11 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 12 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 13 tandem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 4 tridem":
                if data[i].values[0] is nan:
                    continue

                # print("in class 4 single")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 5 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 6 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 7 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 8 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 9 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 10 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 11 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 12 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

            elif i == "class 13 tridem":
                if data[i].values[0] is nan:
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], 'entry', data[i].values[0],
                                        Config.DATA_PATH + r"\vehicle.ahk")
                ahkHandler.writeToFile("Sleep, 2", Config.DATA_PATH + r"\vehicle.ahk")

        ahkHandler.appendToFile("", "sendEnter", "", Config.DATA_PATH + r"\vehicle.ahk")
        ahkScript = ahkHandler.readFile(Config.DATA_PATH + r"\vehicle.ahk")
        ahk.run_script(ahkScript)
        ahkHandler.clearFile(Config.DATA_PATH + r"\vehicle.ahk")

        time.sleep(2)

        ahkScript = ahkHandler.readFile(Config.DATA_PATH + r"\checkBox.ahk")
        ahk.run_script(ahkScript)
        ahkHandler.clearFile(Config.DATA_PATH + r"\checkBox.ahk")

        time.sleep(2)

        if self.single:
            ahkScript = ahkHandler.readFile(Config.DATA_PATH + r"\single.ahk")
            ahk.run_script(ahkScript)
            ahkHandler.clearFile(Config.DATA_PATH + r"\single.ahk")
            time.sleep(2)

        if self.tandem:
            ahkScript = ahkHandler.readFile(Config.DATA_PATH + r"\tandem.ahk")
            ahk.run_script(ahkScript)
            ahkHandler.clearFile(Config.DATA_PATH + r"\tandem.ahk")
            time.sleep(2)

        if self.tridem:
            ahkScript = ahkHandler.readFile(Config.DATA_PATH + r"\tridem.ahk")
            ahk.run_script(ahkScript)
            ahkHandler.clearFile(Config.DATA_PATH + r"\tridem.ahk")
            time.sleep(2)

        if self.steer:
            ahkScript = ahkHandler.readFile(Config.DATA_PATH + r"\steer.ahk")
            ahk.run_script(ahkScript)
            ahkHandler.clearFile(Config.DATA_PATH + r"\steer.ahk")
            time.sleep(2)

        # time.sleep(2)

        ahkHandler.writeToFile("Send, {Enter}", Config.DATA_PATH + r"\general.ahk")
        ahkScript = ahkHandler.readFile(Config.DATA_PATH + r"\general.ahk")
        ahk.run_script(ahkScript)
        ahkHandler.clearFile(Config.DATA_PATH + r"\general.ahk")

        self.single = False
        self.tandem = False
        self.tridem = False
        self.steer = False
