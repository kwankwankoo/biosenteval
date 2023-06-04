import json
fpath = "CHIP-STS_train.json"
sts_data = {'X_A': [], 'X_B': [], 'y': []}

with open(fpath, encoding="utf-8") as f:
    lists = json.load(f)
    for list in lists:
        sample_1 = list["text1"]
        sample_2 = list["text2"]
        target = list["label"]
        # category = list["category"]
        # sts_data["C"].append(category)
        sts_data['X_A'].append(sample_1)
        sts_data['X_B'].append(sample_2)
        sts_data["y"].append(target)

sts_data['y'] = [float(s) for s in sts_data['y']]

# print(sts_data["X_B"])



sorted_corpus = sorted(zip(
                           sts_data['X_A'],
                           sts_data['X_B'],
                           sts_data['y']),
                            key=lambda z: (len(z[0]), len(z[1]), z[2]))

sts_data['X_A'] = [x for (x, y, z) in sorted_corpus]
sts_data['X_B'] = [y for (x, y, z) in sorted_corpus]
sts_data['y'] = [z for (x, y, z) in sorted_corpus]
print(sts_data['y'])