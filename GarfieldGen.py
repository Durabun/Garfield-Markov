import numpy as np
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap

tabby = open('garfield.txt', encoding='utf8').read()
corpus = tabby.split()
#names = ['Garfield: ', 'Jon: ', 'Liz: ']

img = Image.open("3_strip4.png")

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
def chainLine(corpus):
    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
     
    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]


    check = False
    while check == False:
        if chain[-1].endswith("."):
            check = True
            break
        if chain[-1].endswith("!"):
            check = True
            break
        if chain[-1].endswith("?"):
            check = True
            break
        else:
            chain.append(np.random.choice(word_dict[chain[-1]]))
            ' '.join(chain)
    return chain

def sentence(chain):
    n = len(chain)
    i = 0
    lineString = ""
    for i in range(n):
        lineString = lineString+chain[i]+" "
    return lineString
    
def stripGen(x,corpus):
    j = 0
    strip = " "
    for j in range(x):
        strip = strip + sentence(chainLine(corpus))+"\n"
    return strip
    
def comicSelect():
    r = str(random.randint(1,5))
    stripName = "3_strip"+r+".png"
    return stripName
     
def comicGen(x,corpus):
    j = 0
    img = Image.open("3_strip1.png").convert("RGBA")
    fnt=ImageFont.truetype('garfield.ttf',10)
    for j in range(x):
        if j == x-1:
            line = sentence(chainLine(corpus))
            wrapped = textwrap.wrap(line, width=25)
            button_img = Image.new('RGBA',(200,55),"white")
            button_draw = ImageDraw.Draw(button_img)
            for y in range(len(wrapped)):
                button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
            img.paste(button_img,(70+393*j, 45))
        else:
            line = sentence(chainLine(corpus))
            wrapped = textwrap.wrap(line, width=25)
            button_img = Image.new('RGBA',(200,50),"white")
            button_draw = ImageDraw.Draw(button_img)
            for y in range(len(wrapped)):
                button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
            img.paste(button_img,(60+480*j, 45))
    res = img.save('comicStrip.png')
    print("Success!")

def multiComicGen(x,corpus):
    j = 0
    comicName = comicSelect()
    fnt=ImageFont.truetype('garfield.ttf',10)
    if comicName == "3_strip1.png":
        img = Image.open(comicName).convert("RGBA")
        for j in range(x):
            if j == x-1:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=35)
                button_img = Image.new('RGBA', (250,60),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img, (70+393*j,45))
            else:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=30)
                button_img = Image.new('RGBA',(200,55),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img,(60+480*j, 45))
                
    if comicName == "3_strip2.png":
        img = Image.open(comicName).convert("RGBA")
        for j in range(x):
            if j == x-1:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=30)
                button_img = Image.new('RGBA', (190,60),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img, (115+423*j,14))
            else:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=25)
                button_img = Image.new('RGBA',(180,55),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img,(120+400*j, 14))
                
    if comicName == "3_strip3.png":
        img = Image.open(comicName).convert("RGBA")
        for j in range(x):
            if j == x-1:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=30)
                button_img = Image.new('RGBA', (215,60),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img, (480+245*j,80))
            else:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=25)
                button_img = Image.new('RGBA',(200,50),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img,(485+320*j, 10))
                
    if comicName == '3_strip4.png':
        img = Image.open(comicName).convert("RGBA")
        for j in range(x):
            if j == x-1:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=20)
                button_img = Image.new('RGBA', (170,60),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img, (138+400*j,10))
            else:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=25)
                button_img = Image.new('RGBA',(200,50),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img,(140+410*j, 15))
                
    if comicName == '3_strip5.png':
        img = Image.open(comicName).convert("RGBA")
        for j in range(x):
            if j == x-1:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=25)
                button_img = Image.new('RGBA', (175,50),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img, (85+360*j,45))
            else:
                line = sentence(chainLine(corpus))
                wrapped = textwrap.wrap(line, width=15)
                button_img = Image.new('RGBA',(130,70),"white")
                button_draw = ImageDraw.Draw(button_img)
                for y in range(len(wrapped)):
                    button_draw.text((0,y*12),wrapped[y],font=fnt,fill=(0,0,0,255))
                img.paste(button_img,(85+360*j, 45))
                
    res = img.save('comicStrip.png')
    print("Success!")
                    
multiComicGen(3,corpus)
    
        
        
    

