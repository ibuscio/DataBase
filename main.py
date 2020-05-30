import argparse
import logging

logging.basicConfig(level=logging.INFO)

import pandas as pd
logger = logging.getLogger(__name__)

from fortune import Fortune
from data import Engine, Base, Session

def main(filename):
    Base.metadata.create_all(Engine)
    session = Session()
    fortunes = pd.read_csv(filename)

    for index, row in fortunes.iterrows():
        logger.info('Loading rank {} into DB'.format(row['rank']))
        fortune = Fortune(row['rank'],
                           row['title'],
                           row['website'],
                           row['employees'],
                           row['sector'],
                           row['industry'])

        session.add(fortune)
    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The file you want to load into the db', type=str)
    args = parser.parse_args()
    main(args.filename)
