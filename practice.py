'''
print("C:\test")

name = "Python"
print(f"Hello,{name}!")

hoge = len("Python")
print(hoge)

x = "Python"
print(x[0:1])

x = None
print(x)

a = 10
b = 3.14
c = "Hello, Python!"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

lst = [1, 2, 3]
print(lst, lst[0])

print("C:\\test")

x = "Python"

print(x[0:2])

x = None
print(x)

a = 10
b = 3.14
c = "Hello, Python!"
d = True

print(type(a))

lst = [1, 2, 3]

print(lst, lst[0])

lst = [1, 2, 3]
lst.append(4)
print(lst)

lst = [1, 2, 3]
lst.remove(2)
print(lst)

lst = [1, 2]
lst2 = [3, 4]

print(lst + lst2)

x = 15
if x > 10:
    print("xは10より大きい")

x = 0

if x > 10:
    print("xは10より大きい")
elif x > 5:
    print("xは5より大きいが、10以下")
else:
    print("xは5以下")

x = 20
y = 20

print(x>y)
print(x>=y)
print(x==y)
print(x<=y)
print(x<y)

lst = [1, 2, 3]

print(2 in lst)

x = None

print(x is None)

x = 10
y = 20

print(x and y > 15)
print(x or y > 15)

x = 1

if x is not None:
    print("x は None ではない")

x = [1, 2, 3]

for item in x:
    print(item)

for i in range(10):
    print(i)

x = 5

for i in range(10):
    if i == x:
        break
    print(i)
x = 5

for i in range(10):
    if i == x:
        continue
    print(i)

x = 10

while x > 1:
    print(x)
    x = x - 1

tpl = (1, 2, 3)
print(tpl)
print(tpl[0])

tpl = (1, 2)+(3, 4)

print(tpl)

print(len(tpl))

st = {1, 2, 3}

st.add(2)

print(st)

x = {1, 2, 3}
y = {4, 5}

print(x + y)

st = {1, 2, 3}

for i in st:
    print(i)

dct = {'id':'0001', 'name':'guest'}

print(dct['name'])

dct = {'id': '0001', 'name': 'guest'}

for key, value in dct.items():
    print(key, value)
even_list = [x for x in range(1, 10) if x % 2 == 0]
print(even_list)

x = '1 2 3'
print(x.replace(',', '&'))

x = '1, 2, 3'
lst = x.split(',')
print(lst)

x = 10
y = 3

print(x * y)
print(x / y)
print(x // y)
print(x % y)

lst = [1, 2, 3]
print(max(lst))

x = 0
try:
    print(1 / x)
except ZeroDivisionError:
    print('ゼロ除算エラーが発生しました')

x = None

try:
    print(x * 2)
except TypeError as e:
    print(e)

x = -1

if x < 0:
    raise ValueError('あいうえお')

print('C:\test')

lst = [1, 2, 3]
lst.append(4)
print(lst)
lst = [1, 2, 3]
print(len(lst))

lst = [1, 2, 3]
lst.remove(2)
print(lst)

lst = [1, 2, 3]

print(lst in 2)

x = 10
y = 20

print(x > 15 and y > 15)
print(x > 15 or y > 15)
x = [1, 2, 3]
for i in x:
    print(i)

for i in range(10):
    print(i)

x = 5
for i in range(10):
    print(i)
    if i == x:
        break

x = 5
for i in range(10):
    if i == x:
        break
    print(i)
x = 5

for i in range(10):
    if i == x:
        continue
    print(i)
x = 10
while x > 0:
    print(x)
    x = x - 1
tpl = (1, 2, 3)

print(tpl)
print(tpl[0])

tpl = (1, 2) + (3, 4)
print(tpl)
print(len(tpl))

st = {1, 2, 3}

st.add(1)
print(st)

st.remove(1)
print(st)

x = {1, 2, 3}
y = {3, 4, 5}

print(x.add(y))

st = {1, 2, 3}

for i in st:
    print(i)

dct = {'id':'0001', 'name':'guest'}

print(dct(name))

dct = {'id':'0001', 'name':'guest'}
for i in dct[key:value]:
    print(i)

x = "1, 2, 3"

print(x)

lst = x.split(",")

print(lst)

y = '&'.join(lst)

print(y)

lst = [1, 2, 3]

print(lst[max])

x = 0

try:
    print(1)
except ZeroDivisionError:
    print('a')

x = None

try:
    print(x * 2)
except TypeError as e:
    print(e)

x = -1

if x < 1:
    raise ValueError('a')

right = 0
left = 0

for right in range(1, 10):
    for left in range(1, 10):
        total = right * left
        print(f'{right} × {left} = {total}')

for x in range(1, 100):
    if '3' in str(x):
        print(x)

for x in range(1, 100):
    if '3' in str(x):
        lst = x

for i in lst:
    print(i)

list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in list_2d:
    for x in i:
        print(x * 2)

ascii_dict = {'0x30': '0', '0x40': '@', '0x50': 'P'}

for x in ascii_dict

target_text = 'hello'
count_dict = {}
count_dict = count_dict[1] = 1
print(count_dict)

# for char in target_text:
#     if char in count_dict:
#         count_dict[char] += 1
#     else:
#         count_dict[char] = 1
# print(count_dict)

count_dict = {}           # 空っぽ
count_dict['h'] = 1       # 'h'というキーに、値1を設定
print(count_dict)

target_list = [1, 2, 3, None, 5, None, 7]
y = []

for x in target_list:
    if not x == None:
        y = x

print(y)

target_list = [1, 2, 3, None, 5, None, 7]
filtered_list = [str(item) for item in target_list if item is not None]
result = '&'.join(filtered_list)
print(result)

lst = [1, 2 , 3, None, 5]

for x in lst:
    try:
        x * 2
    except TypeError as e:
        print(e)
    print(x)

lst = [1, 2, 3, None, 5]
for x in lst:
    try:
        print(x * 2)
    except TypeError as e:
        print(e)

for x in employees:
    if key == 'L01':
        print('a')


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
    if employee['location_id'] in {'L01', 'L02'}:
        print(employee['id'],employee['name'])

li = [i * 1 for i in range(0,10)]
print(li)

# numbers1 = []

# for i in range(22):
#     if i % 3 == 1:
#         numbers1.append(i)

# print(numbers1)

numbers1 = [i for i in range(22) if i % 3 == 1]
print(numbers1)

print(r'C:\test')

lst = [1, 2, 3]
lst.remove(2)
print(lst)

lst = [1, 2, 3]
lst.append(4)
print(lst)

lst = [1, 2, 3]

print(2 in lst)

x = 5

for i in range(0, 10):
    if i == x:
        continue
    print(i)

x = 10

while x > 0:
    print(x)
    x = x-1

tpl = (1, 2, 3)

print(tpl)
print(tpl[0])

x = {1, 2, 3}
y = {3, 4, 5}

print(x  y)

dct = {'id': '0001','name': 'guest'}

print(dct['name'])

dct = {'id': '0001','name': 'guest'}

for key, value in dct.items():
    print(key, value)

x = '1, 2, 3'

print(x.replace(',', '&'))

lst = {1, 2, 3}
print(max(lst))

def sample():
    print('a')

sample()

lst = [1, 2, 3]

lst.append(4)

print(lst)

lst = [1, 2, 3]

lst.remove(3)

print(lst)

lst = [1, 2, 3]

print(2 in lst)

x = {1, 2, 3}

y = {3, 4, 5}

print(x.union(y))

print(x.)

dct = {'id': '0001', 'name': 'guest'}

for key, value in dct.items():
    print(key, value)

x = 0

try:
    print(1 / x)
except ZeroDivisionError:
    print('ゼロ除算エラーが発生しました')

def sample():
    print('Hello World')

sample()

def greet(name):
    print(f'こんにちは、{name}さん')


greet('テスト')

def add(a, b):
    return a + b

x = add(1, 1)
print(x)

def welcome_message(name='ゲスト'):
    print(f'ようこそ {name} さん')

welcome_message()
welcome_message('管理者')

def print_args(*args, **kwargs):
    print(args)
    print(kwargs)

print_args('A', 'B', key1='X', key2='Y')

lst = [1, 2, 3]

print(4 in lst)

x = {1, 2, 3}

y = {3, 4, 5}

print(y.union(x))

print(y.intersection(x))

dct = {'id': '0001', 'name': 'guest'}

for x in dct.items():
    print(x)

def add(a, b):
    return a + b

print(add(1,1))

def welcome_message(name='ゲスト'):
    print(f'ようこそ{name}さん')

welcome_message()
welcome_message('管理者')
'''

class SimpleClass:
    def __init__(self, name):
        print(f'名前が{name}のオブジェクトを作成しました')

SimpleClass('a')


