import autopy

class InputHandler:
    def loadStructuralInput(self, ahk):
        # select the input tab to input structure details
        winStructInputTab = ahk.find_window(title=b'PerRoad 4.4')
        winStructInputTab.send(autopy.key.tap(autopy.key.Code.F1))
        ahk.run_script('SetWinDelay, 10')
        ahk.run_script('SetWinDelay, 1000')

    def loadSpectraInput(self, ahk):
        # select the input tab to input structure details
        winSpectraInputTab = ahk.find_window(title=b'PerRoad 4.4')
        winSpectraInputTab.send(autopy.key.tap(autopy.key.Code.F2))
        ahk.run_script('SetWinDelay, 10')