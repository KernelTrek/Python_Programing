"""
web_server:
    host: 127.0.0.1
    port: 80

db_server:
    host: 127.0.0.1
    port: 3306
"""
# yaml은 요즘에 많이 사용되는 형태의 파일
# [Step 1] yaml 파일 만들기
import yaml

with open('config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)

with open('config.yml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(data, type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])