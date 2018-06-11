import boto3

def schedule():

	client = boto3.client('events')

	print "provide time in GMT only"
	hour1 = raw_input('Enter start hour: ')
	minute1 = raw_input('Enter start minute: ')

	response = client.put_rule(
	    Name='ec2_start_nawaz',
	    ScheduleExpression='cron(minute1 hour1 * * ? *)'
	)


	hour2 = raw_input('Enter start hour: ')
	minute2 = raw_input('Enter start minute: ')

	response = client.put_rule(
	    Name='ec2_stop_nawaz',
	    ScheduleExpression='cron(minute2 hour2 * * ? *)'
	)

	return "Done"

