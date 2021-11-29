import os
import csv
from collections import defaultdict

#Basic Function
def f_sentence_capitalised(sentence):
    tmp = [s.capitalize() for s in sentence.split()]
    print(tmp)
    return " ".join(tmp)

def f_data_csv_writer(input_dict):
    fieldnames = ['Name', 'Count']
    with open('data.csv', 'w', newline='') as w_csv_file:
        writer = csv.DictWriter(w_csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in input_dict.items():
            writer.writerow({'Name': k, 'Count': v})

def f_end_message(name):
    print(f"{name} 씨, 감사합니다.\n", \
          "좋은 하루 보내세요! 안녕히가세요.。")
    exit()

# Step 1. Check Name
print("안녕하세요. 저는 Rokoboko입니다. 당신의 이름은 무엇입니까 ?")
name = input()
tmp_dict = defaultdict(int)

# Step 2. recommand restaurent
if os.path.isfile('data.csv'):
    with open('data.csv', 'r') as r_csv_file:
        reader = csv.DictReader(r_csv_file)
        is_recommend_yes = False
        for row in reader:
            tmp_dict[row['Name']] = int(row['Count'])
            if is_recommend_yes == False:
                print(f"추천드리는 레스토랑은 {row['Name']} 입니다.\n",\
                      f"이 레스토랑을 좋아하세요? [Yes/No]")
                answer = input()
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    tmp_dict[row['Name']] += 1
                    is_recommend_yes = True

        if is_recommend_yes:
            f_data_csv_writer(tmp_dict)
            f_end_message(name)

print(f"{name} 씨, 좋아하는 레스토랑의 이름은 무엇입니까?")
want_restaurant = f_sentence_capitalised(input())
tmp_dict[want_restaurant] += 1
f_data_csv_writer(tmp_dict)
f_end_message(name)

