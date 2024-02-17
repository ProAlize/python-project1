# python_project1
## 1 Mission Description
Design a Python program to implement the following:
1) Enter the city name and get the corresponding first letter of Chinese Pinyin;
2) Support fuzzy matching and parameter analysis;
3) Keep a diary;
4) Add a loading progress bar (when reading city files);

## 2 Data structure design
<p>Use the dictionary data structure in Python to convert the txt file that stores city names and pinyin initials into a dic dictionary. The key is the Chinese name of the city, and the value is the first letter of the pinyin of the city to achieve subsequent additions, deletions, modifications, and fuzzy matching.</p>
For example: {'Beijing': 'BJ', 'Shanghai': 'SH', 'Shenyang': 'SY'}

## 3 Algorithm design
### 3.1 Read txt file and convert into dictionary
~~~
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
~~~
### 3.2 Fuzzy matching (using fuzzywuzzy)
~~~
from fuzzywuzzy import fuzz
def fuzz_matching(allofkey, keycheck, model):

    if (model == '1'):
        score = fuzz.ratio(allofkey, keycheck)
        return score
    if (model == '2'):
        score = fuzz.token_sort_ratio(allofkey, keycheck)
        return score    #保留匹配分数

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
            print('查无此城，与之最相近的城市名称是：', allofkey,dic.get(allofkey))

~~~   
### 3.3 Parameter analysis
~~~
import argparse

parser = argparse.ArgumentParser(description='模糊匹配')

parser.add_argument('-k', '--keycheck', type=str, required=True, help='待匹配的城市名称')

parser.add_argument('-m', '--model', type=str, required=True, help='匹配模式：1为简单匹配，2为无顺序匹配')

args = parser.parse_args()
~~~
### 3.4 Add a progress bar when reading files
~~~
from tqdm import tqdm

for allofkey in tqdm(dic.keys(), desc='读取文件中'):
    time.sleep(0.1)

~~~
###  3.5 Add log file
~~~
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO,

format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')
~~~
### 3.6 After converting txt to dictionary dic, dic can be modified and rewritten into txt to implement addition, deletion and modification functions.
~~~
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
~~~



