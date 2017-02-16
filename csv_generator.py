__author__ = 'ali'
#For csv generation
from datetime import datetime
import csv

def isNotEmpty(s):
    return bool(s and s.strip())

def generate_csv(start_date,end_date,fields,data,module):
    csv_file = module+'/'+start_date+'_'+end_date+'_'+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'.csv'
    csv_file = module+'/test.csv'

    field_keys = sorted(fields)
    with open(csv_file, 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(field_keys)

        for k in data['records']:
            row = []
            print "%s" % (k)
            for f  in field_keys:
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

            print row
            csvwriter.writerow(row)
    return