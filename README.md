# Python Poll and Bank Analyses

Enclosed are a couple Python scripts that will do some simple analysis.

First up is PyBank, which contains a 'main.py' file that will read 'budget_data.csv' from its 'Resources' folder. From there, it creates a list of all monthly profits and losses from the give time period and spits out the following outputs: the total months, the total profits, the average change in profits, and the greatest increase and decrease in profits (relative to the previous month). This is displayed in both your Python console of choice and in a 'results.txt' file in the 'analysis' folder.

Next up is PyPoll. Its 'main.py' file will automatically read 'election_data.csv' from its 'Resources' folder and compile election data from individual cells. It will count up the total votes, display the candidates, the candidates' total votes, the candidates' percentage of total votes, and the overall winner. Similarly to PyBank, all of this data is then printed out via your Python console and in the analysis folder under the name 'results.txt'. 

## Troubleshooting

Please note that the paths in the repositories should be kept intact, otherwise necessary files may fail to read or write. Also note that while other csv files may be switched out and analysed in the 'Resources' folder for each program, they must have both the same name and formatting as the file they are replacing in order to load properly. I recommend opening up the sample csv's as a guide to make sure the columns line up correctly. (Do note that the last columns in both files are the important ones. The script can still run with blank or arbitary placeholders in the other columns.)
