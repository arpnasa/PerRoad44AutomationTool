from ahk import AHK
from Scripts.InputHandler import InputHandler
from Scripts.OutputHandler import OutputHandler

import pandas as pd

class PerRoad44:
    def __init__(self):
        self.ahk = AHK()

    def runPerRoad44(self):
        self.ahk.run_script('Run D:\Software\PerRoad\PerRoad44')

    def readInputFile(self):
        d = pd.read_excel(r'D:\Prog\PyCharm\Anurag\PerRoad44AutomationTool\Data\input.xlsx')
        print(d)

if __name__ == '__main__':
    pp = PerRoad44()
    # pp.runPerRoad44()
    ip = InputHandler()
    op = OutputHandler()
    # ip.loadStructuralInput(pp.ahk)
    # ip.loadSpectraInput(pp.ahk)
    # op.downlaodOutput(pp.ahk)
    pp.readInputFile()