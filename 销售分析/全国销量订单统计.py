import pandas as pd

# 1、读取Excel 数据
excel_path = 'F:\Python自动化办公训练营\data\某公司销售数据-全国订单明细.xls'
sales_data = pd.read_excel(excel_path)


# 2、获取数据属性
# print(sales_data.shape)# (8568, 19)
# print(sales_data.columns)


# 3、展示前几条数据
# pd.set_option('display.max_columns', None)
# print(sales_data.head())


###测试区###

# 4、创建获取数据的文件夹
class GetData:

    # 5、创建获取地图数据的函数
    @staticmethod
    def area_data():
        # 获取以省份筛选的对
        # 应数据
        sales_map_data = sales_data['省份'].value_counts().rename_axis('省份').reset_index(name='counts')
        return sales_map_data

    # 6、创建获取条形统计图数据的函数
    def bar_data(self):
        return self.area_data().sort_values("counts")

    # 7、获取散点统计图数据的函数
    def scatter_data(self):

        # 以顾客姓名查询对应销售额的成本总和
        sale_e_x = sales_data.groupby(['顾客姓名'])['销售额'].sum()

        # 以顾客姓名查询对应的运输成本总和
        sale_ys_y = sales_data.groupby(['顾客姓名'])['运输成本'].sum()

        sale_ys_y_list = []

        # 遍历series数据
        for k, v in sale_ys_y.items():
            sale_ys_y_list.append([v, k])

        return sale_e_x, sale_ys_y_list

    # 8、创建面积图提供数据
    def create_area_data(self):
        sales_data['订单日期'] = sales_data['订单日期'].dt.to_period('Y')
        # 按订单日期进行分组统计的销售额
        sale_d_xse_y1 = sales_data.groupby(['订单日期'])['销售额'].sum()
        sale_d_xse_y1_list = []
        for i in sale_d_xse_y1:
            sale_d_xse_y1_list.append(int(i))
        # 按订单日期进行分组统计的利润额
        sale_d_lre_y2 = sales_data.groupby(['订单日期'])['利润额'].sum()
        sale_d_lre_y2_list = []
        for i in sale_d_lre_y2:
            sale_d_lre_y2_list.append(int(i))
        return sale_d_xse_y1_list, sale_d_lre_y2_list

    # 9、创建条形统计图提供数据
    def address_jpg(self):

        name_list = ['技术产品', '家具产品', '办公用品']
        add_list = ['东北', '华东', '华北', '华南', '西北', '西南']
        gruop_data = sales_data.groupby(['产品类别', '区域'])['订单数量'].count()
        db_list = []  # 东北地区数量
        hd_list = []  # 华东地区数量
        hb_list = []  # 华北地区数量
        hn_list = []  # 华南地区数量
        xb_list = []  # 西北地区数量
        xn_list = []  # 西南地区数量
        for name in name_list:
            for add in add_list:
                if add == '东北':
                    db_list.append(str(gruop_data[name][add]))
                if add == '华东':
                    hd_list.append(str(gruop_data[name][add]))
                if add == '华北':
                    hb_list.append(str(gruop_data[name][add]))
                if add == '华南':
                    hn_list.append(str(gruop_data[name][add]))
                if add == '西北':
                    xb_list.append(str(gruop_data[name][add]))
                if add == '西南':
                    xn_list.append(str(gruop_data[name][add]))
        return name_list, db_list, hd_list, hb_list, hn_list, xb_list, xn_list

    # 10、创建饼图提供数据
    def project_pie(self):
        name_list = ['技术产品', '家具产品', '办公用品']
        gruop_data = sales_data.groupby(['产品类别'])['订单数量'].count()
        pie_list = []
        for i in name_list:
            pie_list.append([i, str(gruop_data[i])])
        return pie_list


if __name__ == '__main__':
    print(GetData().project_pie())
