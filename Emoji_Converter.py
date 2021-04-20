word=input('>')
words=word.split(' ')
emoji={
    "😊" : "smile",
    "☹️" : "frown"
}
output=""
for x in words:
    output+=emoji.get(x,x)+ " "

print(output)
