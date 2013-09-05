#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import shutil
import sys
import platform

def main():
    
    raw_c_files = glob.glob('*.[Cc][Rr]2')
    raw_n_files = glob.glob('*.[Nn][Ee][Ff]')
    
    raw_c_files.extend(raw_n_files)
    raw_files = raw_c_files

    def classify_company():
        Cpic = 0
        Npic = 0
        NSpic = 0

        for raw_file in raw_files:
            if raw_file[0:4] == 'IMG_':
                Cpic = Cpic + 1
            elif raw_file[0:4] == 'DSCN':
                Npic = Npic + 1
            elif raw_file[0:4] == 'DSC_':
                NSpic = NSpic + 1

        if Cpic>=Npic and Cpic>=NSpic and Cpic:
            return "IMG_"
        elif NSpic>=Npic and NSpic>=Cpic and NSpic:
            return "DSC_"
        elif Npic>=NSpic and Npic>=Cpic and Npic:
            return "DSCN"
        else:
            print "Uh-oh! No Picture here!!(Only support Canon and Nikon camera)"
            if platform.system() == 'Windows':
                os.system("pause")
                sys.exit(0)
            else:
                sys.exit(0)

    company_serial = classify_company()

    if company_serial == 'IMG_':
        raw_ext = '.CR2'
    elif company_serial == 'DSCN':
        raw_ext = '.NEF'
    elif company_serial == 'DSC_':
        raw_ext = '.NEF'
    else:
        pass

    if not os.path.exists('Favorite_RAW'):
        os.mkdir('Favorite_RAW')
    if not os.path.exists('Backup_RAW'):
        os.mkdir('Backup_RAW')

    print "Input your favorite RAW serial number."
    print ""
    print "If you want to Quit just input the q button..."
    print ""

    while True:

        serial_number = raw_input(">>> " + company_serial)
        if serial_number == 'q' or serial_number == 'Q':
            print 'Exit...'
            return
        elif not company_serial+serial_number+raw_ext in raw_files:
            print 'No such file:' + company_serial + serial_number + raw_ext
            print '---'
        elif os.path.exists('./Favorite_RAW/'+company_serial+serial_number+raw_ext):
            print company_serial + serial_number + raw_ext + ' already exists.' 
            print '---'
        else:
            try:
                print "Copy " + company_serial + serial_number + raw_ext +' to /Favorite_RAW folder.' 
                shutil.copy(company_serial+serial_number+raw_ext, './Favorite_RAW')
                if platform.system() == 'Windows':
                    shutil.move(company_serial+serial_number+raw_ext, './Backup_RAW')
                else:
                    shutil.move(company_serial+serial_number+raw_ext, './.Backup_RAW')
                print '---'
            except shutil.Error, e:
                print e

if __name__ == '__main__':
    main()
