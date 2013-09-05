#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import shutil
import sys
import platform

def main():
    jpg_files = glob.glob('*.[Jj][Pp][Gg]')

    def classify_company():
        Cpic = 0
        Npic = 0
        NSpic = 0

        for jpg_file in jpg_files:
            if jpg_file[0:4] == 'IMG_':
                Cpic = Cpic + 1
            elif jpg_file[0:4] == 'DSCN':
                Npic = Npic + 1
            elif jpg_file[0:4] == 'DSC_':
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
    if not os.path.exists('Favorite_Pic'):
        os.mkdir('Favorite_Pic')
    if not os.path.exists('Backup_Pic'):
        os.mkdir('Backup_Pic')

    print "Input your favorite pictures serial number."
    print ""
    print "If you want to Quit just input the q button..."
    print ""

    while True:

        serial_number = raw_input(">>> " + company_serial)
        if serial_number == 'q' or serial_number == 'Q':
            print 'Exit...'
            return
        elif not company_serial+serial_number+'.JPG' in jpg_files:
            print 'No such file:' + company_serial + serial_number + '.JPG'
            print '---'
        elif os.path.exists('./Favorite_Pic/'+company_serial+serial_number+'.JPG'):
            print company_serial + '%s.JPG already exists.' %(serial_number)
            print '---'
        else:
            try:
                print "Copy " + company_serial + "%s.JPG to /Favorite_Pic folder." %(serial_number)
                shutil.copy(company_serial+serial_number+'.JPG', './Favorite_Pic')
                if platform.system() == 'Windows':
                    shutil.move(company_serial+serial_number+'.JPG', './Backup_Pic')
                else:
                    shutil.move(company_serial+serial_number+'.JPG', './.Backup_Pic')
                print '---'
            except shutil.Error, e:
                print e

if __name__ == '__main__':
    main()
