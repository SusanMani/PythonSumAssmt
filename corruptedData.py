# Test generated data from file for corrupt entries

import csv
import time
import logging


# enable logging : include timestamp in log, level of log and message passed
logging.basicConfig(format='[%(asctime)s] |%(levelname)-5s|: %(message)s',level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)

logger.info('Start Reading File ...')


# This functions checks for the string "err"
# in the parameter passed to it
# and returns index number if found
# otherwise returns the value 0 if none is found
def corrupt_check(readings):

    # check for substring "err"
    if any("err" in s for s in readings):

        return readings.index("err") - 1

    else:

        return 0


# Open data set to check for corrupted data
with open('dataGenCorr.csv', 'rU') as csv_datafile:

    # Read file
    csv_reader = csv.reader(csv_datafile)

    for row in csv_reader:

        data_line = str(row)

        # find pipeline number in data set
        comma_index_1 = data_line.find(',')
        pipeline_num = data_line[2:comma_index_1 - 1]

        # find record timestamp in data set
        comma_index_2 = data_line.find(',', data_line.find(',') + 1)
        reading_timestamp = data_line[comma_index_1 + 3: comma_index_2 - 1]

        # Use function corrupt_check for each row in data file
        check_err = corrupt_check(row)

        # if error is found the pipeline & sensor number to sent to error logger
        if check_err != 0:

            # error message if corrupt data is found
            logger.error('ERROR FOUND IN PIPELINE :' + ' ' + pipeline_num +
                         ' AT SENSOR: ' + str(check_err) + ' [Data recorded on the '+ reading_timestamp +']')

        # sleep to test logger timestamp
        time.sleep(0.05)
