import pandas as pd
from aip import AipNlp
import os

def isPostive(text, client):
    try:
        if client.sentimentClassify(text)['items'][0]['positive_prob'] > 0.5:
            return "积极"
        else:
            return "消极"
    except:
        return "积极"  # 如果API调用失败，默认返回"积极"

if __name__ == '__main__':
    # 百度AI的配置
    APP_ID = '66035647'
    API_KEY = 'Ip7xRsBwtsT5qvfS6ZaDCoNu'
    SECRET_KEY = '' # 输入你的密钥
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    # 读取文件
    file_path = r'D:\大学\任务活动\第六学期\统计建模大赛\评论罗伯特python新\数据\爬虫数据202401-202405\罗伯特的评论0101-0501.xls'
    data = pd.read_excel(file_path)
    output_path = r'D:\大学\任务活动\第六学期\统计建模大赛\评论罗伯特python新\数据\爬虫数据202401-202405\罗伯特的评论0101-0501nlp.csv'

    # 检查输出文件是否存在，不存在则创建并写入列头
    if not os.path.exists(output_path):
        data['情感倾向'] = ''  # 初始化情感倾向列
        data.iloc[0:0].to_csv(output_path, index=False, encoding='utf-8-sig')

    for index, row in data.iterrows():
        sentiment = isPostive(row['评论内容'], client)
        row['情感倾向'] = sentiment
        # 逐行追加到CSV文件
        with open(output_path, 'a', encoding='utf-8-sig', newline='') as f:
            row.to_frame().T.to_csv(f, header=False, index=False)
        print("目前分析到：", index + 1, "情感倾向：", sentiment)

    print("分析完成，已保存至", output_path)
