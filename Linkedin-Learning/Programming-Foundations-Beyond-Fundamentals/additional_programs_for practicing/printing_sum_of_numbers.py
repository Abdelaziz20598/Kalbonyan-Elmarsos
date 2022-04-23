infile = open('values.txt', 'rt')
outfile = open('values_totaled.txt', 'wt')
print('processing input')
sum = 0
for line in infile:
    sum += int(line)
    print(line.rstrip(), file=outfile)
print('\nTotal: ' + str(sum), file=outfile)
outfile.close()
print('Output completed')

values_total = open('values_totaled.txt', 'rt')
for line in values_total:
    print(str(line).rstrip())
values_total.close()
