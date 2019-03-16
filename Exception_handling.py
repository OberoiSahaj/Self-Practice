#Random Exception handling for accepted format of input audio files
A= 'xyz.mp3'
B= 'xyzz.mp0'

valid_formats= ['wav', 'flac', 'm4a', 'mp3']

A_format= A.split('.')[1]  #Splitting filename A to get its format
B_format= B.split('.')[1]

try:
    for format in valid_formats:
        if format == A_format:
            pass
        else:
            raise Exception('Input file format not accepted')
except:
    print("Error: Input file format not accepted") #Programmer/User will get this error when he inputs the file with unaccepted format

