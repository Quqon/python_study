import json
import os

d = dict()
d['id'] = 1
d['name'] = 'py'
d['test'] = True
d['study'] = ['java', 'javascript', 'python']


print(type(d))                                                                                          # <class 'dict>
print(os.getcwd())                                                                                      # 현재 디렉토리 경로 확인
file_path = ('/Users/jeong-inho/Python/python_study/python_json/py.json')                               # 미리 py.json이란 파일을 생성해 놓지 않아도 자동으로 생성된다.

with open(file_path, 'w', encoding = 'UTF-8') as fp:
    json.dump(d, fp, indent = 4)                                                                        # indent를 쓰면 json파일을 정렬할수 있다. 보통 4를 쓴다. 2또는 '\t'(tab)도 가능. 'w'는 write를 의미(쓰기모드)파일 생성시 사용.
