import logging

from PyQt5.QtWidgets import QFileDialog


class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(filename, mode='w', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_error(self, message):
        self.logger.error(message)


class TestLogger:
    def __init__(self):
        self.file_name = None

    def select_file(self, file_path):
        # dialog = QFileDialog()
        self.file_name = file_path
        # dialog.setDirectory(self.current_dir)
        # self.file_name, _ = dialog.getSaveFileName(None, "保存log文件", "", "Log files (*.log)")
        # print(self.file_name)
        try:
            with open(self.file_name, 'w') as file:
                return True
        except FileNotFoundError:
            return False

    def add_separator(self):
        separator = "-" * 200
        with open(self.file_name, 'a') as file:
            file.write(separator + '\n')

    # def add_sent_data(self, data):
    #     with open(self.file_name, 'a') as file:
    #         file.write(f'Sent data: {data}\n')
    #
    # def add_received_data(self, data):
    #     with open(self.file_name, 'a') as file:
    #         file.write('Received data:' + '\n')
    #         file.write(data)
    def add_data(self, data):
        with open(self.file_name, 'a') as file:
            file.write(data + '\n')

    def add_table_data(self, table):
        rows = table.rowCount()
        columns = table.columnCount()
        column_widths = []
        for col in range(columns):
            column_widths.append(table.columnWidth(col))
        with open(self.file_name, 'a') as file:
            for row in range(rows):
                row_data = ""
                for col in range(columns):
                    item = table.item(row, col)
                    if item:
                        item_text = item.text().strip()
                        row_data += "{:<{}}".format(item_text, 30)#column_widths[col])
                    else:
                        row_data += "{:<{}}".format("", 30)#column_widths[col])
                file.write(row_data + "\n")

    def add_table_header(self, table):
        columns = table.columnCount()
        column_widths = []
        for col in range(columns):
            column_widths.append(table.columnWidth(col))

        with open(self.file_name, 'a') as file:
            header_line = ""
            for col in range(columns):
                header = table.horizontalHeaderItem(col)
                if header:
                    header_text = header.text().strip()
                    header_line += "{:<{}}".format(header_text, 30)#column_widths[col])
            file.write(header_line + '\n')