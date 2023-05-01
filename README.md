# Renting-Research-Zillow-Bot

Gathers rent information from Zillow via BeautifulSoup and inputs rent information into a Google Form using Selenium. 
The example shown is of rental apartments in San Francisco, California.

Features:
- Uses BeautifulSoup to get renting information from Zillow and scrapes all listed property information
- Uses Selenium to place all property Zillow information to a Google Form and submit information
- Uses Google Forms to store information
- Easily transfer Google Form information to Google Sheets to easily apply Data Science

How to run:
- Download repository
- Go to [Zillow](https://www.zillow.com/) and select an area you are interested in getting data from. When found, 
copy the url and update `ZILLOW_LINK` in `main.py`
- Create a [Google Form](https://docs.google.com/forms) with 6 short response questions. In the order of `address`, 
`price per month`, `bedrooms`, `bathrooms`, `square footage`, `property link`. For more info see screenshots below.
- Copy the newly created Google Form url and update `GOOGLE_FORM` in `main.py`
- Open downloaded repository with a command line interface
- run `pip install selenium`
- run `python main.py`
- Script start and windows will open. If an error occurs, try running the program again as Zillow sometime responds 
with garbage

Program Output:

![alt text](https://github.com/J0K3Rn/Renting-Research-Zillow-Bot/blob/main/screenshots/output.png?raw=true)

Google Form Example:

![alt text](https://github.com/J0K3Rn/Renting-Research-Zillow-Bot/blob/main/screenshots/google_form_example.png?raw=true)

Converted to Google Sheets:

![alt text](https://github.com/J0K3Rn/Renting-Research-Zillow-Bot/blob/main/screenshots/google_sheets.png?raw=true)


