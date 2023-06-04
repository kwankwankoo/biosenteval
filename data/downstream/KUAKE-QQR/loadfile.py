import json
fpath = "KUAKE-QQR_train.json"
qqr_data = {'Q': [], 'Q': [], 'l': []}

with open(fpath, encoding="utf-8") as f:
    lists = json.load(f)
    for list in lists:
        sample_1 = list["query1"]
        sample_2 = list["query2"]
        target = list["label"]
        qqr_data['Q'].append(sample_1)
        qqr_data['Q'].append(sample_2)
        qqr_data["l"].append(target)

qqr_data['l'] = [float(s) for s in qqr_data['l']]



sorted_corpus = sorted(zip(
                           qqr_data['Q'],
                           qqr_data['Q'],
                           qqr_data['l']),
                            key=lambda z: (len(z[0]), len(z[1]), z[2]))

qqr_data['Q'] = [x for (x, y, z) in sorted_corpus]
qqr_data['Q'] = [y for (x, y, z) in sorted_corpus]
qqr_data['l'] = [z for (x, y, z) in sorted_corpus]
print(qqr_data)