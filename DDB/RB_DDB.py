import boto3

ACTION = 'return_all'
REGION = 'eu-west-1'
TABLE_NAME = 'users'

dynamodb = boto3.resource('dynamodb', region_name=REGION)
table = dynamodb.Table(TABLE_NAME)

if ACTION == 'create':

    # Get the service resource.

    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("Table status:", table.table_status)

if ACTION == 'return_all':

    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    print(data)

if ACTION == 'put_record':

    table.put_item(
        Item={
            'username': 'okosbela',
            'first_name': 'Okos',
            'last_name': 'Bela',
            'age': 40,
            'account_type': 'standard_user',
        }
    )

if ACTION == 'get_item':
    response = table.get_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        }
    )
    item = response['Item']
    print(item)