# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\References\MBFileRefAdvanced\ReferencingSampleUI2.ui'
#
# Created: Mon Feb 05 16:05:15 2018
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ReferencingSample(object):
    def setupUi(self, ReferencingSample):
        ReferencingSample.setObjectName("ReferencingSample")
        ReferencingSample.resize(853, 653)
        self.verticalLayout = QtGui.QVBoxLayout(ReferencingSample)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ReferencingSample)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiEditFilePath = QtGui.QLineEdit(self.groupBox)
        self.uiEditFilePath.setObjectName("uiEditFilePath")
        self.horizontalLayout.addWidget(self.uiEditFilePath)
        self.uiBtnBrowsePath = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiBtnBrowsePath.sizePolicy().hasHeightForWidth())
        self.uiBtnBrowsePath.setSizePolicy(sizePolicy)
        self.uiBtnBrowsePath.setMaximumSize(QtCore.QSize(23, 16777215))
        self.uiBtnBrowsePath.setAutoDefault(False)
        self.uiBtnBrowsePath.setObjectName("uiBtnBrowsePath")
        self.horizontalLayout.addWidget(self.uiBtnBrowsePath)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.uiSpinLoadTimes = QtGui.QSpinBox(self.groupBox)
        self.uiSpinLoadTimes.setEnabled(False)
        self.uiSpinLoadTimes.setMinimum(1)
        self.uiSpinLoadTimes.setMaximum(999)
        self.uiSpinLoadTimes.setProperty("value", 1)
        self.uiSpinLoadTimes.setObjectName("uiSpinLoadTimes")
        self.horizontalLayout.addWidget(self.uiSpinLoadTimes)
        self.uiBtnLoad = QtGui.QPushButton(self.groupBox)
        self.uiBtnLoad.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiBtnLoad.sizePolicy().hasHeightForWidth())
        self.uiBtnLoad.setSizePolicy(sizePolicy)
        self.uiBtnLoad.setMaximumSize(QtCore.QSize(50, 16777215))
        self.uiBtnLoad.setObjectName("uiBtnLoad")
        self.horizontalLayout.addWidget(self.uiBtnLoad)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ReferencingSample)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiTableNamespace = QtGui.QTableView(self.groupBox_2)
        self.uiTableNamespace.setMinimumSize(QtCore.QSize(400, 0))
        self.uiTableNamespace.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.uiTableNamespace.setTabKeyNavigation(False)
        self.uiTableNamespace.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.uiTableNamespace.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.uiTableNamespace.setObjectName("uiTableNamespace")
        self.uiTableNamespace.horizontalHeader().setHighlightSections(False)
        self.uiTableNamespace.horizontalHeader().setSortIndicatorShown(False)
        self.uiTableNamespace.horizontalHeader().setStretchLastSection(True)
        self.uiTableNamespace.verticalHeader().setVisible(True)
        self.uiTableNamespace.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_3.addWidget(self.uiTableNamespace)
        self.uiTreeNamespace = QtGui.QTreeWidget(self.groupBox_2)
        self.uiTreeNamespace.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.uiTreeNamespace.setAlternatingRowColors(True)
        self.uiTreeNamespace.setObjectName("uiTreeNamespace")
        self.uiTreeNamespace.header().setCascadingSectionResizes(False)
        self.uiTreeNamespace.header().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.uiTreeNamespace)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiBtnUnload = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiBtnUnload.sizePolicy().hasHeightForWidth())
        self.uiBtnUnload.setSizePolicy(sizePolicy)
        self.uiBtnUnload.setMinimumSize(QtCore.QSize(130, 0))
        self.uiBtnUnload.setMaximumSize(QtCore.QSize(130, 16777215))
        self.uiBtnUnload.setCheckable(False)
        self.uiBtnUnload.setObjectName("uiBtnUnload")
        self.verticalLayout_2.addWidget(self.uiBtnUnload)
        self.uiBtnReload = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiBtnReload.sizePolicy().hasHeightForWidth())
        self.uiBtnReload.setSizePolicy(sizePolicy)
        self.uiBtnReload.setMinimumSize(QtCore.QSize(130, 0))
        self.uiBtnReload.setMaximumSize(QtCore.QSize(130, 16777215))
        self.uiBtnReload.setCheckable(False)
        self.uiBtnReload.setObjectName("uiBtnReload")
        self.verticalLayout_2.addWidget(self.uiBtnReload)
        self.uiBtnDelete = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiBtnDelete.sizePolicy().hasHeightForWidth())
        self.uiBtnDelete.setSizePolicy(sizePolicy)
        self.uiBtnDelete.setMinimumSize(QtCore.QSize(130, 0))
        self.uiBtnDelete.setMaximumSize(QtCore.QSize(130, 16777215))
        self.uiBtnDelete.setCheckable(False)
        self.uiBtnDelete.setObjectName("uiBtnDelete")
        self.verticalLayout_2.addWidget(self.uiBtnDelete)
        spacerItem1 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.line = QtGui.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem2 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiSpinInstanceTimes = QtGui.QSpinBox(self.groupBox_3)
        self.uiSpinInstanceTimes.setMinimum(1)
        self.uiSpinInstanceTimes.setMaximum(999)
        self.uiSpinInstanceTimes.setProperty("value", 1)
        self.uiSpinInstanceTimes.setObjectName("uiSpinInstanceTimes")
        self.horizontalLayout_2.addWidget(self.uiSpinInstanceTimes)
        self.uiBtnInstance = QtGui.QPushButton(self.groupBox_3)
        self.uiBtnInstance.setObjectName("uiBtnInstance")
        self.horizontalLayout_2.addWidget(self.uiBtnInstance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.line_3 = QtGui.QFrame(self.groupBox_3)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        spacerItem4 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.uiBtnRestore = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiBtnRestore.sizePolicy().hasHeightForWidth())
        self.uiBtnRestore.setSizePolicy(sizePolicy)
        self.uiBtnRestore.setMinimumSize(QtCore.QSize(130, 0))
        self.uiBtnRestore.setMaximumSize(QtCore.QSize(120, 16777215))
        self.uiBtnRestore.setCheckable(False)
        self.uiBtnRestore.setObjectName("uiBtnRestore")
        self.verticalLayout_2.addWidget(self.uiBtnRestore)
        spacerItem5 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.uiBtnRestoreShaders = QtGui.QPushButton(self.groupBox_3)
        self.uiBtnRestoreShaders.setObjectName("uiBtnRestoreShaders")
        self.verticalLayout_2.addWidget(self.uiBtnRestoreShaders)
        spacerItem6 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.uiBtnBakeShaders = QtGui.QPushButton(self.groupBox_3)
        self.uiBtnBakeShaders.setObjectName("uiBtnBakeShaders")
        self.verticalLayout_2.addWidget(self.uiBtnBakeShaders)
        spacerItem7 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem7)
        self.line_2 = QtGui.QFrame(self.groupBox_3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        spacerItem8 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.uiBtnShowEdits = QtGui.QPushButton(self.groupBox_3)
        self.uiBtnShowEdits.setCheckable(False)
        self.uiBtnShowEdits.setObjectName("uiBtnShowEdits")
        self.verticalLayout_2.addWidget(self.uiBtnShowEdits)
        spacerItem9 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem9)
        self.uiBtnShowShadersEdits = QtGui.QPushButton(self.groupBox_3)
        self.uiBtnShowShadersEdits.setObjectName("uiBtnShowShadersEdits")
        self.verticalLayout_2.addWidget(self.uiBtnShowShadersEdits)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(ReferencingSample)
        QtCore.QObject.connect(self.uiBtnBrowsePath, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnBrowsePathClicked)
        QtCore.QObject.connect(self.uiBtnLoad, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnLoadClicked)
        QtCore.QObject.connect(self.uiBtnUnload, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnUnloadClicked)
        QtCore.QObject.connect(self.uiBtnReload, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnReloadClicked)
        QtCore.QObject.connect(self.uiBtnDelete, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnDeleteClicked)
        QtCore.QObject.connect(self.uiBtnInstance, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnInstanceClicked)
        QtCore.QObject.connect(self.uiBtnRestore, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnRestoreClicked)
        QtCore.QObject.connect(self.uiBtnShowEdits, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnShowEditsClicked)
        QtCore.QObject.connect(self.uiBtnShowShadersEdits, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnShowShaderEditsClicked)
        QtCore.QObject.connect(self.uiBtnRestoreShaders, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnShaderRestoreClicked)
        QtCore.QObject.connect(self.uiBtnBakeShaders, QtCore.SIGNAL("clicked()"), ReferencingSample.OnBtnShaderBakeClicked)
        QtCore.QMetaObject.connectSlotsByName(ReferencingSample)

    def retranslateUi(self, ReferencingSample):
        ReferencingSample.setWindowTitle(QtGui.QApplication.translate("ReferencingSample", "Referencing Sample", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ReferencingSample", "Reference a File", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnBrowsePath.setText(QtGui.QApplication.translate("ReferencingSample", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnLoad.setText(QtGui.QApplication.translate("ReferencingSample", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ReferencingSample", "Namespaces", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTreeNamespace.headerItem().setText(0, QtGui.QApplication.translate("ReferencingSample", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.uiTreeNamespace.headerItem().setText(1, QtGui.QApplication.translate("ReferencingSample", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnUnload.setText(QtGui.QApplication.translate("ReferencingSample", "Unload", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnReload.setText(QtGui.QApplication.translate("ReferencingSample", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnDelete.setText(QtGui.QApplication.translate("ReferencingSample", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnInstance.setText(QtGui.QApplication.translate("ReferencingSample", "Instance", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnRestore.setText(QtGui.QApplication.translate("ReferencingSample", "Restore to load state", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnRestoreShaders.setText(QtGui.QApplication.translate("ReferencingSample", "Restore a Shader Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnBakeShaders.setText(QtGui.QApplication.translate("ReferencingSample", "Bake a Shader Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnShowEdits.setText(QtGui.QApplication.translate("ReferencingSample", "Show Edits in Popup", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBtnShowShadersEdits.setText(QtGui.QApplication.translate("ReferencingSample", "Shader Edits in Popup", None, QtGui.QApplication.UnicodeUTF8))