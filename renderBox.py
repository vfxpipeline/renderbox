"""
RenderBox

    Artificial Intelligence Render Assistant for Maya, Nuke and Houdini
    RenderBox  Copyright (C) 2021  RAJIV SHARMA

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

"""
from PySide2 import QtWidgets
from gui import renderboxUI

try:
    import pymel.core as pm
    import maya.cmds as cmds
except ImportError as Err:
    print(Err)


class RenderBoxMaya(renderboxUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(RenderBoxMaya, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    rbox = RenderBoxMaya()
    rbox.show()
    app.exec_()
