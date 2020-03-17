import time
import os

from ahk import AHK
from Scripts.StructuralInputHandler import StructuralInputHandler
from Scripts.SpectralInputHandler import SpectralInputHandler
from Scripts.OutputHandler import OutputHandler
from Configuration import Config
from Scripts.DatasetHandler import DataSetHandler
from Scripts.ResetToDefault import ResetToDefault

class PerRoad44:
    def __init__(self):
        self.ahk = AHK()

    def runPerRoad44(self):
        self.ahk.run_script('Run ' + Config.SOFTWARE_PATH)

if __name__ == '__main__':
    pp = PerRoad44()



    # define the InputHandler
    structIP = StructuralInputHandler()

    specIP = SpectralInputHandler()

    # define the OutputHandler
    op = OutputHandler()

    # define the DatasetHandler
    dh = DataSetHandler()

    # to reset the fields
    reset = ResetToDefault()

    # read the input file and store it in a Pandas dataframe
    d = dh.readInputFile()

    # clean the dataset
    data = dh.cleanDataset(d)


    for currInputSet in range(0,len(data)):
        time.sleep(2)

        # run the software
        pp.runPerRoad44()

        time.sleep(2)

        structIP.loadStructuralInput(pp.ahk, data.iloc[currInputSet])

        time.sleep(2)

        specIP.loadSpectraInput(pp.ahk, data.iloc[currInputSet])

        time.sleep(2)

        op.downlaodOutput(pp.ahk, data.iloc[currInputSet])

        time.sleep(2)

        reset.closeSoftware(pp.ahk)


    path = Config.OUTPUT_PATH[:-1]
    files = os.listdir(path)

    for index, file in enumerate(files):
        if '.' not in file:
            os.rename(os.path.join(path, file), os.path.join(path, ''.join([file, '.xlsx'])))