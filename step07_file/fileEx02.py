fs = open("test03.txt", 'w', encoding="utf-8")
fs.write("안녕하세요? \n HI HI")
fs.close()

# 원하는 위치에 생성가능
fs = open("D:/JHY/test03.txt", 'w', encoding="utf-8")
fs.write("안녕하세요? \n HI HI")
fs.close()