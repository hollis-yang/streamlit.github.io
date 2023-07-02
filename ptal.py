# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image


# 设置Favicon
st.set_page_config(page_icon="favicon.ico")

# 标题
st.title('公共交通可达性水平：PTAL:metro:')
st.subheader('&emsp;&emsp;&emsp;&emsp;—— 一种综合性公共交通网络质量评价体系')

# 作者
st.markdown('''##### 版权所有：hollisyang&nbsp;&nbsp;from&nbsp;&nbsp;ECNU:globe_with_meridians:''')

# 字数
st.markdown('全文约 :blue[**1525**] 字，阅读大约需要 :blue[**3.5**] 分钟。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% 前言
st.markdown('### 前言')
st.markdown('&emsp;&emsp;公共交通引导城市发展（TOD）的规划理念自2000年左右开始，随着国内城市轨道交通建设提速而进入公众视野。但长期以来，TOD理念在国内缺乏配套制度与指标支撑，常用的站点覆盖率、线网密度不足以为公共交通的改善提供科学有效的调节依据。国内城市迫切需要更加先进的算法体系为公共交通设施建设及规划、决策、评估提供有力支持。')
st.markdown('&emsp;&emsp;公共交通可达性水平（PTAL）作为TOD理念指引下的量化分析工具，在世界范围内获得了广泛研究和应用，相对同类型的评估方法，PTAL则是一种综合性公共交通网络质量评价体系，其应用对于我国现今城镇化精明增长和精细治理，实现城市交通可持续发展有着重要的价值。')
st.markdown('&emsp;&emsp;公共交通可达性水平PTAL（Public Transport Access Level）算法于1992年在伦敦Hammersmith and Fulham地区率先引入，并在2001年扩展到了整个伦敦市，作为大伦敦地区评估公共交通可达性水平的标准方法。目前，该方法已推广到了荷兰、澳大利亚、新西兰、印度和新加坡等国家。国内部分城市，如北京、上海、天津、武汉也在积极探索使用PTAL作为城市公共交通建设运营过程中的参照指标。')
st.markdown('&emsp;&emsp;PTAL能够评估城市中某一地点获取公共交通服务的便利程度，它一方面反映了评估点所在区域的公共交通:blue[**线网密度**]，另一方面也将:blue[**线网服务能力**]，如发班间隔、线路的可靠性等纳入了考量范围。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% 分级标准
st.markdown('### PTAL分级标准')
st.markdown('&emsp;&emsp;根据伦敦交通局（TfL）发布的《交通评估最佳实践指导手册》中，PTAL一共分为从0到6六个等级，等级越高表示可达性越好。其中等级1和等级6又被进一步细分为1a、1b和6a、6b。各个级别对应的PTAL大小与颜色如下表所示：')

chart = Image.open('./images/ptal.jpg')
st.image(chart, caption='Tfl规定的PTAL分类标准')
london = Image.open('./images/london.jpg')
st.image(london, caption='大伦敦地区PTAL热力图（图源：Accessing Transport Connectivity in London）')
st.markdown("<hr>", unsafe_allow_html=True)


#%% WebCAT
st.markdown('### WebCAT')
st.markdown('&emsp;&emsp;伦敦交通局专门开发了网页端的“PTAL可视化工具”——WebCAT。这是一个基于PTAL向公众开放的面向公共交通可达性评估的定制化快速查询网站。该网站支持基于地理编码以及现状年和规划年的比较查询，在为城市规划决策服务的同时，也为普通百姓的居住选址、公交出行评估提供了开放、专业的途径。')
st.markdown('&emsp;&emsp;WebCAT的网址为： https://tfl.gov.uk/info-for/urban-planning-and-construction/planning-with-webcat/webcat')

webcat = Image.open('./images/webcat.jpg')
st.image(webcat, caption='WebCAT')
st.markdown("<hr>", unsafe_allow_html=True)


#%% PTAL算法详解
st.markdown('### PTAL算法详解')
# 1
st.markdown('##### step1：获取公共交通发车间隔')
st.markdown('&emsp;&emsp;上海市地铁发车间隔数据主要来源于上海地铁官网（取工作日早高峰列车间隔）；而公交发车间隔主要根据不同行政区级别（市区/郊区），设置不同的发车间隔（$6/8/12/18$分钟）。')
# 2
st.markdown('##### step2：获取住宅周边地铁站与公交站点')
st.markdown('&emsp;&emsp;利用百度地图开放平台提供的地点检索API，以住宅为中心，搜索$800m$范围内地铁站与$500m$范围内公交车站。')
# 3
st.markdown('##### step3：计算住宅至公共交通站点步行时间$WT$')
st.markdown('&emsp;&emsp;利用百度地图开放平台提供的步行路径规划服务得到住宅与公共交通站点的步行距离$distance$，并以步行速度$4.8km/h$计算住宅至公共交通站点的步行时间$WN$。')
st.latex(r'WT = \frac{{\text{{distance}}}}{{4.8 \, \text{{km/h}}}} \, (\text{{min}})')
# 4
st.markdown('##### step4：计算平均等待时间$AWT$')
st.markdown('&emsp;&emsp;对于公共交通来说，由于乘客到站时间整体呈正态分布，因此取平均等待时间$AWT$为发车间隔$f$的一半。同时，应考虑车次到站时间偏差，因此在计算$AWT$时，还需加上$K$分钟的缓冲时间（公交取$2$分钟；地铁取$0.75$分钟）。')
st.latex(r'AWT = \frac{{0.5 \times 60}}{{f}} + K')
# 5
st.markdown('##### step5：计算总体可达时间$TWT$')
st.latex(r'TAT = WT + AWT')
# 6
st.markdown('##### step6：分别计算各公交、地铁线路服务频率$EDF$')
st.latex(r'EDF = \frac{30}{TAT}')
# 7
st.markdown(r'##### step7：计算公交可达性指数$AI_{m}$')
st.markdown(r'&emsp;&emsp;$AI_{m}$的计算需要公交与地铁分别进行（但两者的算法一致）。具体计算方法为：取小区周边地铁/公交中某一方式$EDF$中的最大值$EDF_{max}$，赋予其权重为$1$，其余线路的$EDF$值权重为$0.5$，使用以下公式计算此方式下的公交可达性指数$AI_{m}$：')
st.latex(r'AIm = EDF_{\text{max}} + 0.5 \times \sum_{其余线路} EDF')
# 8
st.markdown('##### step8：计算公共交通可达性指数$PTAL$')
st.markdown('&emsp;&emsp;由此，住宅小区的$PTAL$为地铁的$AI$值和公交的$AI$值相加。')
st.latex(r'PTAL = K_{\text{地铁}} \times AI_{\text{地铁}} + K_{\text{公交}} \times AI_{\text{公交}}')
# shanghai
shanghai = Image.open('./images/shanghai.jpg')
st.image(shanghai, caption='上海市PTAL热力图（图源：朱春节,张天然,王波.交通可达性在上海市的应用研究[J].交通与港航,2022,9(01):2-10.）')
st.markdown("<hr>", unsafe_allow_html=True)


#%% 了解更多 & 数据来源
st.markdown('##### 了解住宅评价的更多维度')
st.markdown('&emsp;&emsp;步行指数（Walkscore）角度：  https://hollisyang-walkscore.streamlit.app/')
st.markdown('&emsp;&emsp;环境感知角度：  https://hollisyang-env.streamlit.app/')
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown('##### 数据来源')
st.markdown('&emsp;&emsp;本系统所用二手房数据主要来源于链家  https://sh.lianjia.com/  ；计算公共交通可达性水平PTAL时所使用的地铁站、公交车站数据均来源于百度地图开放平台  https://lbsyun.baidu.com/  所提供的地点检索API； 地铁发车间隔来源于上海地铁官网  http://service.shmetro.com/hcskb/index.htm 。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% liking
st.markdown('感谢您的阅读！')
if st.button(':sparkling_heart: Like :sparkling_heart:'):
    st.write('Thank you for liking！')
    st.balloons()