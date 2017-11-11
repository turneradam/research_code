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
    print(str(argv[1]) + " " + str(max(data, key=lambda x: x[1])))
    # lambda won't work if the list contains any values that are empty
    spec_max = max(data, key=lambda x: x[1])

    half_max = spec_max[1] / 2
    # this gives us the y value of the spectrum half maxium
    print(half_max)

    x = 0
    fwhm_values = []

while len(fwhm_values) < 3:
    for row in data:
        half_max_p = half_max + x
        half_max_m = half_max - x
        if row[1] == half_max:
            # print(row)
            fwhm_values.append(row[0])
        elif row[1] < half_max_p and row[1] > half_max_m:
            # print(row)
            fwhm_values.append(row[0])
        elif x > 4:
            x += 0.1
    # print(fwhm_values)
    # if (len(fwhm_values) > 3):
    #    if max(fwhm_values) > 570 and min(fwhm_values) < 510:
    #        break
    #    else:
    #        continue
    print(len(fwhm_values))

print(fwhm_values)
# print(str(argv[1]) + " " + str(max(fwhm_values) - min(fwhm_values)))
