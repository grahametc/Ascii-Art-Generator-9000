from PIL import Image, ExifTags
import sys, traceback

def convert_img(image):
    try:
        img = Image.open(image)
    except:
        print(f"Cannot find {image}")
        sys.exit() 
        traceback.print_exc()
    img = img.resize((150, 150)).convert('L')
    print(img.getexif())
    if not img.getexif(): # 
            img=img.rotate(90)
    size = w, h = img.size
    pixels = img.load()
    colors = []
    string = ""
    count = 0

    for x in range(w):
        for y in range(h):
            color = pixels[x, y]
            if(color > 0 and color < 52): string+=" "
            elif(color > 51 and color < 128): string+="*"
            elif(color > 127 and color < 193): string += "x"
            else: string += "#"
            count+=1 
            if(count == img.size[0]):
                string+="\n"
                count=0      
    print(string)
    

if __name__ == "__main__":
    img_arg = sys.argv[1]
    convert_img(img_arg)
    
    