import json
from requests import get

res = get("https://collegereadiness.collegeboard.org/api/v1/tcc/views/test_center_closings_service?display_id=closings&city=&state=INDIA&admin_date=2020-09-26&id=")
jsonified = json.loads(res.text)
for centre in jsonified:
	if centre["test_center_id"] == 63100 or centre["name"].find("BISHOP") != -1:
		print(json.dumps(centre, indent=4))
else:
	print("Good to Go, Your Test Centre was not found in this list!")
	print("However you should always check with your centre for the most up to date information")

