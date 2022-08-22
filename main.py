'''
Create @ 2017/03/29
Author: zhouchao
'''


import re
import os


def main():
    dir = cur_file_dir()
    pinmap_dir = dir + r'\Pinmap.txt'
    output_dir = dir + r'\output.atp'
    pattern = re.compile(r'(?<=gOS_Bridge\s)\w+')
    # print(pattern.findall('OS_VSS	ooo\n   OS_VSS	qqq'))
    with open(output_dir, mode='w') as output_file:
        output_file.write('opcode_mode = single;\nimport tset timeplate_1;\n')
        with open(pinmap_dir, mode='r') as f:  # , encoding='UTF-8'
            lines = f.readlines()
            pinlist = pattern.findall(' '.join(lines))
        output_file.write('vm_vector	($tset,' + ','.join(pinlist) + ')\n')
        output_file.write('{\nstart_label OS_Bridge_start:\n')
        pin_cnt = len(pinlist)
        output_file.write('> timeplate_1 ' + '0 ' *
                          pin_cnt + ';\n')  # first all 0 row
        for i in range(pin_cnt):  # Row index
            tmpstr = '> timeplate_1 '
            for j in range(pin_cnt):  # Column	index
                if i == j:
                    tmpstr += '1 '
                else:
                    tmpstr += 'L '
            output_file.write(tmpstr + ';\n')
        output_file.write('> timeplate_1 ' + '0 ' *
                          pin_cnt + ';\n')  # last all 0 row
        output_file.write('}')


def cur_file_dir():
    path = os.getcwd()
    return path


if __name__ == '__main__':
    main()
