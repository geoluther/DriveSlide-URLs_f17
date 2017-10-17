import csv
import sys


def gen_html(file):
	with open(file) as csvfile:
		reader = csv.reader(csvfile)
		for line in reader:
			return "<li><a href='{}'>{}</a></li>".format(line[1], line[0])


def main(files):
	for file in files:
		handle = file.split('.')[0]
		print '<h4>{}</h4>'.format(handle)
		print '<ul class="list-unstyled">'
		print gen_html(file)
		print '</ul>'


if __name__ == "__main__":
	files = [ name for name in sys.argv[1:] ]
	main(files)