import boto3
import json

TABLE_NAME = 'users'


def get_local_client(resource_name):
    return boto3.client(resource_name, region_name='eu-west-1')


class BotoWrapper(object):

    def __init__(self):
        self.local_dynamodb_client = get_local_client('dynamodb')
        self.local_dynamodb_streams_client = get_local_client('dynamodbstreams')

    def get_stream_arn(self):
        describe_table_response = self.local_dynamodb_client.describe_table(TableName=TABLE_NAME)
        return describe_table_response['Table']['LatestStreamArn']

    def get_shard_object_array(self, stream_arn):
        describe_stream_response = self.local_dynamodb_streams_client.describe_stream(StreamArn=stream_arn)
        return describe_stream_response['StreamDescription']['Shards']

    def get_data_from_shard(self, shard_iterator):
        records_in_response = self.local_dynamodb_streams_client.get_records(ShardIterator=shard_iterator, Limit=1000)
        return records_in_response['Records']

    def run_example(self):
        stream_arn = self.get_stream_arn()
        shards = self.get_shard_object_array(stream_arn)

        for shard in shards:
            iterator = self.local_dynamodb_streams_client.get_shard_iterator(
                StreamArn=stream_arn,
                ShardId=shard['ShardId'],
                ShardIteratorType='TRIM_HORIZON'
            )
            records = self.get_data_from_shard(iterator['ShardIterator'])
            for record in records:
                print("####  DYNAMO RECORD  ####")
                print("")
                print(json.dumps(record,
                                 sort_keys=True,
                                 indent=4,
                                 default=str))
                print("")
                print("")


if __name__ == '__main__':
    boto_wrapper = BotoWrapper()
    boto_wrapper.run_example()