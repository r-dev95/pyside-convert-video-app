# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_layout.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QStackedWidget, QTimeEdit, QWidget)
import lib.ui.resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 600)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pbtn_play = QPushButton(self.frame)
        self.pbtn_play.setObjectName(u"pbtn_play")
        icon = QIcon()
        icon.addFile(u":/lib/ui/icons/feather/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbtn_play.setIcon(icon)

        self.gridLayout_2.addWidget(self.pbtn_play, 4, 0, 1, 1)

        self.stacked_widget_video = QStackedWidget(self.frame)
        self.stacked_widget_video.setObjectName(u"stacked_widget_video")

        self.gridLayout_2.addWidget(self.stacked_widget_video, 0, 0, 1, 2)

        self.pbtn_pause = QPushButton(self.frame)
        self.pbtn_pause.setObjectName(u"pbtn_pause")
        icon1 = QIcon()
        icon1.addFile(u":/lib/ui/icons/feather/pause.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbtn_pause.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pbtn_pause, 4, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.slider_play = QSlider(self.frame_2)
        self.slider_play.setObjectName(u"slider_play")
        self.slider_play.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.slider_play, 0, 0, 1, 1)

        self.time_play = QTimeEdit(self.frame_2)
        self.time_play.setObjectName(u"time_play")
        self.time_play.setFrame(False)
        self.time_play.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_play.setReadOnly(True)
        self.time_play.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.time_play.setAccelerated(False)

        self.gridLayout_3.addWidget(self.time_play, 0, 1, 1, 1)

        self.time_duration = QTimeEdit(self.frame_2)
        self.time_duration.setObjectName(u"time_duration")
        self.time_duration.setFrame(False)
        self.time_duration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_duration.setReadOnly(True)
        self.time_duration.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.time_duration.setCalendarPopup(False)

        self.gridLayout_3.addWidget(self.time_duration, 0, 3, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.pbtn_play, self.pbtn_pause)
        QWidget.setTabOrder(self.pbtn_pause, self.slider_play)
        QWidget.setTabOrder(self.slider_play, self.time_play)
        QWidget.setTabOrder(self.time_play, self.time_duration)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pbtn_play.setText("")
        self.pbtn_pause.setText("")
        self.time_play.setDisplayFormat(QCoreApplication.translate("Dialog", u"H:mm:ss", None))
        self.time_duration.setDisplayFormat(QCoreApplication.translate("Dialog", u"H:mm:ss", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"/", None))
    # retranslateUi

