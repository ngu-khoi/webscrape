# list_states_statename_10

list_states_statename_10 provides the unique State IDs found in uszips.csv

## Installation

You must use Python 3.8 for the program to function and install the packages as described in imports.
	
In the directory of the program, you must create another folder 'data' and inside have the 'uszips.csv'

	These can be adjusted appropriately in the program:
		The if condition which finds the existence of the .csv through a particular directory.
		The f = open parameters which attempts to open the .csv through a particular directory.
		The output write location and name of .csv
		

## Usage

Run the program. In several seconds, a .csv file will be produced with only the unique IDs in uszips.csv


## Observations

1) There are 52 unique state IDs. It contains every one of the fifty US States + DC and Puerto Rico
2) Approximately 3000 entries have flawed county_fips or county_fips_all characteristics. FIPS codes are numbers which uniquely identify geographic areas. County-level FIPS codes have five digits of which the first two are the FIPS code of the state to which the county belongs. In the data file, there are county FIPS with only 4 digits. A regular expression in NotePadd+ find function can provide all the entries with 4 digit FIPS.


## Issues

1) Nothing of significance. 


##PS

I have also created programs to produce the unique states and cities, and states and counties. Contact me at khoinguyen12312000@gmail.com if you would like these.