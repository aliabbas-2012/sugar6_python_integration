import fields_list
import requests
import json
import pprint
import  csv_generator
import sys


#defining url
instance_url = 'https://_server_/rest/v10'
username = ''
password = ''

#Login - POST /oauth2/token
auth_url = instance_url + '/oauth2/token'

oauth2_token_arguments = {
    'grant_type' : '',
    'client_id' : '',
    'client_secret' : '',
    'username' : username,
    'password' : password,
    'platform' : 'custom_api'
}
#defining parameters
start_date = sys.argv[1]
end_date = sys.argv[2]

#start_date = "2017-02-08"
#end_date = "2017-02-10"

r = requests.post(auth_url, data = oauth2_token_arguments)
r.headers['Content-Type'] = 'application/json'
content = r.json()
oauth_token = content['access_token']

#print oauth_token

filter_url = instance_url + "/Opportunities/filter"

fields_keys = ','.join(csv_generator.generate_keys(fields_list.opportunity_fields_list))
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


#print '---------------------------------------------------------------'
#print '-------------------content-------------------------------------\n'

headers = {'content-type': 'application/json','oauth-token':oauth_token}
data_request = requests.post(filter_url, data=json.dumps(filter_arguments), headers=headers)
# data_request.headers['Content-Type'] = 'application/json'
# data_request.headers['oauth-token'] = oauth_token
data = data_request.json()

#-----------don't need to print -------------#
#pp = pprint.PrettyPrinter(depth=6)
#pp.pprint(data['records'])

#print '-------------------'
#print len(data['records'])

csv_generator.generate_csv(start_date,end_date,fields_list.opportunity_fields_list,data,'opportunities')