# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import CarController


class Ui_Main(object):
    FUNCTION_GENERATOR_RESOURCE_NAME = 'GPIB0::8::INSTR'
    controller = CarController.CarController(FUNCTION_GENERATOR_RESOURCE_NAME)

    def __init__(self):
        self.check_change = True

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(411, 600)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_program = QtWidgets.QWidget()
        self.tab_program.setObjectName("tab_program")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_program)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_program)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnGo = QtWidgets.QPushButton(self.tab_program)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGo.sizePolicy().hasHeightForWidth())
        self.btnGo.setSizePolicy(sizePolicy)
        self.btnGo.setObjectName("btnGo")
        self.horizontalLayout_2.addWidget(self.btnGo)
        self.btnExit = QtWidgets.QPushButton(self.tab_program)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout_2.addWidget(self.btnExit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_program, "")
        self.tab_remote = QtWidgets.QWidget()
        self.tab_remote.setObjectName("tab_remote")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_remote)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnForwardLeft = QtWidgets.QPushButton(self.tab_remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnForwardLeft.sizePolicy().hasHeightForWidth())
        self.btnForwardLeft.setSizePolicy(sizePolicy)
        self.btnForwardLeft.setObjectName("btnForwardLeft")
        self.gridLayout.addWidget(self.btnForwardLeft, 0, 0, 1, 1)
        self.btnBackwardLeft = QtWidgets.QPushButton(self.tab_remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBackwardLeft.sizePolicy().hasHeightForWidth())
        self.btnBackwardLeft.setSizePolicy(sizePolicy)
        self.btnBackwardLeft.setObjectName("btnBackwardLeft")
        self.gridLayout.addWidget(self.btnBackwardLeft, 2, 0, 1, 1)
        self.btnForward = QtWidgets.QPushButton(self.tab_remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnForward.sizePolicy().hasHeightForWidth())
        self.btnForward.setSizePolicy(sizePolicy)
        self.btnForward.setObjectName("btnForward")
        self.gridLayout.addWidget(self.btnForward, 0, 1, 1, 1)
        self.btnForwardRight = QtWidgets.QPushButton(self.tab_remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnForwardRight.sizePolicy().hasHeightForWidth())
        self.btnForwardRight.setSizePolicy(sizePolicy)
        self.btnForwardRight.setObjectName("btnForwardRight")
        self.gridLayout.addWidget(self.btnForwardRight, 0, 2, 1, 1)
        self.btnStop = QtWidgets.QPushButton(self.tab_remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStop.sizePolicy().hasHeightForWidth())
        self.btnStop.setSizePolicy(sizePolicy)
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 1, 1, 1, 1)
        self.btnBackward = QtWidgets.QPushButton(self.tab_remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBackward.sizePolicy().hasHeightForWidth())
        self.btnBackward.setSizePolicy(sizePolicy)
        self.btnBackward.setObjectName("btnBackward")
        self.gridLayout.addWidget(self.btnBackward, 2, 1, 1, 1)
        self.btnBackwardRight = QtWidgets.QPushButton(self.tab_remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBackwardRight.sizePolicy().hasHeightForWidth())
        self.btnBackwardRight.setSizePolicy(sizePolicy)
        self.btnBackwardRight.setObjectName("btnBackwardRight")
        self.gridLayout.addWidget(self.btnBackwardRight, 2, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_remote, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout.setStretch(0, 8)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Remote Car Controller"))
        self.btnGo.setText(_translate("Main", "GO"))
        self.btnExit.setText(_translate("Main", "EXIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_program), _translate("Main", "Program"))
        self.btnForwardLeft.setText(_translate("Main", "FORWARD/LEFT (34)"))
        self.btnBackwardLeft.setText(_translate("Main", "BACKWARD/LEFT (46)"))
        self.btnForward.setText(_translate("Main", "FORWARD (10)"))
        self.btnForwardRight.setText(_translate("Main", "FORWARD/RIGHT (28)"))
        self.btnStop.setText(_translate("Main", "STOP (4)"))
        self.btnBackward.setText(_translate("Main", "BACKWARD (40)"))
        self.btnBackwardRight.setText(_translate("Main", "BACKWARD/RIGHT (52)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_remote), _translate("Main", "Remote"))

        col_headers = ['Code #', 'Direction', 'Time (Seconds)']
        self.tableWidget.setHorizontalHeaderLabels(col_headers)
        self.tableWidget.cellChanged.connect(self.table_cell_changed)
        self.btnGo.clicked.connect(self.go)
        self.btnExit.clicked.connect(self.exit)
        self.statusbar.showMessage('Ready')

        self.btnForwardLeft.pressed.connect(lambda: self.on_press(self.controller.FORWARD_LEFT_PULSE_COUNT))
        self.btnForwardLeft.released.connect(self.on_release)
        self.btnForward.pressed.connect(lambda: self.on_press(self.controller.FORWARD_PULSE_COUNT))
        self.btnForward.released.connect(self.on_release)
        self.btnForwardRight.pressed.connect(lambda: self.on_press(self.controller.FORWARD_RIGHT_PULSE_COUNT))
        self.btnForwardRight.released.connect(self.on_release)
        self.btnBackwardLeft.pressed.connect(lambda: self.on_press(self.controller.BACKWARD_LEFT_PULSE_COUNT))
        self.btnBackwardLeft.released.connect(self.on_release)
        self.btnBackward.pressed.connect(lambda: self.on_press(self.controller.BACKWARD_PULSE_COUNT))
        self.btnBackward.released.connect(self.on_release)
        self.btnBackwardRight.pressed.connect(lambda: self.on_press(self.controller.BACKWARD_RIGHT_PULSE_COUNT))
        self.btnBackwardRight.released.connect(self.on_release)
        self.btnStop.pressed.connect(lambda: self.on_press(self.controller.STOP_PULSE_COUNT))
        self.btnStop.released.connect(self.on_release)

    def table_cell_changed(self):
        if self.check_change:
            row = self.tableWidget.currentRow()
            column = self.tableWidget.currentColumn()

            # Get code number from first column and get the code description
            if (column == 0) and (self.tableWidget.currentItem() is not None):
                self.check_change = False
                code_num = self.tableWidget.currentItem().text()
                if (str(code_num).strip() != ''):
                    code_description = self.controller.lookup_code_description(int(code_num))

                    # Fill second column with code description
                    item = QTableWidgetItem(code_description)
                    self.tableWidget.setItem(row, 1, item)

                    if (code_description == self.controller.INVALID_CODE_DESCRIPTION):
                        self.tableWidget.item(row, 1).setBackground(QtGui.QColor(255, 102, 102))  # Red

                self.check_change = True

    def exit(self):
        sys.exit(app.exec_())

    def go(self):
        self.StatusBar = self.statusbar

        # Loop through each row
        #   - Get code number from first column (column 0)
        #   - Get code description from second column (column 1)
        #   - Get time from third column (column 2)
        for row in range(self.tableWidget.rowCount()):
            code_number = self.tableWidget.item(row, 0)
            duration = self.tableWidget.item(row, 2)
            if (code_number is not None) and (duration is not None):
                if (str(code_number.text()).strip() != '') and (str(duration.text()).strip() != ''):
                    code_description = self.controller.lookup_code_description(int(code_number.text()))
                    if (code_description != self.controller.INVALID_CODE_DESCRIPTION):
                        self.set_table_row_background_color(row, QtGui.QColor(255, 255, 153))  # Yellow
                        self.StatusBar.showMessage('Sending ' + code_description + ' (' + duration.text() + ' sec)...')
                        self.StatusBar.repaint()
                        self.controller.move(int(code_number.text()), int(duration.text()))
                        self.set_table_row_background_color(row, QtGui.QColor(153, 255, 153))  # Green

        self.StatusBar.showMessage('Ready')

    def set_table_row_background_color(self, row_number, color):
        self.tableWidget.item(row_number, 0).setBackground(color)
        self.tableWidget.item(row_number, 1).setBackground(color)
        self.tableWidget.item(row_number, 2).setBackground(color)

    def on_press(self, directionpulsecount):
        self.controller.move(directionpulsecount)

    def on_release(self):
        self.controller.stop()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

