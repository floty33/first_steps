import json
import csv
import re


def filter_users(logs):
    for user in logs:
        if re.match(r'^\+?1', user.get("phoneNumber", "")):
            if '4.0 Safari' in user.get("userAgent", ""):
                yield (user["name"], user["address"], user["email"])


with open('in.json', 'r') as file:
    logs = json.load(file)


with open('filtered_users.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["name", "address", "email"])
    csvwriter.writerows(filter_users(logs))
