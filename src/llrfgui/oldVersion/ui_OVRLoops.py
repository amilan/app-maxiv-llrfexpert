# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OVRLoops.ui'
#
# Created by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(216, 224)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self._22 = QtGui.QGridLayout()
        self._22.setSpacing(0)
        self._22.setObjectName(_fromUtf8("_22"))
        self.label_152 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_152.sizePolicy().hasHeightForWidth())
        self.label_152.setSizePolicy(sizePolicy)
        self.label_152.setMinimumSize(QtCore.QSize(100, 20))
        self.label_152.setMaximumSize(QtCore.QSize(93, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_152.setFont(font)
        self.label_152.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_152.setObjectName(_fromUtf8("label_152"))
        self._22.addWidget(self.label_152, 0, 0, 1, 1)
        self.taurusBoolLed = TaurusBoolLed(Form)
        self.taurusBoolLed.setObjectName(_fromUtf8("taurusBoolLed"))
        self._22.addWidget(self.taurusBoolLed, 0, 1, 1, 1)
        self.label_153 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_153.sizePolicy().hasHeightForWidth())
        self.label_153.setSizePolicy(sizePolicy)
        self.label_153.setMinimumSize(QtCore.QSize(100, 20))
        self.label_153.setMaximumSize(QtCore.QSize(93, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_153.setFont(font)
        self.label_153.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_153.setObjectName(_fromUtf8("label_153"))
        self._22.addWidget(self.label_153, 1, 0, 1, 1)
        self.taurusBoolLed_2 = TaurusBoolLed(Form)
        self.taurusBoolLed_2.setObjectName(_fromUtf8("taurusBoolLed_2"))
        self._22.addWidget(self.taurusBoolLed_2, 1, 1, 1, 1)
        self.label_147 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy)
        self.label_147.setMinimumSize(QtCore.QSize(100, 20))
        self.label_147.setMaximumSize(QtCore.QSize(93, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_147.setFont(font)
        self.label_147.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_147.setObjectName(_fromUtf8("label_147"))
        self._22.addWidget(self.label_147, 2, 0, 1, 1)
        self.taurusBoolLed_3 = TaurusBoolLed(Form)
        self.taurusBoolLed_3.setObjectName(_fromUtf8("taurusBoolLed_3"))
        self._22.addWidget(self.taurusBoolLed_3, 2, 1, 1, 1)
        self.label_148 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_148.sizePolicy().hasHeightForWidth())
        self.label_148.setSizePolicy(sizePolicy)
        self.label_148.setMinimumSize(QtCore.QSize(100, 20))
        self.label_148.setMaximumSize(QtCore.QSize(93, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_148.setFont(font)
        self.label_148.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_148.setObjectName(_fromUtf8("label_148"))
        self._22.addWidget(self.label_148, 3, 0, 1, 1)
        self.taurusBoolLed_4 = TaurusBoolLed(Form)
        self.taurusBoolLed_4.setObjectName(_fromUtf8("taurusBoolLed_4"))
        self._22.addWidget(self.taurusBoolLed_4, 3, 1, 1, 1)
        self.label_149 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_149.sizePolicy().hasHeightForWidth())
        self.label_149.setSizePolicy(sizePolicy)
        self.label_149.setMinimumSize(QtCore.QSize(100, 20))
        self.label_149.setMaximumSize(QtCore.QSize(93, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_149.setFont(font)
        self.label_149.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_149.setObjectName(_fromUtf8("label_149"))
        self._22.addWidget(self.label_149, 4, 0, 1, 1)
        self.taurusBoolLed_5 = TaurusBoolLed(Form)
        self.taurusBoolLed_5.setObjectName(_fromUtf8("taurusBoolLed_5"))
        self._22.addWidget(self.taurusBoolLed_5, 4, 1, 1, 1)
        self.label_150 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy)
        self.label_150.setMinimumSize(QtCore.QSize(100, 20))
        self.label_150.setMaximumSize(QtCore.QSize(93, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_150.setFont(font)
        self.label_150.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_150.setObjectName(_fromUtf8("label_150"))
        self._22.addWidget(self.label_150, 5, 0, 1, 1)
        self.taurusBoolLed_6 = TaurusBoolLed(Form)
        self.taurusBoolLed_6.setObjectName(_fromUtf8("taurusBoolLed_6"))
        self._22.addWidget(self.taurusBoolLed_6, 5, 1, 1, 1)
        self.label_156 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy)
        self.label_156.setMinimumSize(QtCore.QSize(100, 20))
        self.label_156.setMaximumSize(QtCore.QSize(93, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_156.setFont(font)
        self.label_156.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_156.setObjectName(_fromUtf8("label_156"))
        self._22.addWidget(self.label_156, 7, 0, 1, 1)
        self.taurusBoolLed_8 = TaurusBoolLed(Form)
        self.taurusBoolLed_8.setObjectName(_fromUtf8("taurusBoolLed_8"))
        self._22.addWidget(self.taurusBoolLed_8, 7, 1, 1, 1)
        self.label_142 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy)
        self.label_142.setMinimumSize(QtCore.QSize(100, 20))
        self.label_142.setMaximumSize(QtCore.QSize(93, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_142.setFont(font)
        self.label_142.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_142.setObjectName(_fromUtf8("label_142"))
        self._22.addWidget(self.label_142, 6, 0, 1, 1)
        self.taurusBoolLed_7 = TaurusBoolLed(Form)
        self.taurusBoolLed_7.setObjectName(_fromUtf8("taurusBoolLed_7"))
        self._22.addWidget(self.taurusBoolLed_7, 6, 1, 1, 1)
        self.gridLayout.addLayout(self._22, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_152.setText(QtGui.QApplication.translate("Form", "ADC1: CavA", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed.setProperty(_fromUtf8("ledColor"), QtGui.QApplication.translate("Form", "RED", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed.setProperty(_fromUtf8("ledColorOff"), QtGui.QApplication.translate("Form", "REDOFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_153.setText(QtGui.QApplication.translate("Form", "ADC2: Fw CavA", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_2.setProperty(_fromUtf8("ledColor"), QtGui.QApplication.translate("Form", "RED", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_2.setProperty(_fromUtf8("ledColorOff"), QtGui.QApplication.translate("Form", "REDOFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_147.setText(QtGui.QApplication.translate("Form", "ADC3: FwTet1A", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_3.setProperty(_fromUtf8("ledColor"), QtGui.QApplication.translate("Form", "RED", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_3.setProperty(_fromUtf8("ledColorOff"), QtGui.QApplication.translate("Form", "REDOFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_148.setText(QtGui.QApplication.translate("Form", "ADC4: FwTet2A", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_4.setProperty(_fromUtf8("ledColor"), QtGui.QApplication.translate("Form", "RED", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_4.setProperty(_fromUtf8("ledColorOff"), QtGui.QApplication.translate("Form", "REDOFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_149.setText(QtGui.QApplication.translate("Form", "ADC5: CavB", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_5.setProperty(_fromUtf8("ledColor"), QtGui.QApplication.translate("Form", "RED", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_5.setProperty(_fromUtf8("ledColorOff"), QtGui.QApplication.translate("Form", "REDOFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_150.setText(QtGui.QApplication.translate("Form", "ADC6: FwCavB", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_6.setProperty(_fromUtf8("ledColor"), QtGui.QApplication.translate("Form", "RED", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_6.setProperty(_fromUtf8("ledColorOff"), QtGui.QApplication.translate("Form", "REDOFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_156.setText(QtGui.QApplication.translate("Form", "ADC8: FwTet2B", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_8.setProperty(_fromUtf8("ledColor"), QtGui.QApplication.translate("Form", "RED", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_8.setProperty(_fromUtf8("ledColorOff"), QtGui.QApplication.translate("Form", "REDOFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_142.setText(QtGui.QApplication.translate("Form", "ADC7: FwTet1B", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_7.setProperty(_fromUtf8("ledColor"), QtGui.QApplication.translate("Form", "RED", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusBoolLed_7.setProperty(_fromUtf8("ledColorOff"), QtGui.QApplication.translate("Form", "REDOFF", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusBoolLed

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
