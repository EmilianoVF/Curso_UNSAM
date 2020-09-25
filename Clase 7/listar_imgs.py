import argparse
import os


def listar_imgs():

    '''
    Lista las imagenes dentro del directorio que le pasas incluyendo
    los subdirectorios
    '''
    parser = argparse.ArgumentParser(description='Te lista las imagenes que'
                                     'tenes en tu directorio y subdirectorio')
    parser.add_argument('--path', required=True,
                        help='Es el directorio donde estan las fotos')
    parser.add_argument('--format', default='png', help='Es el formato en el'
                        'que estan tus fotos, por defecto es png')
    args = parser.parse_args()
    directorio = args.path
    format = args.format
    imgs = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-3:] == format:
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
    listar_imgs()
