from sys import argv
# from operator import itemgetter
# import csv
# from glob import glob

def king_of_the_hill(data_set):
    """
    Finds highest abs in list...there is a better way of doing this...
    """
    setter = abs(data_set[0][1])
            
    for entry in data_set:
        if abs(entry[1]) > setter:
            pass
        else:
            setter = abs(entry[1])

    return setter

def search_shit(data_set, val):
    """
    Searches zipped data for the second value
    """
    for shit in data_set:
        if shit[1] == val:
            return shit



with open(argv[1], 'r') as fin:
    data = []
    line_count = 0
    for line in fin:
        if line_count < 29:
            line_count += 1
            continue
        data.append(line.split())
    data.pop()
    for row in data:
        for k in (0, 1):
            row[k] = float(row[k])
    # print(str(argv[1]) + " " + str(max(data, key=lambda x: x[1])))
    # lambda won't work if the list contains any values that are empty
    spec_max = max(data, key=lambda x: x[1])

    half_max = spec_max[1] / 2
    # this gives us the y value of the spectrum half maxium

# print("HALF_MAX = %s" % half_max)



min_vals = [(x[1],half_max - x[1]) for x in data if half_max - x[1] < 0]        
max_vals = [(x[1],half_max - x[1]) for x in data if half_max - x[1] > 0] 

s_min = king_of_the_hill(min_vals) * -1
s_max = king_of_the_hill(max_vals)

adam_lower = search_shit(min_vals, s_min)
adam_upper = search_shit(max_vals, s_max)

match1 = search_shit(data,adam_lower[0])
match22 = search_shit(data,adam_upper[0])

# print("data match lower: " + str(match1))
# print("data match upper: " + str(match22))

if argv[2] == '1':
    print (str(argv[1]) + "\n Spec_max: {spec_max} \n Half_max: {half_max} \n lower_close: {lclose} \n lower_uncertainty: {lu} \n upper_close: {uclose} \n upper_uncertainty: {uu}".format(
        spec_max = spec_max, half_max = half_max, lclose = adam_lower, lu = s_min, uclose = adam_upper, uu = s_max))
elif argv[2] == '0':
    print (str(argv[1]) + " Spec_max: {spec_max} Half_max: {half_max}".format(spec_max = spec_max[0], half_max = half_max))
else:
    print("Please specify output verbose level, 1 is most verbose, 0 is minimally verbose.")