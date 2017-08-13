#!python3
import ui
from os.path import exists 
import csv

_csv_filename = 'myoutput.csv'
_field_names = ('Year', 'Month', 'Day', 'High Price')

def calc_button_action(sender):
	'''
	Here your calc button will call 3 functions.
	1. do_calculations, so you calculate and put the values in your fields
	2. collect_data, will collect all the data from your view and return it as a dict
	3. write_to_csv, you pass your dict you collected the data into and it will be written
	to the csv file.  The file name is at the top of the file.  You could ask for the name
	of the file for example.
	'''
	
	# v is set to your view, so you can access the other objects on you view now and
	# pass your view to other functions!
	v = sender.superview
	
	do_calculations(v)
	data_dict = collect_data(v)
	write_to_csv(_csv_filename, data_dict)
	
def do_calculations(v):
	'''
	in here, just do your calculations and update
	your fields with the calculated data
	'''
	# so to access the date in the ui.DatePicker, lets say its name is cal
	the_date = v['cal'].date
	
	# you can access all your objects as above.
	
	v['txt9'].text = str(10 * 2) # whatever you calculate
	
	
def collect_data(v):
	'''
		in here you are only intrested in collecting your data from the view
		again, you have the view so you can access your fields.
		I have used a dict here to collect the information.
		I think if you are using py 3.6, your dict will keep its order as you add your items
	'''
	
	# I have only filled in a few fields here. But you would add everything from your view
	# you wanted written out to the csv.  Add the items in the order you want them written 
	# to the csv file.
	d = dict(
			Year = v['cal'].date.year,
			Month = v['cal'].date.month,
			Day = v['cal'].date.day,
			HighPrice = v['txt9'].text,
			)
	return d
	
def write_to_csv(filename, data_dict):
	'''
		This function is only concerned with writing your dict to the csv file.  
	'''
	fexists=exists(filename) # We set a var to see if the file exists
	
	fieldnames = list(data_dict.keys()) # get a list of the keys to use as the header
	with open(filename, 'a') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		# only write the header one time to the file
		if not fexists:
			writer.writeheader()
			
		writer.writerow(data_dict)
		
		
if __name__ == '__main__':
	my_screen_fn = 'someview.pyui'
	v = ui.load_view(my_screen_fn)
	v.present(style='sheet', animated=False)
