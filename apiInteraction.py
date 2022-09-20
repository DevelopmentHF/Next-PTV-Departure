# Gets train information from Hampton to Flinders
# Henry Fielding 2022

import requests
from datetime import datetime
from signature import *

# Opens departure data
depart_data = requests.get(getURL('/v3/departures/route_type/0/stop/1086?direction_id=1&max_results=1')).json()
time_data = depart_data['departures'][0]['scheduled_departure_utc']

# Gets individual time elements from `time_data`
date = time_data[:10]
UTC_ToD = time_data[11:-1]
AEST_ToD = str((int(UTC_ToD[:2]) + 10)) + ':' + UTC_ToD[3:]
calc_AEST_ToD = datetime.strptime(AEST_ToD, "%H:%M:%S")

# Gets curent AEST time
now = datetime.now()
curr_time = now.strftime("%H:%M:%S")
calc_curr_time = datetime.strptime(curr_time, "%H:%M:%S")

# Calculates time until the next train arrives at station
time_interval = calc_AEST_ToD - calc_curr_time

# Prints information
print(time_data)
print(f'Time till departure = {time_interval}')