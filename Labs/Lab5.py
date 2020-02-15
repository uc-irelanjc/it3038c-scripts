from datetime import date
print ("Please enter your birthday (YYYY-MM-DD):")
bd_y = int(input("Year:"))
bd_m = int(input("Month (1-12):"))
bd_d = int(input("Date:"))
bd = date(int(bd_y), int(bd_m),  int(bd_d))
now = date.today()
sec_old = (now-bd).total_seconds()
print ("Your are " + str(sec_old) + " seconds old")