# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form2.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QLineEdit, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTabWidget,
    QToolBar, QWidget)

from Annotator import Annotator
from Classes import Classes
from Draw import Draw
from Files import Files

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1045, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1045, 700))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(92, 131, 116, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(147, 177, 166, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush2 = QBrush(QColor(4, 13, 18, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(51, 72, 63, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        brush4 = QBrush(QColor(182, 182, 182, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush4)
        brush5 = QBrush(QColor(34, 34, 34, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush5)
        brush6 = QBrush(QColor(30, 31, 29, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        MainWindow.setPalette(palette)
        MainWindow.setMouseTracking(True)
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionBox = QAction(MainWindow)
        self.actionBox.setObjectName(u"actionBox")
        self.actionBox.setCheckable(True)
        self.actionBox.setChecked(False)
        self.actionBox.setEnabled(True)
        icon = QIcon()
        icon.addFile(u"bounding-box.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBox.setIcon(icon)
        self.actionBox.setShortcutContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
        self.actionBox.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.actionPolygonTool = QAction(MainWindow)
        self.actionPolygonTool.setObjectName(u"actionPolygonTool")
        self.actionPolygonTool.setCheckable(True)
        self.actionPolygonTool.setChecked(True)
        self.actionPolygonTool.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u"polygon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPolygonTool.setIcon(icon1)
        self.actionPolygonTool.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
        self.actionPolygonTool.setAutoRepeat(True)
        self.actionPolygonTool.setVisible(True)
        self.actionPolygonTool.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.actiondelete = QAction(MainWindow)
        self.actiondelete.setObjectName(u"actiondelete")
        self.actiondelete.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u"delete-icon-1864x2048-bp2i0gor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actiondelete.setIcon(icon2)
        self.actiondelete.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionUndo.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u"2349854.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon3)
        self.actionUndo.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.actionSelect_Directory = QAction(MainWindow)
        self.actionSelect_Directory.setObjectName(u"actionSelect_Directory")
        self.actionAdd_Directory = QAction(MainWindow)
        self.actionAdd_Directory.setObjectName(u"actionAdd_Directory")
        self.actionAdd_Files = QAction(MainWindow)
        self.actionAdd_Files.setObjectName(u"actionAdd_Files")
        self.actionSelect_Folder = QAction(MainWindow)
        self.actionSelect_Folder.setObjectName(u"actionSelect_Folder")
        self.actionProject_Directory = QAction(MainWindow)
        self.actionProject_Directory.setObjectName(u"actionProject_Directory")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_and_Return = QAction(MainWindow)
        self.actionSave_and_Return.setObjectName(u"actionSave_and_Return")
        self.actionFrom_Current_Annotations = QAction(MainWindow)
        self.actionFrom_Current_Annotations.setObjectName(u"actionFrom_Current_Annotations")
        self.actionToggle = QAction(MainWindow)
        self.actionToggle.setObjectName(u"actionToggle")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(16)
        sizePolicy1.setVerticalStretch(9)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(999, 640))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setSizeIncrement(QSize(16, 9))
        palette1 = QPalette()
        brush7 = QBrush(QColor(15, 38, 38, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        self.centralwidget.setPalette(palette1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMinimumSize(QSize(360, 46))
        self.lineEdit.setMaximumSize(QSize(400, 46))
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setFrame(False)
        self.lineEdit.setPlaceholderText(u"Input Class Name:")
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.New_Ann = QPushButton(self.centralwidget)
        self.New_Ann.setObjectName(u"New_Ann")
        sizePolicy2.setHeightForWidth(self.New_Ann.sizePolicy().hasHeightForWidth())
        self.New_Ann.setSizePolicy(sizePolicy2)
        self.New_Ann.setMinimumSize(QSize(360, 46))
        self.New_Ann.setMaximumSize(QSize(400, 46))
        self.New_Ann.setToolTipDuration(1000)
        self.New_Ann.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.New_Ann, 6, 0, 1, 1)

        self.Next = QPushButton(self.centralwidget)
        self.Next.setObjectName(u"Next")
        sizePolicy2.setHeightForWidth(self.Next.sizePolicy().hasHeightForWidth())
        self.Next.setSizePolicy(sizePolicy2)
        self.Next.setMinimumSize(QSize(360, 46))
        self.Next.setMaximumSize(QSize(400, 46))
        self.Next.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Next.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.Next, 4, 0, 1, 1)

        self.Files = Files(self.centralwidget)
        self.Files.setObjectName(u"Files")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Files.sizePolicy().hasHeightForWidth())
        self.Files.setSizePolicy(sizePolicy3)
        self.Files.setMinimumSize(QSize(360, 250))
        self.Files.setMaximumSize(QSize(400, 16777215))
        self.Files.setBaseSize(QSize(0, 0))
        self.Files.setMouseTracking(True)
        self.Files.setAcceptDrops(True)
        self.Files.setAutoFillBackground(True)
        self.Files.setFrameShadow(QFrame.Shadow.Sunken)
        self.Files.setTabKeyNavigation(True)
        self.Files.setAlternatingRowColors(True)
        self.Files.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.gridLayout_2.addWidget(self.Files, 8, 0, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.Classes = Classes(self.centralwidget)
        self.Classes.setObjectName(u"Classes")
        sizePolicy3.setHeightForWidth(self.Classes.sizePolicy().hasHeightForWidth())
        self.Classes.setSizePolicy(sizePolicy3)
        self.Classes.setMinimumSize(QSize(360, 200))
        self.Classes.setMaximumSize(QSize(400, 16777215))
        self.Classes.setToolTipDuration(-1)
        self.Classes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Classes.setAutoFillBackground(False)
        self.Classes.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)

        self.gridLayout_2.addWidget(self.Classes, 1, 0, 1, 1)

        self.Prev = QPushButton(self.centralwidget)
        self.Prev.setObjectName(u"Prev")
        sizePolicy2.setHeightForWidth(self.Prev.sizePolicy().hasHeightForWidth())
        self.Prev.setSizePolicy(sizePolicy2)
        self.Prev.setMinimumSize(QSize(360, 46))
        self.Prev.setMaximumSize(QSize(400, 46))
        palette2 = QPalette()
        brush8 = QBrush(QColor(129, 129, 194, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        self.Prev.setPalette(palette2)
        self.Prev.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.Prev, 5, 0, 1, 1)

        self.removeclass = QPushButton(self.centralwidget)
        self.removeclass.setObjectName(u"removeclass")

        self.gridLayout_2.addWidget(self.removeclass, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.Annotator = Annotator(self.centralwidget)
        self.Annotator.setObjectName(u"Annotator")
        self.Annotator.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.Annotator.sizePolicy().hasHeightForWidth())
        self.Annotator.setSizePolicy(sizePolicy3)
        self.Annotator.setMinimumSize(QSize(640, 640))
        self.Annotator.setMaximumSize(QSize(640, 640))
        self.Annotator.setSizeIncrement(QSize(8, 8))
        palette3 = QPalette()
        brush9 = QBrush(QColor(66, 66, 66, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        self.Annotator.setPalette(palette3)
        self.Annotator.setMouseTracking(True)
        self.Annotator.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Annotator.setAutoFillBackground(True)
        self.Draw = Draw(self.Annotator)
        self.Draw.setObjectName(u"Draw")
        self.Draw.setEnabled(True)
        self.Draw.setGeometry(QRect(0, 0, 640, 640))
        sizePolicy3.setHeightForWidth(self.Draw.sizePolicy().hasHeightForWidth())
        self.Draw.setSizePolicy(sizePolicy3)
        self.Draw.setMinimumSize(QSize(640, 640))
        self.Draw.setMaximumSize(QSize(640, 640))
        self.Draw.setSizeIncrement(QSize(8, 8))
        self.Draw.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.Draw.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Draw.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.Annotator, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy4)
        self.toolBar.setMinimumSize(QSize(0, 0))
        self.toolBar.setMaximumSize(QSize(25, 16777215))
        self.toolBar.setBaseSize(QSize(25, 640))
        palette4 = QPalette()
        brush10 = QBrush(QColor(45, 45, 45, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush10)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        self.toolBar.setPalette(palette4)
        self.toolBar.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBar.setMouseTracking(True)
        self.toolBar.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.toolBar.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.toolBar.setWindowTitle(u"toolBar")
#if QT_CONFIG(tooltip)
        self.toolBar.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolBar.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.toolBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toolBar.setAutoFillBackground(True)
        self.toolBar.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.toolBar.setFloatable(True)
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1045, 33))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        self.menuBar.setPalette(palette5)
        self.menuBar.setAutoFillBackground(True)
        self.menuReturn = QMenu(self.menuBar)
        self.menuReturn.setObjectName(u"menuReturn")
        self.menuSave = QMenu(self.menuBar)
        self.menuSave.setObjectName(u"menuSave")
        self.menuOpen_Images = QMenu(self.menuBar)
        self.menuOpen_Images.setObjectName(u"menuOpen_Images")
        self.menuSet_Project_Directory = QMenu(self.menuBar)
        self.menuSet_Project_Directory.setObjectName(u"menuSet_Project_Directory")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuCreate_Training_Set = QMenu(self.menuBar)
        self.menuCreate_Training_Set.setObjectName(u"menuCreate_Training_Set")
        self.menuTest = QMenu(self.menuBar)
        self.menuTest.setObjectName(u"menuTest")
        MainWindow.setMenuBar(self.menuBar)

        self.toolBar.addAction(self.actionBox)
        self.toolBar.addAction(self.actionPolygonTool)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actiondelete)
        self.toolBar.addAction(self.actionUndo)
        self.menuBar.addAction(self.menuReturn.menuAction())
        self.menuBar.addAction(self.menuSave.menuAction())
        self.menuBar.addAction(self.menuOpen_Images.menuAction())
        self.menuBar.addAction(self.menuSet_Project_Directory.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuCreate_Training_Set.menuAction())
        self.menuBar.addAction(self.menuTest.menuAction())
        self.menuReturn.addAction(self.actionSave_and_Return)
        self.menuSave.addAction(self.actionSave)
        self.menuOpen_Images.addAction(self.actionSelect_Directory)
        self.menuOpen_Images.addAction(self.actionAdd_Directory)
        self.menuSet_Project_Directory.addAction(self.actionSelect_Folder)
        self.menuView.addAction(self.actionProject_Directory)
        self.menuCreate_Training_Set.addAction(self.actionFrom_Current_Annotations)
        self.menuTest.addAction(self.actionToggle)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ai For All", None))
        self.actionBox.setText(QCoreApplication.translate("MainWindow", u"Box", None))
#if QT_CONFIG(tooltip)
        self.actionBox.setToolTip(QCoreApplication.translate("MainWindow", u"Bounding Box Mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionBox.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionPolygonTool.setText(QCoreApplication.translate("MainWindow", u"PolygonTool", None))
#if QT_CONFIG(tooltip)
        self.actionPolygonTool.setToolTip(QCoreApplication.translate("MainWindow", u"FreeForm selection mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPolygonTool.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actiondelete.setText(QCoreApplication.translate("MainWindow", u"delete", None))
#if QT_CONFIG(tooltip)
        self.actiondelete.setToolTip(QCoreApplication.translate("MainWindow", u"remove annotations", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actiondelete.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+Shift+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_Directory.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.actionAdd_Directory.setText(QCoreApplication.translate("MainWindow", u"Add Folder", None))
        self.actionAdd_Files.setText(QCoreApplication.translate("MainWindow", u"Add Files", None))
        self.actionSelect_Folder.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.actionProject_Directory.setText(QCoreApplication.translate("MainWindow", u"Project Directory", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_and_Return.setText(QCoreApplication.translate("MainWindow", u"Save and Return", None))
        self.actionFrom_Current_Annotations.setText(QCoreApplication.translate("MainWindow", u"From Current Annotations", None))
        self.actionToggle.setText(QCoreApplication.translate("MainWindow", u"Open image Search", None))
        self.lineEdit.setText("")
#if QT_CONFIG(tooltip)
        self.New_Ann.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.New_Ann.setText(QCoreApplication.translate("MainWindow", u"New Annotation", None))
#if QT_CONFIG(tooltip)
        self.Next.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Next.setText(QCoreApplication.translate("MainWindow", u"Next Annotation", None))
#if QT_CONFIG(whatsthis)
        self.Files.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Classes.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Prev.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Prev.setText(QCoreApplication.translate("MainWindow", u"Previous Annotation", None))
        self.removeclass.setText(QCoreApplication.translate("MainWindow", u"Remove Class", None))
        self.menuReturn.setTitle(QCoreApplication.translate("MainWindow", u"Return", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuOpen_Images.setTitle(QCoreApplication.translate("MainWindow", u"Add Images", None))
        self.menuSet_Project_Directory.setTitle(QCoreApplication.translate("MainWindow", u"Set Project Directory", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuCreate_Training_Set.setTitle(QCoreApplication.translate("MainWindow", u"Create Training Set", None))
        self.menuTest.setTitle(QCoreApplication.translate("MainWindow", u"Search For Image", None))
    # retranslateUi

