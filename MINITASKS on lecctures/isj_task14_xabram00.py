# minitask 1.4
# strings/lines that contain _words_ David and Pavel and 
# do not contain neither _words_ Petr nor Jan
# expected output:
# Iva Pavel David Ada
# Pavel David Jansen
texts = ['David Petr','Iva Pavel David Ada',
         'Davidson Pavelek','Pavel David Jansen']
for text in texts:
    if re.search(r'(?=.*?\bDavid\s\b)?(?=.*?\bPavel\b)(?!.*?\bPetr\b)(?!.*?\bJan\b)',text):
        print(text)
