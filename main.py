# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from gui import Ui_MainWindow
from analitical import Analitical
from diffscheme import Implicit
import numpy as np


import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.analitical = Analitical()
        self.implicit = Implicit()

        self.ui.doubleSpinBoxR.setValue(self.implicit.R)
        self.ui.doubleSpinBoxk.setValue(self.implicit.k)
        self.ui.doubleSpinBoxC.setValue(self.implicit.c)
        self.ui.doubleSpinBoxT.setValue(self.implicit.T)
        self.ui.spinBoxI.setValue(self.implicit.I)
        self.ui.spinBoxK.setValue(self.implicit.K)

        self.ui.pushButton.clicked.connect(lambda: self.update_graph())


    def update_graph(self):


        self.implicit.R = self.ui.doubleSpinBoxR.value()
        self.implicit.k = self.ui.doubleSpinBoxk.value()
        self.implicit.c = self.ui.doubleSpinBoxC.value()
        self.implicit.T = self.ui.doubleSpinBoxT.value()
        self.implicit.I = self.ui.spinBoxI.value()
        self.implicit.K = self.ui.spinBoxK.value()

        self.analitical.R = self.ui.doubleSpinBoxR.value()
        self.analitical.k = self.ui.doubleSpinBoxk.value()
        self.analitical.c = self.ui.doubleSpinBoxC.value()
        self.analitical.T = self.ui.doubleSpinBoxT.value()

        self.implicit.createModel()

        implX = np.linspace(0, np.pi / 2, self.implicit.I + 1)
        analX = np.linspace(0, np.pi / 2, 200)

        impY = self.implicit.getModel()
        analY = self.analitical.getAnalitical(analX)

        penimp = QtGui.QPen()
        penimp.setColor(QtGui.QColor(0, 0, 255))
        penimp.setWidth(.1)

        penana = QtGui.QPen()
        penana.setColor(QtGui.QColor(255, 0, 0))
        penana.setWidth(.1)

        self.ui.graphicsView.clear()
        self.ui.graphicsView.plotItem.plot(analX, analY, pen=penana)
        self.ui.graphicsView.plotItem.plot(implX, impY, pen=penimp)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())