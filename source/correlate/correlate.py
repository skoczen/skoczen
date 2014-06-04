import json
import requests
import pickle

data = pickle.load(open("live.json"))

cols = [
    "month",
    "woke_up_at",
    "fell_asleep_at",
    "sleep_hrs",
    "work_hrs",
    "alone_hrs",
    "friend_hrs",
    "public_hrs",
    "relationship_hrs",
    "orgasm",
    "sex_count",
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
    "winter",
    "spring",
    "summer",
    "fall",
    "moon_phase",
    "in_a_relationship",
]

headers = {'Content-type': 'application/json', }
resp = requests.post("http://correlationbot.com", headers=headers, data=json.dumps({
    "data": data
}))
# print resp
# print resp.content
correlations = resp.json()["correlations"]
for c in correlations:
    c["col1"] = cols[c["column_1"]-1]
    c["col2"] = cols[c["column_2"]-1]
    if str(c["pearson"]) == "nan":
        c["pearson"] = 0
        c["correlation"] = 0

correlations.sort(key=lambda x: x["pearson"], reverse=True)
for c in correlations:
    print "%s<->%s   %s" % (
        c["col1"],
        c["col2"],
        c["pearson"],
    )