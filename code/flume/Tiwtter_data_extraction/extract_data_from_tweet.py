# import necessary packages
import datetime
import tweepy
import schedule


# open the file which contains the account informaiton about accessing to Tweet API
with open('tweet_api.txt') as file:
        text = file.read()
        lines = (text.split('\n'))
        consumer_api_key = lines[0].split(' = ')[1]
        consumer_api_secret_key = lines[1].split(' = ')[1]
        access_token = lines[2].split(' = ')[1]
        access_token_secret = lines[3].split(' = ')[1]


# set up an instance for access to Tweet API
auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# define a class for receiving the streaming data from Tweet API
class MyStreamListener(tweepy.StreamListener):
        # create a daily_data_container list. This list allows us to keep daily tweet data, save
        # these data into a csv file, delete all elements in the list, and use the list to keep
        # next day's tweet data
        global daily_data_container
        daily_data_container = []

        def write_data_to_local(self):
		'''
		Description: This function helps users to write the data which is extracted from
			     twitter API to a local csv file
		Parameters: -self: Class variables
		Returns: None 
		'''
                global daily_data_container

                # GET TIME FOR CSV FILES. Because we collect the streaming data first and save the 
		# streaming data in the next day, we have to get the current time and subtract 1day
		# from the current time.  
		time_mark = datetime.datetime.strftime((datetime.datetime.now()-datetime.timedelta(days=1)), '%Y%m%d')
	
                # write the daily tweet data in daily_data_container to a csv file
                with open('data/tweet_data_' + time_mark + '.csv', 'w') as f:
			for i in range(0, len(daily_data_container)):
				# create the row index for each data row
				daily_data_container[i].insert(0, time_mark + '_streamdata_' + str(i+1))
				# write to the .csv file
				f.write("%s\n" % daily_data_container[i])

                # empty all data in the daily_data_container, print a message
                del daily_data_container[:]
                print('Message: already write daily data (' + time_mark + ') to a csv file and deleted all values in daily_data_container')


        def on_status(self, status):
		'''
                Description: This function helps users to extract data from the twitter API
                Parameters: -self: Class variables
			    -status: twitter information
                Returns: None
                '''
                global daily_data_container
                schedule.run_pending()
		
		# discard retweet data
                if 'RT @' not in status.text:
                        tweet_item = {
                                'id_str': status.id_str,
                                'text': status.text,
                                'received_at': datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
                                }
			# find the tweet posts containg street harassment information
			harassment_word_list = ['cat-called', 'followed', 'physically assaulted', 'harass', 'stalk']
			for word in harassment_word_list:
				if word in tweet_item['text'].lower():
					tweet_content = [tweet_item['id_str'].encode("utf-8") + ',' \
						+ tweet_item['text'].replace(',', '').encode("utf-8") + ',' \
						+ tweet_item['received_at'].encode("utf-8")]

					daily_data_container.append(tweet_content)
					break


if __name__ == '__main__':
	# start to receive data from twitter
	stream_listener = MyStreamListener()
	stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

	# set the scheduler, it allows us to write the twitter data in a csv file on a daily basis
	schedule.every().day.at("1:00").do(stream_listener.write_data_to_local)

    # filter the Tweet text, only exteact the text which contains two key words--"restaurant"
	stream.filter(locations=[144.6075439453,-38.395491533, 145.2035522461,-37.5990001506], languages=['en'])
