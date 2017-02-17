__author__ = 'ali'
#For csv generation
from datetime import datetime
import csv
import os
def isNotEmpty(s):
    return bool(s and s.strip())

def create_dir_if_not_exist(module):
    if os.path.exists(module)==False:
        os.mkdir(module)

def generate_keys(fields):
    keys = []
    for k,v in fields:
        keys.append(k)
    return keys

def generate_columns(fields):
    cols = []
    for k,v in fields:
        cols.append(v)
    return cols

def generate_csv(start_date,end_date,fields,data,module):
    create_dir_if_not_exist(module)
    #csv_file = module+'/'+module.capitalize()+'_'+start_date+'_'+end_date+'_'+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.csv'
    csv_file = module+'/'+module.capitalize()+'_'+start_date+'_'+end_date+'_'+datetime.now().strftime('%Y-%b-%d')+'.csv'


    #csv_file = module+'/test.csv'

    #field_keys = sorted(fields.keys())
    with open(csv_file, 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(generate_columns(fields))

        for k in data['records']:
            row = []
            #print "%s" % (k)
            for f,v  in fields:
                if f in k.keys():
                    if  k[f]!=None:
                        if isinstance(k[f],int):
                            row.append(k[f])
                        else:
                            row.append(k[f].encode('utf-8'))
                    else:
                        row.append('')
                else:
                    row.append('')

            #print row
            csvwriter.writerow(row)
    return