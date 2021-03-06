"""
The program is a possible solution for the problem to concatenate category names,
service names and complaints in JSON format and save the output in CSV format.

The program can be invoked by running simple_collection_process.py with two mandatory arguments.
First mandatory argument is the source folder to specify where the three JSON files located.
Second mandatory argument is the destination folder to specify the location the concatenated
output in CSV format should be saved into.

Possible prompt to invoke:
python simple_collection_process.py -s ~/data-engineer-applicant-exercise/ -d ~/data-engineer-applicant-exercise/simple_collection_process/

Version: Python 3.6.8
Created by: Peter Osztodi
"""


import pandas as pd
import os
import json
from datetime import datetime
import argparse


def input_value():
    parser = argparse.ArgumentParser(description="""
                                                    These arguments are for the purpose to specify the location of JSON 
                                                    files need concatenation (source) and the location the concatenated
                                                    CSV output should be saved. 
                                                 """)
    parser.add_argument(
                        "-s",
                        "--source",
                        type=str,
                        metavar='',
                        required=True,
                        help="Please specify the main directory where your source JSON files located"
                       )

    parser.add_argument(
                        "-d",
                        "--destination",
                        metavar='',
                        required=True,
                        type=str,
                        help="Please specify the main directory where your CSV file should be saved"
                       )
    args = parser.parse_args()
    return {
                "source": args.source,
                "destination": args.destination
            }


def simple_collection_process(source, destination):
    try:

        print('{} source and {} destination directories submitted'.format(source, destination))

        date_time = datetime.now().strftime("%Y-%m-%d")
        if destination[len(destination)-1] != '/':
            destination = '/'.join([destination, ('complaints-' + date_time + '.csv')])
        else:
            destination = destination + 'complaints-' + date_time + '.csv'

        for r, d, f in os.walk(source):
            for file in f:
                if ".json" in file:
                    print('Found ', os.path.join(r, file), ' in source directory')
                    with open(os.path.join(r, file)) as f:
                        content = f.read()
                        content = content.replace('"\\"', '"').replace('\\""', '"')
                        if os.path.splitext(file)[0] == "category_names":
                            category_names = pd.Series(json.loads(content))
                        elif os.path.splitext(file)[0] == "service_names":
                            service_names = pd.Series(json.loads(content))
                        elif os.path.splitext(file)[0] == "complaints":
                            complaints = pd.DataFrame(json.loads(content))
                        else:
                            print('Unknown JSON file found')

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

    inputs = input_value()
    simple_collection_process(inputs['source'], inputs['destination'])


if __name__=='__main__':
    main()