import openpyxl

class ExcelUtils:

    def __init__(self, file_path):
        self.workbook = openpyxl.load_workbook(file_path)

    def get_sheet(self, sheet_name):
        return self.workbook[sheet_name]

    def get_row_data(self, sheet_name, row):
        sheet = self.get_sheet(sheet_name)
        return [cell.value for cell in sheet[row]]

    def get_all_data(self, sheet_name):
        sheet = self.get_sheet(sheet_name)
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(list(row))
        return data