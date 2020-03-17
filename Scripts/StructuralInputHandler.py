import time

import autopy
import pandas as pd
from numpy import nan

from Configuration import Constant, Config
from Scripts.AHKHandler import AHKHandler

class StructuralInputHandler:
    def loadStructuralInput(self, ahk, data):
        # select the input tab to input structure details
        ahk.run_script(Constant.STRUCT_INPUT_SUB_MENU)
        ahk.run_script('SetWinDelay, 10')
        ahk.run_script('SetWinDelay, 1000')

        ahkHandler = AHKHandler()

        data = pd.DataFrame(data)
        data = pd.DataFrame(data.transpose())

        # print((data["no of layers"] == 3).bool())
        # with pd.option_context('display.max_rows', None, 'display.max_columns',
        #                        None):  # more options can be specified also
        #     print(data)

        # print(data["poisons ratio layer 1"].values[0][0])

        if "current season" in data.columns:
            self.csList = list(data["current season"])
            # self.csList = list(currSeason.iloc[currInputSet]) # later [0] = input set / j ... ie, each jth input contains number of season values
            self.csIndex = 0

        if "material type layer 1" in data.columns:
            materialType1 = data["material type layer 1"]
            self.mt1List = list(materialType1)
            self.mt1Index = 0
            self.mt1Count = 1
        # print(list(materialType1.iloc[0])) # prints the first row of the dataframe ie, for the 1st input set

        if "material type layer 2" in data.columns:
            materialType2 = data["material type layer 2"]
            self.mt2List = materialType2.values[0]
            # print(self.mt2List)
            self.mt2Index = 0
            self.mt2Count = 1

        if "material type layer 3" in data.columns:
            materialType3 = data["material type layer 3"]
            self.mt3List = materialType3.values[0]
            self.mt3Index = 0
            self.mt3Count = 1

        if "material type layer 4" in data.columns:
            materialType4 = data["material type layer 4"]
            self.mt4List = materialType4.values[0]
            self.mt4Index = 0
            self.mt4Count = 1

        if "material type layer 5" in data.columns:
            materialType5 = data["material type layer 5"]
            self.mt5List = materialType5.values[0]
            self.mt5Index = 0
            self.mt5Count = 1

        if "grade upper layer 1" in data.columns:
            gradeUpper1 = data["grade upper layer 1"]
            self.gu1List = gradeUpper1.values[0]
            self.gu1Index = 0
            self.gu1Count = 1

        if "grade upper layer 2" in data.columns:
            gradeUpper2 = data["grade upper layer 2"]
            self.gu2List = gradeUpper2.values[0]
            self.gu2Index = 0
            self.gu2Count = 1

        if "grade upper layer 3" in data.columns:
            gradeUpper3 = data["grade upper layer 3"]
            self.gu3List = gradeUpper3.values[0]
            self.gu3Index = 0
            self.gu3Count = 1

        if "grade upper layer 4" in data.columns:
            gradeUpper4 = data["grade upper layer 4"]
            self.gu4List = gradeUpper4.values[0]
            self.gu4Index = 0
            self.gu4Count = 1

        if "grade lower layer 1" in data.columns:
            gradeLower1 = data["grade lower layer 1"]
            self.gl1List = gradeLower1.values[0]
            self.gl1Index = 0
            self.gl1Count = 1

        if "grade lower layer 2" in data.columns:
            gradeLower2 = data["grade lower layer 2"]
            self.gl2List = gradeLower2.values[0]
            self.gl2Index = 0
            self.gl2Count = 1

        if "grade lower layer 3" in data.columns:
            gradeLower3 = data["grade lower layer 3"]
            self.gl3List = gradeLower3.values[0]
            self.gl3Index = 0
            self.gl3Count = 1

        if "grade lower layer 4" in data.columns:
            gradeLower4 = data["grade lower layer 4"]
            self.gl4List = gradeLower4.values[0]
            self.gl4Index = 0
            self.gl4Count = 1

        if "modulus layer 1" in data.columns:
            mod1 = data["modulus layer 1"]
            self.mod1List = mod1.values[0]
            # print(self.mod1List)
            self.mod1Index = 0

        if "modulus layer 2" in data.columns:
            mod2 = data["modulus layer 2"]
            self.mod2List = mod2.values[0]
            # print(self.mod2List)
            self.mod2Index = 0

        if "modulus layer 3" in data.columns:
            mod3 = data["modulus layer 3"]
            self.mod3List = mod3.values[0]
            # print(self.mod3List)
            self.mod3Index = 0

        if "modulus layer 4" in data.columns:
            mod4 = data["modulus layer 4"]
            self.mod4List = mod4.values[0]
            # print(self.mod4List)
            self.mod4Index = 0

        if "modulus layer 5" in data.columns:
            mod5 = data["modulus layer 5"]
            self.mod5List = mod5.values[0]
            print(self.mod5List)
            self.mod5Index = 0

        if "poisons ratio layer 1" in data.columns:
            pr1 = data["poisons ratio layer 1"]
            self.pr1List = pr1.values[0]
            # print(self.pr1List)
            self.pr1Index = 0
            self.pr1Count = 1

        if "poisons ratio layer 2" in data.columns:
            pr2 = data["poisons ratio layer 2"]
            self.pr2List = pr2.values[0]
            # print("hi")
            # print(self.pr2List)
            self.pr2Index = 0
            self.pr2Count = 1

        if "poisons ratio layer 3" in data.columns:
            pr3 = data["poisons ratio layer 3"]
            self.pr3List = pr3.values[0]
            self.pr3Index = 0
            self.pr3Count = 1

        if "poisons ratio layer 4" in data.columns:
            pr4 = data["poisons ratio layer 4"]
            self.pr4List = pr4.values[0]
            self.pr4Index = 0
            self.pr4Count = 1

        if "poisons ratio layer 5" in data.columns:
            pr5 = data["poisons ratio layer 5"]
            self.pr5List = pr5.values[0]
            self.pr5Index = 0
            self.pr5Count = 1

        if "thickness layer 1" in data.columns:
            thickness1 = data["thickness layer 1"]
            self.thickness1List = thickness1.values[0]
            # print(self.thickness1List)
            self.thickness1Index = 0
            self.t1Count = 1

        if "thickness layer 2" in data.columns:
            thickness2 = data["thickness layer 2"]
            self.thickness2List = thickness2.values[0]
            # print(self.thickness2List)
            self.thickness2Index = 0
            self.t2Count = 1

        if "thickness layer 3" in data.columns:
            thickness3 = data["thickness layer 3"]
            self.thickness3List = thickness3.values[0]
            # print(self.thickness3List)
            self.thickness3Index = 0
            self.t3Count = 1

        if "thickness layer 4" in data.columns:
            thickness4 = data["thickness layer 4"]
            self.thickness4List = thickness4.values[0]
            # print(self.thickness4List)
            self.thickness4Index = 0
            self.t4Count = 1

        if "distribution type modulus" in data.columns:
            dtm = data["distribution type modulus"]
            self.dtmList = dtm.values[0]
            # print(self.dtmList)
            self.dtmIndex = 0
            self.dtm1Count = 1
            self.dtm2Count = 1
            self.dtm3Count = 1
            self.dtm4Count = 1
            self.dtm5Count = 1

        if "distribution type thickness" in data.columns:
            dtt = data["distribution type thickness"]
            self.dttList = dtt.values[0]
            # print(self.dtmList)
            self.dttIndex = 0

        if "coefficient of variation modulus" in data.columns:
            cvm = data["coefficient of variation modulus"]
            self.cvmList = cvm.values[0]
            self.cvmIndex = 0

        if "coefficient of variation thickness" in data.columns:
            cvt = data["coefficient of variation thickness"]
            self.cvtList = cvt.values[0]
            # print(self.dtmList)
            self.cvtIndex = 0

        if "criteria top" in data.columns:
            ct = data["criteria top"]
            self.ctList = ct.values[0]
            # print(self.ctList)
            self.ctIndex = 0
            self.ct1Count = 1
            self.ct2Count = 1
            self.ct3Count = 1
            self.ct4Count = 1
            self.ct5Count = 1

        if "criteria middle" in data.columns:
            cm = data["criteria middle"]
            self.cmList = cm.values[0]
            self.cmIndex = 0
            self.cm1Count = 1
            self.cm2Count = 1
            self.cm3Count = 1
            self.cm4Count = 1
            self.cm5Count = 1

        if "criteria bottom" in data.columns:
            cb = data["criteria bottom"]
            self.cbList = cb.values[0]
            self.cbIndex = 0
            self.cb1Count = 1
            self.cb2Count = 1
            self.cb3Count = 1
            self.cb4Count = 1
            self.cb5Count = 1

        if "threshold top" in data.columns:
            tt = data["threshold top"]
            self.ttList = tt.values[0]
            self.ttIndex = 0

        if "threshold middle" in data.columns:
            tm = data["threshold middle"]
            self.tmList = tm.values[0]
            self.tmIndex = 0
            self.tmCount = 1

        if "threshold bottom" in data.columns:
            tb = data["threshold bottom"]
            self.tbList = tb.values[0]
            self.tbIndex = 0
            self.tbCount = 1

        if "target percentile top" in data.columns:
            tpt = data["target percentile top"]
            self.tptList = tpt.values[0]
            self.tptIndex = 0
            self.tptCount = 1

        if "target percentile middle" in data.columns:
            tpm = data["target percentile middle"]
            self.tpmList = tpm.values[0]
            self.tpmIndex = 0
            self.tpmCount = 1

        if "target percentile bottom" in data.columns:
            tpb = data["criteria bottom"]
            self.tpbList = tpb.values[0]
            self.tpbIndex = 0
            self.tpbCount = 1

        if "transfer function box top" in data.columns:
            tfbt = data["transfer function box top"]
            self.tfbtList = tfbt.values[0]
            self.tfbtIndex = 0
            self.tfbtCount = 1

        if "transfer function box middle" in data.columns:
            tfbm = data["transfer function box middle"]
            self.tfbmList = tfbm.values[0]
            # print(self.tfbmList)
            self.tfbmIndex = 0
            self.tfbmCount = 1

        if "transfer function box bottom" in data.columns:
            tfbb = data["transfer function box bottom"]
            self.tfbbList = tfbb.values[0]
            self.tfbbIndex = 0
            self.tfbbCount = 1

        if "k1 top" in data.columns:
            k1t = data["k1 top"]
            self.k1tList = k1t.values[0]
            self.k1tIndex = 0
            self.k1tCount = 1

        if "k1 middle" in data.columns:
            k1m = data["k1 middle"]
            self.k1mList = k1m.values[0]
            self.k1mIndex = 0
            self.k1mCount = 1

        if "k1 bottom" in data.columns:
            k1b = data["k1 bottom"]
            self.k1bList = k1b.values[0]
            self.k1bIndex = 0
            self.k1bCount = 1

        if "k2 top" in data.columns:
            k2t = data["k2 top"]
            self.k2tList = k2t.values[0]
            self.k2tIndex = 0
            self.k2tCount = 1

        if "k2 middle" in data.columns:
            k2m = data["k2 middle"]
            self.k2mList = k2m.values[0]
            self.k2mIndex = 0
            self.k2mCount = 1

        if "k2 bottom" in data.columns:
            k2b = data["k2 bottom"]
            self.k2bList = k2b.values[0]
            self.k2bIndex = 0
            self.k2bCount = 1

        # time.sleep(5)

        for i in data.columns:
            if type(i) == 'str':
                i = i.lower()
            if i == "summer" or i == "no of season" or i == "transfer function box" or i == "k1" or i == "k2":
                continue
            elif i == "no of layers":
                # print(data[i].values[0])
                ahkHandler.writeFile(Constant.headerToClassNN[str(data[i].values[0])], "radioButton", '')
                ahkScript = ahkHandler.readFile()
                # print(ahkScript)
                # print()
                ahk.run_script(ahkScript, blocking=False)
                ahkHandler.clearFile()

            elif i == "fall" or i == "winter" or i == "spring" or i == "spring 2":
                if data[i].values[0] == 'yes':
                    check = True
                else:
                    check = False

                ahkHandler.writeFile(Constant.headerToClassNN[i], "checkBox", check)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "duration summer":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["duration summer"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "duration fall":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["duration fall"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "duration winter":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["duration winter"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "duration spring":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["duration spring"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "duration spring 2":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["duration spring 2"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "mean air summer":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["mean air summer"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "mean air fall":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["mean air fall"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "mean air winter":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["mean air winter"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "mean air spring":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["mean air spring"].values[0])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "mean air spring 2":
                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", data["mean air spring 2"].values[0])
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

            elif i == "material type layer 1" and self.mt1Count > 0:
                num = '1'
                if self.mt1List[0] is nan:
                    # self.mt1Index += 1
                    continue

                if self.mt1List[0].lower() == "ac":
                    num = '1'
                elif self.mt1List[0].lower() == "other":
                    num = '2'

                # self.mt1Index += 1
                self.mt1Count = 0

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade upper layer 1" and self.gu1Count > 0:
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
                self.gu1Count = 0

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)

            elif i == "grade lower layer 1" and self.gl1Count > 0:
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
                self.gl1Count = 0

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

            elif i == "poisons ratio layer 1" and self.pr1Count > 0:
                time.sleep(0.5)
                if self.pr1List[self.pr1Index] is nan:
                    self.pr1Index += 1
                    continue

                self.varLayer = "variability button layer 1"
                self.perLayer = "performance button layer 1"
                self.pr1Count = 0

                ahkHandler.writeFile(Constant.headerToClassNN[i], "entry", self.pr1List[self.pr1Index])
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                self.pr1Index += 1
                time.sleep(0.5)


            elif i == "thickness layer 1"  and self.t1Count > 0:
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
                self.t1Count = 0
                time.sleep(0.5)

            elif i == "distribution type modulus" and self.varLayer == "variability button layer 1" and self.dtm1Count > 0:
                # time.sleep(0.5)
                # print(i)
                num1 = '1'
                if self.dtmList[self.dtmIndex].lower() == "normal":
                    num1 = '1'
                elif self.dtmList[self.dtmIndex].lower() == "log normal" or self.dtmList[self.dtmIndex].lower() == "log-normal":
                    num1 = '2'

                num2 = '1'
                if self.dttList[self.dttIndex].lower() == "normal":
                    num2 = '1'
                elif self.dttList[self.dttIndex].lower() == "log normal" or self.dttList[self.dttIndex].lower() == "log-normal":
                    num2 = '2'

                path = Config.DATA_PATH + r"\var1Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[i],"variabilityDropDown", num1, path, self.varLayer)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation modulus"], "entry", self.cvmList[self.cvmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["distribution type thickness"], "simpleDropDown", num2, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation thickness"], "lastEntry", self.cvtList[self.cvtIndex], path)
                self.dtmIndex += 1
                self.cvmIndex += 1
                self.dttIndex += 1
                self.cvtIndex += 1
                self.dtm1Count = 0

                time.sleep(0.5)

            elif i == "criteria top" and self.perLayer == "performance button layer 1" and self.ct1Count > 0:
                path = Config.DATA_PATH + r"\per1Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[self.perLayer], "clickButton", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                num = '1'
                if self.ctList[self.ctIndex].lower() == "Horizontal Stress".lower():
                    num = '1'
                elif self.ctList[self.ctIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.ctList[self.ctIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.ctList[self.ctIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.ctList[self.ctIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.ctList[self.ctIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.ctList[self.ctIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["top"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria top"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold top"], "entry", self.ttList[self.ttIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile top"], "entry", self.tptList[self.tptIndex], path)

                self.ttIndex += 1
                self.tptIndex += 1

                if "transfer function box top" in data.columns and self.tfbtList[self.tfbtIndex] == 'yes':
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box top"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 top"], "entry", self.k1tList[self.k1tIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 top"], "entry", self.k2tList[self.k2tIndex], path)
                    self.tfbtIndex += 1
                    self.k1tIndex += 1
                    self.k2tIndex += 1

                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.ct1Count = 0
                # time.sleep(0.5)

            elif i == "criteria middle" and self.perLayer == "performance button layer 1" and self.cm1Count > 0:
                path = Config.DATA_PATH + r"\per1Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                num = '1'
                if self.cmList[self.cmIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cmList[self.cmIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cmList[self.cmIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cmList[self.cmIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cmList[self.cmIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cmList[self.cmIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cmList[self.cmIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tmList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpmList[self.tpmIndex], path)

                self.tmIndex += 1
                self.tpmIndex += 1

                if "transfer function box middle" in data.columns and self.tfbmList[self.tfbmIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box middle"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 middle"], "entry", self.k1mList[self.k1mIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 middle"], "entry", self.k2mList[self.k2mIndex], path)
                    self.tfbmIndex += 1
                    self.k1mIndex += 1
                    self.k2mIndex += 1


                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.cm1Count = 0
            #     time.sleep(0.5)

            elif i == "criteria bottom" and self.perLayer == "performance button layer 1" and self.cb1Count > 0:
                path = Config.DATA_PATH + r"\per1Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                num = '1'
                if self.cbList[self.cbIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cbList[self.cbIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cbList[self.cbIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cbList[self.cbIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cbList[self.cbIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cbList[self.cbIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cbList[self.cbIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tbList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpbList[self.tpbIndex], path)

                self.tbIndex += 1
                self.tpbIndex += 1

                if "transfer function box bottom" in data.columns and self.tfbbList[self.tfbbIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box bottom"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 bottom"], "entry", self.k1bList[self.k1bIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 bottom"], "entry", self.k2bList[self.k2bIndex], path)
                    self.tfbbIndex += 1
                    self.k1bIndex += 1
                    self.k2bIndex += 1


                ahkHandler.appendToFile('', 'sleep', '', path)
                self.cb1Count = 0
            #     time.sleep(0.5)

            elif i == "material type layer 2" and self.mt2Count > 0:
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
                self.mt2Count = 0

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                # print(i)
                # print(num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                # print(ahkScript)
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)



            elif i == "grade upper layer 2" and self.gu2Count > 0:
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
                self.gu2Count = 0

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade lower layer 2" and self.gl2Count > 0:
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
                self.gl2Count = 0

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

            elif i == "poisons ratio layer 2" and self.pr2Count > 0:
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
                self.pr2Count = 0
                time.sleep(0.5)


            elif i == "thickness layer 2" and self.t2Count > 0:
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
                self.t2Count = 0
                time.sleep(0.5)

            elif i == "distribution type modulus" and self.varLayer == "variability button layer 2" and self.dtm2Count > 0:
                # time.sleep(0.5)
                # print(i)
                num1 = '1'
                if self.dtmList[self.dtmIndex].lower() == "normal":
                    num1 = '1'
                elif self.dtmList[self.dtmIndex].lower() == "log normal" or self.dtmList[self.dtmIndex].lower() == "log-normal":
                    num1 = '2'

                num2 = '1'
                if self.dttList[self.dttIndex].lower() == "normal":
                    num2 = '1'
                elif self.dttList[self.dttIndex].lower() == "log normal" or self.dttList[self.dttIndex].lower() == "log-normal":
                    num2 = '2'

                path = Config.DATA_PATH + r"\var2Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[i],"variabilityDropDown", num1, path, self.varLayer)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation modulus"], "entry", self.cvmList[self.cvmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["distribution type thickness"], "simpleDropDown", num2, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation thickness"], "lastEntry", self.cvtList[self.cvtIndex], path)
                self.dtmIndex += 1
                self.cvmIndex += 1
                self.dttIndex += 1
                self.cvtIndex += 1
                self.dtm2Count = 0

                time.sleep(0.5)

            elif i == "criteria top" and self.perLayer == "performance button layer 2" and self.ct2Count > 0:
                path = Config.DATA_PATH + r"\per2Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[self.perLayer], "clickButton", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                num = '1'
                if self.ctList[self.ctIndex].lower() == "Horizontal Stress".lower():
                    num = '1'
                elif self.ctList[self.ctIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.ctList[self.ctIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.ctList[self.ctIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.ctList[self.ctIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.ctList[self.ctIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.ctList[self.ctIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["top"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria top"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold top"], "entry", self.ttList[self.ttIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile top"], "entry", self.tptList[self.tptIndex], path)

                self.ttIndex += 1
                self.tptIndex += 1

                if "transfer function box top" in data.columns and self.tfbtList[self.tfbtIndex] == 'yes':
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box top"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 top"], "entry", self.k1tList[self.k1tIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 top"], "entry", self.k2tList[self.k2tIndex], path)
                    self.tfbtIndex += 1
                    self.k1tIndex += 1
                    self.k2tIndex += 1

                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.ct2Count = 0
                # time.sleep(0.5)

            elif i == "criteria middle" and self.perLayer == "performance button layer 2" and self.cm2Count > 0:
                path = Config.DATA_PATH + r"\per2Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)
                if (data["no of layers"] == 2).bool():
                    continue

                num = '1'
                if self.cmList[self.cmIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cmList[self.cmIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cmList[self.cmIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cmList[self.cmIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cmList[self.cmIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cmList[self.cmIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cmList[self.cmIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tmList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpmList[self.tpmIndex], path)

                self.tmIndex += 1
                self.tpmIndex += 1

                if "transfer function box middle" in data.columns and self.tfbmList[self.tfbmIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box middle"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 middle"], "entry", self.k1mList[self.k1mIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 middle"], "entry", self.k2mList[self.k2mIndex], path)
                    self.tfbmIndex += 1
                    self.k1mIndex += 1
                    self.k2mIndex += 1


                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', 'sleep', '', path)
                self.cm2Count = 0
            #     time.sleep(0.5)

            elif i == "criteria bottom" and self.perLayer == "performance button layer 2" and self.cb2Count > 0:
                path = Config.DATA_PATH + r"\per2Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                if (data["no of layers"] == 2).bool():
                    continue

                num = '1'
                if self.cbList[self.cbIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cbList[self.cbIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cbList[self.cbIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cbList[self.cbIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cbList[self.cbIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cbList[self.cbIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cbList[self.cbIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry",
                                        self.tbList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry",
                                        self.tpbList[self.tpbIndex], path)

                self.tbIndex += 1
                self.tpbIndex += 1

                if "transfer function box bottom" in data.columns and self.tfbbList[self.tfbbIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box bottom"], "checkBox",
                                            True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 bottom"], "entry",
                                            self.k1bList[self.k1bIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 bottom"], "entry",
                                            self.k2bList[self.k2bIndex], path)
                    self.tfbbIndex += 1
                    self.k1bIndex += 1
                    self.k2bIndex += 1

                ahkHandler.appendToFile('', 'sleep', '', path)
                self.cb2Count = 0
            #     time.sleep(0.5)


            elif i == "material type layer 3" and self.mt3Count > 0:
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
                self.mt3Count = 0

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade upper layer 3" and self.gu3Count > 0:
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
                self.gu3Count = 0

                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade lower layer 3" and self.gl3Count > 0:
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
                self.gl3Count = 0

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

            elif i == "poisons ratio layer 3" and self.pr3Count > 0:
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
                self.pr3Count = 0
                time.sleep(0.5)


            elif i == "thickness layer 3" and self.t3Count > 0:
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
                self.t3Count = 0
                time.sleep(0.5)

            elif i == "distribution type modulus" and self.varLayer == "variability button layer 3" and self.dtm3Count > 0:
                # time.sleep(0.5)
                # print(i)
                num1 = '1'
                if self.dtmList[self.dtmIndex].lower() == "normal":
                    num1 = '1'
                elif self.dtmList[self.dtmIndex].lower() == "log normal" or self.dtmList[self.dtmIndex].lower() == "log-normal":
                    num1 = '2'

                num2 = '1'
                if self.dttList[self.dttIndex].lower() == "normal":
                    num2 = '1'
                elif self.dttList[self.dttIndex].lower() == "log normal" or self.dttList[self.dttIndex].lower() == "log-normal":
                    num2 = '2'

                path = Config.DATA_PATH + r"\var3Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[i],"variabilityDropDown", num1, path, self.varLayer)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation modulus"], "entry", self.cvmList[self.cvmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["distribution type thickness"], "simpleDropDown", num2, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation thickness"], "lastEntry", self.cvtList[self.cvtIndex], path)
                self.dtmIndex += 1
                self.cvmIndex += 1
                self.dttIndex += 1
                self.cvtIndex += 1
                self.dtm3Count = 0

                time.sleep(0.5)


            elif i == "criteria top" and self.perLayer == "performance button layer 3" and self.ct3Count > 0:
                path = Config.DATA_PATH + r"\per3Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[self.perLayer], "clickButton", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                num = '1'
                if self.ctList[self.ctIndex].lower() == "Horizontal Stress".lower():
                    num = '1'
                elif self.ctList[self.ctIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.ctList[self.ctIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.ctList[self.ctIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.ctList[self.ctIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.ctList[self.ctIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.ctList[self.ctIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["top"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria top"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold top"], "entry", self.ttList[self.ttIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile top"], "entry", self.tptList[self.tptIndex], path)

                self.ttIndex += 1
                self.tptIndex += 1

                if "transfer function box top" in data.columns and self.tfbtList[self.tfbtIndex] == 'yes':
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box top"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 top"], "entry", self.k1tList[self.k1tIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 top"], "entry", self.k2tList[self.k2tIndex], path)
                    self.tfbtIndex += 1
                    self.k1tIndex += 1
                    self.k2tIndex += 1

                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.ct3Count = 0
                # time.sleep(0.5)

            elif i == "criteria middle" and self.perLayer == "performance button layer 3" and self.cm3Count > 0:
                path = Config.DATA_PATH + r"\per3Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                if (data["no of layers"] == 3).bool():
                    continue

                num = '1'
                if self.cmList[self.cmIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cmList[self.cmIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cmList[self.cmIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cmList[self.cmIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cmList[self.cmIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cmList[self.cmIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cmList[self.cmIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tmList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpmList[self.tpmIndex], path)

                self.tmIndex += 1
                self.tpmIndex += 1

                if "transfer function box middle" in data.columns and self.tfbmList[self.tfbmIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box middle"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 middle"], "entry", self.k1mList[self.k1mIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 middle"], "entry", self.k2mList[self.k2mIndex], path)
                    self.tfbmIndex += 1
                    self.k1mIndex += 1
                    self.k2mIndex += 1


                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.cm3Count = 0
            #     time.sleep(0.5)

            elif i == "criteria bottom" and self.perLayer == "performance button layer 3" and self.cb3Count > 0:
                path = Config.DATA_PATH + r"\per3Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                if (data["no of layers"] == 3).bool():
                    continue

                num = '1'
                if self.cbList[self.cbIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cbList[self.cbIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cbList[self.cbIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cbList[self.cbIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cbList[self.cbIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cbList[self.cbIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cbList[self.cbIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tbList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpbList[self.tpbIndex], path)

                self.tbIndex += 1
                self.tpbIndex += 1

                if "transfer function box bottom" in data.columns and self.tfbbList[self.tfbbIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box bottom"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 bottom"], "entry", self.k1bList[self.k1bIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 bottom"], "entry", self.k2bList[self.k2bIndex], path)
                    self.tfbbIndex += 1
                    self.k1bIndex += 1
                    self.k2bIndex += 1


                ahkHandler.appendToFile('', 'sleep', '', path)
                self.cb3Count = 0
            #     time.sleep(0.5)

            elif i == "material type layer 4" and self.mt4Count > 0:
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
                self.mt4Count = 0

                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade upper layer 4" and self.gu4Count > 0:
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
                self.gu4Count = 0

                ahkHandler.writeFile(Constant.headerToClassNN[i], "dropDown", num)
                # ahkHandler.appendToFile(Constant.headerToClassNN[i], "dropDown", num)
                ahkScript = ahkHandler.readFile()
                ahk.run_script(ahkScript, blocking=False)
                time.sleep(0.5)


            elif i == "grade lower layer 4" and self.gl4Count > 0:
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
                self.gl4Count = 0

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

            elif i == "poisons ratio layer 4" and self.pr4Count > 0:
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
                self.pr4Count = 0
                time.sleep(0.5)


            elif i == "thickness layer 4" and self.t4Count > 0:
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
                self.t4Count = 0
                time.sleep(0.5)

            elif i == "distribution type modulus" and self.varLayer == "variability button layer 4" and self.dtm4Count > 0:
                # time.sleep(0.5)
                # print(i)
                num1 = '1'
                if self.dtmList[self.dtmIndex].lower() == "normal":
                    num1 = '1'
                elif self.dtmList[self.dtmIndex].lower() == "log normal" or self.dtmList[self.dtmIndex].lower() == "log-normal":
                    num1 = '2'

                num2 = '1'
                if self.dttList[self.dttIndex].lower() == "normal":
                    num2 = '1'
                elif self.dttList[self.dttIndex].lower() == "log normal" or self.dttList[self.dttIndex].lower() == "log-normal":
                    num2 = '2'

                path = Config.DATA_PATH + r"\var4Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[i],"variabilityDropDown", num1, path, self.varLayer)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation modulus"], "entry", self.cvmList[self.cvmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["distribution type thickness"], "simpleDropDown", num2, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation thickness"], "lastEntry", self.cvtList[self.cvtIndex], path)
                self.dtmIndex += 1
                self.cvmIndex += 1
                self.dttIndex += 1
                self.cvtIndex += 1
                self.dtm4Count = 0

                time.sleep(0.5)

            elif i == "criteria top" and self.perLayer == "performance button layer 4" and self.ct4Count > 0:
                path = Config.DATA_PATH + r"\per4Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[self.perLayer], "clickButton", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                num = '1'
                if self.ctList[self.ctIndex].lower() == "Horizontal Stress".lower():
                    num = '1'
                elif self.ctList[self.ctIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.ctList[self.ctIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.ctList[self.ctIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.ctList[self.ctIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.ctList[self.ctIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.ctList[self.ctIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["top"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria top"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold top"], "entry", self.ttList[self.ttIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile top"], "entry", self.tptList[self.tptIndex], path)

                self.ttIndex += 1
                self.tptIndex += 1

                if "transfer function box top" in data.columns and self.tfbtList[self.tfbtIndex] == 'yes':
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box top"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 top"], "entry", self.k1tList[self.k1tIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 top"], "entry", self.k2tList[self.k2tIndex], path)
                    self.tfbtIndex += 1
                    self.k1tIndex += 1
                    self.k2tIndex += 1

                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.ct4Count = 0
                # time.sleep(0.5)

            elif i == "criteria middle" and self.perLayer == "performance button layer 4" and self.cm4Count > 0:
                path = Config.DATA_PATH + r"\per4Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                if (data["no of layers"] == 4).bool():
                    continue

                num = '1'
                if self.cmList[self.cmIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cmList[self.cmIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cmList[self.cmIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cmList[self.cmIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cmList[self.cmIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cmList[self.cmIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cmList[self.cmIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tmList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpmList[self.tpmIndex], path)

                self.tmIndex += 1
                self.tpmIndex += 1

                if "transfer function box middle" in data.columns and self.tfbmList[self.tfbmIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box middle"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 middle"], "entry", self.k1mList[self.k1mIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 middle"], "entry", self.k2mList[self.k2mIndex], path)
                    self.tfbmIndex += 1
                    self.k1mIndex += 1
                    self.k2mIndex += 1


                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.cm4Count = 0
            #     time.sleep(0.5)

            elif i == "criteria bottom" and self.perLayer == "performance button layer 4" and self.cb4Count > 0:
                path = Config.DATA_PATH + r"\per4Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                if (data["no of layers"] == 4).bool():
                    continue

                num = '1'
                if self.cbList[self.cbIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cbList[self.cbIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cbList[self.cbIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cbList[self.cbIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cbList[self.cbIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cbList[self.cbIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cbList[self.cbIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tbList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpbList[self.tpbIndex], path)

                self.tbIndex += 1
                self.tpbIndex += 1

                if "transfer function box bottom" in data.columns and self.tfbbList[self.tfbbIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box bottom"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 bottom"], "entry", self.k1bList[self.k1bIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 bottom"], "entry", self.k2bList[self.k2bIndex], path)
                    self.tfbbIndex += 1
                    self.k1bIndex += 1
                    self.k2bIndex += 1


                ahkHandler.appendToFile('', 'sleep', '', path)
                self.cb4Count = 0
            #     time.sleep(0.5)

            elif i == "material type layer 5" and self.mt5Count > 0:
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
                self.mt5Count = 0

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

            elif i == "poisons ratio layer 5" and self.pr5Count > 0:
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
                self.pr5Count = 0
                time.sleep(0.5)

            elif i == "distribution type modulus" and self.varLayer == "variability button layer 5" and self.dtm5Count > 0:
                # time.sleep(0.5)
                # print(i)
                num1 = '1'
                if self.dtmList[self.dtmIndex].lower() == "normal":
                    num1 = '1'
                elif self.dtmList[self.dtmIndex].lower() == "log normal" or self.dtmList[self.dtmIndex].lower() == "log-normal":
                    num1 = '2'

                num2 = '1'
                if self.dttList[self.dttIndex].lower() == "normal":
                    num2 = '1'
                elif self.dttList[self.dttIndex].lower() == "log normal" or self.dttList[self.dttIndex].lower() == "log-normal":
                    num2 = '2'

                path = Config.DATA_PATH + r"\var5Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[i],"variabilityDropDown", num1, path, self.varLayer)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation modulus"], "entry", self.cvmList[self.cvmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["distribution type thickness"], "simpleDropDown", num2, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["coefficient of variation thickness"], "lastEntry", self.cvtList[self.cvtIndex], path)
                self.dtmIndex += 1
                self.cvmIndex += 1
                self.dttIndex += 1
                self.cvtIndex += 1
                self.dtm5Count = 0

                time.sleep(0.5)

            elif i == "criteria top" and self.perLayer == "performance button layer 5" and self.ct5Count > 0:
                path = Config.DATA_PATH + r"\per5Auto.ahk"
                ahkHandler.appendToFile(Constant.headerToClassNN[self.perLayer], "clickButton", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                num = '1'
                if self.ctList[self.ctIndex].lower() == "Horizontal Stress".lower():
                    num = '1'
                elif self.ctList[self.ctIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.ctList[self.ctIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.ctList[self.ctIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.ctList[self.ctIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.ctList[self.ctIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.ctList[self.ctIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["top"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria top"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold top"], "entry", self.ttList[self.ttIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile top"], "entry", self.tptList[self.tptIndex], path)

                self.ttIndex += 1
                self.tptIndex += 1

                if "transfer function box top" in data.columns and self.tfbtList[self.tfbtIndex] == 'yes':
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box top"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 top"], "entry", self.k1tList[self.k1tIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 top"], "entry", self.k2tList[self.k2tIndex], path)
                    self.tfbtIndex += 1
                    self.k1tIndex += 1
                    self.k2tIndex += 1

                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.ct5Count = 0
                # time.sleep(0.5)

            elif i == "criteria middle" and self.perLayer == "performance button layer 5" and self.cm5Count > 0:
                path = Config.DATA_PATH + r"\per5Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                if (data["no of layers"] == 5).bool():
                    continue

                num = '1'
                if self.cmList[self.cmIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cmList[self.cmIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cmList[self.cmIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cmList[self.cmIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cmList[self.cmIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cmList[self.cmIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cmList[self.cmIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tmList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpmList[self.tpmIndex], path)

                self.tmIndex += 1
                self.tpmIndex += 1

                if "transfer function box middle" in data.columns and self.tfbmList[self.tfbmIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box middle"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 middle"], "entry", self.k1mList[self.k1mIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 middle"], "entry", self.k2mList[self.k2mIndex], path)
                    self.tfbmIndex += 1
                    self.k1mIndex += 1
                    self.k2mIndex += 1


                # ahkHandler.appendToFile('', 'sendEnter', '', path)
                ahkHandler.appendToFile('', "sleep", '', path)
                self.cm5Count = 0
            #     time.sleep(0.5)

            elif i == "criteria bottom" and self.perLayer == "performance button layer 5" and self.cb5Count > 0:
                path = Config.DATA_PATH + r"\per5Auto.ahk"
                # ahkHandler.appendToFile('', "sleep", '', path)
                # ahkHandler.appendToFile('', "sleep", '', path)

                if (data["no of layers"] == 5).bool():
                    continue

                num = '1'
                if self.cbList[self.cbIndex].lower() == "Horizontal Stress".lower():
                        num = '1'
                elif self.cbList[self.cbIndex].lower() == "Vertical Stress".lower():
                    num = '2'
                elif self.cbList[self.cbIndex].lower() == "Principal Stress".lower():
                    num = '3'
                elif self.cbList[self.cbIndex].lower() == "Horizontal Strain".lower():
                    num = '4'
                elif self.cbList[self.cbIndex].lower() == "Vertical Strain".lower():
                    num = '5'
                elif self.cbList[self.cbIndex].lower() == "Principal Strain".lower():
                    num = '6'
                elif self.cbList[self.cbIndex].lower() == "Vertical Deflection".lower():
                    num = '7'

                # ahkHandler.appendToFile('', "sleep", '', path)
                ahkHandler.appendToFile(Constant.headerToClassNN["middle"], "checkBox", True, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["criteria middle"], "dropDown", num, path)
                ahkHandler.appendToFile(Constant.headerToClassNN["threshold middle"], "entry", self.tbList[self.tmIndex], path)
                ahkHandler.appendToFile(Constant.headerToClassNN["target percentile middle"], "entry", self.tpbList[self.tpbIndex], path)

                self.tbIndex += 1
                self.tpbIndex += 1

                if "transfer function box bottom" in data.columns and self.tfbbList[self.tfbbIndex] == 'yes':
                    # ahkHandler.appendToFile('', "sleep", '', path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["transfer function box bottom"], "checkBox", True, path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k1 bottom"], "entry", self.k1bList[self.k1bIndex], path)
                    ahkHandler.appendToFile(Constant.headerToClassNN["k2 bottom"], "entry", self.k2bList[self.k2bIndex], path)
                    self.tfbbIndex += 1
                    self.k1bIndex += 1
                    self.k2bIndex += 1


                ahkHandler.appendToFile('', 'sleep', '', path)
                self.cb5Count = 0
            #     time.sleep(0.5)

        numLayers = data["no of layers"].values[0]

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var1Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            # print(ahkScript)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var1Auto.ahk")
            numLayers -= 1

            time.sleep(4)

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var2Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var2Auto.ahk")
            numLayers -= 1

            time.sleep(4)

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var3Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var3Auto.ahk")
            numLayers -= 1

            time.sleep(4)

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var4Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var4Auto.ahk")
            numLayers -= 1

            time.sleep(4)

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\var5Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\var5Auto.ahk")
            numLayers -= 1

            time.sleep(4)

        numLayers = data["no of layers"].values[0]

        if numLayers > 0:
            ahkHandler.appendToFile('', 'justSendEnter', '', Config.DATA_PATH + r"\per1Auto.ahk")
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\per1Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\per1Auto.ahk")
            numLayers -= 1
            time.sleep(4)

        if numLayers > 0:
            ahkHandler.appendToFile('', 'justSendEnter', '', Config.DATA_PATH + r"\per2Auto.ahk")
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\per2Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            # print(ahkScript)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\per2Auto.ahk")
            numLayers -= 1
            time.sleep(4)

        if numLayers > 0:
            ahkHandler.appendToFile('', 'justSendEnter', '', Config.DATA_PATH + r"\per3Auto.ahk")
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\per3Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            # print(ahkScript)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\per3Auto.ahk")
            numLayers -= 1
            time.sleep(4)

        if numLayers > 0:
            ahkHandler.appendToFile('', 'justSendEnter', '', Config.DATA_PATH + r"\per4Auto.ahk")
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\per4Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            # print(ahkScript)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\per4Auto.ahk")
            numLayers -= 1
            time.sleep(4)

        if numLayers > 0:
            ahkHandler.appendToFile('', 'justSendEnter', '', Config.DATA_PATH + r"\per5Auto.ahk")
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\per5Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            # print(ahkScript)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\per5Auto.ahk")
            numLayers -= 1
            time.sleep(4)

        numLayers = data["no of layers"].values[0]

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod1Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod1Auto.ahk")
            numLayers -= 1

            time.sleep(2)

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod2Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod2Auto.ahk")
            numLayers -= 1

            time.sleep(2)

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod3Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod3Auto.ahk")
            numLayers -= 1

            time.sleep(2)

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod4Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod4Auto.ahk")
            numLayers -= 1

            time.sleep(2)

        if numLayers > 0:
            ahkScript = ahkHandler.readFile(filename=Config.DATA_PATH + r"\mod5Auto.ahk")
            ahk.run_script(ahkScript, blocking=False)
            ahkHandler.clearFile(filename=Config.DATA_PATH + r"\mod5Auto.ahk")
            numLayers -= 1

        ahk.run_script("Send, {Enter}\nSleep, 2\n")