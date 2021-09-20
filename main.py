'''Import Stack ADT + Functions for conversions'''
from helper import *

infilename = input('Hello there! Please read README.txt before running this programme! \n' 'Please enter the INPUT file name: ')
outfilename = input('Please enter desired OUTPUT file name: ')
infile = open(infilename, 'r')
outfile = open(outfilename, 'w')
lines = infile.readlines()
count = 0

for line in lines:
    count += 1
    in_type = line[0]
    out_type = line[1]
    string0 = line[3:-1]

    '''Check that there are no invalid characters in a string + standardise brackets + remove spaces'''
    string = cleanString(string0)
    if string == -1:
        outfile.writelines(' IN' + str(count) + '    ' + string0 + '\n')
        outfile.writelines('OUT' + str(count) + '    ' + 'ERROR: Refer to ERROR message on console.' + '\n' + '\n')
        print('Input {}: Incorrect characters found. Refer to error message above. \n '.format(count))
        continue

    if in_type == '0' and out_type == '1':
        '''INFIX to PREFIX'''
        output = in_pre(string)

    elif in_type == '0' and out_type == '2':
        '''INFIX to POSTFIX'''
        output = in_post(string)

    elif in_type == '1' and out_type == '0':
        '''PREFIX to INFIX'''
        output = pre_in(string)

    elif in_type == '1' and out_type == '2':
        '''PREFIX to POSTFIX'''
        output = pre_post(string)

    elif in_type == '2' and out_type == '0':
        '''POSTFIX to INFIX'''
        output = post_in(string)

    elif in_type == '2' and out_type == '1':
        '''POSTFIX to PREFIX'''
        output = post_pre(string)

    else:
        raise SyntaxError('Incorrect labelling of strings for processing')

    outfile.writelines(' IN' + str(count) + '    ' + string + '\n')
    outfile.writelines('OUT' + str(count) + '    ' + output + '\n' + '\n')
    print('Input {}: Done! \n '.format(count))

infile.close()
outfile.close()
print("Done! Please check the output file, '{}', for outputs!".format(outfilename))
