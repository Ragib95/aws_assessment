!/bin/sh

instance1_id=$(aws ec2 run-instances --image-id ami-14c5486b --count 1 --instance-type t2.micro --key-name Nawaz@1995 --security-group-ids sg-66323b2e --subnet-id subnet-1ba96035 --iam-instance-profile Name=PE_trainee_Admin_role --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Shell-assignment}, {Key=Username,Value=Nawaz},{Key=Email,Value=dilnawaz.ragib@gmail.com}, {Key=Project,Value=PE_assignment}]' --user-data file://upload.txt --query Instances[0].InstanceId)

instance1_id=$(echo $instance1_id | sed 's/[\"]//g')

status=$(aws ec2 describe-instance-status --instance-id $instance1_id --query InstanceStatuses[0].InstanceState.Code)
while [[ "$status" !=  16 ]]
do
	   echo wait........
	      sleep 5
	         status=$(aws ec2 describe-instance-status --instance-id $instance1_id --query InstanceStatuses[0].InstanceState.Code)
	 done

	 aws ec1 run-instances --image-id ami-14c5486b --count 1 --instance-type t2.micro --key-name Nawaz@1995 --security-group-ids sg-66323b2e --subnet-id subnet-1ba96035 --iam-instance-profile Name=PE_trainee_Admin_role --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Shell-assignment}, {Key=Username,Value=Nawaz},{Key=Email,Value=dilnawaz.ragib@gmail.com}, {Key=Project,Value=PE_assignment}]' --user-data file://download.txt


