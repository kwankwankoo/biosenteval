import json

ctc_data = {'X': [], 'y': []}
tgt2idx = {'Disease': 0, 'Symptom': 1, 'Sign': 2, 'Pregnancy-related Activity': 3, 'Neoplasm Status': 4,
           'Non-Neoplasm Disease Stage': 5, 'Allergy Intolerance': 6, 'Organ or Tissue Status': 7,
           'Life Expectancy': 8, 'Oral related': 9, 'Pharmaceutical Substance or Drug': 10, 'Therapy or Surgery': 11,
           'Device': 12, 'Nursing': 13, 'Diagnostic': 14, 'Laboratory Examinations': 15, 'Risk Assessment': 16,
           'Receptor Status': 17, 'Age': 18, 'Special Patient Characteristic': 19, 'Literacy': 20, 'Gender': 21,
           'Education': 22, 'Address': 23, 'Ethnicity': 24, 'Consent': 25, 'Enrollment in other studies': 26,
           'Researcher Decision': 27, 'Capacity': 28, 'Ethical Audit': 29, 'Compliance with Protocol': 30,
           'Addictive Behavior': 31, 'Bedtime': 32, 'Exercise': 33, 'Diet': 34, 'Alcohol Consumer': 35,
           'Sexual related': 36, 'Smoking Status': 37, 'Blood Donation': 38, 'Encounter': 39,
           'Disabilities': 40, 'Healthy': 41, 'Data Accessible': 42, 'Multiple': 43}

with open("CHIP-CTC_train.json", encoding="utf-8") as f:
    lists = json.load(f)
    for list in lists:
        sample = list["text"]
        target = list["label"]
        ctc_data['X'].append(sample)
        ctc_data['y'].append(tgt2idx[target])

sorted_corpus_train = sorted(zip(ctc_data['X'], ctc_data['y']),
                                     key=lambda z: (len(z[0]), z[1]))
train_samples = [x for (x, y) in sorted_corpus_train]
train_labels = [y for (x, y) in sorted_corpus_train]

print(train_labels)