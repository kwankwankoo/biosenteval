import json
import logging


import logging
# #步骤：创建记录器》设置记录级别》创建输出对象》配置输出级别》配置打印格式》内容记录
# #设置日志记录器, 日志集
# logger = logging.getLogger('loggingtest')
# #设置日志集级别
# logger.setLevel('INFO')
# #控制台日志输出
# console = logging.StreamHandler()
# console.setLevel("INFO")
# #设置日志打印格式
# formatter = logging.Formatter("%(asctime)s: %(message)s")
# #为日志记录文件加入上述设置的日志格式
# console.setFormatter(formatter)
# #将控制台日志打印加入到日志集
# logger.addHandler(console)
# #内容记录
# logger.info('logging test')

logging.basicConfig(format='%(asctime)s: %(message)s',level=logging.INFO)
logging.basicConfig(format='%(asctime)s: %(message)s',level=logging.DEBUG)
fpath = "KUAKE-QIC_train.json"
qic_data = {'X': [], 'y': []}
tgt2idx = {'病情诊断' :1 ,'病因分析' :2 ,'治疗方案' :3 ,'就医建议' :4 ,'指标解读' :5 ,'疾病表述' :6,
            '后果表述' :7 ,'注意事项' :8 ,'功效作用' :9 ,'医疗费用' :10 ,'其他' :11}
with open(fpath, encoding="utf-8") as f:
    lists = json.load(f)
    for list in lists:
        sample = list["query"]
        target = list["label"]
        qic_data['X'].append(sample)
        qic_data['y'].append(tgt2idx[target])

# logger.info("location found")
# print(qic_data['X'])
# print(qic_data['y'])

logging.info("This is logging")