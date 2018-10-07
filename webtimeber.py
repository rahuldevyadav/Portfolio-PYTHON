import time
import webbrowser as wb

#Nuber breaks to take
numberOfBreaks=int(input('Number of breaks -'))
#Breaks after how many hours
nubersOfHours=int(input('numbers of hour to work -'))
i=0
while i<numberOfBreaks:
    # print current time
    print('Current time', time.ctime())
    time.sleep(nubersOfHours*60*60)
    #open video in breaks
    wb.open('https://www.youtube.com/watch?v=kRz7McXotvo')
    i+=1

