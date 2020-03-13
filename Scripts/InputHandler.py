import time

import autopy
import pandas as pd
from numpy import nan

from Configuration import Constant, Config
from Scripts.AHKHandler import AHKHandler

class InputHandler:
    def loadStructuralInput(self, ahk, data):
        # select the input tab to input structure details
        winStructInputTab = ahk.find_window(title=b'PerRoad 4.4')
        winStructInputTab.send(autopy.key.tap(autopy.key.Code.F1))
        ahk.run_script('SetWinDelay, 10')
        ahk.run_script('SetWinDelay, 1000')

        ahkHandler = AHKHandler()

        currInputSet = 0

        if "current season" in data.columns:
            currSeason = data["current season"]
            self.csList = list(currSeason.iloc[currInputSet]) # later [0] = input set / j ... ie, each jth input contains number of season values
            self.csIndex = 0

        if "material type layer 1" in data.columns:
            materialType1 = data["material type layer 1"]
            self.mt1List = list(materialType1.iloc[currInputSet])
            self.mt1Index = 0
        # print(list(materialType1.iloc[0])) # prints the first row of the dataframe ie, for the 1st input set

        if "material type layer 2" in data.columns:
            materialType2 = data["material type layer 2"]
            self.mt2List = list(materialType2.iloc[currInputSet])
            self.mt2Index = 0

        if "material type layer 3" in data.columns:
            materialType3 = data["material type layer 3"]
            self.mt3List = list(materialType3.iloc[currInputSet])
            self.mt3Index = 0

        if "material type layer 4" in data.columns:
            materialType4 = data["material type layer 4"]
            self.mt4List = list(materialType4.iloc[currInputSet])
            self.mt4Index = 0

        if "material type layer 5" in data.columns:
            materialType5 = data["material type layer 5"]
            self.mt5List = list(materialType5.iloc[currInputSet])
            self.mt5Index = 0

        if "grade upper layer 1" in data.columns:
            gradeUpper1 = data["grade upper layer 1"]
            self.gu1List = list(gradeUpper1.iloc[currInputSet])
            self.gu1Index = 0

        if "grade upper layer 2" in data.columns:
            gradeUpper2 = data["grade upper layer 2"]
            self.gu2List = list(gradeUpper2.iloc[currInputSet])
            self.gu2Index = 0

        if "grade upper layer 3" in data.columns:
            gradeUpper3 = data["grade upper layer 3"]
            self.gu3List = list(gradeUpper3.iloc[currInputSet])
            self.gu3Index = 0

        if "grade upper layer 4" in data.columns:
            gradeUpper4 = data["grade upper layer 4"]
            self.gu4List = list(gradeUpper4.iloc[currInputSet])
            self.gu4Index = 0

        if "grade lower layer 1" in data.columns:
            gradeLower1 = data["grade lower layer 1"]
            self.gl1List = list(gradeLower1.iloc[currInputSet])
            self.gl1Index = 0

        if "grade lower layer 2" in data.columns:
            gradeLower2 = data["grade lower layer 2"]
            self.gl2List = list(gradeLower2.iloc[currInputSet])
            self.gl2Index = 0

        if "grade lower layer 3" in data.columns:
            gradeLower3 = data["grade lower layer 3"]
            self.gl3List = list(gradeLower3.iloc[currInputSet])
            self.gl3Index = 0

        if "grade lower layer 4" in data.columns:
            gradeLower4 = data["grade lower layer 4"]
            self.gl4List = list(gradeLower4.iloc[currInputSet])
            self.gl4Index = 0

        if "grade lower layer 4" in data.columns:
            gradeLower4 = data["grade lower layer 4"]
            self.gl4List = list(gradeLower4.iloc[currInputSet])
            self.gl4Index = 0

        if "modulus layer 1" in data.columns:
            mod1 = data["modulus layer 1"]
            self.mod1List = list(mod1.iloc[currInputSet])
            # print(self.mod1List)
            self.mod1Index = 0

        if "modulus layer 2" in data.columns:
            mod2 = data["modulus layer 2"]
            self.mod2List = list(mod2.iloc[currInputSet])
            # print(self.mod2List)
            self.mod2Index = 0

        if "modulus layer 3" in data.columns:
            mod3 = data["modulus layer 3"]
            self.mod3List = list(mod3.iloc[currInputSet])
            # print(self.mod3List)
            self.mod3Index = 0

        if "modulus layer 4" in data.columns:
            mod4 = data["modulus layer 4"]
            self.mod4List = list(mod4.iloc[currInputSet])
            # print(self.mod4List)
            self.mod4Index = 0

        if "modulus layer 5" in data.columns:
            mod5 = data["modulus layer 5"]
            self.mod5List = list(mod5.iloc[currInputSet])
            print(self.mod5List)
            self.mod5Index = 0

        if "poisons ratio layer 1" in data.columns:
            pr1 = data["poisons ratio layer 1"]
            self.pr1List = list(pr1.iloc[currInputSet])
            # print(self.pr1List)
            self.pr1Index = 0

        if "poisons ratio layer 2" in data.columns:
            pr2 = data["poisons ratio layer 2"]
            self.pr2List = list(pr2.iloc[currInputSet])
            # print("hi")
            # print(self.pr2List)
            self.pr2Index = 0

        if "poisons ratio layer 3" in data.columns:
            pr3 = data["poisons ratio layer 3"]
            self.pr3List = list(pr3.iloc[currInputSet])
            self.pr3Index = 0

        if "poisons ratio layer 4" in data.columns:
            pr4 = data["poisons ratio layer 4"]
            self.pr4List = list(pr4.iloc[currInputSet])
            self.pr4Index = 0

        if "poisons ratio layer 5" in data.columns:
            pr5 = data["poisons ratio layer 5"]
            self.pr5List = list(pr5.iloc[currInputSet])
            self.pr5Index = 0

        if "thickness layer 1" in data.columns:
            thickness1 = data["thickness layer 1"]
            self.thickness1List = list(thickness1.iloc[currInputSet])
            # print(self.thickness1List)
            self.thickness1Index = 0

        if "thickness layer 2" in data.columns:
            thickness2 = data["thickness layer 2"]
            self.thickness2List = list(thickness2.iloc[currInputSet])
            # print(self.thickness2List)
            self.thickness2Index = 0

        if "thickness layer 3" in data.columns:
            thickness3 = data["thickness layer 3"]
            self.thickness3List = list(thickness3.iloc[currInputSet])
            # print(self.thickness3List)
            self.thickness3Index = 0

        if "thickness layer 4" in data.columns:
            thickness4 = data["thickness layer 4"]
            self.thickness4List = list(thickness4.iloc[currInputSet])
            # print(self.thickness4List)
            self.thickness4Index = 0

        if "distribution type modulus" in data.columns:
            dtm = data["distribution type modulus"]
            self.dtmList = list(dtm.iloc[currInputSet])
            # print(self.dtmList)
            self.dtmIndex = 0

        if "distribution type thickness" in data.columns:
            dtt = data["distribution type thickness"]
            self.dttList = list(dtt.iloc[currInputSet])
            # print(self.dtmList)
            self.dttIndex = 0

        if "coefficient of variation modulus" in data.columns:
            cvm = data["coefficient of variation modulus"]
            self.cvmList = list(cvm.iloc[currInputSet])
            # print(self.dtmList)
            self.cvmIndex = 0

        if "coefficient of variation thickness" in data.columns:
            cvt = data["coefficient of variation thickness"]
            self.cvtList = list(cvt.iloc[currInputSet])
            # print(self.dtmList)
            self.cvtIndex = 0


        for i in data.columns:
            i = i.lower()
            if i == "summer" or i == "no of season" or i == "transfer function box" or i == "k1" or i == "k2":
                continue
            elif i == "no of layers":
                ahkHandler.writeFile(Constant.headerToClassNN[str(data[i][0])], "radioButton", '')
                ahkScript = ahkHandler.readFile()
                # print(ahkScript)
                # print()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()

            elif i == "fall" or i == "winter" or i == "spring" or i == "spring 2":
                if data[i][0] == 'yes':
                    check = True
                else:
                    check = False

                ahkHandler.writeFile(Constant.headerToClassNN[i], "checkBox", check)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "current season":
                # time.sleep(2)
                if self.csList[self.csIndex] is nan:
                    self.csIndex += 1
                    continue

                setSeason = '1'
                if self.csList[self.csIndex].lower() == 'summer':
                    setSeason = '1'
                elif self.csList[self.csIndex].lower() == 'fall':
                    setSeason = '2'
                elif self.csList[self.csIndex].lower() == 'winter':
                    setSeason = '3'
                elif self.csList[self.csIndex].lower() == 'spring':
                    setSeason = '4'
                elif self.csList[self.csIndex].lower() == 'spring 2':
                    setSeason = '5'

                self.csIndex += 1

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\mod1Auto.ahk")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\mod2Auto.ahk")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\mod3Auto.ahk")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\mod4Auto.ahk")
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\mod5Auto.ahk")

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\var1Auto.ahk")

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\var2Auto.ahk")

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\var3Auto.ahk")

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\var4Auto.ahk")

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", setSeason,
                                        Config.DATA_PATH + r"\var5Auto.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)

            elif i == "material type layer 1":
                num = '1'
                if self.mt1List[self.mt1Index] is nan:
                    self.mt1Index += 1
                    continue

                if self.mt1List[self.mt1Index].lower() == "ac":
                    num = '1'
                elif self.mt1List[self.mt1Index].lower() == "other":
                    num = '2'

                self.mt1Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade upper layer 1":
                num = '1'
                if self.gu1List[self.gu1Index] is nan:
                    self.gu1Index += 1
                    continue

                if self.gu1List[self.gu1Index] == 82:
                    num = '1'
                elif self.gu1List[self.gu1Index] == 76:
                    num = '2'
                elif self.gu1List[self.gu1Index] == 70:
                    num = '3'
                elif self.gu1List[self.gu1Index] == 64:
                    num = '4'
                elif self.gu1List[self.gu1Index] == 58:
                    num = '5'
                elif self.gu1List[self.gu1Index] == 52:
                    num = '6'
                elif self.gu1List[self.gu1Index] == 46:
                    num = '7'

                self.gu1Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "grade lower layer 1":
                num = '1'
                if self.gl1List[self.gl1Index] is nan:
                    self.gl1Index += 1
                    continue

                if self.gl1List[self.gl1Index] == -10:
                    num = '1'
                elif self.gl1List[self.gl1Index] == -16:
                    num = '2'
                elif self.gl1List[self.gl1Index] == -22:
                    num = '3'
                elif self.gl1List[self.gl1Index] == -28:
                    num = '4'
                elif self.gl1List[self.gl1Index] == -34:
                    num = '5'
                elif self.gl1List[self.gl1Index] == -40:
                    num = '6'

                self.gl1Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "modulus layer 1":
                # time.sleep(2)
                if self.mod1List[self.mod1Index] is nan:
                    self.mod1Index += 1
                    continue
                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", self.mod1List[self.mod1Index], Config.DATA_PATH + r"\mod1Auto.ahk")
                self.mod1Index += 1

            elif i == "poisons ratio layer 1":
                time.sleep(0.5)
                if self.pr1List[self.pr1Index] is nan:
                    self.pr1Index += 1
                    continue

                self.varLayer = "variability button layer 1"
                self.perLayer = "performance button layer 1"

                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.pr1List[self.pr1Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.pr1Index += 1
                time.sleep(0.5)


            elif i == "thickness layer 1":
                # time.sleep(0.5)
                if self.thickness1List[self.thickness1Index] is nan:
                    self.thickness1Index += 1
                    continue
                self.varLayer = "variability button layer 1"
                self.perLayer = "performance button layer 1"
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.thickness1List[self.thickness1Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.thickness1Index += 1
                time.sleep(0.5)

            elif i == "distribution type modulus" and self.varLayer == "variability button layer 1":
                print(i)
                num = '1'
                if self.dtmList[self.dtmIndex].lower() == "normal":
                    num = '1'
                elif self.dtmList[self.dtmIndex].lower() == "log normal" or self.dtmList[self.dtmIndex].lower() == "log-normal":
                    num = '2'

                path = Config.DATA_PATH + r"\var1Auto.ahk"
                # if "layer 1" in self.varLayer:
                #     # print(self.varLayer, path)
                #     path = Config.DATA_PATH + r"\var1Auto.ahk"
                # elif "layer 2" in self.varLayer:
                #     # print(self.varLayer, path)
                #     path = Config.DATA_PATH + r"\var2Auto.ahk"
                # elif "layer 3" in self.varLayer:
                #     # print(self.varLayer, path)
                #     path = Config.DATA_PATH + r"\var3Auto.ahk"
                # elif "layer 4" in self.varLayer:
                #     # print(self.varLayer, path)
                #     path = Config.DATA_PATH + r"\var4Auto.ahk"
                # elif "layer 5" in self.varLayer:
                #     # print(self.varLayer, path)
                #     path = Config.DATA_PATH + r"\var5Auto.ahk"


                # ahkHandler.appendToFile(Constant.headerToClassNN[i],"variabilityDropDown", num, path, self.varLayer)
                # ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation modulus"], "entry", self.cvmList[self.cvmIndex], path)
                # ahkHandler.appendToFile(Constant.headerToClassNN["distribution type thickness"], "dropDown", num, path)
                # ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation thickness"], "lastEntry", self.cvtList[self.cvtIndex], path)
                # self.dtmIndex += 1
                # self.cvmIndex += 1
                # self.dttIndex += 1
                # self.cvtIndex += 1
                #
                # # ahkHandler.writeFile(Constant.headerToClassNN[i], "variabilityDropDown", num, self.varLayer)
                # ahkScript = ahkHandler.readFile(path)
                # # print(ahkScript)
                # ahk.run_script(ahkScript, blocking=False)
                # time.sleep(0.5)
                # ahkHandler.clearFile(path)

            # elif i == "coefficient of variation modulus":
            #     path = Config.DATA_PATH + r"\var1Auto.ahk"
            #     if "layer 1" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var1Auto.ahk"
            #     elif "layer 2" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var2Auto.ahk"
            #     elif "layer 3" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var3Auto.ahk"
            #     elif "layer 4" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var4Auto.ahk"
            #     elif "layer 5" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var5Auto.ahk"
            #
            #     ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", self.cvmList[self.cvmIndex], path)
            #     # ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.cvmList[self.cvmIndex])
            #     # ahkScript = ahkHandler.readFile()
            #     # ahk.run_script(ahkScript, blocking=False)
            #     # time.sleep(0.5)
            #     self.cvmIndex += 1

            #     ControlSetText, Edit1, 20, ahk_exe PerRoad44.exe
            # Control, Choose, 2, ComboBox2, ahk_exe PerRoad44.exe
            # ControlSetText, Edit2, 6, ahk_exe PerRoad44.exe

            # elif i == "distribution type thickness":
            #     num = '1'
            #     if self.dttList[self.dttIndex].lower() == "normal":
            #         num = '1'
            #     elif self.dttList[self.dttIndex].lower() == "log normal" or self.dttList[self.dttIndex].lower() == "log-normal":
            #         num = '2'
            #
            #     path = Config.DATA_PATH + r"\var1Auto.ahk"
            #     if "layer 1" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var1Auto.ahk"
            #     elif "layer 2" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var2Auto.ahk"
            #     elif "layer 3" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var3Auto.ahk"
            #     elif "layer 4" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var4Auto.ahk"
            #     elif "layer 5" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var5Auto.ahk"
            #
            #     self.dttIndex += 1
            #     ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num, path)
                # ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num,)
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                # time.sleep(0.5)

            # elif i == "coefficient of variation thickness":
            #     path = Config.DATA_PATH + r"\var1Auto.ahk"
            #     if "layer 1" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var1Auto.ahk"
            #     elif "layer 2" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var2Auto.ahk"
            #     elif "layer 3" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var3Auto.ahk"
            #     elif "layer 4" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var4Auto.ahk"
            #     elif "layer 5" in self.varLayer:
            #         path = Config.DATA_PATH + r"\var5Auto.ahk"
            #
            #     ahkHandler.appendToFile(Constant.headerToClassNN[i], "lastEntry", self.cvtList[self.cvtIndex], path)
            #     # ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.cvtList[self.cvtIndex])
            #     # ahkScript = ahkHandler.readFile()
            #     # ahk.run_script(ahkScript, blocking=False)
            #     # ahk.run_script("Send, {Enter}")
            #     self.cvtIndex += 1
                # time.sleep(0.5)

            elif i == "material type layer 2":
                num = '1'
                if self.mt2List[self.mt2Index] is nan:
                    self.mt2List[self.mt2Index] += 1
                    continue

                if self.mt2List[self.mt2Index].lower() == "ac":
                    num = '1'
                elif self.mt2List[self.mt2Index].lower() == "cracked ac":
                    num = '2'
                elif self.mt2List[self.mt2Index].lower() == "pcc":
                    num = '3'
                elif self.mt2List[self.mt2Index].lower() == "rub pcc":
                    num = '4'
                elif self.mt2List[self.mt2Index].lower() == "c and s pcc":
                    num = '5'
                elif self.mt2List[self.mt2Index].lower() == "B and S PCC".lower():
                    num = '6'
                elif self.mt2List[self.mt2Index].lower() == "Gran Base".lower():
                    num = '7'
                elif self.mt2List[self.mt2Index].lower() == "Soil".lower():
                    num = '8'
                elif self.mt2List[self.mt2Index].lower() == "Rock".lower():
                    num = '9'
                elif self.mt2List[self.mt2Index].lower() == "Other".lower():
                    num = '10'

                self.mt2Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                # print(i)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                # print(ahkScript)
                ahk.run_script(ahkScript, blocking=False)
                # time.sleep(0.5)



            elif i == "grade upper layer 2":
                num = '1'
                if self.gu2List[self.gu2Index] is nan:
                    self.gu2Index += 1
                    continue

                if self.gu2List[self.gu2Index] == 82:
                    num = '1'
                elif self.gu2List[self.gu2Index] == 76:
                    num = '2'
                elif self.gu2List[self.gu2Index] == 70:
                    num = '3'
                elif self.gu2List[self.gu2Index] == 64:
                    num = '4'
                elif self.gu2List[self.gu2Index] == 58:
                    num = '5'
                elif self.gu2List[self.gu2Index] == 52:
                    num = '6'
                elif self.gu2List[self.gu2Index] == 46:
                    num = '7'

                self.gu2Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade lower layer 2":
                num = '1'
                if self.gl2List[self.gl2Index] is nan:
                    self.gl1Index += 1
                    continue

                if self.gl2List[self.gl2Index] == -10:
                    num = '1'
                elif self.gl2List[self.gl2Index] == -16:
                    num = '2'
                elif self.gl2List[self.gl2Index] == -22:
                    num = '3'
                elif self.gl2List[self.gl2Index] == -28:
                    num = '4'
                elif self.gl2List[self.gl2Index] == -34:
                    num = '5'
                elif self.gl2List[self.gl2Index] == -40:
                    num = '6'

                self.gl2Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "modulus layer 2":
                if self.mod2List[self.mod2Index] is nan:
                    self.mod2Index += 1
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", self.mod2List[self.mod2Index], Config.DATA_PATH + r"\mod2Auto.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                self.mod2Index += 1

            elif i == "poisons ratio layer 2":
                # time.sleep(0.5)
                if self.pr2List[self.pr2Index] is nan:
                    self.pr2Index += 1
                    continue

                self.varLayer = "variability button layer 2"
                self.perLayer = "performance button layer 2"

                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.pr2List[self.pr2Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.pr2Index += 1
                time.sleep(0.5)


            elif i == "thickness layer 2":
                # time.sleep(0.5)
                if self.thickness2List[self.thickness2Index] is nan:
                    self.thickness2Index += 1
                    continue

                self.varLayer = "variability button layer 2"
                self.perLayer = "performance button layer 2"
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.thickness2List[self.thickness2Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.thickness2Index += 1
                time.sleep(0.5)


            elif i == "material type layer 3":
                num = '1'
                if self.mt3List[self.mt3Index] is nan:
                    self.mt3List[self.mt3Index] += 1
                    continue

                if self.mt3List[self.mt3Index].lower() == "AC".lower():
                    num = '1'
                elif self.mt3List[self.mt3Index].lower() == "Cracked AC".lower():
                    num = '2'
                elif self.mt3List[self.mt3Index].lower() == "PCC".lower():
                    num = '3'
                elif self.mt3List[self.mt3Index].lower() == "Rub PCC".lower():
                    num = '4'
                elif self.mt3List[self.mt3Index].lower() == "C and S PCC".lower():
                    num = '5'
                elif self.mt3List[self.mt3Index].lower() == "B and S PCC".lower():
                    num = '6'
                elif self.mt3List[self.mt3Index].lower() == "Gran Base".lower():
                    num = '7'
                elif self.mt3List[self.mt3Index].lower() == "Soil".lower():
                    num = '8'
                elif self.mt3List[self.mt3Index].lower() == "Rock".lower():
                    num = '9'
                elif self.mt3List[self.mt3Index].lower() == "Other".lower():
                    num = '10'

                self.mt3Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade upper layer 3":
                num = '1'
                if self.gu3List[self.gu3Index] is nan:
                    self.gu3Index += 1
                    continue

                if self.gu3List[self.gu3Index] == 82:
                    num = '1'
                elif self.gu3List[self.gu3Index] == 76:
                    num = '2'
                elif self.gu3List[self.gu3Index] == 70:
                    num = '3'
                elif self.gu3List[self.gu3Index] == 64:
                    num = '4'
                elif self.gu3List[self.gu3Index] == 58:
                    num = '5'
                elif self.gu3List[self.gu3Index] == 52:
                    num = '6'
                elif self.gu3List[self.gu3Index] == 46:
                    num = '7'

                self.gu3Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade lower layer 3":
                num = '1'
                if self.gl3List[self.gl3Index] is nan:
                    self.gl3Index += 1
                    continue

                if self.gl3List[self.gl3Index] == -10:
                    num = '1'
                elif self.gl3List[self.gl3Index] == -16:
                    num = '2'
                elif self.gl3List[self.gl3Index] == -22:
                    num = '3'
                elif self.gl3List[self.gl3Index] == -28:
                    num = '4'
                elif self.gl3List[self.gl3Index] == -34:
                    num = '5'
                elif self.gl3List[self.gl3Index] == -40:
                    num = '6'

                self.gl3Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "modulus layer 3":
                if self.mod3List[self.mod3Index] is nan:
                    self.mod3Index += 1
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", self.mod3List[self.mod3Index], Config.DATA_PATH + r"\mod3Auto.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                self.mod3Index += 1

            elif i == "poisons ratio layer 3":
                # time.sleep(0.5)
                if self.pr3List[self.pr3Index] is nan:
                    self.pr3Index += 1
                    continue

                self.varLayer = "variability button layer 3"
                self.perLayer = "performance button layer 3"

                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.pr3List[self.pr3Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.pr3Index += 1
                time.sleep(0.5)


            elif i == "thickness layer 3":
                # time.sleep(0.5)
                if self.thickness3List[self.thickness3Index] is nan:
                    self.thickness3Index += 1
                    continue

                self.varLayer = "variability button layer 3"
                self.perLayer = "performance button layer 3"
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.thickness3List[self.thickness3Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.thickness3Index += 1
                time.sleep(0.5)


            elif i == "material type layer 4":
                num = '1'
                if self.mt4List[self.mt4Index] is nan:
                    self.mt4List[self.mt4Index] += 1
                    continue

                if self.mt4List[self.mt4Index].lower() == "AC".lower():
                    num = '1'
                elif self.mt4List[self.mt4Index].lower() == "Cracked AC".lower():
                    num = '2'
                elif self.mt4List[self.mt4Index].lower() == "PCC".lower():
                    num = '3'
                elif self.mt4List[self.mt4Index].lower() == "Rub PCC".lower():
                    num = '4'
                elif self.mt4List[self.mt4Index].lower() == "C and S PCC".lower():
                    num = '5'
                elif self.mt4List[self.mt4Index].lower() == "B and S PCC".lower():
                    num = '6'
                elif self.mt4List[self.mt4Index].lower() == "Gran Base".lower():
                    num = '7'
                elif self.mt4List[self.mt4Index].lower() == "Soil".lower():
                    num = '8'
                elif self.mt4List[self.mt4Index].lower() == "Rock".lower():
                    num = '9'
                elif self.mt4List[self.mt4Index].lower() == "Other".lower():
                    num = '10'

                self.mt4Index += 1

                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade upper layer 4":
                num = '1'
                if self.gu4List[self.gu4Index] is nan:
                    self.gu4Index += 1
                    continue

                if self.gu4List[self.gu4Index] == 82:
                    num = '1'
                elif self.gu4List[self.gu4Index] == 76:
                    num = '2'
                elif self.gu4List[self.gu4Index] == 70:
                    num = '3'
                elif self.gu4List[self.gu4Index] == 64:
                    num = '4'
                elif self.gu4List[self.gu4Index] == 58:
                    num = '5'
                elif self.gu4List[self.gu4Index] == 52:
                    num = '6'
                elif self.gu4List[self.gu4Index] == 46:
                    num = '7'

                self.gu4Index += 1

                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade lower layer 4":
                num = '1'
                if self.gl4List[self.gl4Index] is nan:
                    self.gl4Index += 1
                    continue

                if self.gl4List[self.gl4Index] == -10:
                    num = '1'
                elif self.gl4List[self.gl4Index] == -16:
                    num = '2'
                elif self.gl4List[self.gl4Index] == -22:
                    num = '3'
                elif self.gl4List[self.gl4Index] == -28:
                    num = '4'
                elif self.gl4List[self.gl4Index] == -34:
                    num = '5'
                elif self.gl4List[self.gl4Index] == -40:
                    num = '6'

                self.gl4Index += 1

                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "modulus layer 4":
                if self.mod4List[self.mod4Index] is nan:
                    self.mod4Index += 1
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", self.mod4List[self.mod4Index], Config.DATA_PATH + r"\mod4Auto.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                self.mod4Index += 1

            elif i == "poisons ratio layer 4":
                # time.sleep(0.5)
                if self.pr4List[self.pr4Index] is nan:
                    self.pr4Index += 1
                    continue

                self.varLayer = "variability button layer 4"
                self.perLayer = "performance button layer 4"

                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.pr4List[self.pr4Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.pr4Index += 1
                time.sleep(0.5)


            elif i == "thickness layer 4":
                # time.sleep(0.5)
                if self.thickness4List[self.thickness4Index] is nan:
                    self.thickness4Index += 1
                    continue

                self.varLayer = "variability button layer 4"
                self.perLayer = "performance button layer 4"
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.thickness4List[self.thickness4Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.thickness4Index += 1
                time.sleep(0.5)




            elif i == "material type layer 5":
                num = '1'
                if self.mt5List[self.mt5Index] is nan:
                    self.mt5List[self.mt5Index] += 1
                    continue

                if self.mt5List[self.mt5Index].lower() == "Gran Base".lower():
                    num = '1'
                elif self.mt5List[self.mt5Index].lower() == "Soil".lower():
                    num = '2'
                elif self.mt5List[self.mt5Index].lower() == "Rock".lower():
                    num = '3'
                elif self.mt5List[self.mt5Index].lower() == "Other".lower():
                    num = '4'

                self.mt5Index += 1

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num, Config.DATA_PATH + r"\modAuto.ahk")
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)



            elif i == "modulus layer 5":
                if self.mod5List[self.mod5Index] is nan:
                    self.mod5Index += 1
                    continue

                ahkHandler.appendToFile(Constant.headerToClassNN[i], "entry", self.mod5List[self.mod5Index], Config.DATA_PATH + r"\mod5Auto.ahk")
                # ahkScript = ahkHandler.readFile()
                # ahk.run_script(ahkScript, blocking=False)
                self.mod5Index += 1

            elif i == "poisons ratio layer 5":
                # time.sleep(0.5)
                if self.pr5List[self.pr5Index] is nan:
                    self.pr5Index += 1
                    continue

                self.varLayer = "variability button layer 5"
                self.perLayer = "performance button layer 5"
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.pr5List[self.pr5Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.pr5Index += 1
                time.sleep(0.5)


        # ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod4Auto.ahk")
        # ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod4Auto.ahk")
        #
        # time.sleep(2)
        #
        # ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod5Auto.ahk")
        # ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod5Auto.ahk")
        #
        # time.sleep(2)

        # ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var1Auto.ahk")
        # ahk.run_script(ahkScript, blocking=False)
        # ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var1Auto.ahk")

        # time.sleep(2)

        # ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var2Auto.ahk")
        # ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var2Auto.ahk")

        # time.sleep(2)

        # ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var3Auto.ahk")
        # ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var3Auto.ahk")

        # time.sleep(2)

        ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod1Auto.ahk")
        ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod1Auto.ahk")

        time.sleep(2)

        ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod2Auto.ahk")
        ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod2Auto.ahk")

        time.sleep(2)

        ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod3Auto.ahk")
        ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod3Auto.ahk")

        # time.sleep(2)

        # ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var4Auto.ahk")
        # ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var4Auto.ahk")
        #
        # time.sleep(2)
        #
        # ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var5Auto.ahk")
        # ahk.run_script(ahkScript, blocking=False)
        ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var5Auto.ahk")

    def loadSpectraInput(self, ahk):
        # select the input tab to input structure details
        winSpectraInputTab = ahk.find_window(title=b'PerRoad 4.4')
        winSpectraInputTab.send(autopy.key.tap(autopy.key.Code.F2))
        ahk.run_script('SetWinDelay, 10')