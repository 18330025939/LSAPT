import json
import os.path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QContextMenuEvent
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget, QMenu, QAction, QFileDialog
from Lib.ui import UI

class TreeWidgetIO:
    @staticmethod
    def export_tree_widget(tree_widget, file_path):
        data = TreeWidgetIO._serialize_tree_widget(tree_widget)
        with open(file_path, 'w') as file:
            file.truncate(0)
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def import_tree_widget(file_path, parent_item):
        with open(file_path, 'r') as file:
            data = json.load(file)
        TreeWidgetIO._deserialize_tree_widget(data, parent_item)

    @staticmethod
    def _serialize_tree_widget(tree_widget):
        data = []

        root_item = tree_widget.invisibleRootItem()
        for i in range(root_item.childCount()):
            item = root_item.child(i)
            data.append(TreeWidgetIO._serialize_item(item))

        return data

    @staticmethod
    def _serialize_item(item):
        data = {
            'text': item.text(0),
            'expanded': item.isExpanded(),
            'children': []
        }
        for i in range(item.childCount()):
            child = item.child(i)
            data['children'].append(TreeWidgetIO._serialize_item(child))

        return data

    @staticmethod
    def _deserialize_tree_widget(data, parent_item):
        for item_data in data:
            item = QTreeWidgetItem(parent_item)
            item.setText(0, item_data['text'])
            item.setExpanded(item_data['expanded'])
            TreeWidgetIO._deserialize_tree_widget(item_data['children'], item)


class ModuleLib(QTreeWidget):
    def __init__(self, form):
        super().__init__()
        self.name = None
        self.version = None
        self.func = None
        self.tree = form
        self.item = None

        self.setup_context_menu()
        self.current_dir = os.path.join(os.getcwd(), UI.useCaseLibDir)
        if not os.path.exists(self.current_dir):
            os.makedirs(self.current_dir)
    def setup_context_menu(self):
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.handle_context_menu)
        self.tree.itemClicked.connect(self.clicked_item)

        self.exportAction = QAction("导出", self.tree)
        self.importAction = QAction("导入", self.tree)
        self.addItemAction = QAction("增加节点", self.tree)
        self.deleteItemAction = QAction("删除节点", self.tree)

        self.exportAction.triggered.connect(self.export_tree)
        self.importAction.triggered.connect(self.import_tree)

    def handle_context_menu(self, pos):
        self.menu = QMenu(self)
        self.menu.addAction(self.exportAction)
        self.menu.addAction(self.importAction)
        self.menu.addAction(self.addItemAction)
        self.menu.addAction(self.deleteItemAction)

        action = self.menu.exec_(self.tree.mapToGlobal(pos))

        if action == self.addItemAction:
            # self.add_item()
            pass
        elif action == self.deleteItemAction:
            self.delete_item()

    def add_item(self, name):
        if name:
            items = self.tree.findItems(name, Qt.MatchExactly)
            if len(items) == 0:
                root = self.tree.invisibleRootItem()
                root_item = QTreeWidgetItem(root, [name])

    def delete_item(self):
        select_items = self.tree.selectedItems()
        for item in select_items:
            parent_item = item.parent()
            if parent_item:
                parent_item.takeChild(parent_item.indexOfChild(item))

    def export_tree(self):
        dialog = QFileDialog()
        dialog.setDirectory(self.current_dir)
        file_path, _ = dialog.getSaveFileName(self, "导出文件", "", "JSON Files (*.json)")
        if file_path:
            TreeWidgetIO.export_tree_widget(self.tree, file_path)

    def import_tree(self):
        dialog = QFileDialog()
        dialog.setDirectory(self.current_dir)
        file_path, _ = dialog.getOpenFileName(None, "导入文件", "", "JSON Files (*.json)")
        if file_path:
            self.tree.clear()
            TreeWidgetIO.import_tree_widget(file_path, self.tree)

    def clicked_item(self, item, column):
        self.column = column

    def expand_to_config(self):
        current_item = self.tree.currentItem()
        if current_item is not None and current_item.isSelected():
            file_name = current_item.text(self.column)
            file_path = os.path.join(self.current_dir, file_name + '.json')
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)

                return data
            except FileNotFoundError:
                pass
        return None

    def save_from_config(self, name, data):
        # root_item = self.tree.invisibleRootItem()
        current_item = self.tree.currentItem()
        if current_item is not None and current_item.isSelected() and current_item.parent() is None:
            items = self.tree.findItems(name, Qt.MatchExactly)
            if len(items) == 0:
                new_item = QTreeWidgetItem(current_item)
                new_item.setText(self.column, name)

            file_path = os.path.join(self.current_dir, name + '.json')

            with open(file_path, 'w') as f:
                f.truncate(0)
                json.dump(data, f, ensure_ascii=False, indent=4)

