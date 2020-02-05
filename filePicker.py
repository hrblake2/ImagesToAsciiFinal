from PIL import Image
import os
import re

def print_image(imagefile):

    chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    # open, resize, and load image
    img = Image.open(imagefile)
    resized_img = img.resize((img.width // 2, img.height // 2)) # format image to fit screen
    width = resized_img.size[0]
    height = resized_img.size[1]
    img = resized_img.load()

    # 3 empty arrays
    avg = [[(0) for (y) in range(height)] for (x) in range(width)]
    mid = [[(0) for (y) in range(height)] for (x) in range(width)]
    final = [[(0) for (y) in range(height)] for (x) in range(width)]

    for (i) in range(height):
        for (j) in range(width):
            avg[j][i] = ((img[j, i][0] + img[j, i][1] + img[j, i][2]) / 3) # pixel matrix of averaged RGB values
            mid[j][i] = int(avg[j][i] / 4) # (av_list / 4) match averaged RGB values to ASCII character
            final[j][i] = chars[mid[j][i]] # final ASCII character matrix
            print(final[j][i] * 2, end='')
        print('')

def file_check(file):
    if file in os.getcwd():
        return file
    else:
        while file not in os.listdir(os.getcwd()):
            print('Files in current working directory: ', end='')
            endswithjpg = re.compile(r'jpg$')
            for i in os.listdir('C:\\Users\\Harrison\\PycharmProjects\\ASCIIArt\\venv'):
                if endswithjpg.search(i) is not None:
                    print(i, end=' ')
            print('\nChoose a file: ')
            file = input()

    return file

def main():
    file = file_check('dog.jpeg')
    print_image(file)

if __name__ == "__main__":
    main()
