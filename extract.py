"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='tests/test-neos-2020.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos_dict = {}
    neos = []
    keys = ['pdes', 'name', 'diameter', 'pha']
    with open(neo_csv_path, 'r') as neos_file:
        reader = csv.DictReader(neos_file)
        for row in reader:
            designation = row['pdes']
            name = row['name']
            diameter = row['diameter']
            if row['pha'] == 'Y':
                hazardous = True
            if row['pha'] == 'N' or row['pha'] == '':
                hazardous = False
            neo = NearEarthObject(designation,name,diameter,hazardous)
            neos.append(neo)
    return neos

def load_approaches(cad_json_path='tests/test-cad-2020.json'):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    ca = []
    with open(cad_json_path, 'r') as cad_file:
        contents = json.load(cad_file)
        for item in contents['data']:
            ca.append(CloseApproach(item[0],time=item[3],distance=float(item[4]),velocity=float(item[7])))
            
    return ca
