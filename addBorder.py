def addBorder(picture):
    picture_asterisk = []
    for i in range(len(picture)):
        picture_asterisk.append('*'+picture[i]+'*')
    picture_asterisk.insert(0, '*' * len(picture_asterisk[0]))
    picture_asterisk.append('*' * len(picture_asterisk[0]))
    
    return picture_asterisk
