__author__ = 'ali'
#For csv generation
from datetime import datetime
import csv
import os
import sys
import io

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
        #print(str(v))
        try:
            cols.append(str(v))
        except:
            print('')

    return cols

def generate_csv(start_date,end_date,fields,data,module):
    create_dir_if_not_exist(module)
    #csv_file = module+'/'+module.capitalize()+'_'+start_date+'_'+end_date+'_'+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.csv'
    csv_file = module+'/'+module.capitalize()+'_'+start_date+'_'+end_date+'_'+datetime.now().strftime('%Y-%b-%d')+'.csv'
  
    #csv_file = module+'/test.csv'

    #field_keys = sorted(fields.keys())
    with open(csv_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

        columns = generate_columns(fields)

        if sys.version_info.major >= 3:
            writer_file =  io.StringIO()
        else:
            writer_file =  io.BytesIO()

        csvwriter.writerow(columns)


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