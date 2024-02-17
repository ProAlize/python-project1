from fuzzywuzzy import fuzz
from tqdm import tqdm
import time
import logging
import argparse

logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')

welcome_str = """
*************************************************
城市名称拼音首字母查询系统
1.新建城市名
2.查询城市信息
3.显示全部城市信息
4.删除城市信息
5.修改城市信息


0.退出
*************************************************
"""

parser = argparse.ArgumentParser(description='模糊匹配')
parser.add_argument('-k', '--keycheck', type=str, required=True, help='待匹配的城市名称')
parser.add_argument('-m', '--model', type=str, required=True, help='匹配模式：1为简单匹配，2为无顺序匹配')
args = parser.parse_args()


def fuzz_matching(allofkey, keycheck, model):
    if (model == '1'):
        score = fuzz.ratio(allofkey, keycheck)
        return score
    if (model == '2'):
        score = fuzz.token_sort_ratio(allofkey, keycheck)
        return score#保留匹配分数


if __name__ == '__main__':

    while True:
        # 主程序，死循环
        print(welcome_str)
        action = input("请选择要进行的操作:")
        if action == '0':
            print("再见")
            break
        # 结束条件

        elif action == '1':
            """print("新建城市名")
            Chinesename = input("请输入中文名称")
            name = input("请输入拼音首字母")
            new_dic={
            'Chinesename':Chinesename,
            'name':name
            }
            file = open('cities.txt', 'a')
            js = json.dumps(new_dic,ensure_ascii=False)
            file.write(js)
            file.close()"""
            Chinesename = input("请输入城市中文名称：")
            name = input("请输入城市名称的拼音首字母大写：")
            file = open('cities.txt', mode='a')
            file.writelines(['\n', Chinesename, ':', name])
            print("已成功添加！")
            file.close()


        elif action == '2':
            print("查询城市信息")
            fr = open('cities.txt', 'r')
            dic = {}
            keys = []  # 用来存储读取的顺序
            for line in fr:
                if line.isspace():
                    continue
                else:
                    v = line.strip().split(':')
                    dic[v[0]] = v[1]
                    keys.append(v[0])
            '''keycheck = input("请输入要查询的城市中文名称：")
            model = input("请选择匹配模式：")'''

            scoretemp = 0
            for allofkey in tqdm(dic.keys(), desc='读取文件中'):
                time.sleep(0.1)
                score = fuzz_matching(allofkey, args.keycheck, args.model)
                if (score > scoretemp):
                    scoretemp = score

            keycheck = args.keycheck
            model = args.model

            for allofkey in dic.keys():
                if (fuzz_matching(allofkey, keycheck, model) == scoretemp):
                    if (scoretemp == 100):
                        print('该城市名称的首字母是：', dic.get(allofkey))
                    else:
                        print('查无此城，与之最相近的城市名称是：', allofkey, dic.get(allofkey))






        elif action == '3':
            fr = open('cities.txt', 'r')
            dic = {}
            keys = []  # 用来存储读取的顺序
            for line in fr:
                if line.isspace():
                    continue
                else:
                    v = line.strip().split(':')
                    dic[v[0]] = v[1]
                    keys.append(v[0])
            print(dic)




        elif action == '4':
            print("删除城市信息")
            fr = open('cities.txt', 'r')
            dic = {}
            keys = []  # 用来存储读取的顺序
            for line in fr:
                if line.isspace():
                    continue
                else:
                    v = line.strip().split(':')
                    dic[v[0]] = v[1]
                    keys.append(v[0])
            fr = open('cities.txt', 'w')
            mistake = input("请输入需要删除的城市名称：")
            dic.pop(mistake)

            for key, value in tqdm(dic.items(), desc='重新写入中'):
                fr.writelines([key, ':', value, '\n'])

            fr.close()
            print("已成功删除！")


        elif action == '5':
            fr = open('cities.txt', 'r')
            dic = {}
            keys = []  # 用来存储读取的顺序
            for line in fr:
                if line.isspace():
                    continue
                else:
                    v = line.strip().split(':')
                    dic[v[0]] = v[1]
                    keys.append(v[0])
            change = input('请输入需要改变的城市名称：')
            new_name = input('请输入新的拼音首字母：')
            dic[change] = new_name
            fr = open('cities.txt', 'w')
            for key, value in tqdm(dic.items(), desc='重新写入中'):
                fr.writelines([key, ':', value, '\n'])

            fr.close()
            print(change, ':', dic[change])
            print("已修改！")


        else:
            print("错误，请重新输入")
