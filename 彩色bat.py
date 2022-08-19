file_ = open("color.cmd","w")
write = "color"
for i in range(21):
    word = write + i
    txt = txt + word + "\n"
return_ = file_.write(txt)
print (return_)


