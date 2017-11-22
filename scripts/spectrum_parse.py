from sys import argv
# from operator import itemgetter
# import csv
# from glob import glob

# script, fl_file1, fl_file2, fl_file3 = argv

# file_list = [fl_file1, fl_file2, fl_file3]
# file_list = []
# for file in glob(argv[1]):
#    file_list.append(file)

# with open('sample.dat', 'r') as fin:
#    data = [line.split() for line in fin]
#    print(data)
# for fl_file_x in file_list:
with open(argv[1], 'r') as fin:
    data = []
    line_count = 0
    for line in fin:
        if line_count < 29:
            line_count += 1
            continue
        data.append(line.split())
    data.pop()
#       data1 = [float(i) for i in data]
#       print(data1)
    for row in data:
        for k in (0, 1):
            row[k] = float(row[k])
#        print(data)
    print(str(argv[1]) + str(max(data, key=lambda x: x[1])))
    # lambda won't work if the list contains any values that are empty
