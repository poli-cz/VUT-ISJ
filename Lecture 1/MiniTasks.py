# minitask 1.1
# expected output ['b', '/b', 'i', '/i']
import re
text = '<b>foo</b> and <i>so on</i>'
print(re.findall(r'<(.{1,2})>',text))

# minitask 1.2
# expected output ['resource load failed', 'flow failed']
import re
text = '''
INFO 2019-02-17 12:13:44 resource load failed
INFO 2019-02-18 22:09:17 authentication failed
INFO 2019-02-18 10:55:48 data received
INFO 2019-02-19 19:53:31 flow failed
'''
pattern = '''
    \w+                 # failure type
    \s                  # a white character
    [\d-]+              # date such as 2019-02-21
    \s                  # a white character
    [\d:]+              # time such as 21:15:06
    \s                  # a white character
    (.{0,13}\sfailed)   # failure description
'''
print(re.findall(pattern,text, re.VERBOSE))

# minitask 1.3
# change the last du to DU
import re
pattern = re.compile(r'dupl')
text = ['du du du', 'du po ledu', 'dopředu du', 'i dozadu du', 'dudu dupl']
for row in text:
    print(re.sub(pattern, 'DUpl' , row))
    
# minitask 1.4
# strings/lines that contain _words_ David and Pavel and 
# do not contain neither _words_ Petr nor Jan
# expected output:
# Iva Pavel David Ada
# Pavel David Jansen
texts = ['David Petr','Iva Pavel David Ada',
         'Davidson Pavelek','Pavel David Jansen']
for text in texts:
    if re.search(r'(r'(?=.*?\bDavid\s\b)?(?=.*?\bPavel\b)(?!.*?\bPetr\b)(?!.*?\bJan\b)',text)',text):
        print(text)
