# filter-string-csv
Script for copy rows that contains specific string or keywords in a CSV file to other CSV file.

This script is useful when:
- The CSV file has large quantity of rows.
- Excel could hang due to special sequence of strings of characters.
- Content of the CSV file could led to initiate malicious connections.
- You have not have bash (for example in a machine with Windows without a subsystem) or just prefer to use this instead of bash.

### Guidelines

1. Add the strings you would like to find into your CSV files, in the variables kwd_1, kwd_2,.. and, include this variables in the if statement.

1. Run the script, for example:

`mike@DS42T:~$python filter-string-csv.py`

2. You'll be asked to enter the file name of the CSV file that could contains the strings or keywords.

File to read: `yourcsvfile.csv`

3. Now you'll be asked for the file where you want to have the results.

File to log ocurrences: `thenewcsvfile.csv`


### Notes

1. In Windows I don't see the rows highlighted.
2. If you would like to improve or correct this script, you're more than welcome. I am learning.

Hope this script could be useful for you.
