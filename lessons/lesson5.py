import re

s = 'AC/DSAC/DC/A/CD/C/AC'
res = re.match('AC', s)
# print(res)
# print(res[0])
# match начало
# до первого search
# [0] искоемое
ree = re.search('DC', s)
# print(ree)
# print(ree[0])
# findall все штуки
rea = re.findall('A', s)
red = re.split('A', s)
print(rea)
# split делит по "" N maxsplit максимальная длина деления
# sub замена
sub = re.sub('A', 'D', s)
print(sub)
fullmatch = re.fullmatch('A', s)
# fullmatch сравнение


text = 'карта map и обьект bitmap'
textt = re.findall("map", text)
text2 = re.findall(r"\bmap\b", text)
print(textt)
print(text2)

t = 'еда беду побЕда '
tt = re.findall(r'еда', t)
print(tt)
# ()группирующие скопки
# символьный класс (еда Еда еду Еду)
# [сюда пишут все что надо затронуть]
# ^ знак не

sim = re.findall(r'[еЕ]д[ау]', t)
si = re.findall(r'[а-яА-Я0-9]', t)
print(si)
print(sim)

gogle = 'Google o Gooogle Gooooogle'
gog = re.findall(r'o{5}', gogle)
goge = re.findall(r'o{2,}?', gogle)
print(gog)
print(goge)

