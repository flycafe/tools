##########################################
# $Name:     fm.py
# $Function: file modify module
# $Versin:   V1.0
# $Author:   Yin Xi
# $Created:  2016-12-15
##########################################

import os

#replace a line in file
def f_replace_line(src_file,target_line,new_line):
        bak_file=src_file + '.bk'
        os.system('cp -p ' + src_file + ' ' + bak_file)
        f=file(src_file,'r')
        lines=f.readlines()
        flen=len(lines)
        for i in range(flen):
                if target_line in lines[i]:
                        lines[i]=new_line
                        f.close()
        f=file(src_file,'w')
        f.writelines(lines)
