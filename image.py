from PIL import Image, ExifTags
import sys, traceback, argparse

def convert_img(image, size):
    try:
        img = Image.open(image)
        img = img.resize((size, size)).convert('L')
    except:
        print(" Usage: python3 image.py -f imagefile -s 0-200")
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
            if(color >= 0 and color <= 51): string+=" "
            elif(color >= 52 and color <= 127): string+="*"
            elif(color >= 128 and color <= 192): string += "x"
            else: string += "#"
            count+=1 
            if(count == img.size[0]):
                string+="\n"
                count=0      
    print(string)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image to ascii art")
    parser.add_argument("-file", "-f", required=True)
    parser.add_argument("-size", "-s", default=100)
    args = parser.parse_args()
    if(int(args.size) > 200): 
        args.size = 200
        print("(Max size is 200x200)")
    convert_img(args.file, int(args.size))
    