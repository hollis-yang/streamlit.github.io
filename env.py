# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image
import pandas as pd


# 设置Favicon
st.set_page_config(page_icon="favicon.ico")

# 标题
st.title('环境感知:deciduous_tree:')
st.subheader('&emsp;&emsp;&emsp;&emsp;—— 衡量城市空间品质的重要参考')

# 作者
st.markdown('''##### 版权所有：hollisyang&nbsp;&nbsp;from&nbsp;&nbsp;ECNU:globe_with_meridians:''')

# 字数
st.markdown('全文约 :blue[**1560**] 字，阅读大约需要 :blue[**3.5**] 分钟。')
st.markdown("<hr>", unsafe_allow_html=True)

#%% 前言
st.markdown('### 前言')
st.markdown('&emsp;&emsp;近年来，国家宏观政策不断强调“以人为本”，对于城市来说，城市规划逐步从“增长优先”向“品质提升”转型，市民日益提升的空间品质需求催生了对于人本视角街道环境品质的研究。国内外实证研究已证明，具有高可见度的街道绿化与天空能直接改善市民对于其所在社区的空间品质感受，同时也能有效增进场所感、舒缓压力和促进户外活动。除了宏观政策对“以人为本”的转型与要求外，当前中国新型城镇化也逐步迈入对于空间品质需要日益提升的阶段。因此，对于街道绿化与天空可视率正成为重点关注对象之一。')
st.markdown('&emsp;&emsp;然而，国内外对街道空间品质的测度主要源自遥感影像。这种自上而下鸟瞰视角的测度不仅不能全面地反应街道空间品质特征，也无法做到与市民的实际感受一致。因此，基于人本视角的街道环境感知主要源于在当今大数据时代新兴的街景大数据。在过去的10年中，以百度街景、谷歌街景等为代表的街景数据已被广泛运用在街道安全程度、绿视率、天空可视率等研究当中。')
st.markdown('&emsp;&emsp;另外，随着人工智能的不断发展，机器学习技术为自动化提取街景图片中的绿色特征与天空特征提供了新的可能。以SegNet、PSPNet、DeepLab等为代表的深度学习模型能够准确有效地识别图片中的天空、人行道、车道、建筑、绿化等多重要素；而以支持向量机等为代表的机器学习算法则能根据图片特征对于街景数据进行高效清洗和特征识别。')

deeplab = Image.open('./images/deeplab.png')
st.image(deeplab, 'DeepLab v3+语义分割模型整体架构')
st.markdown("<hr>", unsafe_allow_html=True)


#%% GluonCV
st.markdown('### GluonCV')
st.markdown('&emsp;&emsp;GluonCV是一个基于MXNet深度学习框架的计算机视觉工具包，旨在帮助研究人员和开发人员构建和训练深度学习模型来解决计算机视觉任务，其最主要的特点是其提供了一系列预训练模型与灵活API，使得开发者使用和调整模型变得简单且高效。')
modelzoo = Image.open('./images/modelzoo.jpg')
st.image(modelzoo, 'GluonCV所提供的模型库（包括分类、目标检测、分割、姿态估计、动作识别、深度预测）')
st.markdown('&emsp;&emsp;语义分割是计算机视觉的重要分支，其目标是将图像中的每个像素分配给不同的语义类别。例如，在本程序中使用了语音分割技术标记图像中像素的不同类别，如道路、植被、天空、行人等。除GIS街景语义分割外，这种像素级别的细粒度标注还广泛应用于自动驾驶、医学图像分析等。')
st.markdown('&emsp;&emsp;GluonCV中提供了一些经过大规模数据集训练和验证的语义分割模型，如FCN、DeepLab和PSPNet等。这些模型具有强大的感知能力和准确性，并且已经在各种标准数据集上进行了广泛测试和验证。')
# ade20k
res1 = {
    "Name": ["fcn_resnet50_ade", "fcn_resnet101_ade", "psp_resnet50_ade", "psp_resnet101_ade", "deeplab_resnet50_ade", "deeplab_resnet101_ade", "deeplab_resnest50_ade", "deeplab_resnest101_ade", "deeplab_resnest200_ade", "deeplab_resnest269_ade"],
    "Method": ["FCN", "FCN", "PSP", "PSP", "DeepLabV3", "DeepLabV3", "DeepLabV3 + ResNeSt", "DeepLabV3 + ResNeSt", "DeepLabV3 + ResNeSt", "DeepLabV3 + ResNeSt"],
    "pixAcc": [79, 80.6, 80.1, 80.8, 80.5, 81.1, 81.2, 82.1, 82.5, 82.6],
    "mIoU": [39.5, 41.6, 41.5, 43.3, 42.5, 44.1, 45.1, 46.9, 48.4, 47.6]
}
res1 = pd.DataFrame(res1)
res1.index = range(1, len(res1) + 1)
st.dataframe(res1)
st.markdown('<p style="text-align: center; font-size:14px; color:rgba(250, 250, 250, 0.6);">ADE20K数据集下各训练模型对比</p>', unsafe_allow_html=True)
# cityscapes
res2 = {
    "Name": [
        "psp_resnet101_citys",
        "deeplab_resnet50_citys",
        "deeplab_resnet101_citys",
        "danet_resnet50_citys",
        "danet_resnet101_citys",
        "icnet_resnet50_citys",
        "fastscnn_citys"
    ],
    "Method": [
        "PSP",
        "DeepLabV3",
        "DeepLabV3",
        "DANet",
        "DANet",
        "ICNet",
        "FastSCNN"
    ],
    "pixAcc": [96.4, 96.3, 96.4, 96.3, 96.5, 95.5, 95.1],
    "mIoU": [79.9, 78.7, 79.4, 78.5, 80.1, 74.5, 72.3]
}
res2 = pd.DataFrame(res2)
res2.index = range(1, len(res2) + 1)
st.dataframe(res2)
st.markdown('<p style="text-align: center; font-size:14px; color:rgba(250, 250, 250, 0.6);">Cityscapes数据集下各训练模型对比</p>', unsafe_allow_html=True)
st.markdown('&emsp;&emsp;经过对上海市街景图片在GluonCV提供的不同模型与数据集下进行测试，本程序在计算环境感知得分时选择调用:blue[**网络结构为resnet101的DeeplabV3模型**]，:blue[**训练集为ADE20K**]，该模型的pixAcc（像素精度）为$81.1$；mIoU（平均交并比）为$44.1$。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% 环境感知得分的计算流程
st.markdown('### 环境感知得分的计算流程')
st.markdown('&emsp;&emsp;本系统所使用的街景图像来自百度地图开放平台全景静态图API，通过输入视线水平和垂直方向角度及视点位置（住宅经纬度）可以获得住宅的街景图。为了更贴近人本视角的要求，在获取街景时统一设置垂直角度为$0\degree$，即平视。在视线水平角度方向，分别抓取前后视、左右视四个方向共$4$张街景图片，每个视线方向的视角为$90\degree$。这样的采集形式可以全面囊括住宅周围的街道环境。')
fov = Image.open('./images/example.jpg')
st.image(fov, '四视角街景图像获取')
st.markdown('&emsp;&emsp;待采集完$4$张街景图片后，通过调用GluonCV深度学习模型进行语义分割，提取其中的植被、天空元素，分别计算每一张街景的绿视率和天空可视率（植被或天空像元数/图片总像元数）。接着，计算每张街景的绿视率和天空可视率之和。最终，取$4$张街景绿视率和天空可视率的算数平均值为该住宅的环境感知得分。')
lujiazui = Image.open('./images/lujiazui.jpg')
st.image(lujiazui, '陆家嘴附近某小区四视角街景语义分割结果')

st.markdown("<hr>", unsafe_allow_html=True)




#%% 了解更多 & 数据来源
st.markdown('##### 了解住宅评价的更多维度')
st.markdown('&emsp;&emsp;步行指数（Walkscore）角度：  https://hollisyang-walkscore.streamlit.app/')
st.markdown('&emsp;&emsp;公共交通可达性水平（PTAL）角度：  https://hollisyang-ptal.streamlit.app/')
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown('##### 数据来源')
st.markdown('&emsp;&emsp;本系统所用二手房数据主要来源于链家  https://sh.lianjia.com/  ；计算环境感知得分时所使用的街景数据来源于百度地图开放平台  https://lbsyun.baidu.com/  所提供的全景静态图API；街景语义分割所用深度学习模型来源于计算机视觉开源深度学习工具包GluonCV  https://cv.gluon.ai/contents.html 。')
st.markdown("<hr>", unsafe_allow_html=True)


#%% liking
st.markdown('感谢您的阅读！')
if st.button(':sparkling_heart: Like :sparkling_heart:'):
    st.write('Thank you for liking！')
    st.balloons()