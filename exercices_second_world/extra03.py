from datetime import datetime

date_string = "29 November, 2022"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
