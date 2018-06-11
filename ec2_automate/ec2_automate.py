import ec2_change
import ec2_default

user = raw_input('Do you want to change the schedule(y or n): ')


if user == 'y':
	ec2_change.schedule()
else:
    ec2_default.schedule()


