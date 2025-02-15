from PIL import Image

def convert_img():
    img = Image.open("image.jpg")
    img = img.resize((150, 150)).convert('L').rotate(0)
    img.show()
    size = w, h = img.size
    pixels = img.load()
    colors = []
    string = ""
    count = 0
    for x in range(w):
        for y in range(h):
            color = pixels[x, y]
            if(color > 0 and color < 52):
                string+="."
            elif(color > 51 and color < 128):
                string+=":"
            elif(color > 127 and color < 193):
                string += "*"
            else:
                string += "#"
            count+=1 
            if(count == img.size[0]):
                string+="\n"
                count=0
    #print(img.size)       
    print(string)



convert_img()