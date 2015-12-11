month_days= [('January',[31]),('February',[28,29]),('March',[31]), ('April',[30]),('May',[31]),('June',[30]),('July',[31]),('August',[31]),
('September',[30]),('October',[31]),('November',[30]),('December',[31]) ]

day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#Question 1
def days_in_month(month):
   for i in range (len(month_days)):
        for x in range(len(month_days[i])):
            if month==month_days[i][x]:
                return month_days[i][1]

#Question 2
def day_of_week(d,m,y):
    if m==1 or m==2:
        m+=12
        y-=1
        day = (((13*m+3) / 5 + d + y + (y / 4) - (y / 100) + (y / 400)) %7)
        return day_names[day]

    else:
        day = (((13*m+3) / 5 + d + y + (y /  4) - (y / 100) + (y / 400)) %7)
        return day_names[day]

#Question 3
def unlucky(year):
    return [(day,month,year) for day in range(1,14) for month in range (1,13) if ((day==13) and (day_of_week(day,month,year)=='Friday'))]

#Question 4
def mostUnlucky():
    newList=[]
    for i in range(0,2011):
        if len(unlucky(i))>2:
           print unlucky(i)
            #newList+=[unlucky(i)]
    #return newList
