# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_quantam.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 1071)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(300, 830, 121, 131))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.distance_value_bar_right = QtWidgets.QSlider(self.gridLayoutWidget_3)
        self.distance_value_bar_right.setMinimum(-255)
        self.distance_value_bar_right.setMaximum(255)
        self.distance_value_bar_right.setOrientation(QtCore.Qt.Vertical)
        self.distance_value_bar_right.setObjectName("distance_value_bar_right")
        self.gridLayout_5.addWidget(self.distance_value_bar_right, 0, 1, 1, 1)
        self.distance_value_bar_left = QtWidgets.QSlider(self.gridLayoutWidget_3)
        self.distance_value_bar_left.setMinimum(-255)
        self.distance_value_bar_left.setMaximum(255)
        self.distance_value_bar_left.setOrientation(QtCore.Qt.Vertical)
        self.distance_value_bar_left.setObjectName("distance_value_bar_left")
        self.gridLayout_5.addWidget(self.distance_value_bar_left, 0, 0, 1, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(490, 640, 154, 200))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.k_p_spinbox_angle = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.k_p_spinbox_angle.setSingleStep(0.05)
        self.k_p_spinbox_angle.setProperty("value", 1.0)
        self.k_p_spinbox_angle.setObjectName("k_p_spinbox_angle")
        self.gridLayout_2.addWidget(self.k_p_spinbox_angle, 0, 1, 1, 1)
        self.k_i_a_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.k_i_a_label.setObjectName("k_i_a_label")
        self.gridLayout_2.addWidget(self.k_i_a_label, 1, 0, 1, 1)
        self.k_p_a_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.k_p_a_label.setObjectName("k_p_a_label")
        self.gridLayout_2.addWidget(self.k_p_a_label, 0, 0, 1, 1)
        self.k_d_spinbox_angle = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.k_d_spinbox_angle.setSingleStep(0.05)
        self.k_d_spinbox_angle.setObjectName("k_d_spinbox_angle")
        self.gridLayout_2.addWidget(self.k_d_spinbox_angle, 2, 1, 1, 1)
        self.k_d_a_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.k_d_a_label.setObjectName("k_d_a_label")
        self.gridLayout_2.addWidget(self.k_d_a_label, 2, 0, 1, 1)
        self.a_dist_spinbox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.a_dist_spinbox.setSingleStep(0.05)
        self.a_dist_spinbox.setObjectName("a_dist_spinbox")
        self.gridLayout_2.addWidget(self.a_dist_spinbox, 5, 1, 1, 1)
        self.a_dist_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.a_dist_label.setObjectName("a_dist_label")
        self.gridLayout_2.addWidget(self.a_dist_label, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 2)
        self.k_i_spinbox_angle = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.k_i_spinbox_angle.setSingleStep(0.05)
        self.k_i_spinbox_angle.setObjectName("k_i_spinbox_angle")
        self.gridLayout_2.addWidget(self.k_i_spinbox_angle, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(510, 970, 121, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.angle_value_label_left = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.angle_value_label_left.setAlignment(QtCore.Qt.AlignCenter)
        self.angle_value_label_left.setObjectName("angle_value_label_left")
        self.horizontalLayout_8.addWidget(self.angle_value_label_left)
        self.angle_value_label_right = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.angle_value_label_right.setAlignment(QtCore.Qt.AlignCenter)
        self.angle_value_label_right.setObjectName("angle_value_label_right")
        self.horizontalLayout_8.addWidget(self.angle_value_label_right)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(690, 970, 121, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.signal_label_left = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.signal_label_left.setAlignment(QtCore.Qt.AlignCenter)
        self.signal_label_left.setObjectName("signal_label_left")
        self.horizontalLayout_9.addWidget(self.signal_label_left)
        self.signal_label_right = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.signal_label_right.setAlignment(QtCore.Qt.AlignCenter)
        self.signal_label_right.setObjectName("signal_label_right")
        self.horizontalLayout_9.addWidget(self.signal_label_right)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(510, 830, 121, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.angle_value_bar_right = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.angle_value_bar_right.setMinimum(-255)
        self.angle_value_bar_right.setMaximum(255)
        self.angle_value_bar_right.setOrientation(QtCore.Qt.Vertical)
        self.angle_value_bar_right.setObjectName("angle_value_bar_right")
        self.gridLayout_4.addWidget(self.angle_value_bar_right, 0, 1, 1, 1)
        self.angle_value_bar_left = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.angle_value_bar_left.setMinimum(-255)
        self.angle_value_bar_left.setMaximum(255)
        self.angle_value_bar_left.setOrientation(QtCore.Qt.Vertical)
        self.angle_value_bar_left.setObjectName("angle_value_bar_left")
        self.gridLayout_4.addWidget(self.angle_value_bar_left, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 1357, 562))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img1_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.img1_label.setMinimumSize(QtCore.QSize(560, 560))
        self.img1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img1_label.setObjectName("img1_label")
        self.horizontalLayout.addWidget(self.img1_label)
        self.img2_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.img2_label.setMinimumSize(QtCore.QSize(560, 560))
        self.img2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img2_label.setObjectName("img2_label")
        self.horizontalLayout.addWidget(self.img2_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.fps_label = QtWidgets.QLabel(self.centralwidget)
        self.fps_label.setGeometry(QtCore.QRect(20, 20, 391, 18))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.fps_label.setFont(font)
        self.fps_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fps_label.setObjectName("fps_label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(260, 640, 20, 361))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(890, 640, 211, 61))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.send_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(14)
        self.send_checkbox.setFont(font)
        self.send_checkbox.setChecked(False)
        self.send_checkbox.setObjectName("send_checkbox")
        self.verticalLayout_7.addWidget(self.send_checkbox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(640, 890, 50, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(690, 830, 131, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.signal_right_bar = QtWidgets.QSlider(self.gridLayoutWidget)
        self.signal_right_bar.setMinimum(-255)
        self.signal_right_bar.setMaximum(255)
        self.signal_right_bar.setOrientation(QtCore.Qt.Vertical)
        self.signal_right_bar.setObjectName("signal_right_bar")
        self.gridLayout_3.addWidget(self.signal_right_bar, 0, 1, 1, 1)
        self.signal_left_bar = QtWidgets.QSlider(self.gridLayoutWidget)
        self.signal_left_bar.setMinimum(-255)
        self.signal_left_bar.setMaximum(255)
        self.signal_left_bar.setOrientation(QtCore.Qt.Vertical)
        self.signal_left_bar.setObjectName("signal_left_bar")
        self.gridLayout_3.addWidget(self.signal_left_bar, 0, 0, 1, 1)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 640, 231, 223))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sensor_info_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(18)
        self.sensor_info_label_3.setFont(font)
        self.sensor_info_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sensor_info_label_3.setObjectName("sensor_info_label_3")
        self.verticalLayout_6.addWidget(self.sensor_info_label_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setObjectName("formLayout_2")
        self.host_name_label = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.host_name_label.setMouseTracking(False)
        self.host_name_label.setReadOnly(True)
        self.host_name_label.setObjectName("host_name_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.host_name_label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.server_ip_label = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.server_ip_label.setMouseTracking(False)
        self.server_ip_label.setReadOnly(True)
        self.server_ip_label.setObjectName("server_ip_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.server_ip_label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.address_label = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.address_label.setMouseTracking(False)
        self.address_label.setReadOnly(True)
        self.address_label.setObjectName("address_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.address_label)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_6.addLayout(self.formLayout_2)
        self.integ_error_x_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.integ_error_x_label.setText("")
        self.integ_error_x_label.setObjectName("integ_error_x_label")
        self.verticalLayout_6.addWidget(self.integ_error_x_label)
        self.integ_error_y_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.integ_error_y_label.setText("")
        self.integ_error_y_label.setObjectName("integ_error_y_label")
        self.verticalLayout_6.addWidget(self.integ_error_y_label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(680, 640, 201, 118))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 8, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.threshold_slider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold_slider.sizePolicy().hasHeightForWidth())
        self.threshold_slider.setSizePolicy(sizePolicy)
        self.threshold_slider.setMaximum(255)
        self.threshold_slider.setProperty("value", 100)
        self.threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_slider.setObjectName("threshold_slider")
        self.horizontalLayout_2.addWidget(self.threshold_slider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(440, 890, 50, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(300, 970, 121, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.distance_value_label_left = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.distance_value_label_left.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_value_label_left.setObjectName("distance_value_label_left")
        self.horizontalLayout_7.addWidget(self.distance_value_label_left)
        self.distance_value_label_right = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.distance_value_label_right.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_value_label_right.setObjectName("distance_value_label_right")
        self.horizontalLayout_7.addWidget(self.distance_value_label_right)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 640, 154, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.k_i_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.k_i_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.k_i_label.setObjectName("k_i_label")
        self.gridLayout.addWidget(self.k_i_label, 1, 0, 1, 1)
        self.k_i_spinbox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.k_i_spinbox.setSingleStep(0.05)
        self.k_i_spinbox.setObjectName("k_i_spinbox")
        self.gridLayout.addWidget(self.k_i_spinbox, 1, 1, 1, 1)
        self.k_p_spinbox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.k_p_spinbox.setSingleStep(0.05)
        self.k_p_spinbox.setProperty("value", 1.0)
        self.k_p_spinbox.setObjectName("k_p_spinbox")
        self.gridLayout.addWidget(self.k_p_spinbox, 0, 1, 1, 1)
        self.k_d_spinbox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.k_d_spinbox.setSingleStep(0.05)
        self.k_d_spinbox.setObjectName("k_d_spinbox")
        self.gridLayout.addWidget(self.k_d_spinbox, 2, 1, 1, 1)
        self.k_d_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.k_d_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.k_d_label.setObjectName("k_d_label")
        self.gridLayout.addWidget(self.k_d_label, 2, 0, 1, 1)
        self.k_p_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.k_p_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.k_p_label.setObjectName("k_p_label")
        self.gridLayout.addWidget(self.k_p_label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(890, 820, 211, 172))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.manual_button = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(14)
        self.manual_button.setFont(font)
        self.manual_button.setChecked(True)
        self.manual_button.setObjectName("manual_button")
        self.verticalLayout_8.addWidget(self.manual_button)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.test_left_spinbox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_7)
        self.test_left_spinbox.setDecimals(0)
        self.test_left_spinbox.setMinimum(-255.0)
        self.test_left_spinbox.setMaximum(255.0)
        self.test_left_spinbox.setSingleStep(1.0)
        self.test_left_spinbox.setObjectName("test_left_spinbox")
        self.horizontalLayout_4.addWidget(self.test_left_spinbox)
        self.test_right_spinbox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_7)
        self.test_right_spinbox.setDecimals(0)
        self.test_right_spinbox.setMinimum(-255.0)
        self.test_right_spinbox.setMaximum(255.0)
        self.test_right_spinbox.setSingleStep(1.0)
        self.test_right_spinbox.setObjectName("test_right_spinbox")
        self.horizontalLayout_4.addWidget(self.test_right_spinbox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.start_button = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.start_button.setCheckable(True)
        self.start_button.setObjectName("start_button")
        self.verticalLayout_8.addWidget(self.start_button)
        self.csv_button = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.csv_button.setCheckable(True)
        self.csv_button.setObjectName("csv_button")
        self.verticalLayout_8.addWidget(self.csv_button)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(830, 870, 50, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.preview_button = QtWidgets.QCheckBox(self.centralwidget)
        self.preview_button.setGeometry(QtCore.QRect(910, 20, 207, 18))
        font = QtGui.QFont()
        font.setFamily("A-OTF UD Shin Go Pr6N")
        font.setPointSize(14)
        self.preview_button.setFont(font)
        self.preview_button.setChecked(True)
        self.preview_button.setObjectName("preview_button")
        self.camera_button = QtWidgets.QPushButton(self.centralwidget)
        self.camera_button.setGeometry(QtCore.QRect(890, 730, 208, 32))
        self.camera_button.setCheckable(True)
        self.camera_button.setObjectName("camera_button")
        self.process_time = QtWidgets.QLabel(self.centralwidget)
        self.process_time.setGeometry(QtCore.QRect(670, 0, 229, 44))
        font = QtGui.QFont()
        font.setPointSize(37)
        self.process_time.setFont(font)
        self.process_time.setText("")
        self.process_time.setObjectName("process_time")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 21))
        self.menubar.setObjectName("menubar")
        self.menuW = QtWidgets.QMenu(self.menubar)
        self.menuW.setObjectName("menuW")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.actionFASFA = QtWidgets.QAction(MainWindow)
        self.actionFASFA.setObjectName("actionFASFA")
        self.menuW.addAction(self.action_quit)
        self.menubar.addAction(self.menuW.menuAction())

        self.retranslateUi(MainWindow)
        self.action_quit.triggered['bool'].connect(MainWindow.close)
        self.distance_value_bar_left.valueChanged['int'].connect(self.distance_value_label_left.setNum)
        self.distance_value_bar_right.valueChanged['int'].connect(self.distance_value_label_right.setNum)
        self.signal_left_bar.valueChanged['int'].connect(self.signal_label_left.setNum)
        self.signal_right_bar.valueChanged['int'].connect(self.signal_label_right.setNum)
        self.threshold_slider.valueChanged['int'].connect(self.label_4.setNum)
        self.angle_value_bar_left.valueChanged['int'].connect(self.angle_value_label_left.setNum)
        self.angle_value_bar_right.valueChanged['int'].connect(self.angle_value_label_right.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "角度"))
        self.k_i_a_label.setText(_translate("MainWindow", "K_I"))
        self.k_p_a_label.setText(_translate("MainWindow", "K_P"))
        self.k_d_a_label.setText(_translate("MainWindow", "K_D"))
        self.a_dist_label.setText(_translate("MainWindow", "a_dist"))
        self.angle_value_label_left.setText(_translate("MainWindow", "0"))
        self.angle_value_label_right.setText(_translate("MainWindow", "0"))
        self.signal_label_left.setText(_translate("MainWindow", "0"))
        self.signal_label_right.setText(_translate("MainWindow", "0"))
        self.img1_label.setText(_translate("MainWindow", "Img1"))
        self.img2_label.setText(_translate("MainWindow", "Img2"))
        self.fps_label.setText(_translate("MainWindow", "FPS:"))
        self.label_9.setText(_translate("MainWindow", "モータ制御シグナル"))
        self.send_checkbox.setText(_translate("MainWindow", "送信"))
        self.label_11.setText(_translate("MainWindow", "→"))
        self.sensor_info_label_3.setText(_translate("MainWindow", "ステータス"))
        self.label_2.setText(_translate("MainWindow", "IPアドレス"))
        self.label_3.setText(_translate("MainWindow", "送信元IP"))
        self.label.setText(_translate("MainWindow", "ホスト名"))
        self.label_8.setText(_translate("MainWindow", "２値化閾値"))
        self.label_4.setText(_translate("MainWindow", "100"))
        self.label_10.setText(_translate("MainWindow", "＋"))
        self.distance_value_label_left.setText(_translate("MainWindow", "0"))
        self.distance_value_label_right.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "距離"))
        self.k_i_label.setText(_translate("MainWindow", "K_I"))
        self.k_d_label.setText(_translate("MainWindow", "K_D"))
        self.k_p_label.setText(_translate("MainWindow", "K_P"))
        self.label_13.setText(_translate("MainWindow", "テスト用"))
        self.manual_button.setText(_translate("MainWindow", "マニュアル操作"))
        self.start_button.setText(_translate("MainWindow", "受信 開始/停止"))
        self.csv_button.setText(_translate("MainWindow", "CSV 開始/停止"))
        self.label_12.setText(_translate("MainWindow", "←"))
        self.preview_button.setText(_translate("MainWindow", "カメラ映像のプレビュー"))
        self.camera_button.setText(_translate("MainWindow", "シャッター"))
        self.menuW.setTitle(_translate("MainWindow", "ファイル"))
        self.action_quit.setText(_translate("MainWindow", "終了"))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionFASFA.setText(_translate("MainWindow", "FASFA"))
