'''
x = {1, 2, 3}
y = {3, 4, 5}

print(x.union(y))
print(x.intersection(y))

x = '1, 2, 3'

print(x.replace(',','&'))

x = '1, 2, 3'
lst = x.split(',')
print(lst)

y = '&'.join(lst)
print(y)

def print_args(*args, **kwargs):
    print(args, kwargs)

print_args('A', 'B', key1='X', key2='Y')

class SimpleClass():
    def __init__(self, name):
        print(f'名前が{name}のオブジェクトを作成しました')

x = SimpleClass('サンプル')
employees = [
    {'id': '0001', 'name': '田中', 'location_id': 'L01'},
    {'id': '0002', 'name': '山田', 'location_id': 'L02'},
    {'id': '0003', 'name': '小林', 'location_id': 'L01'},
    {'id': '0004', 'name': '藤本', 'location_id': 'L03'},
    {'id': '0005', 'name': '佐々木', 'location_id': 'L02'},
    {'id': '0006', 'name': '松田', 'location_id': 'L04'},
    {'id': '0007', 'name': '中村', 'location_id': 'L01'},
    {'id': '0008', 'name': '石川', 'location_id': 'L03'},
    {'id': '0009', 'name': '清水', 'location_id': 'L05'},
    {'id': '0010', 'name': '近藤', 'location_id': 'L02'}
]

for employee in employees:
    if employee['location_id'] in {'L01', 'LO2'}:
        print(employee['id'], employee['name'])

def print_args(*args, **kwargs):
    print(args)
    print(kwargs)

print_args('key1=X', key2='Y')

class SimpleClass():
    count = 0

    def __init__(self,name):
        self.name = name
        SimpleClass.count += 1
        print(f'名前が{name}のオブジェクトを作成しました')

    def print_name(self):
        print(self.name)

    @classmethod
    def print_count(cls):
        print(cls.count)

x = SimpleClass('サンプル')

x.print_name()
x.print_count()

x = '1, 2, 3'

print(x.replace(',','&'))

x = '1, 2, 3'

lst = x.split(',')

print(lst)

y = '&'.join(lst)

print(y)
lst = [1, 2, 3]

x = max(lst)

print(x)

x = 0

try:
    print(1 / x)
except ZeroDivisionError:
    print('abc')

x = None

try:
    print(x * 2)
except TypeError:

x = -1

for x in range(1, 10):
    for y in range(1, 10):
        z = x * y
        print(f'{x} × {y} = {z}')
'''

ファイル「わかるをつくる中学英語問題集 1」に対して以下の操作を行なってください。

x = 感嘆文・話法・仮定法
x の基本問題カラムに「基本 {親番号}-{小番号}」の記述をしてください。
  親番1の子番号は4つ、
  親番2の子番号は4つ、
  親番3の子番号は4つ、
  親番4の子番号は4つ、
  親番5の子番号は6つ、
  親番6の子番号は7つ、
でお願いします
また、x の基本問題カラムに「応用 {親番号}-{小番号}」の記述をしてください。
  親番1の子番号は4つ、
  親番2の子番号は3つ、
  親番3の子番号は2つ、
  親番4の子番号は3つ、
  親番5の子番号は3つ、
でお願いします




