import pandas as pd


def get_sheet(file_path, sheetName):
    data = pd.read_excel(file_path, sheet_name=sheetName)
    return data


def get_total_number_rows(file_path, sheetName):
    data = get_sheet(file_path, sheetName)
    total_row = data.shape[0]
    return total_row


def get_cell_value(file_path, sheetName, row_number, column_name):
    data = get_sheet(file_path, sheetName)
    value = data.loc[row_number, column_name]
    return value


def write_to_excel(file_path, sheetName, row_number, column_name, value_to_write):
    data = get_sheet(file_path, sheetName)
    data.loc[row_number, column_name] = value_to_write
    write = pd.ExcelWriter(file_path)
    data.to_excel(write, sheet_name=sheetName)
    write.save()