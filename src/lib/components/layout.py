# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QDialog, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTimeEdit, QWidget)
import lib.components.resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 600)
        icon = QIcon()
        icon.addFile(u":/lib/components/icons/feather/video.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 2, 1, 2)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 5, 1, 2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/lib/components/icons/feather/clock.svg"))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_3, 1, 1, 1, 1)

        self.time_start = QTimeEdit(self.groupBox_2)
        self.time_start.setObjectName(u"time_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_start.sizePolicy().hasHeightForWidth())
        self.time_start.setSizePolicy(sizePolicy1)
        self.time_start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_start.setReadOnly(False)

        self.gridLayout_5.addWidget(self.time_start, 1, 2, 1, 2)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_4, 1, 4, 1, 1)

        self.time_end = QTimeEdit(self.groupBox_2)
        self.time_end.setObjectName(u"time_end")
        sizePolicy1.setHeightForWidth(self.time_end.sizePolicy().hasHeightForWidth())
        self.time_end.setSizePolicy(sizePolicy1)
        self.time_end.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.time_end, 1, 5, 1, 2)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 2, 1, 1, 6)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 3, 3, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 3, 5, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 3, 6, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/lib/components/icons/feather/layout.svg"))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_5, 4, 1, 1, 1)

        self.spin_x = QSpinBox(self.groupBox_2)
        self.spin_x.setObjectName(u"spin_x")
        sizePolicy1.setHeightForWidth(self.spin_x.sizePolicy().hasHeightForWidth())
        self.spin_x.setSizePolicy(sizePolicy1)
        self.spin_x.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spin_x.setMaximum(10000)

        self.gridLayout_5.addWidget(self.spin_x, 4, 2, 1, 1)

        self.spin_y = QSpinBox(self.groupBox_2)
        self.spin_y.setObjectName(u"spin_y")
        sizePolicy1.setHeightForWidth(self.spin_y.sizePolicy().hasHeightForWidth())
        self.spin_y.setSizePolicy(sizePolicy1)
        self.spin_y.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spin_y.setMaximum(10000)

        self.gridLayout_5.addWidget(self.spin_y, 4, 3, 1, 1)

        self.spin_w = QSpinBox(self.groupBox_2)
        self.spin_w.setObjectName(u"spin_w")
        sizePolicy1.setHeightForWidth(self.spin_w.sizePolicy().hasHeightForWidth())
        self.spin_w.setSizePolicy(sizePolicy1)
        self.spin_w.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spin_w.setMaximum(10000)

        self.gridLayout_5.addWidget(self.spin_w, 4, 5, 1, 1)

        self.spin_h = QSpinBox(self.groupBox_2)
        self.spin_h.setObjectName(u"spin_h")
        sizePolicy1.setHeightForWidth(self.spin_h.sizePolicy().hasHeightForWidth())
        self.spin_h.setSizePolicy(sizePolicy1)
        self.spin_h.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spin_h.setMaximum(10000)

        self.gridLayout_5.addWidget(self.spin_h, 4, 6, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 4, 0, 1, 2)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.time_video_play = QTimeEdit(self.groupBox)
        self.time_video_play.setObjectName(u"time_video_play")
        self.time_video_play.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_video_play.setReadOnly(True)
        self.time_video_play.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.gridLayout_4.addWidget(self.time_video_play, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)

        self.line_video_width = QLineEdit(self.groupBox)
        self.line_video_width.setObjectName(u"line_video_width")
        self.line_video_width.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_video_width.setReadOnly(True)

        self.gridLayout_4.addWidget(self.line_video_width, 0, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 4, 1, 1)

        self.line_video_height = QLineEdit(self.groupBox)
        self.line_video_height.setObjectName(u"line_video_height")
        self.line_video_height.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_video_height.setReadOnly(True)

        self.gridLayout_4.addWidget(self.line_video_height, 0, 5, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 2)

        self.list_widget_log = QListWidget(self.frame)
        self.list_widget_log.setObjectName(u"list_widget_log")
        self.list_widget_log.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.gridLayout_2.addWidget(self.list_widget_log, 6, 0, 1, 2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cbox_auto_scroll = QCheckBox(self.frame_2)
        self.cbox_auto_scroll.setObjectName(u"cbox_auto_scroll")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbox_auto_scroll.sizePolicy().hasHeightForWidth())
        self.cbox_auto_scroll.setSizePolicy(sizePolicy2)
        self.cbox_auto_scroll.setChecked(True)

        self.gridLayout_6.addWidget(self.cbox_auto_scroll, 1, 1, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 5, 0, 1, 2)

        self.frame_1 = QFrame(self.frame)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_input_fpath = QLineEdit(self.frame_1)
        self.line_input_fpath.setObjectName(u"line_input_fpath")
        self.line_input_fpath.setDragEnabled(True)
        self.line_input_fpath.setReadOnly(True)

        self.gridLayout_3.addWidget(self.line_input_fpath, 0, 0, 1, 1)

        self.pbtn_run = QPushButton(self.frame_1)
        self.pbtn_run.setObjectName(u"pbtn_run")
        icon1 = QIcon()
        icon1.addFile(u":/lib/components/icons/feather/file-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbtn_run.setIcon(icon1)

        self.gridLayout_3.addWidget(self.pbtn_run, 1, 1, 1, 1)

        self.line_output_fpath = QLineEdit(self.frame_1)
        self.line_output_fpath.setObjectName(u"line_output_fpath")
        self.line_output_fpath.setDragEnabled(True)
        self.line_output_fpath.setReadOnly(True)

        self.gridLayout_3.addWidget(self.line_output_fpath, 1, 0, 1, 1)

        self.pbtn_select = QPushButton(self.frame_1)
        self.pbtn_select.setObjectName(u"pbtn_select")
        icon2 = QIcon()
        icon2.addFile(u":/lib/components/icons/feather/file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbtn_select.setIcon(icon2)

        self.gridLayout_3.addWidget(self.pbtn_select, 0, 1, 1, 1)

        self.rbtn_input_file = QRadioButton(self.frame_1)
        self.rbtn_input_file.setObjectName(u"rbtn_input_file")
        sizePolicy2.setHeightForWidth(self.rbtn_input_file.sizePolicy().hasHeightForWidth())
        self.rbtn_input_file.setSizePolicy(sizePolicy2)
        self.rbtn_input_file.setCheckable(True)
        self.rbtn_input_file.setChecked(True)

        self.gridLayout_3.addWidget(self.rbtn_input_file, 0, 2, 1, 1)

        self.rbtn_output_file = QRadioButton(self.frame_1)
        self.rbtn_output_file.setObjectName(u"rbtn_output_file")
        sizePolicy2.setHeightForWidth(self.rbtn_output_file.sizePolicy().hasHeightForWidth())
        self.rbtn_output_file.setSizePolicy(sizePolicy2)
        self.rbtn_output_file.setCheckable(False)

        self.gridLayout_3.addWidget(self.rbtn_output_file, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.line_input_fpath, self.pbtn_select)
        QWidget.setTabOrder(self.pbtn_select, self.line_output_fpath)
        QWidget.setTabOrder(self.line_output_fpath, self.pbtn_run)
        QWidget.setTabOrder(self.pbtn_run, self.time_start)
        QWidget.setTabOrder(self.time_start, self.time_end)
        QWidget.setTabOrder(self.time_end, self.spin_x)
        QWidget.setTabOrder(self.spin_x, self.spin_y)
        QWidget.setTabOrder(self.spin_y, self.spin_w)
        QWidget.setTabOrder(self.spin_w, self.spin_h)
        QWidget.setTabOrder(self.spin_h, self.cbox_auto_scroll)
        QWidget.setTabOrder(self.cbox_auto_scroll, self.rbtn_input_file)
        QWidget.setTabOrder(self.rbtn_input_file, self.rbtn_output_file)
        QWidget.setTabOrder(self.rbtn_output_file, self.time_video_play)
        QWidget.setTabOrder(self.time_video_play, self.line_video_width)
        QWidget.setTabOrder(self.line_video_width, self.line_video_height)
        QWidget.setTabOrder(self.line_video_height, self.list_widget_log)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u8a2d\u5b9a", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u958b\u59cb", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u7d42\u4e86", None))
        self.label_3.setText("")
        self.time_start.setDisplayFormat(QCoreApplication.translate("Dialog", u"H:mm:ss", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"~", None))
        self.time_end.setDisplayFormat(QCoreApplication.translate("Dialog", u"H:mm:ss", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"X\u5ea7\u6a19", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Y\u5ea7\u6a19", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u6a2a\u5e45", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u9ad8\u3055", None))
        self.label_5.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u30d3\u30c7\u30aa\u60c5\u5831", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7dcf\u518d\u751f\u6642\u9593\uff1a", None))
        self.time_video_play.setDisplayFormat(QCoreApplication.translate("Dialog", u"H:mm:ss", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u89e3\u50cf\u5ea6\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u00d7", None))
        self.cbox_auto_scroll.setText(QCoreApplication.translate("Dialog", u"\u81ea\u52d5\u30b9\u30af\u30ed\u30fc\u30eb", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u30ed\u30b0\uff1a", None))
        self.line_input_fpath.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u30d5\u30a1\u30a4\u30eb\u30d1\u30b9\uff08\u8aad\u8fbc\uff09", None))
        self.pbtn_run.setText(QCoreApplication.translate("Dialog", u"\u5b9f\u884c", None))
        self.line_output_fpath.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u30d5\u30a1\u30a4\u30eb\u30d1\u30b9\uff08\u4fdd\u5b58\uff09", None))
        self.pbtn_select.setText(QCoreApplication.translate("Dialog", u"\u9078\u629e", None))
        self.rbtn_input_file.setText(QCoreApplication.translate("Dialog", u"\u5909\u63db\u524d", None))
        self.rbtn_output_file.setText(QCoreApplication.translate("Dialog", u"\u5909\u63db\u5f8c", None))
    # retranslateUi

