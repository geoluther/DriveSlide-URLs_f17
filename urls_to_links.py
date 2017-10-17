import csv
import sys


filename = sys.argv[1]

handle = filename.split('.')[0]
handle = handle.split(' ')[-1]

print '<div id="{}">'.format(handle)
print '<h4>{}</h4>'.format(handle)
print '<ul class="list-unstyled">'

with open(filename) as csvfile:
	reader = csv.reader(csvfile)

	for line in reader:
		url = "<li><a href='{}'>{}</a></li>".format(line[1], line[0])
		print url


print '</ul></div>'