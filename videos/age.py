

year =input("type in your birthday here (dd/mm/yy): ")
this_date = input("insert current date here: ")

day = int(year[0:2])
month = int(year[3:5])
just_year = int(year[6:])

nday = int(this_date[0:2])
nmonth = int(this_date[3:5])
njust_year = int(this_date[6:])

years_old = njust_year - just_year - 1


if day <= nday:
    if month <= nmonth:
        years_old = years_old + 1
        


print (years_old)

