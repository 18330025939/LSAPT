import json
import os
import shutil
from PyQt5.QtCore import QTemporaryFile, Qt
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QTableWidget, QAbstractItemView, QHeaderView, QAction, QMenu
from PyQt5 import QtCore, QtGui, QtWidgets
from Lib.ui import UI

class TableWidgetIO:
    @staticmethod
    def export_table_widget(table_widget, file_path):
        data = []
        row_count = table_widget.rowCount()
        column_count = table_widget.columnCount()

        for row in range(row_count):
            row_data = {}
            for column in range(column_count):
                item = table_widget.item(row, column)
                if item is not None:
                    row_data[table_widget.horizontalHeaderItem(column).text()] = item.text()
            if len(row_data):
                data.append(row_data)

        with open(file_path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def import_table_widget(table_widget, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

            # table_widget.setRowCount(len(data))
            # column_count = table_widget.columnCount()

            for row, row_data in enumerate(data):
                for column, (header, value) in enumerate(row_data.items()):
                    item = QTableWidgetItem(value)
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                    table_widget.setItem(row, column, item)
            rows = row + 1
            for row in range(rows, table_widget.rowCount()):
                for column in range(table_widget.columnCount()):
                    item = table_widget.item(row, column)
                    if item and item.text().strip():
                        item.setText('')
            return rows

    @staticmethod
    def save_temporary_table(table_widget):
        current_path = os.getcwd()
        directory = os.path.join(current_path, UI.testItemsDir)
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, UI.testItemsTempFile)
        TableWidgetIO.export_table_widget(table_widget, file_path)

    @staticmethod
    def load_temporary_table(table_widget):
        table_widget.clearContents()
        current_path = os.getcwd()
        directory = os.path.join(current_path, UI.testItemsDir)
        file_path = os.path.join(directory, UI.testItemsTempFile)
        if os.path.exists(file_path):
            return TableWidgetIO.import_table_widget(table_widget, file_path)
        else:
            return 0


class ConfigItems(QTableWidget):
    def __init__(self, form):
        super().__init__()
        self.index = 0
        self.table = form

        self.row = 0
        self.col = 0

        self.current_dir = os.path.join(os.getcwd(), UI.testItemsDir)
        if not os.path.exists(self.current_dir):
            os.makedirs(self.current_dir)
        self.index = TableWidgetIO.load_temporary_table(self.table)
        self.setup_context_menu()
        # print(self.index, self.table.currentRow())

    def setup_context_menu(self):
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.handle_context_menu)
        self.table.cellClicked.connect(self.clicked_item)
        self.table.setCurrentCell(self.index, 0)

        self.deleteAction = QAction("删除行", self.table)

        self.deleteAction.triggered.connect(self.delete_item)

    def handle_context_menu(self, pos):
        self.menu = QMenu(self)
        self.menu.addAction(self.deleteAction)

        self.menu.exec_(self.table.mapToGlobal(pos))

    def delete_item(self):
        selected_row = self.table.currentRow()
        item = self.table.item(selected_row, 1)
        test_name = item.text()
        if item:
            self.table.removeRow(selected_row)
            # self.table.clearContents()
            for row in range(selected_row, self.index):
                item = self.table.item(row, 0)
                if item:
                    value = int(item.text()) - 1
                    new_item = QTableWidgetItem(str(value))
                    self.table.setItem(row, 0, new_item)
            # current_state = self.table.item(self.row, self.col).isSelected()
            # if current_state:
            #     self.table.item(self.row, self.col).setSelected(False)
            self.index -= 1
            self.table.setCurrentCell(self.index, 0)

            self.delete_test_item(test_name)

    def clicked_item(self, row, col):
        print(row, col)
        self.row = row
        self.col = col
        # UI.logger.log_debug(row, col, self.index, self.table.rowCount())

    def expand_to_config(self):
        current_row = self.table.currentRow()
        name_item = self.table.item(current_row, 1)
        if name_item:
            file_name = name_item.data(Qt.DisplayRole)
            file_path = os.path.join(self.current_dir, file_name + '.json')
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)

                return data
            except FileNotFoundError:
                pass

        return None

    def col_attribute_check(self, column, data):
        for row in range(self.index):
            item = self.table.item(row, column)
            if item and item.text() == data:
                return True
        return False

    def save_from_config(self, data):
        current_row = self.table.currentRow()
        # print(current_row, self.index)
        item = self.table.item(current_row, 1)
        if self.col_attribute_check(1, data[self.table.horizontalHeaderItem(1).text()]):
            return
        if item is not None and current_row != 0:
            # UI.logger.log_debug('save from config not None')
            self.table.insertRow(current_row)
            for col in range(self.table.columnCount()):
                column_attribute = self.table.horizontalHeaderItem(col).text()
                item = QTableWidgetItem(data[column_attribute])
                self.table.setItem(current_row, col, item)
            # UI.logger.log_debug('save from config insert row')
            for row in range(current_row + 1, self.index + 1):
                item = self.table.item(row, 0)
                if item:
                    value = int(item.text()) + 1
                    new_item = QTableWidgetItem(str(value))
                    self.table.setItem(row, 0, new_item)
            # UI.logger.log_debug('save from config rewrite level')
            current_state = self.table.item(self.row, self.col).isSelected()
            if current_state:
                self.table.item(self.row, self.col).setSelected(False)
        else:
            # UI.logger.log_debug('save from config None')
            for col in range(self.table.columnCount()):
                column_attribute = self.table.horizontalHeaderItem(col).text()
                if column_attribute in data:
                    print(column_attribute, data[column_attribute])
                    new_item = QTableWidgetItem(data[column_attribute])
                    self.table.setItem(current_row, col, new_item)

        self.index += 1
        self.table.setCurrentCell(self.index, 0)

    def save_test_item(self, name, data):
        file_path = os.path.join(self.current_dir, name + '.json')
        # print(file_path)
        with open(file_path, 'w') as f:
            f.truncate(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
        TableWidgetIO.save_temporary_table(self.table)

    def delete_test_item(self, name):
        file_path = os.path.join(self.current_dir, name + '.json')
        if os.path.exists(file_path):
            os.remove(file_path)

    def get_table_current_row(self):
        return self.table.currentRow() + 1

    def export_table(self, table_dir):
        dialog = QFileDialog()
        export_dir = os.path.join(self.current_dir, table_dir)
        dialog.setDirectory(export_dir)
        file_path, _ = dialog.getSaveFileName(self, "导出文件", "", "JSON Files (*.json)")
        # print(file_path)
        if file_path:
            TableWidgetIO.export_table_widget(self.table, file_path)

        # row_count = self.table.rowCount()
        # column_count = self.table.columnCount()
        for row in range(self.index):
            item = self.table.item(row, 1)
            if item:
                source_file = os.path.join(self.current_dir, item.text() + '.json')
                if os.path.exists(source_file):
                    destination_file = os.path.join(export_dir, item.text() + '.json')
                    shutil.move(source_file, destination_file)
        file_path = os.path.join(self.current_dir, UI.testItemsTempFile)
        if os.path.exists(file_path):
            os.remove(file_path)

    def import_table(self):
        dialog = QFileDialog()
        dialog.setDirectory(self.current_dir)
        file_path, _ = dialog.getOpenFileName(None, "导入文件", "", "JSON Files (*.json)")
        if file_path:
            TableWidgetIO.import_table_widget(self.table, file_path)
            self.current_dir = os.path.dirname(file_path)
            return self.current_dir

        return None


class TestItems(QTableWidget):
    def __init__(self, form):
        super().__init__()
        self.index = 0
        self.table = form

    def set_item(self, row, col, value):
        item = QTableWidgetItem(value)
        self.table.setItem(row, col, item)

    def get_current_row(self):
        return self.table.currentRow()

    def set_row_background(self, row, color):
        for col in range(self.table.columnCount()):
            item = self.table.item(row, col)
            if item is not None:
                item.setBackground(color)
        self.table.show()

    def get_item_text(self, row, col):
        item = self.table.item(row, col)
        return item.text()


