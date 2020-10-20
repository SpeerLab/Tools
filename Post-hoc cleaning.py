import os
import glob
import shutil

Base_folder = 'Z:\\Chenghang\\10.3.2020_B2P4A_A\\'
ac_folder = Base_folder + 'acquisition\\'
ana_folder = Base_folder + "analysis\\"
tiff_folder = Base_folder + "stormtiffs\\"

Isfile = glob.glob(ac_folder + '488storm*')
if (Isfile == []) == True:
    print('No 488storm found')
else:
    a = round(len(Isfile) / 7 * 0.05)
    if a < 1:
        a = 1
    b = a * 7
    Isfile_del = Isfile[b:(len(Isfile)-1)]
    for file in Isfile_del:
        os.remove(file)
    print('Delete 95% 488storm.dax')

Isfile = glob.glob(ac_folder + '561storm*')
if (Isfile == []) == True:
    print('No 561storm found')
else:
    a = round(len(Isfile) / 7 * 0.05)
    if a < 1:
        a = 1
    b = a * 7
    Isfile_del = Isfile[b:(len(Isfile)-1)]
    for file in Isfile_del:
        os.remove(file)
    print('Delete 95% 561storm.dax')

Isfile = glob.glob(ac_folder + '647storm*')
if (Isfile == []) == True:
    print('No 647storm found')
else:
    a = round(len(Isfile) / 7 * 0.05)
    if a < 1:
        a = 1
    b = a * 7
    Isfile_del = Isfile[b:(len(Isfile)-1)]
    for file in Isfile_del:
        os.remove(file)
    print('Delete 95% 647storm.dax')

Isfile = glob.glob(ac_folder + '750storm*')
if (Isfile == []) == True:
    print('No 750storm found')
else:
    a = round(len(Isfile) / 7 * 0.05)
    if a < 1:
        a = 1
    b = a * 7
    Isfile_del = Isfile[b:(len(Isfile)-1)]
    for file in Isfile_del:
        os.remove(file)
    print('Delete 95% 750storm.dax')

Isfile = glob.glob(ac_folder + 'Conv_*')
if (Isfile == []) == True:
    print('No Conv.dax found')
else:
    for file in Isfile:
        os.remove(file)
    print('Delete Conv.dax')

Isfile = glob.glob(ac_folder + 'FFC_*')
if (Isfile == []) == True:
    print('No FFC.dax found')
else:
    for file in Isfile:
        os.remove(file)
    print('Delete FFC.dax')

Isfile = glob.glob(ac_folder + 'Regbead_*')
if (Isfile == []) == True:
    print('No Regbead.dax found')
else:
    for file in Isfile:
        os.remove(file)
    print('Delete RegBead.dax')

Isfile = glob.glob(tiff_folder + '*')
if (Isfile == []) == True:
    print('No .tiff found')
else:
    shutil.rmtree(tiff_folder)
    print('Delete all .tiff')

Isfile = glob.glob(ana_folder + 'individual_sections\\*')
if (Isfile == []) == True:
    print('No individual_sections found')
else:
    if os.path.exists(ana_folder + 'individual_sections\\0000\\aligned\\'):
        for anyfolder in Isfile:
            shutil.rmtree(anyfolder + '\\aligned\\')
            shutil.rmtree(anyfolder + '\\rawimages\\for_matlab\\')
        print('Individual_secions cleaned')
    else:
        print('Individual_sections already cleaned (..\\0000\\aligned\\ does not exist)')

Isfile = glob.glob(ana_folder + 'unaligned_original\\storm_merged\\*')
if (Isfile == []) == True:
    print('No unaligned_original, Z-alignment not finished? ')
else:
    Isfile = glob.glob(ana_folder + 'unaligned\\*')
    if (Isfile == []) == False:
        shutil.rmtree(ana_folder + 'unaligned\\')
        print('Delete unaligned')
    Isfile = glob.glob(ana_folder + 'rigid_align\\*')
    if (Isfile == []) == False:
        shutil.rmtree(ana_folder + 'rigid_align\\')
        print('Delete rigid_align')
    Isfile = glob.glob(ana_folder + 'cropped\\*')
    if (Isfile == []) == False:
        shutil.rmtree(ana_folder + 'cropped\\')
        print('Delete cropped')

print('Done!')
