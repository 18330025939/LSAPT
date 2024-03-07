import os.path
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from MultiConfig.ui_multiConfig import Ui_MultiConfig
from Lib.module import ModuleLib
from Lib.ui import UI
from Lib.item import ConfigItems


class MultiConfigWindow(QWidget):
    def __init__(self, form):
        super().__init__()
        self.form = form
        self.ui = Ui_MultiConfig()
        self.ui.setupUi(self.form)
        # self.form.show()

        self.form.closeEvent = self.on_close
        UI.treeModule = ModuleLib(self.ui.treeUserCasesLib)
        UI.tableItem = ConfigItems(self.ui.tableTestItem)

        self.ui.btnRead.clicked.connect(self.read_table_to_config)
        self.ui.btnWrite.clicked.connect(self.write_config_to_table)
        self.ui.btnUnfold.clicked.connect(self.unfold_lib_to_config)
        self.ui.btnSave.clicked.connect(self.save_config_to_lib)
        self.ui.btnImport.clicked.connect(self.import_file_to_table)
        self.ui.btnExport.clicked.connect(self.export_table_to_file)
        self.ui.editRootItem.returnPressed.connect(self.edit_root_item)
        self.ui.btnNewProject.clicked.connect(self.new_table_project)

    def on_close(self, event):
        self.form.hide()

    def get_test_instr_object_name(self):
        return self.ui.editTestInstr.objectName()

    def get_test_pass_object_name(self):
        return self.ui.editPassText.objectName()

    def get_test_fail_object_name(self):
        return self.ui.editFailText.objectName()

    def get_retry_text_object_name(self):
        return self.ui.editRetryText.objectName()

    def get_image_path_object_name(self):
        return self.ui.editImgPath.objectName()

    def get_timeout_object_name(self):
        return self.ui.editTimeOut.objectName()

    def get_test_skip_object_name(self):
        return self.ui.rdoBtnSkipTest.objectName()
        # return self.ui.rdoBtnOnlyTest.objectName()
        # return self.ui.chkBoxPdtDel.objectName()

    def get_show_info_object_name(self):
        return self.ui.editShowInfo.objectName()

    def switch_configs_object_name(self, config):
        cases = {
            "cmd": self.get_test_instr_object_name(),
            "skipTest": self.get_test_skip_object_name(),
            "result": self.get_show_info_object_name(),
            "pass": self.get_test_pass_object_name(),
            "fail": self.get_test_fail_object_name(),
            "retry": self.get_test_retry_object_name(),
            "timeout": self.get_timeout_object_name()
        }
        cases.get(config, self.default)()

    def parameter_config_generation(self):
        config = {}
        config.setdefault(self.ui.editTestInstr.objectName(), self.ui.editTestInstr.toPlainText())
        config.setdefault(self.ui.editTestName.objectName(), self.ui.editTestName.text())
        config.setdefault(self.ui.editTimeOut.objectName(), self.ui.editTimeOut.text())
        config.setdefault(self.ui.editImgPath.objectName(), self.ui.editImgPath.text())
        config.setdefault(self.ui.editShowInfo.objectName(), self.ui.editShowInfo.text())
        config.setdefault(self.ui.editPassText.objectName(), self.ui.editPassText.text())
        config.setdefault(self.ui.editFailText.objectName(), self.ui.editFailText.text())
        config.setdefault(self.ui.editRetryText.objectName(), self.ui.editRetryText.text())
        config.setdefault(self.ui.chkBoxPdtDel.objectName(), self.ui.chkBoxPdtDel.isChecked())
        config.setdefault(self.ui.chkBoxErrCtn.objectName(), self.ui.chkBoxErrCtn.isChecked())
        config.setdefault(self.ui.chkBoxArtPart.objectName(), self.ui.chkBoxArtPart.isChecked())
        config.setdefault(self.ui.rdoBtnSkipTest.objectName(), self.ui.rdoBtnSkipTest.isChecked())
        config.setdefault(self.ui.rdoBtnOnlyTest.objectName(), self.ui.rdoBtnOnlyTest.isChecked())
        return config

    def parameter_config_analysis(self, configs):
        for key, value in configs.items():
            if key == self.ui.editTestInstr.objectName():
                self.ui.editTestInstr.setPlainText(value)
            elif key == self.ui.chkBoxErrCtn.objectName():
                self.ui.chkBoxErrCtn.setChecked(value)
            elif key == self.ui.editTestName.objectName():
                self.ui.editTestName.setText(value)
            elif key == self.ui.editTimeOut.objectName():
                self.ui.editTimeOut.setText(value)
            elif key == self.ui.editPassText.objectName():
                self.ui.editPassText.setText(value)
            elif key == self.ui.editFailText.objectName():
                self.ui.editFailText.setText(value)
            elif key == self.ui.editImgPath.objectName():
                self.ui.editImgPath.setText(value)
            elif key == self.ui.chkBoxPdtDel.objectName():
                self.ui.chkBoxPdtDel.setChecked(value)
            elif key == self.ui.chkBoxArtPart.objectName():
                self.ui.chkBoxArtPart.setChecked(value)
            elif key == self.ui.rdoBtnOnlyTest.objectName():
                self.ui.rdoBtnOnlyTest.setChecked(value)
            elif key == self.ui.rdoBtnSkipTest.objectName():
                self.ui.rdoBtnSkipTest.setChecked(value)
            elif key == self.ui.editShowInfo.objectName():
                self.ui.editShowInfo.setText(value)

    def unfold_lib_to_config(self):
        configs = UI.treeModule.expand_to_config()
        if configs is not None:
            self.parameter_config_analysis(configs)

    def save_config_to_lib(self):
        UI.logger.log_debug('save config to lib')
        if self.ui.editTestName.text() == "":
            return
        data = self.parameter_config_generation()
        UI.treeModule.save_from_config(self.ui.editTestName.text().strip(), data)

    def edit_root_item(self):
        UI.treeModule.add_item(self.ui.editRootItem.text())
        self.ui.editRootItem.clear()

    def read_table_to_config(self):
        configs = UI.tableItem.expand_to_config()
        if configs is not None:
            self.parameter_config_analysis(configs)

    def write_config_to_table(self):
        UI.logger.log_debug('write config to table')
        if self.ui.editTestName.text() == "":
            return

        data = {"Level": str(UI.tableItem.get_table_current_row()),
                "测试项名称":  self.ui.editTestName.text()}
        UI.tableItem.save_from_config(data)
        config = self.parameter_config_generation()
        UI.logger.log_debug('parameter config generation')
        UI.tableItem.save_test_item(self.ui.editTestName.text().strip(), config)

    def show_platform_info(self, data):
        self.ui.editPlatInfo.append(data)

    @staticmethod
    def import_file_to_table(self):
        current_path = UI.tableItem.import_table()
        if current_path is not None:
            file_path = os.path.join(current_path, UI.platformInfoFile)
            if os.path.exists(file_path):
                UI.platWin.set_platform_info(file_path)
        else:
            mes_box = QMessageBox()
            mes_box.setIcon(QMessageBox.Warning)
            mes_box.setText("文件打开失败，请检查文件格式或内容！")
            mes_box.setWindowTitle('警告')
            mes_box.exec_()

    def export_table_to_file(self):
        if UI.platWin.get_hw_plat_info() is None:
            mes_box = QMessageBox()
            mes_box.setIcon(QMessageBox.Warning)
            mes_box.setText("请先进行平台信息配置！")
            mes_box.setWindowTitle('警告')
            mes_box.exec_()
        else:
            data = UI.platWin.get_platform_config_info()
            self.show_platform_info(data)
            mes_box = QMessageBox()
            mes_box.setIcon(QMessageBox.Information)
            mes_box.setText("请检查平台配置信息！")
            mes_box.setWindowTitle('提示')
            mes_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            ok_button = mes_box.button(QMessageBox.Ok)
            ok_button.setText('确认')
            cancel_button = mes_box.button(QMessageBox.Cancel)
            cancel_button.setText('取消')
            result = mes_box.exec_()
            if result == QMessageBox.Ok:
                UI.tableItem.export_table(UI.platWin.get_hw_plat_info())
            else:
                pass

    def new_table_project(self):
        UI.tableItem.new_table()
        UI.platWin.clear_platform_config_info()
        self.ui.editPlatInfo.clear()
