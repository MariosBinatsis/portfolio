import os
import calendar
import csv
import copy 
import datetime

today = datetime.datetime.now()

cuyear = today.year 
cumonth = today.month
cuday = today.day
cuhour = today.hour
cumins = today.minute

months = ['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']

pathfile = 'events.csv'
isExist = os.path.exists(pathfile)

myevents = dict()
if isExist == False:
    file = open('events.csv','x')
    file.close()
    
    file = open('events.csv','w')
    file.write("Date,Hour,Duration,Title\n")
    file.close()
else:
    with open('events.csv','r',newline ='') as read_obj:
        csvreader = csv.reader(read_obj)
        n = 0
        for row in csvreader:
            myevents[n] = row
            n = n + 1


def today_events(today,myevents):
    datenow = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    
    for x in range(0,len(myevents)):
        splittime = myevents[x][1].split(':')
        if myevents[x][0] == datenow and today.hour < int(splittime[0]):
            time  = int(splittime[0]) - today.hour
            print('Ειδοποίηση: Σε '+ str(time) + ' ώρες έχει προγραμματιστεί το γεγονός  <<'+ myevents[x][3] +'>>\n')
        
            

    
    
def print_calendar(yearnum,monthnum,myevents):
    
    month = calendar.monthcalendar(yearnum,monthnum)
    monthrange = calendar.monthrange(yearnum,monthnum)
    editmonth = copy.deepcopy(month)
    
    if monthnum == 0:
     previousmonthrange = calendar.monthrange(yearnum,12)
    else:
     previousmonthrange = calendar.monthrange(yearnum,monthnum)

    for j in range(monthrange[0]):
        editmonth[0][j] = previousmonthrange[1] - monthrange[0]+1 + j
    
    p = 1
    for j in range(7):
        if editmonth[len(editmonth)-1][j] == 0:
            editmonth[len(editmonth)-1][j] = p
            p = p+1
    
        
        
    print('_________________________________________________\n')
    print(months[monthnum-1],yearnum)
    print('\n_________________________________________________\n')
    print('  ΔΕΥ |  ΤΡΙ |  ΤΕΤ |  ΠΕΜ |  ΠΑΡ |  ΣΑΒ |  ΚΥΡ\n')
    
    for i in range(len(month)):
        if i!= 0:
         print('\n')
        for j in range(len(month[i])):
            day = month[i][j]
            hasevent = checkforevents(yearnum,monthnum,day,myevents)
            
            if day <= 9 and day !=0 and hasevent == False:
             print( '[  ' ,str(editmonth[i][j]),']',' |', end="",sep="")
            elif day <= 9 and day !=0 and hasevent ==True:
                print( '[ *' ,str(editmonth[i][j]),']',' |', end="",sep="")
                
            if day > 9 and day !=0 and hasevent == False:
             print( '[ ' ,str(editmonth[i][j]),']',' |', end="",sep="")
            elif day > 9 and day !=0 and hasevent == True:
                print( '[*' ,str(editmonth[i][j]),']',' |', end="",sep="")
                
           
            if day == 0 and editmonth[i][j] > 9:
             print( '  ' ,str(editmonth[i][j]),' ',' |', end="",sep="")
            elif day == 0 and editmonth[i][j] <= 9:
             print( '   ' ,str(editmonth[i][j]),' ',' |', end="",sep="")
            
    print('\n_________________________________________________')
    print('Πατήστε Enter για προβολή του επόμενου μήνα,"q" για έξοδο ή κάποια από τις παρακάτω επιλογές: \n')
    print('"-" για πλοήγηση στον προηγούμενο μήνα\n')
    print('"+" για διαχείρηση γεγονότων του ημερολογίου\n')
    print('"*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα\n\n')


    

        
def checkforevents(year,month,day,myevents):
    n = 0
    for x in range(1,len(myevents)):
        splitrow = myevents[x][0].split('-')
        if splitrow[0] == str(year) and splitrow[1] == str(month) and splitrow[2] == str(day):
                n = n + 1
    if n>0 :
         return True
    else:
         return False
        
    

def menu2(cumonth,cuyear):
    print('Διαχείρηση γεγονότων ημερολογίου, επιλέξτε ενέργεια:\n')
    print('1 Καταγραφή νέου γεγονότος\n')
    print('2 Διαγραφή γεγονότος\n')
    print('3 Ενημέρωση γεγονότος\n')
    print('0 Επιστροφή στο κυρίως μενού\n')
    x = input("->")
    while int(x)<0 and int(x)>4:
        x = input("Εισάγετε μια τιμή από 0 έως 4 -> ")
    return int(x)


def insert_event(today,myevents):

    """YYYY-MM-DD"""
    
    year = int(input('\nΈτος γεγονότος: '))
    while year < today.year:
        year = int(input('\nΕισάγετε έτος μεγαλύτερο του '+str(today.year)+': '))
        
    month = int(input('\nΜήνας γεγονότος: '))
    while (month > 12 or month < 1):
        month = int(input('\nΕισάγετε μια τιμή μεταξύ 1-12 : '))
        
    day = int(input('\nΗμέρα γεγονότος: '))
    monthrange = calendar.monthrange(year,month)
    while (day < 1 or day > monthrange[1]):
        day = int(input('\nΕισάγετε ημερομηνία η οποία να ανήκει στον επιλεγμένο μήνα: ')) 
    date = str(year)+'-'+str(month)+'-'+ str(day)

    """HH:MM"""

    hour = int(input('\nΏρα γεγονότος: '))
    while hour < 0 or hour > 23:
        hour = int(input('\nΕισάγετε μια τιμή μεταξύ 0-23: ')) 
    minutes = int(input('\nΛεπτά γεγονότος: '))
    while minutes < 0 or minutes > 59:
        minutes = int(input('\nΕισάγετε μια τιμή μεταξύ 0-59: ')) 
    hhmm = str(hour) + ':' + str(minutes)

    """ΔΙΑΡΚΕΙΑ"""

    duration = int(input('\nΧρονική διάρκεια γεγονότος: '))
    while duration < 0:
        duration = int(input('\nΕισάγετε μια θετική τιμή: '))
    dur = str(duration)

    """ΤΙΤΛΟΣ"""

    title = str(input('\nΕισάγετε τίτλο γεγονότος: '))
    title = title.replace(","," ")

    eventenddate = time_converter(year,month,day,hour,minutes,duration)

    data = [date,hhmm,dur,title]
    myevents[len(myevents)] = data
    


def time_converter(year,month,day,hour,minutes,duration):
    minutes = minutes + duration % 60
    if minutes > 60:
        minutes = minutes - 60
        hour = hour + 1
    hour = hour + duration // 60
    if hour > 23 :
        hour = hour - 23
        day = day + 1
    x = calendar.monthrange(year,month)[1]
    if day > x:
        month = month + 1
        day = day - x
    if month > 12:
        year = year +1
        month = month -12
    eventenddate = str(year)+'-'+str(month)+'-'+str(day)+','+str(hour)+':'+str(minutes)
    return eventenddate
    

def read_events(myevents):
    year = int(input('Εισάγετε έτος: '))
    while year < today.year:
        year = int(input('\nΕισάγετε έτος μεγαλύτερο του '+str(today.year)+':'))
    month = int(input('\nEισάγετε μήνα: '))
    while (month > 12 or month < 1) or month < today.month:
        month = int(input('\nΕισάγετε μια τιμή μεταξύ 1-12 και μεγαλύτερη του '+str(today.month)+':'))
    eventdates = dict()
    n = 0
    for x in range(0,len(myevents)):
        row = myevents[x][0]
        splitrow = row.split('-')
        if splitrow[0] == str(year):
            if splitrow[1] == str(month):
                 eventdates[n] = myevents[x]
                 n = n+1
    return eventdates
            

def delete_event(eventdate,myevents):
    header = ['Date', 'Hour', 'Duration', 'Title']
    newevents = dict()
    newevents[0] = header
    n = 1
    for x in range(1,len(myevents)):
        if myevents [x][0] == eventdate[0] and myevents[x][1] == eventdate[1] and myevents[x][2] == eventdate[2] and myevents[x][3] == eventdate[3]:
            exists = True
        else:
            exists = False
        if exists == False:
            newevents[n] = myevents[x]
            n = n + 1
    return newevents

    
    

print_calendar(cuyear,cumonth,myevents)
today_events(today,myevents)
x = input("->")
while x != 'q':
    if x == '-':
        if cumonth == 1 :
            cuyear = cuyear -1
            cumonth = 12
        else:
            cumonth = cumonth - 1
        print_calendar(cuyear,cumonth,myevents)
        x = input("->")
    elif x =='':
        if cumonth == 12:
            cuyear = cuyear + 1
            cumonth = 1
        else:
            cumonth = cumonth + 1
        print_calendar(cuyear,cumonth,myevents)
        x = input("->")
    elif x == '+':
        menukey = menu2(cumonth,cuyear)
        if menukey == 0:
            print_calendar(cuyear,cumonth,myevents)
            x = input("->")
        elif menukey == 1:
            insert_event(today,myevents)
        elif menukey == 2:
            print('=== Αναζήτηση γεγονότων ===\n')
            eventdates = read_events(myevents)
            if len(eventdates) != 0:
                for n in range(len(eventdates)):
                    print('\n'+str(n)+'. ['+str(eventdates[n][3])+']'+'  -> Date: '+ str(eventdates[n][0])+', Time: '+str(eventdates[n][1])+', Duration: '+str(eventdates[n][2])+'\n')
                value = int(input('\nΕπιλέξτε γεγονός προς διαγραφή:'))
                while value < 0 or value > len(eventdates)-1:
                    value = int(input('\nΕπιλέξτε μια τιμη μεταξύ 0-' +str(len(eventdates)-1)+':'))

                myevents = delete_event(eventdates[value],myevents)                           
            else:
                print('\nΔεν βρέθηκε γεγονός τη συγκεκριμένη ημερονία\n')
                
            
        elif menukey == 3:
            print('=== Αναζήτηση γεγονότων ===\n')
            eventdates = read_events(myevents)
            if len(eventdates) != 0:
                for n in range(len(eventdates)):
                    print('\n'+str(n)+'. ['+str(eventdates[n][3])+']'+'  -> Date: '+ str(eventdates[n][0])+', Time: '+str(eventdates[n][1])+', Duration: '+str(eventdates[n][2])+'\n')
                value = int(input('\nΕπιλέξτε γεγονός προς ενημέρωση:'))
                while value < 0 or value > len(eventdates)-1:
                    value = int(input('\nΕπιλέξτε μια τιμη μεταξύ:' +str(len(eventdates))))
                newdate = input('Ημερομηνία γεγονότος '+'('+ eventdates[value][0]+ '): ')
                if newdate == '':
                    newdate = eventdates[value][0]
                newtime = input('Ώρα γεγονότος '+'('+ eventdates[value][1]+ '): ')
                if newtime == '':
                    newtime = eventdates[value][1]
                newduration = input('Διάρκεια γεγονότος ('+ eventdates[value][2] + '): ')
                if newduration == '':
                    newduration = eventdates[value][2]
                newtitle = input('Τίτλος γεγονότος ('+eventdates[value][3]+'): ')
                if newtitle == '':
                    newtitle = eventdates[value][3]
                myevents[value+1] = [newdate,newtime,newduration,newtitle]
            else:
                print('\nΔεν βρέθηκε γεγονός τη συγκεκριμένη ημερονία\n')
    elif x == '*':
        print('=== Αναζήτηση γεγονότων ===\n')
        eventdates = read_events(myevents)
        if len(eventdates) != 0:
            for n in range(len(eventdates)):
                print('\n'+str(n)+'. ['+str(eventdates[n][3])+']'+'  -> Date: '+str(eventdates[n][0])+', Time: '+str(eventdates[n][1])+', Duration: '+str(eventdates[n][2])+'\n')
        else:
            print('Δεν υπάρχουν γεγονότα στηνεπιλεγμένη ημερομηνία')
        value = input('\nΠατήστε οποιοδήποτε χαρακήρα για επιστροφή στο κυρίως μενού:')
        print_calendar(cuyear,cumonth,myevents)
        x = input('->')
    else:
        x = input("Εισάγετε μια από τις παραπάνω επιλογές->")
else:
    with open('events.csv','w',newline = '') as file:
        writer = csv.writer(file)
        for x in myevents:
            writer.writerow(myevents[x])
    




    



    

  
