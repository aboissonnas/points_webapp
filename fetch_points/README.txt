INSTALLATION:


Before using this webapp, ensure that both Python 3.8 (or higher) and Django 4.0 (or higher) are installed.

 - See the Python Beginner's Guide for how to download and install Python. https://wiki.python.org/moin/BeginnersGuide/Download
 - See the Django download page for how to download and install Django. https://www.djangoproject.com/download/

Clone the repository to your local machine. No further installation is required.


USAGE:


In a command line, navigate to the directory containing `manage.py` and run `python manage.py runserver`. This will start up the webapp so that it can send and receive requests. To stop the webapp, press CTRL+C.

To view the webapp in your browser, enter `http://127.0.0.1:8000/points` into the navigation bar. "127.0.0.1" is an IP address that refers to your local machine, and the webapp is running on port 8000. If you want to change the port that the webapp uses, run `python manage.py runserver PORT_NUMBER` after replacing PORT_NUMBER with the port you wish to use.

The data storage for this webapp is persistent. If you want to delete old data:
 - Go to your command line and press CTRL+C to stop the webapp.
 - Run `python manage.py shell`. This will open up a Python shell. Enter the following lines:
 - - from points.models import PointsRecord
 - - for record in PointsRecord.objects.all():
 - -     record.delete()
 - You will have to press "enter" twice after `record.delete()`.
 - To exit the shell, enter the line `exit()` and press "enter".

For more information on the Django API and how to use it to interact with the database, see the Django documentation. https://docs.djangoproject.com/en/4.0/

The webapp itself has four pages: the index, add transactions, spend points, and view balance. The page you start out on is the index, and has links to the other three pages.

On the "add transactions" page, there are three labeled text boxes, a "submit" button, and a "back" hyperlink. The "back" link will return you to the index.
 - Please note that subsequent entries in the "payer" box must exactly match in order to be processed as the same payer. "DANNON" and "Dannon" and "dannon" will all be processed as different payers.
 - The "points" box will accept positive or negative integers, but no decimals or fractions.
 - Entries in the "timestamp" box must be in the format "YYYY-MM-DD HH:MM:SS". The box is prepopulated, but this value must be changed before you hit the "submit" button or it will not be accepted.

On the "spend points" page, there is one text box, a "submit" button, and a "back" hyperlink. The "back" link will return you to the index.
 - This text box will accept positive or negative integers, but negative integers will be converted to positive on the back end.
 - When you hit the "submit" button, the text box and "submit" button will disappear and be replaced with a report on how many points were spent by each payer.
 - In order to spend more points, hit the "back" button and then follow the link back to the "spend points" page, or click into the navigational bar on your browser and then hit "enter".

On the "view balance" page, there is a report on the current balances of each payer and a "back" hyperlink. The "back" link will return you to the index.