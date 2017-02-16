import fields_list
import requests
import json
import pprint
import csv_generator
import sys

#defining url
instance_url = 'https://copperfasten.providentcrm.com/rest/v10'
username = 'SalUpwork17'
password = 'titanhq0702'

#Login - POST /oauth2/token
auth_url = instance_url + '/oauth2/token'

oauth2_token_arguments = {
    'grant_type' : 'password',
    'client_id' : 'SalUpwork090217',
    'client_secret' : 'spamtitan',
    'username' : username,
    'password' : password,
    'platform' : 'custom_api'
}


r = requests.post(auth_url, data = oauth2_token_arguments)
r.headers['Content-Type'] = 'application/json'
content = r.json()
oauth_token = content['access_token']
print oauth_token

#defining parameters
#defining parameters
start_date = sys.argv[1]
end_date = sys.argv[2]

#start_date = "2017-02-08"
#end_date = "2017-02-10"

filter_url = instance_url + "/Leads/filter"

fields_keys = ','.join(fields_list.lead_fields_list.keys())
filter_arguments = {"filter":
                        [
                            {"$and":
                              [
                               {"date_entered":{"$gte":start_date}},
                               {"date_entered":{"$lte":end_date}}
                              ]
                            }
                        ],
                    "max_num":-1,
                    "offset":0,
                    "fields":fields_keys,
                    "order_by":"date_entered",
                    "favorites":False,
                    "my_items":False
}


print '---------------------------------------------------------------'
print '-------------------content-------------------------------------\n'
headers = {'content-type': 'application/json','oauth-token':oauth_token}
data_request = requests.post(filter_url, data=json.dumps(filter_arguments), headers=headers)
# data_request.headers['Content-Type'] = 'application/json'
# data_request.headers['oauth-token'] = oauth_token
data = data_request.json()

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(data['records'])

print '-------------------'
print len(data['records'])



csv_generator.generate_csv(start_date,end_date,fields_list.lead_fields_list.keys(),data,'leads')

