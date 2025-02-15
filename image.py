from PIL import Image
import sys

def convert_img(image):
    
    try:
        img = Image.open(image)
    except:
        print("Cannot find " + "'" + image + "'")
        sys.exit()
    img = img.resize((200, 200)).convert('L').rotate(90)
    size = w, h = img.size
    pixels = img.load()
    colors = []
    string = ""
    count = 0
    for x in range(w):
        for y in range(h):
            color = pixels[x, y]
            if(color > 0 and color < 52):
                string+=" "
            elif(color > 51 and color < 128):
                string+="*"
            elif(color > 127 and color < 193):
                string += "x"
            else:
                string += "#"
            count+=1 
            if(count == img.size[0]):
                string+="\n"
                count=0
    #print(img.size)       
    print(string)



if __name__ == "__main__":
    img_arg = sys.argv[1]
    convert_img(img_arg)