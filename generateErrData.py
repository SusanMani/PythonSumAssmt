# Problem 1
# This file generates random sensor data with random error inserted

import random
import csv
import time


# Generates random numbers between a and b that are less than 1
def generate_data(a, b):

    sensor = []

    for i in range(a,b):

        # generate random floats between 0 and 1
        numbers = random.uniform(0, 1)
        sensor.insert(i,numbers)

    return sensor


# Get timestamp
def get_timestamp():

    stamp = time.gmtime()

    # change to correct format
    timestamp = time.strftime("%x %X", stamp)

    return timestamp


# Write random sensor data to file
# This is also used to generate dataGenCorr.csv
with open('dataGenCorr.csv', 'a') as csv_file:

    print('Opening file ....')

    data_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL, lineterminator='\r')

    # generate data for 32 regions
    print('Generating data set...')

    # generate random index to insert error
    random_1 = random.randint(1,31)
    random_2 = random.randint(1,15)

    for data in range(0, 32):

        # generate timestamp
        time_stamp = get_timestamp()

        # generate the required pipeline sensor data (16 points each)
        x = generate_data(0, 16)

        # when random index is reached one error is inserted
        if data == random_1:

            # convert string to list
            get_x = list(x)

            # insert error into file
            get_x[random_2] = "err"

            # convert list back to string to insert into file
            x = get_x

        # append number of pipeline and date timestamp to data
        y = [data + 1] + [time_stamp] + x

        print(y)

        # write to csv
        data_writer.writerow(y)

    print('Writing data to file ....')
    print('File Generated.')

