import pandas as pd
import os
import json
from datetime import datetime
import argparse


def input_value():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="Please specify the main directory where your source files located")
    args = parser.parse_args()
    return args.source


def simple_collection_process(source):
    try:

        print(source, ' source directory submitted')

        date_time = datetime.now().strftime("%Y-%m-%d")
        if source[len(source)-1] != '/':
            destination = '/'.join([source, ('complaints-' + date_time + '.csv')])
        else:
            destination = source + 'complaints-' + date_time + '.csv'

        for r, d, f in os.walk(source):
            for file in f:
                if ".json" in file:
                    print('Found ', os.path.join(r, file), ' in source directory')
                    with open(os.path.join(r, file)) as f:
                        content = f.read()
                        content = content.replace('"\\"', '"').replace('\\""', '"')
                        if os.path.splitext(file)[0] == "category_names":
                            category_names = pd.Series(json.loads(content))
                        if os.path.splitext(file)[0] == "service_names":
                            service_names = pd.Series(json.loads(content))
                        if os.path.splitext(file)[0] == "complaints":
                            complaints = pd.DataFrame(json.loads(content))

        print('Concat JSON files')

        complaints['category_names'] = complaints['category_id'].map(category_names)
        complaints['service_names'] = complaints['service_id'].map(service_names)
        complaints = complaints.rename(columns={'service_names': 'Service Name', 'category_names': 'Category Name',
                                                'created_at': 'Complaint Created At', 'text': 'Complaint Text'
                                                })

        complaints[['Service Name', 'Category Name', 'Complaint Created At', 'Complaint Text']].to_csv(destination, index=False)
        print('CSV saved to destination', destination)

    except Exception as e:
        print(e)
        exit(1)


def main():

    source = input_value()
    simple_collection_process(source)


if __name__=='__main__':
    main()