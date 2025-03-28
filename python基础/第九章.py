#一.json数据格式
# 基本概念：JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，本质是带有特定格式的字符串
#   python与json转换
# 序列化（Python → JSON）：
##准备列表，列表内每一个元素都是字典，将其转换为JSON
import json

from pyecharts.globals import ThemeType

data = [{"name":"张三","age":18}]
json_str = json.dumps(data,ensure_ascii=False)  # 避免中文转义
print(type(data))
print(type(json_str))
print(json_str)
##准备字典，将字典转换为JSON
d = {"name":"周杰伦","addr":"中国"}
json_s = json.dumps(d,ensure_ascii=False)
print(type(d))
print(type(json_s))
print(json_str)

# 反序列化（JSON → Python）
##将JSON字符串转换为Python数据类型[{k: v, k: v}，{k: v, k: v}]
json_str = '[{"name":"李四","age":20}]'
data = json.loads(json_str)
print(type(data))
print(data)
##将JSON字符串转换为Python数据类型{k: v, k: v}
str = '{"name":"周杰伦","addr":"中国"}'
d = json.loads(str)
print(type(str))
print(type(d))
print(d)


#二.pyecharts
#导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

#创建一个折线图对象
line = Line()
#给折线图对象添加x轴的数据
line.add_xaxis(["中国", "美国", "日本"])
#给折线图对象添加y轴的数据
line.add_yaxis("GDP", [30, 20, 10])
#设置全局配置项set_global_opts设置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
#通过render方法，将代码生成图像
line.render()

# 关键配置：
# TitleOpts：标题（位置、内容）。
# LegendOpts：图例显示。
# ToolboxOpts：工具栏（导出图片等）。
# VisualMapOpts：视觉映射（颜色映射）。


#三.地图
# 示例:中国地图
"""
演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
#准备地图对象
map = Map()
#准备数据
data = [
    ("北京市",99),
    ("上海市",199),
    ("山西省",299),
    ("天津市",399),
    ("广东省",499)
]
#添加数据
map.add("测试地图",data,"china")
#设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"}
        ]
    )
)
#绘图
map.render()



#四.柱状图与时间线
#水平柱状图
"""
演示基础柱状图的开发
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
#使用Bar构建基础柱状图
bar = Bar()
#添加x轴数据
bar.add_xaxis(["太原","阳泉","晋中"])
#添加y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
#反转x轴和y轴
bar.reversal_axis()
bar.render()
#设置数值标签在右侧

#时间线柱状图
"""
演示时间线柱状图的开发
"""
from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
#使用Bar构建基础柱状图
bar1 = Bar()
bar2 = Bar()
#添加x轴数据
bar1.add_xaxis(["太原","阳泉","晋中"])
bar2.add_xaxis(["太原","阳泉","晋中"])
#添加y轴数据
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar2.add_yaxis("GDP",[40,30,20],label_opts=LabelOpts(position="right"))
#反转x轴和y轴
bar1.reversal_axis()
bar2.reversal_axis()
#创建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT})
#timeline对象添加bar柱状图
timeline.add(bar1,"2021")
timeline.add(bar2,"2022")
#自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("基础时间线柱状图.html")

















