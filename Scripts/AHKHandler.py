from Configuration import Constant, Config


class AHKHandler:

    def writeToFile(self, s, filename):
        f = open(filename, "a")
        f.write(s)
        f.write("\n")

    def writeFile(self, variable, Type, check, varLayer=''):
        f = open(Config.DATA_PATH + r"\auto.ahk", "w+")

        if Type == "checkBox":
            if check:
                # f.write("Sleep, 1000")
                f.write(Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
                # f.write("Control, Enable,," + variable + Constant.AHK_EXE)
                f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CHECK + variable + Constant.AHK_EXE)
                # f.write("Sleep, 2\n")

            else:
                f.write(Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
                f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_UNCHECK + variable + Constant.AHK_EXE)

        elif Type == "radioButton":
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CLICK + variable + Constant.AHK_EXE)

        elif Type == "dropDown":
            f.write(Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CHOOSE + check + "," + variable + Constant.AHK_EXE)

        elif Type == "variabilityDropDown":
            f.write(Constant.CONTROL_CLICK + Constant.headerToClassNN[varLayer] + Constant.AHK_EXE)
            f.write("WinActivate\nSleep, 2\n")
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CHOOSE + check + "," + variable + Constant.AHK_EXE)

        elif Type == "entry":
            f.write(
                Constant.SET_CONTROL_DELAY + Constant.CONTROL_SET_TEXT + variable + "," + str(check) + Constant.AHK_EXE)

        f.close()

    def appendToFile(self, variable, Type, check, filename, layer=''):
        f = open(filename, "a")
        if Type == "checkBox":
            if check:
                # f.write("Sleep, 50\n")
                f.write(Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
                # f.write("Control, Enable,," + variable + Constant.AHK_EXE)
                f.write(Constant.CONTROL_CHECK + variable + Constant.AHK_EXE)
                f.write("Sleep, 2\n")
            else:
                # f.write("Sleep, 50\n")
                f.write(Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
                f.write(Constant.CONTROL_UNCHECK + variable + Constant.AHK_EXE)
                f.write("Sleep, 2\n")

        elif Type == "radioButton":
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CLICK + variable + Constant.AHK_EXE)

        elif Type == "clickButton":
            f.write(Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
            f.write(Constant.CONTROL_CLICK + variable + Constant.AHK_EXE)
            f.write("WinActivate\nSleep, 2\n")


        elif Type == "dropDown":
            f.write(Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CHOOSE + check + "," + variable + Constant.AHK_EXE)

        elif Type == "simpleDropDown":
            f.write("WinActivate\nSleep, 2\n")
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CHOOSE + check + "," + variable + Constant.AHK_EXE)

        elif Type == "entry":
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CLICK + variable + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_SET_TEXT + variable + "," + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CLICK + variable + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_SEND + variable + ", {Home}+{End}" + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_EDIT_PASTE + str(
                check) + "," + variable + Constant.AHK_EXE)
            f.write("\n")

        elif Type == "sleep":
            f.write("Sleep, 1000\n")

        elif Type == "sendEnter":
            # f.write("WinActivate\nSleep, 2\n")
            # f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_SET_TEXT + variable + "," + str(check) + Constant.AHK_EXE)
            f.write("Sleep, 1000\n")
            f.write("Send, {Enter}\nSleep, 2\n")

        elif Type == "justSendEnter":
            f.write("Send, {Enter}\nSleep, 2\n")

        elif Type == "lastEntry":
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CLICK + variable + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_SET_TEXT + variable + "," + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CLICK + variable + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_SEND + variable + ", {Home}+{End}" + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_EDIT_PASTE + str(
                check) + "," + variable + Constant.AHK_EXE)
            f.write("\n")

            # f.write("WinActivate\nSleep, 2\n")
            # f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_SET_TEXT + variable + "," + str(check) + Constant.AHK_EXE)
            f.write("Sleep, 1000\n")
            f.write("Send, {Enter}\nSleep, 2\n")
            # f.write("Sleep, 1000\n")


        elif Type == "variabilityDropDown":
            f.write(Constant.CONTROL_FOCUS + Constant.headerToClassNN[layer] + Constant.AHK_EXE)
            f.write(Constant.CONTROL_CLICK + Constant.headerToClassNN[layer] + Constant.AHK_EXE)
            f.write("WinActivate\nSleep, 2\n")
            f.write("Sleep, 1000\n")
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_FOCUS + variable + Constant.AHK_EXE)
            f.write(Constant.SET_CONTROL_DELAY + Constant.CONTROL_CHOOSE + check + "," + variable + Constant.AHK_EXE)
            f.write("\n")

        f.close()

    def readFile(self, filename=Config.DATA_PATH + r"\auto.ahk"):
        f = open(filename, "r")
        ahk_script = f.read()
        # print(ahk_script)
        f.close()
        return ahk_script

    def clearFile(self, filename=Config.DATA_PATH + r"\auto.ahk"):
        f = open(filename, "w+")
        f.truncate(0)
        f.close()

    def readOutputFile(self):
        self.f = open(Config.DATA_PATH + r"\output.txt", "w+")
        out = self.f.readline()
        # f.close()
        return out

    # def closeOutputFile(self):
    #     self.f.close()
