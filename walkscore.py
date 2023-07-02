# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image
import pandas as pd


# 设置Favicon
st.set_page_config(page_icon="favicon.ico")

# 标题
st.title('步行指数：Walkscore:walking:')
st.subheader('&emsp;&emsp;&emsp;—— 量化小区周边设施远近与便捷程度的可靠指标')

# 作者
st.markdown('''##### 版权所有：hollisyang&nbsp;&nbsp;from&nbsp;&nbsp;ECNU:globe_with_meridians:''')

# 字数
st.markdown('全文约 :blue[**1095**] 字，阅读大约需要 :blue[**2.5**] 分钟。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% 前言
st.markdown('### 前言')
st.markdown('&emsp;&emsp;随着时代的发展，居民对自己的生活标准要求越来越高，对自己周围的设施要求相应提高。人们的活动范围大多围绕着工作和居住的场所，由此产生了 :blue[**工作圈**] 和 :blue[**生活圈**] 这两个概念。生活圈中的幸福感大多来源于日常生活的便捷，例如炒菜忘了买葱，下楼去趟便利店，两三分钟后拿着一把小葱开了门继续做饭。亦或是吃饱饭足后，和家人漫步去旁边的公园欣赏夜色，或者去周围的电影院看个电影，这就是人们所期待的现代生活方式。')
st.markdown('&emsp;&emsp;因此，国内外大量学者围绕现代城市生活的便捷性展开了诸多专业研究，其中涉及 :blue[**步行指数**] 的与周遭生活圈的便捷性研究，就是既有理论数据又有实用价值的应用性科学研究之一。')
st.markdown('&emsp;&emsp;步行指数（Walkscore）在2007年由美国学者&nbsp;:blue[**Jesse Kocher**]&nbsp;等人提出，在基本公共服务可步行性的研究产生深远影响。步行指数的测算方法由&nbsp;:blue[**卢银桃和王德**]&nbsp;于2012年引入国内。')
st.markdown('&emsp;&emsp;作为一种量化标准，Walkscore主要用来测算人们去到这些周边设施的远近程度和步行的便捷程度。在提倡建设智慧城市理念的今天，社区生活圈的构建体现了以人为本的发展理念，重视个体需求的特性。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% 步行指数的分类
st.markdown('### 步行指数的分类')
st.markdown('&emsp;&emsp;步行指数算法包含两个层面，即&nbsp;:blue[**单点步行指数**]&nbsp;和&nbsp; :blue[**面域步行指数**]&nbsp;。')
st.markdown('''- 单点步行指数是指一个具体地点的可步行性，如广场、学校、住宅等。
- 面域步行指数则是基于多个单点步行指数而计算得出的区域可步行性，如街区、社区、城市等。
''')

sf = Image.open(r'./images/sf_walkscore.jpg')
jkv = Image.open(r'./images/jkv_walkscore.jpg')
sf = sf.resize((300, 300))
jkv = jkv.resize((330, 300))

# 使用st._columns()创建两个列
col1, col2 = st.columns(2)
# 在第一个列中显示第一幅图像
with col1:
    st.image(sf, caption='美国旧金山市面域步行指数')
# 在第二个列中显示第二幅图像
with col2:
    st.image(jkv, caption='美国杰克逊维尔市面域步行指数')

st.markdown('&emsp;&emsp;在本系统中，您可以通过应用程序所提供的交互式按钮与地图获得各小区的唯一ID号，输入ID号后，程序将自动计算该小区的:blue[**单点步行指数**]。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% 具体算法
st.markdown('### 具体算法')
st.markdown('&emsp;&emsp;计算步行指数Walkscore需要准备设施分类与权重衰减表：基于设施类别及权重对不同设施赋予一定权值，并通过考虑步行距离的衰减效应，设置基于距离的衰减系数以修正不同距离的设施权重，最终累加后等比例扩大至100。')
st.markdown('&emsp;&emsp;由于我国的实际国情，本程序中所使用的设施分类和权重衰减表如下：')

# 设施分类表
st.markdown('**设施分类表**')
weight = {
  '餐饮': [0.75, 0.45, 0.25, 0.25, 0.225, 0.225, 0.225, 0.225, 0.2, 0.2], # 3
  '购物': [1, 0.75, 0.75, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25], # 4.5
  '生活服务': [0.5, 0.25, 0.25], # 1
  '休闲娱乐': [0.5, 0.5, 0.25, 0.25], # 1.5
  '运动健身': [1], # 1
  '医疗': [1], # 1
  '公园': [1], # 1
  '学校': [1], # 1
  '银行': [1] # 1
}

df = pd.DataFrame.from_dict(weight, orient='index')
df = df.rename(columns=lambda x: x + 1)  # 将列名替换为数字
df['Σ'] = df.sum(axis=1)
df = df.fillna('/')  # 将NaN值替换为/
st.dataframe(df)

# 权重衰减表
st.markdown('**权重衰减表**')
data = {
    '距离': ['0-400m', '400-600m', '>1000m'],
    '衰减系数': ['1', '0.8', '0.12']
}
df_sj = pd.DataFrame(data)
st.dataframe(df_sj)

# 解释
st.markdown('''
            - 设施分类表中定义了$9$种不同设施及其权重。
            - 不同设施列入计算的数量不同，为体现设施的多样性，将设施分类表中的&nbsp;$1,2,3...,10$&nbsp;定义为设施的个数。如某地点周边有餐饮设施$3$处，则在餐饮设施一项中得分为&nbsp;&nbsp;$0.75+0.45+0.25=1.45$。
            - 不同距离的设施具有不同的衰减系数。例如距离$400-600m$内的设施，其衰减系数为$0.8$，计算步行得分时需要将分类表中对应权重乘以$0.8$。
            - 所有设施的权重和为$15$，将每一类设施的得分累加后需要将其等比例扩大至$100$得到最终的步行指数Walkscore。
            ''')
st.markdown("<hr>", unsafe_allow_html=True)


#%% 步行指数分级
st.markdown('### 步行指数分级')
st.markdown('&emsp;&emsp;步行指数Walkscore满分为$100$，可根据具体得分将其分为$5$个不同的等级：')
chart = Image.open(r'./images/walkscore.jpg')
st.image(chart)
st.markdown("<hr>", unsafe_allow_html=True)


#%% 了解更多 & 数据来源
st.markdown('##### 了解住宅评价的更多维度')
st.markdown('&emsp;&emsp;环境感知角度：  https://hollisyang-env.streamlit.app/')
st.markdown('&emsp;&emsp;公共交通可达性水平（PTAL）角度：  https://hollisyang-ptal.streamlit.app/')
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown('##### 数据来源')
st.markdown('&emsp;&emsp;本系统所用二手房数据主要来源于链家  https://sh.lianjia.com/  ；计算步行指数Walkscore时所使用的POI数据来源于百度地图开放平台  https://lbsyun.baidu.com/  所提供的地点检索API。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% liking
st.markdown('感谢您的阅读！')
if st.button(':sparkling_heart: Like :sparkling_heart:'):
    st.write('Thank you for liking！')
    st.balloons()