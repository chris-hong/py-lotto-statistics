# this is test page for beginning

# greeting = 'HI~ Hello~ Greeting!!~'
#
# print(greeting)

from htmldom import htmldom

dom = htmldom.HtmlDom("http://m.naver.com").createDom()

p = dom.find("*")

print(p.html())


