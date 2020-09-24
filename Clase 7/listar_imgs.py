import os
import sys

directorio = str(sys.argv[1])


def listar_imgs(directorio):

    '''
    Lista las imagenes dentro del directorio que le pasas incluyendo
    los subdirectorios
    '''
    imgs = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-3:] == 'png':
                imgs.append(name)
    if len(imgs) == 0:
        print('No hay imagenes en tu directorio')
    else:
        print('Las imagenes en tu directorio son :')
        print('---------------------------------')
        for img in imgs:
            print(img)
    return


if __name__ == '__main__':
    listar_imgs(sys.argv[1])
