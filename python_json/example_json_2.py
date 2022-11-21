import json
file_path = '/Users/jeong-inho/Python/python_study/python_json/py.json'

#파일 읽어오기
with open(file_path, 'r') as fp:                                                    # 파일을 불러올때는 'r'을 쓴다 read를 의미.(읽기 모드)
    data = json.load(fp)                                                            # json 형태의 파일 읽어오기

# print(data['id'])
# print(data['study'])

#수정되기 전 json 파일이 출력
print(json.dumps(data, indent = 4))                                                 # json 으로 읽은 파일 출력, dump를 쓰면 TypeError: dump() missing 1 required positional argument: 'fp' 발생
                                                                                    # 파이썬 객체를 한줄의(직렬화된) json 문자열로 변환합니다.

# 불러온 json 파일을 수정하고 저장하기
data['test'] = False
data['study'] = ['Java', 'Javascript', 'Python', 'C', 'C#', 'Ruby', 'kotlin']

with open(file_path, 'w', encoding = 'UTF-8') as fp:
    json.dump(data, fp, indent = 4)                                                 # 첫번째 인자로는 파이썬 객체(data), 두번째는 pile pointer(파일 객체)

# 수정한 json 파일을 다시 불러와 출력
with open(file_path, 'r') as fp:                                                    # 파일을 불러올때는 'r'을 쓴다 read를 의미.(읽기 모드)
    data = json.load(fp)

print(json.dumps(data, indent = 4))