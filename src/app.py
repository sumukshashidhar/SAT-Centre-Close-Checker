import json
from requests import get

# CHANGE THESE CONSTANTS ACCORDING TO YOUR REQUIREMENTS
DATE = "2020-09-26"
STATE = "INDIA"
CENTRE_CODE = "63377"

display_all = input("type yes if you want all schools to be displayed at the end anyways, if you don't trust the technology").lower()

res = get(f"https://collegereadiness.collegeboard.org/api/v1/tcc/views/test_center_closings_service?display_id=closings&city=&state={STATE}&admin_date={DATE}&id=")
jsonified = json.loads(res.text)
for centre in jsonified:
	if centre["test_center_id"] == CENTRE_CODE or centre["name"].find("BISHOP") != -1:
		print(json.dumps(centre, indent=4))
		print("\n\n\nFound. Call the College Board IMMEDIATELY\n\n\n")
		print(f"The Centre Says:\n\n\n {centre['notes']}\n\n\n")
		break
else:
	print("Good to Go, Your Test Centre was not found in this list!")
	print("However you should always check with your centre for the most up to date information")

if display_all.contains("yes"):
	print(json.dumps(jsonified, indent=4))
