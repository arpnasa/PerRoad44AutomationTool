import os
import sys

import autopy

from Configuration import Constant


class ResetToDefault:
    def closeSoftware(self, ahk):
        os.system("TASKKILL /F /IM PerRoad44.exe")
