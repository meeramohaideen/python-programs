days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
day=int(input("Enter the day no. sunday is 0 modnay is 1 and so on:"))
for i in range(0,7):
    days1=days[i]
    if(days[day]==days1):
        print("holi day")
        break
    else:
        print("working day")
        break
