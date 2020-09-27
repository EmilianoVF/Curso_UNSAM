import os
import datetime
import time
import argparse


def listar_imgs():

    '''
    Lista las imagenes dentro del directorio que le pasas incluyendo
    los subdirectorios
    '''

    imgs = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-3:] == formato:
                imgs.append([root, name, dirs])

    if len(imgs) == 0:
        print('No hay imagenes en tu directorio')
    else:
        print('Las imagenes en tu directorio son :')
        print('---------------------------------')
        for root, img, dirs in imgs:
            print(img)
    return imgs


def modifica_imgs(imgs):
    new_imgs = []
    for root, img, dirs in imgs:
        path = os.path.join(root, img)
        fecha = img[len(img) - 12: -4:]
        ts_modifi = time.mktime(time.strptime(fecha, '%Y%m%d'))
        ts_acceso = datetime.datetime.now().timestamp()
        name_img = img[0:len(img)-13] + '.png'
        os.utime(path, (ts_acceso, ts_modifi))
        os.rename(path, os.path.join(root, name_img))
        new_imgs.append([root, name_img, dirs])
    return new_imgs


def traslada_imgs(new_imgs):
    if not os.path.isdir(second_path):
        os.mkdir(second_path)
    for root, img, dirs in new_imgs:
        old_path = os.path.join(root, img)
        new_path = os.path.join(second_path, img)
        os.rename(old_path, new_path)
    return


def borro_directorios(directorio):
    for root, dirs, files in os.walk(directorio, topdown=False):
        if os.path.isdir(root) and len(os.listdir(root)) == 0:
            os.rmdir(root)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Te lista las imagenes que'
                                     'tenes en tu directorio y subdirectorio')
    parser.add_argument('--path', required=True,
                        help='Es el directorio donde estan las fotos')
    parser.add_argument('--formato', default='png', help='Es el formato en el'
                        'que estan tus fotos, por defecto es png')
    parser.add_argument('--second_path', required=True,
                        help='Lugar a donde van a parar tus imagenes')
    args = parser.parse_args()
    second_path = args.second_path
    directorio = args.path
    formato = args.formato
    imgs = listar_imgs()
    new_imgs = modifica_imgs(imgs)
    traslada_imgs(new_imgs)
    borro_directorios(directorio)
