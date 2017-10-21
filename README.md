usage: get_dcm_series_description.py [-h] [-indir INDIR] [-outfile OUTFILE]
                                     [-v]

this code takes the series description name (for ex: CT, T2WI, T1WI. These names are different for each institution) from the dicom file in corrent directory tree and creates a list. This code depends on python3, pydicom, argparse, os and time.

optional arguments:
  -h, --help        show this help message and exit
  -indir INDIR      : the name of the dir_tree where dicom datas are, default:
                    '.'
  -outfile OUTFILE  : name of file to seve the list.
  -v, --version     show program's version number and exit
