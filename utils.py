from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
from openai import api_key
# import os

#设置一个函数 这样之后就可以通过调用它来得到脚本的内容
def generate_script(subject,video_length,creativity,api_key):
#设置标题提示模版和脚本提示模版
    title_Template=ChatPromptTemplate.from_messages(
        [
            ("human","请为{subject}这个主题的视频想一个吸引人的标题")
        ]
    )
    Script_Template=ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。
             脚本内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽略：
             ```{wikipedia_search}```""")
        ]
    )
#调用api
    model=ChatOpenAI(model="gpt-4o-mini",openai_api_key=api_key,temperature=creativity)
#把提示词模版和ai连接起来
    title_chain = title_Template | model
    Script_Chain=Script_Template | model

#引入参数
    title=title_chain.invoke({"subject":subject}).content
    search=WikipediaAPIWrapper()
    search_result=search.run(subject)

    script=Script_Chain.invoke({"title":title,"duration":video_length,"wikipedia_search":search_result}).content
#返回得到的内容
    return title,search_result,script

# print(generate_script("sora模型", 1, 0.7, os.getenv("OPENAI_API_KEY")))