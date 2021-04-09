import pandas as pd
from graphics import *
import math

damage = pd.read_csv(r'~/Desktop/DC5-Data/Damage Reports/mc1-reports-data.csv')

win1 = GraphWin("Damage", 995, 823)
win1.setCoords(0,823,995,0)
myImage = Image(Point(497.5,411.5), '~/Desktop/DC5-Data/Damage Reports/map.png')
myImage.draw(win1)

points = [Point(149,234), Point(288,190), Point(488,163), Point(668,263,), Point(319,444), Point(294,318), Point(966,494), Point(889,756), Point(579,659), Point(747,645), Point(851,596), Point(847,473), Point(707,463), Point(481,306), Point(382,303), Point(389,396), Point(565,531), Point(583,420), Point(478,431)]

for i in range(1,20):

    df = damage[damage['location'] == i]
    size = df.shape[0]

    c = Circle(points[i-1], math.sqrt(size)/2)

    dmg = (df['sewer_and_water'].mean() + df['power'].mean() + df['roads_and_bridges'].mean() + df['medical'].mean() + df['buildings'].mean()) / 5
    print(dmg)
    c.setFill(color_rgb(255, 255 - int(dmg / 10 * 255), 255 - int(dmg / 10 * 255)))
    c.setOutline(color_rgb(255, 255 - int(dmg / 10 * 255), 255 - int(dmg / 10 * 255)))
    c.draw(win1)
    

for i in range(1,255):
    r = Rectangle(Point(i+50,700), Point(i+51,715))
    r.setOutline(color_rgb(255, 255 - i, 255 - i))
    r.draw(win1)

r1 = Rectangle(Point(51,700), Point(306,715))
r1.setOutline('black')
r1.draw(win1)
input("press ENTER to quit")


