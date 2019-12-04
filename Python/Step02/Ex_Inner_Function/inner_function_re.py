#================== RE ================================
#=============== 정규표현식 ============================
improt re
re.match('패턴','문자열')
re.match('Hello','Hello, world!!')
re.search('^Hello','Hello, world!')
re.search('world!$','Hello, world!')
re.match('[0-9]*','1234')
re.match('[0-9]+','abcd')
re.match('h{3}','hhhhhhabcd')
re.match('\d+','1234')
re.match('\D+','1234')
re.match('\D+','abcd')
re.match('\w+','abcd_1234')
re.match('\W+','abcd_1234')
re.match('\W+','(:)')

#================= 컴파일러 =============================
p = re.compile('[0-9]+')
p.match('1234')
p.search('hello')
p.search('010-0230-1221')