# -*- coding: utf-8 -*-
import argparse, dicom, os, time

parser = argparse.ArgumentParser(
    description='''this code takes the series description name
    (for ex: CT, T2WI, T1WI. These names are different for each institution)
    from the dicom file in corrent directory tree and creates a list.
    This code depends on python3, pydicom, argparse, os and time.''',
    )
parser.add_argument("-indir", nargs= 1, help=": the name of the dir_tree where dicom datas are, default: '.'  ")
parser.add_argument("-outfile", nargs= 1, help=": name of file to seve the list.  ")
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1, Oct/21/2017')
args = parser.parse_args()

try:
    in_dir = args.indir[0]
except:
    in_dir = '.' # defaul target directory
try:
    out_file = args.outfile[0]
except:
    pass

print("in_dir is '" + in_dir + "'")
print("out_file is '" + out_file + "'")


n, total = 0, 0
start = time.time()

print()
print('code running')

sequence_list = []

print()
for root, dirs, files in os.walk(in_dir):
    total += 1
print("a total of", total, "files")
print()
verpose_point = total // 20 + 1

for root, dirs, files in os.walk(in_dir):
    for file_name in files:
        file_path = root + "/" + file_name
        try:
            ds = dicom.read_file(file_path)
            try:
                sequence_name = ds.SeriesDescription
            except:
                sequence_name = 'NoName'
                print('NoName was found!!')
            if sequence_name in sequence_list:
                pass
            else:
                sequence_list.append(sequence_name)

        except:
            pass

    n += 1
    if n == 1 or n == 3 or n == 10 or n % verpose_point == 0:
        elapsed_time = time.time() - start
        print("{0}/{1} cases checked".format(n, total))
        try:
            print("elapsed/est_total: {0:2.2f}/{1:2.2f} sec".format(elapsed_time, ((elapsed_time/n)*total)))
        except:
            pass
        print(len(sequence_list), "different names, ex: ", sequence_list[-1:])
        print(' ')


try:
    f = open(out_file, 'w')
    for x in sequence_list:
        f.write(", " + str(x) + ": \n")
    f.close()
except:
    pass

elapsed_time = time.time() - start
print(sequence_list)
print()
print("finished!")
print("{0} different names found in {1:2.0f} sec".format(len(sequence_list), elapsed_time))
