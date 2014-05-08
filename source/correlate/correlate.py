import json
import requests
import pickle

data = pickle.load(open("live.json"))

cols = [
    "date",
    "woke_up_at",
    "fell_asleep_at",
    "sleep_hrs",
    "work_hrs",
    "alone_hrs",
    "friend_hrs",
    "public_hrs",
    "relationship_hrs",
    "off",
    "sex",
    "interacted_with_art",
    "worked_out",
    "meditated",
    "left_the_house",
    "nature_time",
    "inbox_zero",
    "travelling_or_out_of_routine",
    "number_of_sleep_beers",
    "number_of_fun_beers",
    "presence",
    "happiness",
    "creativity",
    "morning_mood",
    "unbusy",
    "notes length",
]

headers = {'Content-type': 'application/json', }
resp = requests.post("http://correlationbot.com", headers=headers, data=json.dumps({
    "data": data
}))
print resp
print resp.content
correlations = resp.json()["correlations"]
for c in correlations:
    print c["column_1"]
    print c["column_2"]
    c["col1"] = cols[c["column_1"]-1]
    c["col2"] = cols[c["column_2"]-1]
correlations.sort(key=lambda x: x["pearson"], reverse=True)
print correlations
for c in correlations:
    print "%s<->%s   %s" % (
        c["col1"],
        c["col2"],
        c["pearson"],
    )
