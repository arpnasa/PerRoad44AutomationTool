from collections import OrderedDict


from ahk import AHK
from Scripts.InputHandler import InputHandler
from Scripts.OutputHandler import OutputHandler
from Configuration import Config
from Scripts.DatasetHandler import DataSetHandler

import pandas as pd

class PerRoad44:
    def __init__(self):
        self.ahk = AHK()

    def runPerRoad44(self):
        self.ahk.run_script('Run ' + Config.SOFTWARE_PATH)

if __name__ == '__main__':
    pp = PerRoad44()

    # run the software
    pp.runPerRoad44()

    # define the InputHandler
    ip = InputHandler()

    # define the OutputHandler
    op = OutputHandler()

    # define the DatasetHandler
    dh = DataSetHandler()

    # read the input file and store it in a Pandas dataframe
    d = dh.readInputFile()

    # clean the dataset
    data = dh.cleanDataset(d)


    ip.loadStructuralInput(pp.ahk, data)
    # ip.loadSpectraInput(pp.ahk)
    # op.downlaodOutput(pp.ahk)

    # note: here the data is accessed by [col][row]
    row = len(data.axes[0])
    col = len(data.axes[1])

    # print(row, col)

    h = dh.header
    h = list(OrderedDict.fromkeys(h))
    # print(*h, sep='\n')

    # print(data["fall"])
    # print(data["winter"])
    # print(data["spring"])
    # print(data["spring 2"])

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(data)
    # print(data)
    # print(data['current season'])
    # print(data.columns)