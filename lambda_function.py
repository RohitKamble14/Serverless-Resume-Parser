import json
import boto3
import fitz
import urllib.parse

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ResumeData')

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    print("Fetching file from S3")
    print("Bucket:", bucket)
    print("Key:", key)

    response = s3.get_object(Bucket=bucket, Key=key)
    pdf_content = response['Body'].read()

    with open("/tmp/resume.pdf", "wb") as f:
        f.write(pdf_content)

    doc = fitz.open("/tmp/resume.pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    lines = text.splitlines()
    name = lines[0] if len(lines) > 0 else "Unknown"
    email = next((line for line in lines if "@" in line), "Unknown")
    phone = next((line for line in lines if any(char.isdigit() for char in line) and len(line) >= 10), "Unknown")

    print("Extracted:", name, email, phone)

    table.put_item(Item={
        'Email': email,
        'Name': name,
        'Phone': phone
    })

    return {
        'statusCode': 200,
        'body': json.dumps('Resume processed successfully.')
    }
