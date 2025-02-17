from PIL import Image, ExifTags
import sys, traceback

def convert_img(image, size):
    try:
        img = Image.open(image)
        img = img.resize((size, size)).convert('L')
    except:
        traceback.print_exc()
        sys.exit() 
    if not img.getexif(): # 
            img=img.rotate(90)
    size = w, h = img.size
    pixels = img.load()
    colors = []
    string = ""
    count = 0

    for y in range(h):
        for x in range(w-1, -1, -1): # image is inverted by pillow for a reason unfamiliar to me
            color = pixels[y, x]
            if(color > 0 and color <= 51): string+=" "
            elif(color >= 52 and color <= 127): string+="*"
            elif(color >= 128 and color <= 192): string += "x"
            else: string += "#"
            count+=1 
            if(count == img.size[0]):
                string+="\n"
                count=0      
    print(string)
    
if __name__ == "__main__":
    img_arg = sys.argv[1]
    size_arg = int(sys.argv[2])
    if(size_arg > 200): 
        size_arg = 200
        print("(Max size is 200x200)")
    convert_img(img_arg, size_arg)
    