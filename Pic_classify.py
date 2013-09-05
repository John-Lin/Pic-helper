#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import glob
import shutil
import platform

def main():
    raw_c_files = glob.glob('*.[Cc][Rr]2')
    raw_n_files = glob.glob('*.[Nn][Ee][Ff]')
    jpg_files = glob.glob('*.[Jj][Pp][Gg]')
    mov_c_files = glob.glob('*.[Mm][Oo][Vv]')
    mov_n_files = glob.glob('*.[Aa][Vv][Ii]')
    png_files = glob.glob('*.[Pp][Nn][Gg]')

    raw_c_files.extend(raw_n_files)
    mov_c_files.extend(mov_n_files)

    raw_files = raw_c_files
    mov_files = mov_c_files

    if not os.path.exists('RAW') and len(raw_files) != 0:
        os.mkdir('RAW')
    if not os.path.exists('JPG') and len(jpg_files) != 0:
        os.mkdir('JPG')
    if not os.path.exists('MOV') and len(mov_files) != 0:
        os.mkdir('MOV')
    if not os.path.exists('PNG') and len(png_files) != 0:
        os.mkdir('PNG')

    if os.path.exists('Pic_selector.exe') and os.path.exists('JPG') and platform.system() == 'Windows':
        shutil.copy('Pic_selector.exe' ,'./JPG')
    elif os.path.exists('Pic_selector.py') and os.path.exists('JPG') and not os.path.exists('Pic_selector.exe'):
        shutil.copy('Pic_selector.py' ,'./JPG')

    if os.path.exists('RAW_selector.exe') and os.path.exists('RAW') and platform.system() == 'Windows':
        shutil.copy('RAW_selector.exe' ,'./RAW')
    elif os.path.exists('RAW_selector.py') and os.path.exists('RAW') and not os.path.exists('RAW_selector.exe'):
        shutil.copy('RAW_selector.py' ,'./RAW')

    if raw_files == mov_files == jpg_files == png_files == []:
        print "No file can be classified!"
        if platform.system() == 'Windows':
            os.system("pause")
            sys.exit(0)
        else:
            sys.exit(0)

    for raw_file in raw_files:
        try:
            print "Move %s to %s" %(raw_file, os.path.join('\RAW', raw_file))
            shutil.move(raw_file, './RAW')
        except shutil.Error, e:
            print e

    for mov_file in mov_files:
        try:
            print "Move %s to %s" %(mov_file, os.path.join('\MOV', mov_file))
            shutil.move(mov_file, './MOV')
        except shutil.Error, e:
            print e

    for jpg_file in jpg_files:
        try:
            print "Move %s to %s" %(jpg_file, os.path.join('\JPG', jpg_file))
            shutil.move(jpg_file, './JPG')
        except shutil.Error, e:
            print e

    for png_file in png_files:
        try:
            print "Move %s to %s" %(png_file, os.path.join('\PNG', png_file))
            shutil.move(png_file, './PNG')
        except shutil.Error, e:
            print e

    print "All Image files have been classified finished!"

    if platform.system() == 'Windows':
        os.system("pause")
        sys.exit(0)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
