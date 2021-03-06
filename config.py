"""
Setup required data path.

Create file structure related to the WORKSPACE (default to the user home)
and stores paths in config.yaml.
"""

import os
import yaml

from seisnn import utils

WORKSPACE = os.path.expanduser('~')
SDS_ROOT = os.path.join(WORKSPACE, 'SDS_ROOT')
SFILE_ROOT = os.path.join(WORKSPACE, 'SFILE_ROOT')

DATASET_ROOT = os.path.join(WORKSPACE, 'dataset')
SQL_ROOT = os.path.join(WORKSPACE, 'sql_database')

CATALOG_ROOT = os.path.join(WORKSPACE, 'catalog')
GEOM_ROOT = os.path.join(WORKSPACE, 'geom')
MODELS_ROOT = os.path.join(WORKSPACE, 'models')

config = {
    'WORKSPACE': WORKSPACE,
    'SDS_ROOT': SDS_ROOT,
    'SFILE_ROOT': SFILE_ROOT,

    'DATASET_ROOT': DATASET_ROOT,
    'SQL_ROOT': SQL_ROOT,

    'CATALOG_ROOT': CATALOG_ROOT,
    'GEOM_ROOT': GEOM_ROOT,
    'MODELS_ROOT': MODELS_ROOT,
}


if __name__ == '__main__':
    path_list = [
        DATASET_ROOT,
        SQL_ROOT,

        CATALOG_ROOT,
        MODELS_ROOT,
        GEOM_ROOT,
    ]
    for d in path_list:
        utils.make_dirs(d)

    path = os.path.join(os.path.expanduser("~"), 'config.yaml')
    with open(path, 'w') as file:
        yaml.dump(config, file, sort_keys=False)

    print('SeisNN initialized.')
