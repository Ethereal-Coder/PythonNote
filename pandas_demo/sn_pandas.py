# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-4-23
Description:
"""


from storage.mongo_mgr import mongo_sn_goods
import pandas as pd
import numpy as np
import json
import csv

spec_dict = {
    '20089': '型号',
    '157122': '型号',
    '20358': '型号',
    '20268': '型号',
    '20061': '型号',
    '456003': '型号',  # ?
    '457529': '型号',
    '253003': '型号',
    '500192': '型号',
    '500037': '型号',
    '500353': 'sp',
    '500354': 'sp',
    '500748': ['批准文号', '?'],
    '420003': ['型号', '货号'],
    '361003': ['货号', '型号'],
    '88507': ['货号', '型号'],

}

all_count = mongo_sn_goods().collection.find(
    {'params': {'$exists': True}}
).count()

print('sn goods len: %s' % all_count)

# all = mongo_sn_goods().collection.find(
#     {'params': {'$exists': True}},
#     {"base_id": 1, "second_id": 1, "third_id": 1, 'params': 1}
# )

data_list = []
for i in range(int(all_count/10000) + 1):
    al_doods = mongo_sn_goods().collection.find(
        {'params': {'$exists': True}},
        {"base_id": 1, "second_id": 1, "third_id": 1, 'params': 1}
    ).skip(i*10000).limit(10000)
    for a in al_doods:
        if a['params']:
            brand = a['params'].get('品牌', None)
            if brand:
                spec = a['params'].get('型号', None)
                if spec is None:
                    spec = a['params'].get('货号', None)
                    if spec is None:
                        spec = a['params'].get('批准文号', None)
                temp = {}
                temp['_id'] = a['_id']
                temp['cid1'] = a['base_id']
                temp['cid2'] = a['second_id']
                temp['cid3'] = a['third_id']
                temp['brand'] = brand
                temp['spec'] = spec
                data_list.append(temp)
    print(len(data_list))

print('convert to DataFrame')

df = pd.DataFrame(data_list)
# print(df)
# print(df.T)
# print(df.shape)
# print(df.dtypes)
# print(df.ndim)
# print(df.values)

# print(df.info())
# print(df.head(3))
# print(df.tail(3))
# print(df.describe())

# sv = df.sort_values(by='cid', ascending=False)
# sv = df.sort_values(by='brand', ascending=True)
# sv = df.sort_values(by='spec', ascending=False)
# sv = df.sort_values(by=['brand', 'spec'], ascending=[False, False])
# print(sv)
# print(sv['brand'])
# print(sv[2:3:1]['brand'])

# loc iloc
# print(df.iloc[1:6:2, [0, 2, 3]])

# print(df.iloc[1:2:, 2:3:])
# df.iloc[1:2:, 2:3:] = 10086
# df.iloc[1:2:, 2:3:] = np.nan
# print(df.iloc[1:2:, 2:3:])
# print(df.iloc[:10, ])

# print(df[(df['brand'].str.len() == 2) & (df['_id'] % 3 == 2)])


# print(pd.isnull(df))
# print(pd.isnull(df['spec']))
# print(df[pd.isnull(df['spec'])])
# print(pd.notnull(df))

# dr = df.dropna(axis=0, how='any', inplace=False)
# print(dr)

# df.dropna(axis=0, how='any', inplace=True)
# print(df)

df.fillna('null')

# df[df == 557710460710] = np.nan
# print(df)


# grouped1 = df.groupby('brand')
# print(grouped1)
# for gl in list(grouped1):
#     print(gl)
#     print('*'* 50)
# print(dict(list(grouped1)))
# print(dict(list(grouped1)).keys())


grouped2 = df.groupby(['cid1', 'brand', 'spec'])
# print(grouped2)
# print(grouped2.mean())
# print(grouped2.size())
# print(grouped2.groups)

cbp_list = []
for name, group in grouped2:
    # print(name)
    # print(group)
    # print(group['_id'].count())
    # print('*' * 50)
    cbp_list.append([name[0], name[1], name[2], group['_id'].count()])

# with open('sn_cbp.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ["cid", 'brand', 'spec', 'count']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(cbp_list)
print('start store result to csv')
with open('sn_cbp_cid1_001.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["cid1", 'brand', 'spec', 'count']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(cbp_list)

# g_list = list(grouped2)
# print(g_list)
# print(g_list[1])

# dg = dict(list(grouped2))
# print(dg.keys())
# print(dg)


# grouped22 = df.groupby(['cid2', 'brand', 'spec'])
#
# cbp_list = []
# for name, group in grouped22:
#     cbp_list.append([name[0], name[1], name[2], group['_id'].count()])
#
# with open('sn_cbp_cid2.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ["cid2", 'brand', 'spec', 'count']
#     writer = csv.writer(csvfile)
#     writer.writerow(fieldnames)
#     writer.writerows(cbp_list)
#
#
# grouped23 = df.groupby(['cid3', 'brand', 'spec'])
#
# cbp_list = []
# for name, group in grouped23:
#     cbp_list.append([name[0], name[1], name[2], group['_id'].count()])
#
# with open('sn_cbp_cid3.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ["cid3", 'brand', 'spec', 'count']
#     writer = csv.writer(csvfile)
#     writer.writerow(fieldnames)
#     writer.writerows(cbp_list)