'''
1.修改要处理的文件的路径 lu_jing1

2.修改要插入的关键词路径 lu_jing2

3.修改处理后的文件路径 lu_jing3

4.【可选项，默认文墨插入3个关键词】修改文章末尾要插入的关键词数量

'''


import os,re
import random


lu_jing1 = r'C:\Users\Administrator\Desktop\文本处理\要处理的文本'
# 关键词路径
lu_jing2 = r'C:\Users\Administrator\Desktop\关键词库\比尔盖茨推荐书\比尔盖茨书'
lu_jing3 = r'C:\Users\Administrator\Desktop\文本处理\处理后的文本'
# 关键词数量
keywords_Number = 4


#读取文件名
def eachFile(filepath):
    file_pash_list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s'%(filepath,allDir))
        file_pash_list.append(child)
    return file_pash_list

def save(content,file_name):
    # 3.修改处理后的文件路径
    with open(r'{}\{}.txt'.format(lu_jing3,file_name),'w',encoding='utf-8') as f:
        f.write(content)
        f.close()

def run():


    # 1.修改要处理的文件的路径
    paths = eachFile(lu_jing1)

    for inx, m_path in enumerate(paths):
        file_name = m_path.split("\\")[-1].split(".")[-2]
        # print(file_name)
        f = open(m_path, 'r', encoding='utf-8')
        read = f.readlines()
        read_str = ''.join(read)
        f.close()

        # 2.修改要插入的关键词路径
        # 打开关键词库
        keywords = open(lu_jing2+'.txt', 'r', encoding='utf-8').readlines()
        keywords_one = [x.strip() for x in random.sample(keywords, 1)]
        # 4.【可选项，默认文墨插入3个关键词】修改文章末尾要插入的关键词数量
        keywords_three = [x.strip() for x in random.sample(keywords, keywords_Number)]

        content ="<h2>{}</h2>".format(keywords_one[0]) + read_str +"<h2>关于{}的相关词：</h2>".format(keywords_one[0])+"<p>"+','.join(keywords_three) + "</p>"
        title = "【{}】".format(keywords_one[0]) + file_name
        save(content, title)
        print('第{}个文件处理完成,文件名:{}'.format((inx + 1),title))


if __name__ == '__main__':
    run()