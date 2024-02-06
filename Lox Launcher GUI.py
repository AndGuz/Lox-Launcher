from UX_ONLY.MainUX import *
import minecraft_launcher_lib as mclib
from pathlib import Path

import sys
app = QtWidgets.QApplication(sys.argv)
LoxLauncher = QtWidgets.QMainWindow()
ui = Ui_LoxLauncher()
ui.setupUi(LoxLauncher)
LoxLauncher.show()
sys.exit(app.exec_())