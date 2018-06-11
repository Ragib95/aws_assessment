import boto3

def lambda_handler(event, context):
    #print event['Records'][0]['s3']['object']['key']
    print 'I am triggered'
    
    s3 = boto3.resource('s3')
    source= { 'Bucket' : 'nawaz95', 'Key': event['Records'][0]['s3']['object']['key']}
    dest = s3.Bucket('nawaz95replica')
    dest.copy(source, event['Records'][0]['s3']['object']['key'] )
    
    print 'Replica done: ', event['Records'][0]['s3']['object']['key'] 
    return 'Success'