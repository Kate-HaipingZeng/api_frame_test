import os
import xlrd
from common.conf_utils import configer


class ExcelUtils():

    def __init__(self, excel_path, sheet_name):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()
        self.merged = self.get_merged()

    def get_sheet(self):
        #  注意格式
        #  formatting_info=True 支持各种格式信息，默认为False
        wb = xlrd.open_workbook(self.excel_path, formatting_info=True)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    def get_merged(self):
        merged = self.sheet.merged_cells
        return merged

        #  __开头的方法表示私有，只能在这个类里面使用
        #  获取普通单元格的值
    def get_cell_value(self, rows_index, cols_index):
        cell_value = self.sheet.cell_value(rows_index, cols_index)
        return cell_value

    #   获取所有单元格的值
    def get_sheet_value(self, row_index, col_index):
        cell_value = 1
        for (start_rows, end_rows, start_cols, end_cols) in self.merged:
            if row_index >= start_rows and row_index < end_rows:
                if col_index >= start_cols and col_index < end_cols:
                    cell_value = self.get_cell_value(start_rows, start_cols)
                    break
                else:
                    cell_value = self.get_cell_value(row_index, col_index)
            else:
                cell_value = self.get_cell_value(row_index, col_index)
        else:
            cell_value = self.get_cell_value(row_index, col_index)
        return cell_value
    #   获取excel的值
    def get_excel_value(self):
        all_data = []
        #  获取第一行
        first_row = self.sheet.row(0)
        #  对下面的行进行循环找数据
        for n_row in range(1, self.get_row_count()):
            row_dict = {}
            # row_dict["操作步骤"]=excelUtils.get_sheet_value(n_row,1)
            #   获取列
            for n_col in range(0, len(first_row)):
                # row_dict[excelUtils.get_sheet_value(0, n_col)] = excelUtils.get_sheet_value(n_row,n_col)
                #  读取一行的数据放到字典里面去
                row_dict[first_row[n_col].value] = self.get_sheet_value(n_row, n_col)
            #  这个判断条件根据自己的excel文件进行添加
            if row_dict[first_row[2].value] == '否':
                continue
            else:
                #  循环追加数据
                all_data.append(row_dict)
        return all_data



if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    print(current_path)
    excel_path = os.path.join(current_path, '../', configer.TEST_CASE_PATH)
    print(excel_path)
    excelUtils = ExcelUtils(excel_path, 'Sheet1')
    print(excelUtils.get_col_count())
    print(excelUtils.get_row_count())
    for n_row in excelUtils.get_excel_value():
        print(n_row)
    # print(excelUtils.merged)





