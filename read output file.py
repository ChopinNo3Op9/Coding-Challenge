'''
Read in txt and filter out values, then output.
'''
import pandas as pd

filename = 'read_output_file.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
df = pd.DataFrame([l.strip().split(' ') for l in lines])
df[9] = pd.to_numeric(df[9])

count = (df[9] > 5000).sum()
summ = df[df[9] > 5000][9].sum()

output = "bytes_" + filename
with open(output, 'w') as file:
    file.write("{}\n".format(count))
    file.write("{}\n".format(summ))

