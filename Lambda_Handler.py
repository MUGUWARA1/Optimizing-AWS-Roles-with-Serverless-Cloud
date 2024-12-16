import boto3
import json
import logging
import os
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)






def publish_to_sns(url, eventsource):
    # Initialize the SNS client
    client = boto3.client('sns')
    
    # Create the SNS input payload
    sns_input = {
        'TopicArn': os.environ['SNS_TOPIC_ARN'],
        'Message': f"Hello, here is the report from Lambda de Karim Derouich  : \n source : {eventsource} \n {url}",
        'Subject': f"Lambda report, date: {datetime.now()}"
    }
    
    # Publish the message to the SNS topic
    response = client.publish(**sns_input)
    
    # Return the response
    return response

def get_Roles_With_No_Permission_Boundary(event):
    try:
        iam_client = boto3.client('iam')
        roles = iam_client.list_roles()['Roles']
        
        # convertir format de datetime au string f
        for role in roles:
            if 'CreateDate' in role:
                role['CreateDate'] = role['CreateDate'].isoformat()
                
        # Verifier chaque role si il a un PB 
        roles_without_PB=[]   
        for role in roles :
            if 'PermissionsBoundary' not in role:
                roles_without_PB.append({
                        'RoleName': role['RoleName'],
                        'RoleArn': role['Arn']
                    })
                        

        logger.info("Roles retrieved successfully")
        
        
        
        
        s3 = boto3.client('s3')
        # Upload JSON to S3
        
        bucket_name = 'emi-artifacts'
        object_key = 'roles_without_permissions_boundary1.json'
        res={"roles": roles_without_PB}
        summary_json = json.dumps(res, indent=4)
        s3.put_object(Body=summary_json, Bucket=bucket_name, Key=object_key)
        url = generate_presigned_url(bucket_name,object_key)
        resultat = {"url":url ,"roles":roles_without_PB}
        publish_to_sns(url,event)
        
    
        return resultat

        
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}
        
        
def generate_presigned_url(bucket_name, object_key, expiration=3600):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_key},
                                                    ExpiresIn=expiration)
    except Exception as e:
        logger.error(f"Error generating pre-signed URL: {str(e)}")  
        return None
    
    return response


def lambda_handler(event , context):
    try:
        return get_Roles_With_No_Permission_Boundary(event)
    except Exception as e:
        logger.error(f"Lambda handler error: {str(e)}")
        return {"error": str(e)}



#publish_to_sns(get_Roles_With_No_Permission_Boundary(),event)