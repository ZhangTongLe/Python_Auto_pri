from bs4 import BeautifulSoup
from pyecharts.charts import Pie, Map, Geo, Line, Bar, Timeline, Liquid, WordCloud, Page, Scatter
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType, ChartType

from pyecharts import options as opts

from 销售分析.全国销量订单统计 import GetData


class Report(GetData):

    # 创建地图
    def area_base(self):
        area_data = self.area_data()

        area_map = (
            Map()
                .add("地图", [list(z) for z in zip(list(area_data["省份"]), list(area_data["counts"]))], "china",
                     is_map_symbol_show=True, label_opts=opts.LabelOpts(color="#fff"),
                     tooltip_opts=opts.TooltipOpts(is_show=True), zoom=1.2, center=[105, 30])
                .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
                .set_global_opts(title_opts=opts.TitleOpts(title="全国各省销量明细", pos_top='5%',
                                                           title_textstyle_opts=opts.TextStyleOpts(color="#FF0000")),
                                 visualmap_opts=opts.VisualMapOpts(max_=1600, is_piecewise=True))
            # .render("map_base.html")
        )

        return area_map

    # 创建条形统计图
    def bar_base(self):
        bar_data = self.area_data().sort_values("counts")
        c = (
            Bar()
                .add_xaxis(list(bar_data["省份"]))
                .add_yaxis('省份排名统计图', list(bar_data["counts"]))
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(title_opts=opts.TitleOpts(title="城市排名"))
            # .render("省份统计排名.html")
        )
        return c

    # 创建散点图
    def scatter_base(self):
        sale_e_x, sale_ys_y_list = self.scatter_data()
        c = (
            Scatter()
                .add_xaxis(sale_e_x)

                .add_yaxis("运输成本", sale_ys_y_list, symbol_size=5, label_opts=opts.LabelOpts(is_show=False), )

                .set_global_opts(
                title_opts=opts.TitleOpts(title="顾客的运输与销售"),
                visualmap_opts=opts.VisualMapOpts(
                    type_="color", max_=150, min_=20, dimension=1
                ),

                # 显示分隔线
                xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
                yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
                #
                tooltip_opts=opts.TooltipOpts(  # tooltip是鼠标移上去的提示
                    formatter=JsCode(
                        "function(params){return '运输成本:'+ params.value[1].toFixed(2) + '<br>'+ '销售额:'+ params.value[0].toFixed(2)+ '<br>' + '顾客姓名：' + params.value[2] }",

                    )
                ),

            )
            # .render("散点图.html")
        )
        return c

    # 创建面积图
    def create_area_jpg(self):
        sale_d_xse_y1_list, sale_d_lre_y2_list = self.create_area_data()

        c = (
            Line()
                .add_xaxis(['2009', '2010', '2011', '2012'])
                .add_yaxis("销售额", sale_d_xse_y1_list, is_smooth=True)
                .add_yaxis("利润额", sale_d_lre_y2_list, is_smooth=True)
                .set_series_opts(
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="面积图"),
                xaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    is_scale=False,
                    boundary_gap=False,
                ),
            )
            # .render("面积图.html")
        )

        return c

    # 创建产品分类地区统计图
    def create_type_jpg(self):
        name_list, db_list, hd_list, hb_list, hn_list, xb_list, xn_list = self.address_jpg()

        c = (
            Bar({"theme": ThemeType.MACARONS})
                .add_xaxis(name_list)
                .add_yaxis("东北区域", db_list)
                .add_yaxis("华东区域", hd_list)
                .add_yaxis("华北区域", hb_list)
                .add_yaxis("华南区域", hn_list)
                .add_yaxis("西北区域", xb_list)
                .add_yaxis("西南区域", xn_list)

            #     .set_global_opts(
            #     title_opts={"text": "订单数量"}
            # )
            # .render("条形图.html")
        )
        return c

    # 创建产品分类饼图
    def create_pie_jpg(self):
        pie_list = self.project_pie()
        c = (
            Pie()
                .add("", pie_list)
                .set_global_opts(title_opts=opts.TitleOpts(title="饼图"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            # .render("pie.html")
        )
        return c

    # 创建仪表盘
    def many_report(self):
        # page = Page(layout=Page.DraggablePageLayout)
        # page.add(Report().area_base(), Report().bar_base(), Report().scatter_base(), Report().create_area_jpg(),
        #          Report().create_type_jpg(),Report().create_pie_jpg())

        page = (Page(page_title="全国订单详情")
                .add(Report().area_base())
                .add(Report().bar_base())
                .add(Report().scatter_base())
                .add(Report().create_area_jpg())
                .add(Report().create_type_jpg())
                .add(Report().create_pie_jpg())

                ).render('全国销售统计.html')

    # 把地图数据写出到html
    def write_html(self):
        with open("全国销售统计.html", "r+", encoding='utf-8') as html:
            html_bf = BeautifulSoup(html, 'lxml')
            divs = html_bf.select('.chart-container')

            # 全国地图销量明细
            divs[0][
                'style'] = "width:411px;height:303px;position:absolute;top:20px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"

            # 省份排名
            divs[1][
                "style"] = "width:309px;height:405px;position:absolute;top:313px;left:1000px;border-style:solid;border-color:#444444;border-width:0px;"

            # 顾客的运输成本和销售额，散点图
            divs[2][
                "style"] = "width:400px;height:303px;position:absolute;top:350px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"

            # 面积图，按年分的销售额与利润额
            divs[3][
                "style"] = "width:460px;height:304px;position:absolute;top:400px;left:440px;border-style:solid;border-color:#444444;border-width:0px;"

            # 产品分类订单数量明细
            divs[4][
                "style"] = "width:460px;height:405px;position:absolute;top:20px;left:440px;border-style:solid;border-color:#444444;border-width:0px;"

            # 饼图产品分类明细
            divs[5][
                "style"] = "width:400px;height:300px;position:absolute;top:20px;left:1000px;border-style:solid;border-color:#444444;border-width:0px;"

            body = html_bf.find("body")

            body["style"] = 'background-image:"F:\\FriendCloud\\销售分析\\bg.jpg"'

            html_new = str(html_bf)
            html.seek(0, 0)
            html.truncate()
            html.write(html_new)
            html.close()


if __name__ == '__main__':
    # Report().area_base()
    # Report().bar_base()
    # Report().scatter_base()
    Report().many_report()
    Report().write_html()
    print("报表完成")
