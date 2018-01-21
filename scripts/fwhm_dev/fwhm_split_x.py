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

# cut the spectrum in half horizontally

first_half = [(x[1],half_max - x[1]) for x in data if spec_max[0] - x[0] > 0] 
second_half = [(x[1],half_max - x[1]) for x in data if spec_max[0] - x[0] < 0] 

s_first_half = king_of_the_hill(first_half)
s_second_half = king_of_the_hill(second_half)

first_half_close = search_shit(first_half, s_first_half)
second_half_close = search_shit(second_half, s_second_half)

first_half_match = search_shit(data,first_half_close[0])
second_half_match = search_shit(data,second_half_close[0])

fwhm = first_half_match[0] - second_half_match[0] 

# print("data match lower: " + str(match1))
# print("data match upper: " + str(match22))

if argv[2] == '0':
    print (str(argv[1]) + " Spec_max: {spec_max} FWHM: {fwhm}".format(spec_max = spec_max, fwhm = fwhm))
elif argv[2] == '1':
    print (str(argv[1]) + "\nSpec_max: {spec_max} \nHalf_max: {half_max} \nFWHM: {fwhm} \n lower_close: {lclose} \n lower_xy: {lxy} \n upper_close: {uclose} \n upper_xy: {uxy}".format(
        spec_max = spec_max, half_max = half_max, fwhm = fwhm, lclose = adam_lower, lxy = match1, uclose = adam_upper, uxy = match2))
elif argv[2] == '2':
    print (str(argv[1]) + " Spec_max: {spec_max} FWHM: {fwhm}".format(spec_max = spec_max, fwhm = fwhm))
elif argv[2] == '3':
    print (str(argv[1]) + "\nSpec_max: {spec_max} \nHalf_max: {half_max} \nfirst_close: {f_close} \nsecond_close: {s_close} \nfirst_half_match: {fmatch} \nsecond_half_match: {smatch} \nFWHM: {fwhm}".format(
        spec_max = spec_max, half_max = half_max, f_close = first_half_close, s_close = second_half_close, fmatch = first_half_match, smatch = second_half_match, fwhm = fwhm))
elif argv[2] == '4':    
    pass
    #print (str(argv[1]) + "\n Spec_max: {spec_max} \n Half_max: {half_max} \nFWHM: {fwhm} \nlower_close: {lclose} \n lower_uncertainty: {lu} \n upper_close: {uclose} \n upper_uncertainty: {uu}".format(
     #   spec_max = spec_max, half_max = half_max, fwhm = fwhm, lclose = adam_lower, lu = s_min, uclose = adam_upper, uu = s_max))
else:
    print("Please specify output verbose level (3-0), 3 is most verbose, 0 is minimally verbose.")