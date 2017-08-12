import csv
import ui

_csv_filename = 'myoutputV3.csv'
_field_names = ('Year', 'Month', 'Day', 'High Price')


def calc_button_action(sender):
    '''
    Here your calc button will call 3 functions.
    1. do_calculations, so you calculate and put the values in your fields
    2. collect_data, will collect all data from your view and returns a tuple
    3. write_to_csv, pass in the tuple you collected and it will be written to
    the csv file.  The file name is at the top of the file.  You could ask for
    the name of the file for example.
    '''

    # your view is the sender's superview, so you can access the other objects
    # on you view now and pass your view to other functions!
    view = sender.superview
    do_calculations(view)
    data = collect_data(view)
    write_to_csv(_csv_filename, data)


def do_calculations(view):
    '''
    in here, just do your calculations and update your fields with the
    calculated data
    '''
    # so to access the date in the ui.DatePicker, lets say its name is cal
    the_date = view['cal'].date  # noqa

    # you can access all your objects as above.
    view['txt9'].text = str(10 * 2)  # whatever you calculate


def collect_data(view):
    '''
    in here you are only intrested in collecting your data from the view
    again, you have the view so you can access your fields.
    Using a tuple now! not a dict
    '''

    # I have only filled in a few fields here. But you would add everything
    # from your view you wanted written out to the csv.  Add the items in the
    # order you want them written to the csv file.
    the_date = view['cal'].date
    return (the_date.year,
            the_date.month,
            the_date.day,
            view['txt9'].text)


def write_to_csv(filename, data_list):
    '''
    This function is only concerned with writing your list to the csv file.
    '''
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                               quoting=csv.QUOTE_MINIMAL)
        if csvfile.tell() == 0:  # if we are at the beginning of the file
            csvwriter.writerow(_field_names)  # then write out the header
        csvwriter.writerow(data_list)


if __name__ == '__main__':
    my_screen_fn = 'someview.pyui'
    ui.load_view(my_screen_fn).present(style='sheet', animated=False)
