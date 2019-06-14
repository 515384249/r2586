# -*- coding: utf-8 -*-
# coding:utf-8


'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import bijiao
from tools import myclass
import xlrd  # excel读工具

from tools.myclass import CellJieGou, OneData

wb = xlrd.open_workbook("E:\北京交通大学办公室号码表(1).xlsx")  # 打开文件  這個文件名要根據傳過來的值確定
sheets = wb.sheet_names()
print((sheets))
for i in range(len(sheets)):
    table = wb.sheet_by_index(i)
    print(table.name)
    nrows = table.nrows  # 行数
    print(nrows)
    ncols = table.ncols  # 列数
    print("列數=%s" % ncols)
    colnames = table.row_values(1)
    print("列名字=%s" % colnames)
    WorkList = []
    cells = []
    lines = []
    realtype = ''
    for i in range(0, nrows):
        row = table.row_values(i)  # 获取每行值
        for j in range(0, ncols):
            if type(row[j]) == float:  # 如果值为float则转换为int,避免出现1输出为1.0的情况
                row[j] = int(row[j])
                row[j] = str(row[j])
            thtype = bijiao.th_type(row[j])
            tdtype = bijiao.td_type(row[j])
            cell = CellJieGou()
            cell.td_type = tdtype
            cell.th_type = thtype
            cell.row_num = i
            cell.col_num = j
            cell.sheet_name = table.name
            k = i
            if cell.td_type == 'dianhua':
                # while k < i:
                #     if table.cell(k, j).value == 'dianhua_th':
                #         realtype = 'dianhuahaoma'
                #         break
                #     k = k - 1
                # if realtype == 'dianhuahaoma':
                cell.read_type = 'dianhua'

                cells.append(cell)
