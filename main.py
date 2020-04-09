# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from gui import Ui_MainWindow
from analitical import Analitical

#v0
from diffscheme import Implicit
#v1
from diffscheme import Explicit
#v2
from diffscheme import Expl

import numpy as np


import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.analitical = Analitical()
        #v0
        self.initImplicit()

        #v1
        self.initExplicit()

        #v2
        self.initExpl()

        self.ui.pushButton.clicked.connect(lambda: self.update_graph())

    #v0
    def initImplicit(self):
        self.implicit = Implicit()
        self.ui.doubleSpinBoxR.setValue(self.implicit.R)
        self.ui.doubleSpinBoxk.setValue(self.implicit.k)
        self.ui.doubleSpinBoxC.setValue(self.implicit.c)
        self.ui.doubleSpinBoxT.setValue(self.implicit.T)
        self.ui.spinBoxI.setValue(self.implicit.I)
        self.ui.spinBoxK.setValue(self.implicit.K)

    #v1
    def initExplicit(self):
        self.explicit = Explicit()
        self.ui.doubleSpinBoxR.setValue(self.explicit.R)
        self.ui.doubleSpinBoxk.setValue(self.explicit.k)
        self.ui.doubleSpinBoxC.setValue(self.explicit.c)
        self.ui.doubleSpinBoxT.setValue(self.explicit.T)
        self.ui.spinBoxI.setValue(self.explicit.I)
        self.ui.spinBoxK.setValue(self.explicit.K)

    #v2
    def initExpl(self):
        self.expl = Expl()
        self.ui.doubleSpinBoxR.setValue(self.expl.R)
        self.ui.doubleSpinBoxk.setValue(self.expl.k)
        self.ui.doubleSpinBoxC.setValue(self.expl.c)
        self.ui.doubleSpinBoxT.setValue(self.expl.T)
        self.ui.spinBoxI.setValue(self.expl.I)
        self.ui.spinBoxK.setValue(self.expl.K)

    #v0
    def updateImplicit(self):
        self.implicit.R = self.ui.doubleSpinBoxR.value()
        self.implicit.k = self.ui.doubleSpinBoxk.value()
        self.implicit.c = self.ui.doubleSpinBoxC.value()
        self.implicit.T = self.ui.doubleSpinBoxT.value()
        self.implicit.I = self.ui.spinBoxI.value()
        self.implicit.K = self.ui.spinBoxK.value()

        self.implicit.createModel()

        implX = np.linspace(0, np.pi / 2, self.implicit.I + 1)
        impY = self.implicit.getModel()
        self.ui.graphicsView.plotItem.plot(implX, impY, pen='b')

    #v1
    def updateExplicit(self):
        self.explicit.R = self.ui.doubleSpinBoxR.value()
        self.explicit.k = self.ui.doubleSpinBoxk.value()
        self.explicit.c = self.ui.doubleSpinBoxC.value()
        self.explicit.T = self.ui.doubleSpinBoxT.value()
        self.explicit.I = self.ui.spinBoxI.value()
        self.explicit.K = self.ui.spinBoxK.value()

        self.explicit.createModel()

        explX = np.linspace(0, np.pi / 2, self.explicit.I + 1)
        explY = self.explicit.getModel()

        self.ui.graphicsView.plotItem.plot(explX, explY, pen='b')

    #v2
    def updateExpl(self):
        self.expl.R = self.ui.doubleSpinBoxR.value()
        self.expl.k = self.ui.doubleSpinBoxk.value()
        self.expl.c = self.ui.doubleSpinBoxC.value()
        self.expl.T = self.ui.doubleSpinBoxT.value()
        self.expl.I = self.ui.spinBoxI.value()
        self.expl.K = self.ui.spinBoxK.value()

        self.expl.createModel()

        explX = np.linspace(0, np.pi / 2, self.expl.I + 1)
        explY = self.expl.getModel()

        self.ui.graphicsView.plotItem.plot(explX, explY, pen='b')

    def update_graph(self):

        self.analitical.R = self.ui.doubleSpinBoxR.value()
        self.analitical.k = self.ui.doubleSpinBoxk.value()
        self.analitical.c = self.ui.doubleSpinBoxC.value()
        self.analitical.T = self.ui.doubleSpinBoxT.value()

        analX = np.linspace(0, np.pi / 2, 200)
        analY = self.analitical.getAnalitical(analX)

        self.ui.graphicsView.clear()
        self.ui.graphicsView.plotItem.plot(analX, analY, pen='r')
        #v0
        self.updateImplicit()
        #v1
        #self.updateExplicit()
        #v2
        #self.updateExpl()
        self.ui.resultanal.setText("―")
        self.ui.resultch.setText("―")
        self.ui.resultanal.setStyleSheet("color: rgb(255, 0, 0);")
        self.ui.resultch.setStyleSheet("color: rgb(0, 0, 255);")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())