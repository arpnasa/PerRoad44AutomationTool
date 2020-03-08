import autopy

class OutputHandler:
    def downlaodOutput(self, ahk):
        # open the output tab
        winOutputTab = ahk.find_window(title=b'PerRoad 4.4')  # Find the opened window
        winOutputTab.send(autopy.key.tap(autopy.key.Code.F3))
        ahk.run_script('SetWinDelay, 10')

        # click on perform analysis
        winOutputSubTab = ahk.find_window_by_title(title=b'Output & Design Module')
        winOutputSubTab.send(autopy.key.tap(autopy.key.Code.F4))
        ahk.run_script('SetWinDelay, 10')

        # click ok
        winInfoTab = ahk.find_window_by_title(title=b'Please Note...')
        winInfoTab.send(autopy.key.tap(autopy.key.Code.F5))
        ahk.run_script('SetWinDelay, 10')

        # save the output file
        ahk.send_raw("$h123.xls",100)
        ahk.run_script('Send, {ENTER}')

        winOutputSubTab.close()