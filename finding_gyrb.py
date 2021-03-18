#!/usr/bin/python
import sys
import os
import getopt

opts,args = getopt.getopt(sys.argv[1:],'-i:',['inputpath='])
for opt_name,opt_value in opts:
    if opt_name in ('-i','--inputpath'):
       path1 = '/home/gyrb/input/'+opt_value+'/'
files = os.listdir(path1)
for file in files:
    fas = {}
    gyr = "[protein=DNA gyrase subunit B]"
    gene = "[gene=gyrB]"
    gyr2 = "[protein=DNA gyrase, B subunit]"
    gyr3 = "gyrase subunit B"
    with open(path1+file, 'r') as fh:
         for line in fh:
             if line.startswith('>'):
                id = line.strip().split('>',1)[1]
                fas[id] = ''
                name = os.path.splitext(file)[0] + "_" + "gyrB"
             else:
                fas[id] += line.replace('\n','')
         for key in fas.keys():
             key = str(key)
             if gyr in key:
                with open(name + ".fas", 'w') as f:
                     f.write('>'+name+'_'+key+'\n')
                     f.write(fas[key] + '\n')
             elif gene in key:
                with open(name + ".fas", 'w') as f:
                     f.write('>'+name+'_'+key+'\n')
                     f.write(fas[key] + '\n')
             elif gyr2 in key:
                with open(name + ".fas", 'w') as f:
                     f.write('>'+name+'_'+key+'\n')
                     f.write(fas[key] + '\n')
             elif gyr3 in key:
                with open(name + ".fas", 'w') as f:
                     f.write('>'+name+'_'+key+'\n')
                     f.write(fas[key] + '\n')
