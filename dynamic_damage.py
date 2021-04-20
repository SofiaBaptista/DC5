"""
This file was made to process the damage reports as a function of time.
"""
import pandas as pd
from graphics import *
import math
import datetime
import time

damage = pd.read_csv(r'~/Desktop/DC5-Data/Damage Reports/mc1-reports-data.csv')

#These points correspond to where we want the circles on each district. points[0]=district 1 and so on.
points = [Point(149,234), Point(288,190), Point(488,163), Point(668,263,), Point(319,444), Point(294,318), Point(966,494), Point(889,756), Point(579,659), Point(747,645), Point(851,596), Point(847,473), Point(707,463), Point(481,306), Point(382,303), Point(389,396), Point(565,531), Point(583,420), Point(478,431)]

win1 = GraphWin("Damage", 995, 823)
win1.setCoords(0,823,995,0)
myImage = Image(Point(497.5,411.5), '~/Desktop/DC5-Data/Damage Reports/map.png')
myImage.draw(win1)

#how much time in hours each frame should vary by
vary_time = 12

#how long you want to see each frame
seconds_per_time = 5

'''
#This loop draws the scale
for i in range(1,255):
    r = Rectangle(Point(i+50,700), Point(i+51,715))
    r.setOutline(color_rgb(i, 255 - i, 0))
    r.draw(win1)
r1 = Rectangle(Point(51,700), Point(306,715))
r1.setOutline('black')
r1.draw(win1)
'''

start_date = datetime.datetime(2020, 4, 6, 0, 0)
end_date = datetime.datetime(2020, 4, 11, 0, 0)
delta = datetime.timedelta(hours=vary_time)

#give time to record
time.sleep(25)

#First, iterate through time
while start_date <= end_date:

    #draw the date
    txt = Text(Point(300,25), "Reports between "+str(start_date)+" and "+str(start_date+delta))
    txt.setSize(20)
    txt.draw(win1)

    #filter by time
    df_new = damage[(damage['time'] > str(start_date)) & (damage['time'] < str(start_date+delta))]

    for i in range(1,20):

        #filter data by district
        df = df_new[df_new['location'] == i]
        size = df.shape[0]

        #the radius of the circle is proportional to the square root of the size of the frame so that the area is directly proportional to the size (A=πr^2)
        #note for this visualization the factor of the radius needs to be edited depending on the time delta
        c = Circle(points[i-1], math.sqrt(size)/2)

        #a complex way to get average damage
        divide_by = 0
        dmg = 0
        places = ['sewer_and_water', 'power', 'roads_and_bridges', 'medical', 'buildings']
        for i in range(5):
            if str(df[places[i]].mean()) != 'nan':
                #print(str(df[places[i]].mean()))
                dmg += df[places[i]].mean()
                divide_by += 1

        #dmg = (df['sewer_and_water'].mean() + df['power'].mean() + df['roads_and_bridges'].mean() + df['medical'].mean() + df['buildings'].mean()) / 5
        if divide_by == 0:
            divide_by = 1
        dmg /= divide_by
        c.setFill(color_rgb(int(dmg / 10 * 255), 255 - int(dmg / 10 * 255), 0))
        c.setOutline('black')
        c.draw(win1)

    time.sleep(seconds_per_time)

    #a janky way to clear the window but not the map
    for item in win1.items[:]:
        try:
            x=item.getWidth()
        except:
            item.undraw()
    win1.update()

    start_date += delta





input("press ENTER to quit")