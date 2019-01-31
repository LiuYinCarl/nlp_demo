import jieba
import docx
import os
from iat import iat
from test_webtts import tts
from start_app import start_app
from play_audio import playMusic


def get_statements(path):
    """
    从单份的实验报告中提取文本
    :path: 文件保存路径
    :return: 文本(str)
    """
    file = docx.Document(path)  # 可修改文件名
    text = ""
    for para in file.paragraphs:
        text += para.text
    for tmp in [' ', '\t', '\n', '，', '。']:
        text = text.replace(tmp, '')
    return text


def seg(text):
    """
    分词
    :param statements:
    :return:
    """
    seg_list = jieba.cut(text)  # 搜索引模擎式
    print(seg_list)
    return list(seg_list)


# 合法的可求相似度的文件拓展名
EFFECTIVE_SUFFIX = ['.docx', '.txt']


def get_file_name(path):
    """
    获取所有的合法文件的文件名
    :param path: 附件的保存路径
    :return: 文件名列表
    """
    for now_path, dirs, files in os.walk(path):
        legal_files = []
        for file in files:
            extension_name = os.path.splitext(file)[1]
            if extension_name in EFFECTIVE_SUFFIX:
                legal_files.append(file)
    return legal_files


keywords = {'打开', '复习', '开启', '启动', '访问'}


if __name__ == '__main__':
    text = iat()
    seg_list = seg(text)
    print(seg_list)
    ms_files = get_file_name('.\\ms_file')
    print(ms_files)
    print(seg_list[1])

    if set(seg_list) & keywords:
        for file in ms_files:
            if str(seg_list[1]) in str(file):
                # get text from docx
                text = get_statements(path='ms_file\\' + file)
                # start MS Word
                start_app(app='Word.Application', filepath=os.getcwd() + '\\ms_file\\' + file)
                # get wav
                tts(text=text)
                # play wav
                playMusic(filename='.\\audio\\xiaoyan.wav')









