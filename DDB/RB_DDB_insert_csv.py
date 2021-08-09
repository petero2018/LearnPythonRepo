import boto3
import csv
import ast
from boto3.dynamodb.conditions import Key
from dynamodb_json import json_util as util

import json

TABLE_NAME = 'customer_validation'
CSV_PATH = '/Users/peterosztodi/Files/Railsbank/DDB/CUSTOMER-VALIDATION.csv'
REGION = 'eu-west-1'

CUSTOMER_VALIDATION_SCHEMA = [{'AttributeName': 'id','AttributeType':'S'},
]

CUSTOMER_VALIDATION_KEYS = [
{
    'AttributeName': 'id',
    'KeyType': 'HASH'
}
]

dynamodb_client = boto3.client("dynamodb", region_name=REGION)
dynamodb_resource = boto3.resource("dynamodb", region_name=REGION)


def create_table_if_not_exists(table_name, Keys, Schema):

    existing_tables = dynamodb_client.list_tables()['TableNames']
    if TABLE_NAME not in existing_tables:

        dynamodb_client.create_table(
            TableName=table_name,
            KeySchema=Keys,
            AttributeDefinitions=Schema,
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        return True

    print(f'Table {TABLE_NAME} already exists in this environment!')
    return False


def put_item(table_name, data):

    response = dynamodb_client.put_item(
        TableName=table_name,
        Item=data
    )
    return response


def read_csv(path):
    with open(path) as f:
        csv_content = f.read().splitlines()
    return csv_content


def convert_string_to_object(item):
    has_content = len(item) > 0
    contains_dict = any(x in ['{', '}'] for x in item)
    contains_list = any(x in ['[', ']'] for x in item)
    if has_content:
        if any([contains_dict, contains_list]):
            return ast.literal_eval(item)
    return []


def clean_up_number(item):
    item_null = item.lower() == 'null'
    item_empty = item == ''

    if any([item_null, item_empty]):
        return '0'
    return str(item)


def put_customer_validation_data():

    try:
        csv_content = read_csv(CSV_PATH)
        csv_reader = csv.reader(csv_content, delimiter=',')

        first_record = True

        for row in csv_reader:
            if (first_record):
                first_record = False
                continue

            id_ = row[0]
            customer_id = row[1]
            date = row[2]
            enduser_id = row[3]
            req_resp_ind = row[4]
            request_type = row[5]
            zoot_application_id = row[6]
            data_provider_attempt = convert_string_to_object(row[7])
            data_provider_hit = convert_string_to_object(row[8])
            decision = row[9]
            decision_reason_code = row[10]
            decision_reason_description = row[11]
            address1 = row[12]
            address2 = row[13]
            annual_income = clean_up_number(row[14])
            cell_phone = row[15]
            city = row[16]
            country = row[17]
            dob = row[18]
            email = row[19]
            first_name = row[20]
            ip_address = row[21]
            last_name = row[22]
            ssn = row[23]
            state = row[24]
            zip_ = row[25]
            middle_name = row[26]
            adverse_action = convert_string_to_object(row[27])
            cash_apr = clean_up_number(row[28])
            credit_limit = clean_up_number(row[29])
            credit_score = clean_up_number(row[30])
            funding_partner = row[31]
            retail_apr = clean_up_number(row[32])
            lender_dti = clean_up_number(row[33])
            lender_score = clean_up_number(row[34])
            mla_indicator = row[35]
            tu_credit_attributes = row[36]

            item = {
                'id': {'S': str(id_)},
                'customer_id': {'S': str(customer_id)},
                'date': {'S': str(date)},
                'enduser_id': {'S': str(enduser_id)},
                'req_resp_ind': {'S': str(req_resp_ind)},
                'request_type': {'S': str(request_type)},
                'zoot_application_id': {'S': str(zoot_application_id)},
                'data_provider_attempt': {'L': data_provider_attempt},
                'data_provider_hit': {'L': data_provider_hit},
                'decision': {'S': str(decision)},
                'decision_reason_code': {'S': str(decision_reason_code)},
                'decision_reason_description': {'S': str(decision_reason_description)},
                'address1': {'S': str(address1)},
                'address2': {'S': str(address2)},
                'annual_income': {'N': annual_income},
                'cell_phone': {'S': str(cell_phone)},
                'city': {'S': str(city)},
                'country': {'S': str(country)},
                'dob': {'S': str(dob)},
                'email': {'S': str(email)},
                'first_name': {'S': str(first_name)},
                'ip_address': {'S': str(ip_address)},
                'last_name': {'S': str(last_name)},
                'ssn': {'S': str(ssn)},
                'state': {'S': str(state)},
                'zip': {'S': str(zip_)},
                'middle_name': {'S': str(middle_name)},
                'adverse_action': {'L': adverse_action},
                'cash_apr': {'N': cash_apr},
                'credit_limit': {'N': credit_limit},
                'credit_score': {'N': credit_score},
                'funding_partner': {'S': str(funding_partner)},
                'retail_apr': {'N': retail_apr},
                'lender_dti': {'N': lender_dti},
                'lender_score': {'N': lender_score},
                'mla_indicator': {'S': str(mla_indicator)},
                'tu_credit_attributes': {'S': str(tu_credit_attributes)}
            }

            response = put_item(TABLE_NAME, item)
        print("Put succeeded:")
        print(f'status_code: {response.status_code}')
    except Exception as e:
        print(str(e))


def unmarshall(dynamodb_json):
    regular_json = util.loads(dynamodb_json)
    return regular_json



def get_customer_validation_data(date):
    table = dynamodb_resource.Table(TABLE_NAME)

    fe = Key('date').gt(date)
    response = table.scan(
        FilterExpression=fe
    )

    return response


if __name__ == '__main__':
    if create_table_if_not_exists(TABLE_NAME, CUSTOMER_VALIDATION_KEYS, CUSTOMER_VALIDATION_SCHEMA):
        put_customer_validation_data()

    date = '2021-07-01'

    resp = get_customer_validation_data(date)
    regular_json = unmarshall(resp.get('Items', []))
    pretty_payload = json.dumps(regular_json, indent=2)

    print(pretty_payload)
    print(f'number of items in payload: {len(regular_json)}')
