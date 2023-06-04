import json
fpath = "KUAKE-QTR_train.json"
qtr_data = {'Q': [], 'T': [], 'l': []}

with open(fpath, encoding="utf-8") as f:
    lists = json.load(f)
    for list in lists:
        sample_1 = list["query"]
        sample_2 = list["title"]
        target = list["label"]
        qtr_data['Q'].append(sample_1)
        qtr_data['T'].append(sample_2)
        qtr_data["l"].append(target)

qtr_data['l'] = [float(s) for s in qtr_data['l']]

# print(sts_data["X_B"])



sorted_corpus = sorted(zip(
                           qtr_data['Q'],
                           qtr_data['T'],
                           qtr_data['l']),
                            key=lambda z: (len(z[0]), len(z[1]), z[2]))

qtr_data['Q'] = [x for (x, y, z) in sorted_corpus]
qtr_data['T'] = [y for (x, y, z) in sorted_corpus]
qtr_data['l'] = [z for (x, y, z) in sorted_corpus]
print(qtr_data)