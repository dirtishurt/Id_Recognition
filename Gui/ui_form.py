# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

from Camera import Camera
from Github import Github

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(True)
        MainWindow.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionRemove = QAction(MainWindow)
        self.actionRemove.setObjectName(u"actionRemove")
        self.actionWhy = QAction(MainWindow)
        self.actionWhy.setObjectName(u"actionWhy")
        self.actionDo = QAction(MainWindow)
        self.actionDo.setObjectName(u"actionDo")
        self.actionI = QAction(MainWindow)
        self.actionI.setObjectName(u"actionI")
        self.actionHate = QAction(MainWindow)
        self.actionHate.setObjectName(u"actionHate")
        self.actionMyself = QAction(MainWindow)
        self.actionMyself.setObjectName(u"actionMyself")
        self.action_Yes = QAction(MainWindow)
        self.action_Yes.setObjectName(u"action_Yes")
        self.action_Yes_2 = QAction(MainWindow)
        self.action_Yes_2.setObjectName(u"action_Yes_2")
        self.action_New = QAction(MainWindow)
        self.action_New.setObjectName(u"action_New")
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        self.action_Remove = QAction(MainWindow)
        self.action_Remove.setObjectName(u"action_Remove")
        self.actionChange_Camera = QAction(MainWindow)
        self.actionChange_Camera.setObjectName(u"actionChange_Camera")
        self.actionRemove_2 = QAction(MainWindow)
        self.actionRemove_2.setObjectName(u"actionRemove_2")
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        self.actionSelect = QAction(MainWindow)
        self.actionSelect.setObjectName(u"actionSelect")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionAdd_2 = QAction(MainWindow)
        self.actionAdd_2.setObjectName(u"actionAdd_2")
        self.actionHello = QAction(MainWindow)
        self.actionHello.setObjectName(u"actionHello")
        self.actionOpen_Annotator = QAction(MainWindow)
        self.actionOpen_Annotator.setObjectName(u"actionOpen_Annotator")
        self.actionSelect_Files = QAction(MainWindow)
        self.actionSelect_Files.setObjectName(u"actionSelect_Files")
        self.actionTrain_Model = QAction(MainWindow)
        self.actionTrain_Model.setObjectName(u"actionTrain_Model")
        self.actionTrain_Model_2 = QAction(MainWindow)
        self.actionTrain_Model_2.setObjectName(u"actionTrain_Model_2")
        self.actionFrom_Project_Directory = QAction(MainWindow)
        self.actionFrom_Project_Directory.setObjectName(u"actionFrom_Project_Directory")
        self.actionSelect_Project_Directory = QAction(MainWindow)
        self.actionSelect_Project_Directory.setObjectName(u"actionSelect_Project_Directory")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionOpen_ReadME = QAction(MainWindow)
        self.actionOpen_ReadME.setObjectName(u"actionOpen_ReadME")
        self.actionSelect_pt_File = QAction(MainWindow)
        self.actionSelect_pt_File.setObjectName(u"actionSelect_pt_File")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(600, 500))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setBaseSize(QSize(1600, 900))
        palette = QPalette()
        brush = QBrush(QColor(63, 63, 63, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.camer_output = Camera(self.centralwidget)
        self.camer_output.setObjectName(u"camer_output")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.camer_output.sizePolicy().hasHeightForWidth())
        self.camer_output.setSizePolicy(sizePolicy1)
        self.camer_output.setMinimumSize(QSize(640, 360))
        self.camer_output.setMaximumSize(QSize(2560, 1440))
        self.camer_output.setSizeIncrement(QSize(16, 9))
        self.camer_output.setBaseSize(QSize(16, 9))
        palette1 = QPalette()
        brush1 = QBrush(QColor(62, 180, 137, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.camer_output.setPalette(palette1)
        self.camer_output.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.camer_output)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confidence_slider = QSlider(self.centralwidget)
        self.confidence_slider.setObjectName(u"confidence_slider")
        self.confidence_slider.setMaximumSize(QSize(16777215, 20))
        palette2 = QPalette()
        brush2 = QBrush(QColor(70, 180, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        self.confidence_slider.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setKerning(True)
        self.confidence_slider.setFont(font1)
        self.confidence_slider.setMinimum(5)
        self.confidence_slider.setMaximum(95)
        self.confidence_slider.setSingleStep(5)
        self.confidence_slider.setPageStep(5)
        self.confidence_slider.setValue(5)
        self.confidence_slider.setOrientation(Qt.Orientation.Horizontal)
        self.confidence_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.confidence_slider.setTickInterval(5)

        self.horizontalLayout.addWidget(self.confidence_slider)

        self.confidence_percent = QLineEdit(self.centralwidget)
        self.confidence_percent.setObjectName(u"confidence_percent")
        self.confidence_percent.setMaximumSize(QSize(16777215, 20))
        self.confidence_percent.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.confidence_percent)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy2)
        self.listView.setMinimumSize(QSize(264, 0))

        self.gridLayout.addWidget(self.listView, 0, 0, 2, 2)

        self.end_button = QPushButton(self.centralwidget)
        self.end_button.setObjectName(u"end_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.end_button.sizePolicy().hasHeightForWidth())
        self.end_button.setSizePolicy(sizePolicy3)
        self.end_button.setMinimumSize(QSize(132, 20))
        self.end_button.setMaximumSize(QSize(132, 16777215))
        palette3 = QPalette()
        brush3 = QBrush(QColor(49, 49, 49, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        self.end_button.setPalette(palette3)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.end_button.setFont(font2)

        self.gridLayout.addWidget(self.end_button, 2, 0, 1, 1)

        self.run_button = QPushButton(self.centralwidget)
        self.run_button.setObjectName(u"run_button")
        sizePolicy3.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy3)
        self.run_button.setMinimumSize(QSize(132, 20))
        self.run_button.setMaximumSize(QSize(132, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        self.run_button.setPalette(palette4)
        self.run_button.setFont(font2)
        self.run_button.setAutoFillBackground(False)
        self.run_button.setAutoDefault(False)
        self.run_button.setFlat(False)

        self.gridLayout.addWidget(self.run_button, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 33))
        self.menubar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.menubar.setAutoFillBackground(True)
        self.menuwhere_is_the_box = QMenu(self.menubar)
        self.menuwhere_is_the_box.setObjectName(u"menuwhere_is_the_box")
        self.menuDatasets = QMenu(self.menubar)
        self.menuDatasets.setObjectName(u"menuDatasets")
        self.menuCreateModels = QMenu(self.menubar)
        self.menuCreateModels.setObjectName(u"menuCreateModels")
        self.menuGithub = Github(self.menubar)
        self.menuGithub.setObjectName(u"menuGithub")
        self.menuLoad_Model = QMenu(self.menubar)
        self.menuLoad_Model.setObjectName(u"menuLoad_Model")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuImport_Model = QMenu(self.menubar)
        self.menuImport_Model.setObjectName(u"menuImport_Model")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.confidence_slider, self.confidence_percent)

        self.menubar.addAction(self.menuwhere_is_the_box.menuAction())
        self.menubar.addAction(self.menuDatasets.menuAction())
        self.menubar.addAction(self.menuCreateModels.menuAction())
        self.menubar.addAction(self.menuImport_Model.menuAction())
        self.menubar.addAction(self.menuLoad_Model.menuAction())
        self.menubar.addAction(self.menuGithub.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuwhere_is_the_box.addAction(self.actionChange_Camera)
        self.menuDatasets.addAction(self.actionImport)
        self.menuCreateModels.addAction(self.actionOpen_Annotator)
        self.menuCreateModels.addAction(self.actionTrain_Model_2)
        self.menuLoad_Model.addAction(self.actionSelect_Project_Directory)
        self.menuHelp.addAction(self.actionOpen_ReadME)
        self.menuImport_Model.addAction(self.actionSelect_pt_File)

        self.retranslateUi(MainWindow)
        self.run_button.clicked.connect(self.camer_output.update)
        self.end_button.clicked.connect(self.camer_output.close)
        self.confidence_percent.textEdited.connect(self.confidence_slider.update)

        self.run_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.actionWhy.setText(QCoreApplication.translate("MainWindow", u"Why", None))
        self.actionDo.setText(QCoreApplication.translate("MainWindow", u"Do", None))
        self.actionI.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.actionHate.setText(QCoreApplication.translate("MainWindow", u"Hate", None))
        self.actionMyself.setText(QCoreApplication.translate("MainWindow", u"Myself", None))
        self.action_Yes.setText(QCoreApplication.translate("MainWindow", u"%Yes", None))
        self.action_Yes_2.setText(QCoreApplication.translate("MainWindow", u"&Yes", None))
        self.action_New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open", None))
        self.action_Remove.setText(QCoreApplication.translate("MainWindow", u"&Remove", None))
        self.actionChange_Camera.setText(QCoreApplication.translate("MainWindow", u"Change_Camera", None))
        self.actionRemove_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSelect.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionAdd_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionHello.setText(QCoreApplication.translate("MainWindow", u"Hello", None))
        self.actionOpen_Annotator.setText(QCoreApplication.translate("MainWindow", u"Open Annotator", None))
        self.actionSelect_Files.setText(QCoreApplication.translate("MainWindow", u"Select Files", None))
        self.actionTrain_Model.setText(QCoreApplication.translate("MainWindow", u"Train Model", None))
        self.actionTrain_Model_2.setText(QCoreApplication.translate("MainWindow", u"Train Model", None))
        self.actionFrom_Project_Directory.setText(QCoreApplication.translate("MainWindow", u"From Project Directory", None))
        self.actionSelect_Project_Directory.setText(QCoreApplication.translate("MainWindow", u"Select Project Directory", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionOpen_ReadME.setText(QCoreApplication.translate("MainWindow", u"Open ReadME", None))
        self.actionSelect_pt_File.setText(QCoreApplication.translate("MainWindow", u"Select .pt File", None))
        self.confidence_percent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confidence:", None))
        self.end_button.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.menuwhere_is_the_box.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuDatasets.setTitle(QCoreApplication.translate("MainWindow", u"Datasets", None))
        self.menuCreateModels.setTitle(QCoreApplication.translate("MainWindow", u"Create Model", None))
        self.menuGithub.setTitle(QCoreApplication.translate("MainWindow", u"Github", None))
        self.menuLoad_Model.setTitle(QCoreApplication.translate("MainWindow", u"Set Project Directory", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuImport_Model.setTitle(QCoreApplication.translate("MainWindow", u"Import Model", None))
    # retranslateUi

