#从之前的后端代码文件中引入generate_script
import streamlit as st
from utils import generate_script

st.title("视频脚本生成器")
#侧边栏弄一个输入API密钥的
with st.sidebar:
    openai_api_key= st.text_input("请输入OpenAI API密钥：",type="password")
    st.markdown("[获取OpenAI API密钥](https://openai.com/api/)")
#设置一些输入参数的
subject= st.text_input("请输入视频的主题")
video_length= st.number_input("请输入视频的大致时长（单位：分钟）", min_value=0.1,step=0.1)
creativity=st.slider("请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）",min_value=0.0,value=0.2,max_value=1.0,step=0.1)
#设置提交按钮
submit= st.button("生成脚本")
#如果上面没有达成条件 要求重新输入 并且停止运行程序
if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not video_length:
    st.info("请输入视频的大致时长")
    st.stop()
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()
#上面满足条件则......一个旋转按钮表示思考，将之前generate_script返回的title,search_result,script赋值给title,search_result,script，注意要一一对齐，要么可能出现标题那里出现维基百科信息的情况
if submit:
    with st.spinner("AI 思考中......请稍等"):
        title,search_result,script = generate_script(subject,video_length,creativity,openai_api_key)
    st.success("视频脚本已生成")
    st.subheader("标题：")
    st.write(title)
    st.subheader("视频脚本：")
    st.write(script)
    with st.expander("维基百科搜索结果"):
        st.info(search_result)






