

class CellJieGou:
    """一个简单的类实例"""
    sheet_name = ''
    table_name = ''
    row_num = 0
    col_num = 0
    th_type = ''
    td_type = ''
    dianhua = ''
    read_type = ''

    def __init__(self):
        pass

    def get_th_type(self):
        pass

    def get_td_type(self):
        pass

    def get_dianhua(self):
        # 往本行的两侧找
        pass

    def get_real_type(self):
        pass


class OneData:
    yuan = ''
    xi = ''
    xingming = ''
    dianhua = ''
    youxiang = ''
    dizhi = ''
    zhiwu = ''
    id = ''
    cells = []

    def __init__(self, realpart, imagpart):
        pass
# 1先找电话，根据电话建立 onedata实体， 赋值dianhua，
# 2  实体  前几列是否有电话
# 3 没有的话，找前几列的cell，匹配对应的type
# 4  有的话  找前一个电话 <olnum <self.colnum 的cell ,匹配对应的 type
# 5  给 属性赋值
# 6  将实体写入数据库
#
