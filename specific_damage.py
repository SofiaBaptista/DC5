"""
This file was made to help visualize the damage reports specific to the types of damaged facilities.
"""
import pandas as pd
from graphics import *
import math

damage = pd.read_csv(r'~/Desktop/DC5-Data/Damage Reports/mc1-reports-data.csv')

#These points correspond to where we want the circles on each district. points[0]=district 1 and so on.
points = [Point(149,234), Point(288,190), Point(488,163), Point(668,263,), Point(319,444), Point(294,318), Point(966,494), Point(889,756), Point(579,659), Point(747,645), Point(851,596), Point(847,473), Point(707,463), Point(481,306), Point(382,303), Point(389,396), Point(565,531), Point(583,420), Point(478,431)]

#This visualization seperates out the damage reports by all the different categories and displays seperate circles for each.
win2 = GraphWin("Specific Damage", 995, 823)
win2.setCoords(0,823,995,0)
myImage = Image(Point(497.5,411.5), '~/Desktop/DC5-Data/Damage Reports/map.png')
myImage.draw(win2)

#we needed 5 different scales
for i in range(1,255): #for medical
    r = Rectangle(Point(i+50,550), Point(i+51,565))
    r.setOutline(color_rgb(255, 255 - i, 255))
    r.draw(win2)
for i in range(1,255): #for buildings
    r = Rectangle(Point(i+50,600), Point(i+51,615))
    r.setOutline(color_rgb(255 - i, 255, 255 - i))
    r.draw(win2)
for i in range(1,255): #for roads and bridges
    r = Rectangle(Point(i+50,650), Point(i+51,665))
    r.setOutline(color_rgb(255-i, 255-i, 255-i))
    r.draw(win2)
for i in range(1,255): #for power
    r = Rectangle(Point(i+50,700), Point(i+51,715))
    r.setOutline(color_rgb(255, 255, 255 - i))
    r.draw(win2)
for i in range(1,255): #for sewer and water
    r = Rectangle(Point(i+50,750), Point(i+51,765))
    r.setOutline(color_rgb(255 - i, 255 - i, 255))
    r.draw(win2)


#draw the outline rectangles
for i in range(550, 751, 50):
    r1 = Rectangle(Point(51,i), Point(306,i+15))
    r1.setOutline('black')
    r1.draw(win2)

#This loop creates the circles
for i in range(1,20):

    #filter data by district
    df = damage[damage['location'] == i]

    for location in ['sewer_and_water', 'power', 'roads_and_bridges', 'medical', 'buildings']:

        #filter out the empty values
        df_new = df[df[location] != None]

        #the variables we want to visualize
        size = df_new.shape[0]
        dmg = df_new[location].mean()

        #vary the points/colors by location

        if location == 'medical':
            center = Point(points[i-1].getX()-20, points[i-1].getY()-20)
            c = Circle(center, math.sqrt(size)/8)
            c.setFill(color_rgb(255, 255 - int(dmg / 10 * 255), 255))
            c.setOutline('black')
            c.draw(win2)
        if location == 'buildings':
            center = Point(points[i-1].getX()-20, points[i-1].getY()+20)
            c = Circle(center, math.sqrt(size)/8)
            c.setFill(color_rgb(255 - int(dmg / 10 * 255), 255, 255 - int(dmg / 10 * 255)))
            c.setOutline('black')
            c.draw(win2)
        if location == 'roads_and_bridges':
            center = Point(points[i-1].getX()+20, points[i-1].getY()-20)
            c = Circle(center, math.sqrt(size)/8)
            c.setFill(color_rgb(255 - int(dmg / 10 * 255), 255 - int(dmg / 10 * 255), 255 - int(dmg / 10 * 255)))
            c.setOutline('black')
            c.draw(win2)
        if location == 'power':
            center = Point(points[i-1].getX()+20, points[i-1].getY()+20)
            c = Circle(center, math.sqrt(size)/8)
            c.setFill(color_rgb(255, 255, 255 - int(dmg / 10 * 255)))
            c.setOutline('black')
            c.draw(win2)
        if location == 'sewer_and_water':
            center = Point(points[i-1].getX(), points[i-1].getY())
            c = Circle(center, math.sqrt(size)/8)
            c.setFill(color_rgb(255 - int(dmg / 10 * 255), 255 - int(dmg / 10 * 255), 255))
            c.setOutline('black')
            c.draw(win2)

input("press ENTER to move on to the next visualization")




#The next visualization is exactly the same as the last except with a standardized color scheme. 
#It is more difficult to distinguish locations but easier to compare them to one another.
win3 = GraphWin("Specific Damage", 995, 823)
win3.setCoords(0,823,995,0)
myImage = Image(Point(497.5,411.5), '~/Desktop/DC5-Data/Damage Reports/map.png')
myImage.draw(win3)

#single scale this time
for i in range(1,255): #for medical
    r = Rectangle(Point(i+50,700), Point(i+51,715))
    r.setOutline(color_rgb(i, 255-i, 0))
    r.draw(win3)
r1 = Rectangle(Point(51,700), Point(306,715))
r1.setOutline('black')
r1.draw(win3)


#This loop creates the circles
for i in range(1,20):

    #filter data by district
    df = damage[damage['location'] == i]

    for location in ['sewer_and_water', 'power', 'roads_and_bridges', 'medical', 'buildings']:

        #filter out the empty values
        df_new = df[df[location] != None]

        #the variables we want to visualize
        size = df_new.shape[0]
        dmg = df_new[location].mean()

        #vary the points/colors by location

        if location == 'medical':
            center = Point(points[i-1].getX()-20, points[i-1].getY()-20)
        if location == 'buildings':
            center = Point(points[i-1].getX()-20, points[i-1].getY()+20)
        if location == 'roads_and_bridges':
            center = Point(points[i-1].getX()+20, points[i-1].getY()-20)
        if location == 'power':
            center = Point(points[i-1].getX()+20, points[i-1].getY()+20)
        if location == 'sewer_and_water':
            center = Point(points[i-1].getX(), points[i-1].getY())

        c = Circle(center, math.sqrt(size)/8)
        c.setFill(color_rgb(int(dmg / 10 * 255), 255 - int(dmg / 10 * 255), 0))
        c.setOutline('black')
        c.draw(win3)

input("press ENTER to quit")