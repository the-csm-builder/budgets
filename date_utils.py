import time

def date_to_epoch_start_of_month(date_string):
  # Convert the date string to a time tuple
  time_tuple = time.strptime(date_string, "%m/%d/%Y %I:%M:%S %p")
 
  # Convert the time tuple to the epoch time
  epoch = int(time.mktime(time_tuple))
 
  # Convert the epoch time to a time tuple in the GMT timezone
  gmt_time_tuple = time.gmtime(epoch)
 
  # Modify the time tuple to set the day of the month to 1 (the first day of the month)
  gmt_time_tuple = gmt_time_tuple[:2] + (1,) + gmt_time_tuple[3:]
 
  # Convert the modified time tuple to the epoch time for the start of the month
  start_of_month_epoch = int(time.mktime(gmt_time_tuple))

  epoch_string = str(start_of_month_epoch)
 
  return epoch_string
  
  

