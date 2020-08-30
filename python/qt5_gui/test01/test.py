#!/usr/bin/env python3

import os
import sys
import yaml
# 引入 PyQt5.QtWidgetes 模块
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH']
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QFileDialog
from Ui_hello import Ui_MainWindow
from Ui_config import Ui_Dialog
from Ui_email_info import Ui_Dialog as Ui_EmailInfo

config_path = os.path.join(os.path.dirname(__file__), 'config.yml')

board_dict = {
    'AHB8304HIB-AIStick':'AHB-8304HIB-AiStick',
    'AHB8308HIB-AIStick':'AHB-8308HIB-AiStick',
    'AHB8316HIB-AIStick':'AHB-8316HIB-AiStick'
}

board_pack_dict = {
    'AHB8304HIB-AIStick':'AHB8304HIB_AIStick',
    'AHB8308HIB-AIStick':'AHB8308HIB_AIStick',
    'AHB8316HIB-AIStick':'AHB8316HIB_AIStick'
}

client_dict = {
    '标准版本':'General',
    'UNV版本':'UNV',
    'Metro版本':'Metro',
    'SuperSun版本':'SuperSun'
}

client_dict_v2 = {
    '标准版本':'general',
    'UNV版本':'unv',
    'Metro版本':'metro',
    'SuperSun版本':'supersun'
}

with open(config_path) as f:
    cont = f.read()

cf = yaml.load(cont, Loader=yaml.FullLoader)

def save_yaml():
    with open(config_path, "w") as f:
        yaml.dump(cf, f)

class dialog_email(QDialog, Ui_EmailInfo):
    def __init__(self):
        super(dialog_email, self).__init__()
        self.setupUi(self)
        self.textEdit.setReadOnly(True)
        email_txt = '刘芳：\n'\
        '你好！该版本为' + cf['test_name'] + '\n'\
        '测试表见: '+ cf['test_list_dir'] + '\n'\
        '做包地址、版本信息文件见：' + cf['pack_dir'] + '\n'\
        '测试内容见测试单：' + cf['test_list_url']
        self.textEdit.setText(email_txt)

class dialog_config(QDialog, Ui_Dialog):
    def __init__(self):
        super(dialog_config, self).__init__()
        self.setupUi(self)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText(str(cf.get('dist_target')))
        self.lineEdit_2.setReadOnly(True)
        lib_dir = cf.get('lib_dir')
        if lib_dir != None:
            self.lineEdit_2.setText(str(lib_dir))
        self.pushButton.clicked.connect(self.getDirName)
        self.pushButton_2.clicked.connect(self.saveConfig)
        self.pushButton_3.clicked.connect(self.getLibDirName)

    def getLibDirName(self):
        lib_dir = self.lineEdit_2.text()
        lib_choose = QFileDialog.getExistingDirectory(self, '选取文件夹', lib_dir)
        if lib_choose == "":
            print('取消选择')
            return
        self.lineEdit_2.setText(lib_choose)

    def getDirName(self):
        dir_name = self.lineEdit.text()
        dir_choose = QFileDialog.getExistingDirectory(self, '选取文件夹', dir_name)
        if dir_choose == "":
            print("取消选择")
            return
        self.lineEdit.setText(dir_choose)

    def saveConfig(self):
        dir_name = self.lineEdit.text()
        cf['dist_target'] = dir_name
        lib_dir = self.lineEdit_2.text()
        cf['lib_dir'] = lib_dir
        save_yaml()

class mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.radioButton.clicked.connect(self.checkRadioButton)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        svn_ver = cf.get('svn_ver')
        if svn_ver != None:
            self.lineEdit_4.setText(str(svn_ver))
        board_info = cf.get('board_info')
        if board_info != None:
            self.comboBox.setCurrentText(board_info)
        ver_info = cf.get('ver_info')
        if ver_info != None:
            self.comboBox_2.setCurrentText(ver_info)
        client_info = cf.get('client_type')
        if client_info != None:
            self.comboBox_3.setCurrentText(client_info)
        test_list_url = cf.get('test_list_url')
        if test_list_url != None:
            self.lineEdit.setText(test_list_url)
        self.pushButton.clicked.connect(self.genDirPushButton)
        self.pushButton_2.clicked.connect(self.generatePushButton)
        self.pushButton_4.clicked.connect(self.genEmailInfo)
        self.actiona.triggered.connect(self.configAction)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.comboBox.currentTextChanged.connect(self.boardCBoxChanged)
        self.comboBox_2.currentTextChanged.connect(self.verCBoxChanged)
        self.comboBox_3.currentTextChanged.connect(self.clientCBoxChanged)

    def genEmailInfo(self):
        print('生成邮件信息')
        form1 = dialog_email()
        form1.show()
        form1.exec_()
        self.show()

    def clientCBoxChanged(self):
        client_info = self.comboBox_3.currentText()
        print("Client Type:", client_info)
        cf['client_type'] = client_info
        save_yaml()

    def boardCBoxChanged(self):
        board_info = self.comboBox.currentText()
        print("Board:", board_info)
        cf['board_info'] = board_info
        save_yaml()

    def verCBoxChanged(self):
        ver_info = self.comboBox_2.currentText()
        print("Ver:", ver_info)
        cf['ver_info'] = ver_info
        save_yaml()

    def checkRadioButton(self):
        if self.radioButton.isChecked():
            QMessageBox.information(self,"消息框标题","我RadioButton按钮被选中啦！",QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.information(self,"消息框标题","我RadioButton按钮被取消啦！",QMessageBox.Yes | QMessageBox.No)

    def genDirPushButton(self):
        home_dir = cf['dist_target']
        if os.path.isdir(home_dir):
            board_type = self.comboBox.currentText()
            client_type = self.comboBox_3.currentText()
            gen_ver = self.comboBox_2.currentText()
            gen_date = self.dateEdit.date().toString("yyyyMMdd")
            svn_no = self.lineEdit_4.text()
            gen_name = gen_ver + '.' + svn_no + '.'+ client_dict_v2[client_type]
            gen_dir = home_dir + '/' + board_dict[board_type] + '/' + client_type + '/' + gen_ver + '/' + gen_date + '/' + gen_name
            is_exist = os.path.exists(gen_dir)
            if not is_exist:
                replay = QMessageBox.information(self,'提示','确定要创建目录',QMessageBox.Yes | QMessageBox.No)
                if replay == QMessageBox.Yes:
                    os.makedirs(gen_dir)
                print(gen_dir)
            else:
                QMessageBox.information(self,"警告","输出目录已存在!",QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.information(self,"警告","输出目录不存在! 请重新配置...",QMessageBox.Yes | QMessageBox.No)

    def generatePushButton(self):
        board_type = self.comboBox.currentText()
        ver_type = self.comboBox_2.currentText()
        ver_time = self.dateEdit.date().toString("yyyyMMdd")
        svn_no = self.lineEdit_4.text()
        client_type = self.comboBox_3.currentText()
        ver_name = board_type + '_'+ client_dict[client_type] +'_HVR.' + ver_type + '.' + ver_time
        test_name = ver_name + ' ' + '软件' + client_type + '测试'
        cf['test_name'] = test_name
        pack_dir_base = 'http://192.168.250.4/svn/zview_4sdi_dvr/software/projects_2018/01_HVR/04devs/03_packages/AHB83XXHIB_AI'
        pack_dir_full = pack_dir_base + '/' + board_pack_dict[board_type] + '/' + ver_type + '/' + ver_time + '/' + ver_type + '.' + svn_no + '.' + client_dict_v2[client_type]
        cf['pack_dir'] = pack_dir_full
        self.textEdit.setText(pack_dir_full)
        self.lineEdit_2.setText(ver_name)
        self.lineEdit_3.setText(test_name)
        test_dir_base = r'\\192.168.250.10\TestFolder\HVR\AHB-83xxHFT(HIB-AI)'
        test_dir_full = test_dir_base + '\\' + board_dict[board_type] + '\\' + client_type + '\\' + ver_type  + '\\' + ver_time + '\\' + ver_type + '.' + svn_no + '.' + client_dict_v2[client_type]
        cf['test_list_dir'] = test_dir_full
        self.textEdit_2.setText(test_dir_full)
        test_list_url = self.lineEdit.text()
        cf['test_list_url'] = test_list_url
        save_yaml()

    def configAction(self):
        form1 = dialog_config()
        form1.show()
        form1.exec_()
        self.show()

# 顶置
# self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
# 取消顶置
# self.setWindowFlags(QtCore.Qt.Widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 生成 mywindow 实例
    window = mywindow()
    # 显示窗口
    window.show()
    sys.exit(app.exec_())
