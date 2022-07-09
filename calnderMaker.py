import datetime 

DAYS = ['Monday' , 'Tuesday' , 'Wendsday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']
MONTHS = ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']

while True : 
    print('Enter year: ') 
    response = input('> ')

    if response.isdecimal() and int(response) > 0 : 
        year = int(response)
        break

    print('Please enter a valid year like 2070')

while True : 
    print('Enter month: ') 
    response = input('> ')

    if response.isdecimal() and int(response) > 0 and int(response) <= 12 : 
        month = int(response)
        break

    print('Please enter a valid month like 1')

def getCalanderFor(year , month) : 
    calText = ''
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    
    weekSeparator = ('+----------' * 7) + '+\n'    

    blankRow = ('|          ' * 7) + '|\n' 

    currentDate = datetime.date(year , month , 1 )

    while currentDate.weekday() != 6 :
        currentDate -=  datetime.timedelta(days= 1)

    while True : 
        calText += weekSeparator 

        dayNumberRow = '' 
        for i in range(7) : 
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        
        dayNumberRow += '|\n'

        calText += dayNumberRow 
        for i in range(3) : 
            calText += blankRow 

        if currentDate.month != month : 
            break       

    calText += weekSeparator 
    return calText 

calText = getCalanderFor(year , month)
print(calText) 

calanderfileName = 'calander_{}_{}.txt'.format(year , month)
with open(calanderfileName, 'w') as fileObj :
    fileObj.write(calText)

print('saved to ' + calanderfileName)    