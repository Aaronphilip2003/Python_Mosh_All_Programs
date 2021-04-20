word=input('>')
words=word.split(' ')
emoji={
    ":)" : "😊",
    ":(" : "☹️"
}
output=""
for x in words:
    output+=emoji.get(x,x)+ " "

print(output)
