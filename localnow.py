# localnow().py v1.0.1 - Thursday, July 6, 2017
"""
	Returns a PyTZ object with the local time & timezone

	Ref: https://stackoverflow.com/questions/13218506/how-to-get-system-timezone-setting-and-pass-it-to-pytz-timezone#17365806
"""

def localnow():
	import time
	from datetime import datetime

	import pytz  # $ pip install pytz
	from tzlocal import get_localzone  # $ pip install tzlocal

	# get local timezone
	tz = get_localzone()

	# test it

	# print (tz)

	# run_utc, now = datetime.utcnow(), datetime.now()
	ts = time.time()
	run_utc, now = datetime.utcfromtimestamp(ts), datetime.fromtimestamp(ts)

	rundate = run_utc.replace(tzinfo=pytz.utc).astimezone(tz) # utc -> local
	assert rundate.replace(tzinfo=None) == now

	#print(rundate.replace(microsecond=0).isoformat())
	return(rundate)

print(localnow().replace(microsecond=0))
print("localnow():", localnow())
print("localnow().isoformat:", localnow().isoformat())
print("localnow().replace(microsecond=0):", localnow().replace(microsecond=0))
print("localnow().replace(microsecond=0).isoformat():", localnow().replace(microsecond=0).isoformat())
