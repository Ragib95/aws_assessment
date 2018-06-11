import boto3


def schedule():
	client = boto3.client('events')

	response = client.put_rule(
	    Name='ec2_start_nawaz',
	    ScheduleExpression='cron(0 10 * * ? *)'
	)

	response = client.put_rule(
	    Name='ec2_start_nawaz',
	    ScheduleExpression='cron(0 20 * * ? *)'
	)

	return "Done"