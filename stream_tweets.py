from TwitterAPI import TwitterAPI
import time

CONSUMER_KEY = 'zi4TunNmC22NABYXfKeamrzdO'
CONSUMER_SECRET = 'VT9ZiDwdNd8NwNRIIy1OFdDADiRtWzoPveZSPpse3tnlEn8sPu'
ACCESS_TOKEN_KEY = '2714754073-mAGJk4TOSBOADWuVZYbcYiQ3XOZ4j7OUw6AwGhJ'
ACCESS_TOKEN_SECRET = 'gAfl8hYK01Rb1ZslaQe4onL1TOdU44Y442ZBLtaYiVPoM'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('statuses/filter', {'locations':'100,13,101,18', 'lang':'th'})

for item in r:
    #print(item['created_at'] + item['text'] if 'text' in item else item)
	try:
		data = "created_at : "+item['created_at'] + ", user's id : "+item.get('user').get('id_str') + ", lang : "+item['lang'] + ", text : "+item['text']+"\n"
		#", location : " +item.get('user').get('location', 'no location') 
		print(data)

	except BaseException as e:
		print('failed ondata '+str(e) +"\n")
		#time.sleep(5)