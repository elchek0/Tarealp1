import re

texto = '''
13-04-2021
2021-13-04
2021-04-13
123123
joaquin
13-04-2021
joaquin.torres@usm.cl
121l3223k21
12-19-2001
27-06-2001
26-02-2002
40-43-0001
'''
print(re.findall(r'\d{2}-\d{2}-\d{4}',texto))