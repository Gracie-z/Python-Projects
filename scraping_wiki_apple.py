import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Apple_Inc."
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

app_table = soup.find("table", attrs={"class": "wikitable float-left"})
app_table_data = app_table.tbody.find_all("tr")

# store all the headings, i.e., Year, Revenue in mil.USD etc. in a list
headings = []
for heading in app_table_data[0].find_all("th"):
    headings.append(heading.text.replace("\n", "").strip())
print(headings)
app_table_data.pop(0)

# Get the content of the table by iterating over the columns and then the rows
table_data = []
for tr in app_table_data:
    year = []
    for td in tr.find_all("td"):
        year.append(td.text.replace("\n", ' ').strip())
    year[0] = year[0][:4]
    data = {}
    for td, th in zip(year, headings):
        data[th] = td
    table_data.append(data)
print(table_data)

# store the data in an csv file
with open("apple.csv", "w") as out_f:
    writer = csv.DictWriter(out_f, headings)
    # create an object that maps dictionaries onto output rows,
    # headings identify the order in which values in the dictionary
    # passed to the writerow() method are written to file out_f

    writer.writeheader()  # write a row with the field names to the writer's file object
    for row in table_data:
        if row:
            writer.writerow(row)  # write the row parameter to the writer's file object
