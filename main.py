from lib2to3.pgen2 import pgen
from operator import imod
from tkinter.tix import Tree
from turtle import bgcolor, down, left
import pyautogui as pyg

DUR = 0.01
START_X = 465
# START_Y = 395
START_Y = 407

x = START_X
y = START_Y


def MouseClick(x, y):
    pyg.click(x, y, duration=DUR)

while(True):
    for row in range(8):
        for col in range(8):
            
            jewel_color = pyg.pixel(x, y)
            right_two_in_a_row = pyg.pixel(x+50, y)
            # left_two_in_a_row = pyg.pixel(x-50, y)
            down_two_in_a_col = pyg.pixel(x, y+50)
            # up_two_in_a_col = pyg.pixel(x, y-50)

            right_jump_two_in_a_row = pyg.pixel(x+100, y)
            # left_jump_two_in_a_row = pyg.pixel(x-100, y)
            down_jump_two_in_a_col = pyg.pixel(x, y+100)
            # up_jump_two_in_a_col = pyg.pixel(x, y-100)

            '''
              a
            AABa
              a
            '''
            if(jewel_color == right_two_in_a_row):
                print("right two in a row")
                right_third_in_the_row1 = pyg.pixel(x+100, y-50)
                right_third_in_the_row2 = pyg.pixel(x+150, y)
                right_third_in_the_row3 = pyg.pixel(x+100, y+50)

                left_third_in_the_row1 = pyg.pixel(x-50, y-50)
                left_third_in_the_row2 = pyg.pixel(x-100, y)
                left_third_in_the_row3 = pyg.pixel(x-50, y+50)

                if(jewel_color == right_third_in_the_row1):
                    MouseClick(x+100, y-50)
                    MouseClick(x+100, y)
                    print("right_third_in_the_row1")
                if(jewel_color == right_third_in_the_row2): 
                    MouseClick(x+150, y)
                    MouseClick(x+100, y)
                    print("right_third_in_the_row2")
                if(jewel_color == right_third_in_the_row3):
                    MouseClick(x+100, y+50)
                    MouseClick(x+100, y)
                    print("right_third_in_the_row3")

                if(jewel_color == left_third_in_the_row1):
                    MouseClick(x-50, y-50)
                    MouseClick(x-50, y)
                    print("left_third_in_the_row1")
                if(jewel_color == left_third_in_the_row2):
                    MouseClick(x-100, y)
                    MouseClick(x-50, y)
                    print("left_third_in_the_row2")

                if(jewel_color == left_third_in_the_row3):
                    MouseClick(x-50, +50)
                    MouseClick(x-50, y)
                    print("left_third_in_the_row3")
                

            '''
             A
             A
            aBa
             a
            '''
            if(jewel_color == down_two_in_a_col):
                print("down two in a col")
                down_third_in_the_col1 = pyg.pixel(x-50, y+100)
                down_third_in_the_col2 = pyg.pixel(x, y+150)
                down_third_in_the_col3 = pyg.pixel(x+50, y+100)

                up_third_in_the_col1 = pyg.pixel(x-50, y-50)
                up_third_in_the_col2 = pyg.pixel(x, y-100)
                up_third_in_the_col3 = pyg.pixel(x+50, y-50)

                if(jewel_color == down_third_in_the_col1):
                    MouseClick(x-50, y+100)
                    MouseClick(x, y+100)
                    print("down_third_in_the_col1")

                if(jewel_color == down_third_in_the_col2):
                    MouseClick(x, y+150)
                    MouseClick(x, y+100)
                    print("down_third_in_the_col2")

                if(jewel_color == down_third_in_the_col3):
                    MouseClick(x+50, y+100)
                    MouseClick(x, y+100)
                    print("dwon_third_in_the_col3")

                if(jewel_color == up_third_in_the_col1):
                    MouseClick(x-50, y-50)
                    MouseClick(x, y-50)
                    print("up_third_in_the_col1")

                if(jewel_color == up_third_in_the_col2):
                    MouseClick(x, y-100)
                    MouseClick(x, y-50)
                    print("up_third_in_the_col2")

                if(jewel_color == up_third_in_the_col3):
                    MouseClick(x+50, y-50)
                    MouseClick(x, y-50)
                    print("up_third_in_the_col3")

            '''
             a
            ABA
             a
            '''

            if(jewel_color == right_jump_two_in_a_row):
                print("right jump two in a row")
                right_hole_in_a_row1 = pyg.pixel(x+50, y-50)
                right_hole_in_a_row2 = pyg.pixel(x+50, y+50)

                if(jewel_color == right_hole_in_a_row1):
                    MouseClick(x+50, y-50)
                    MouseClick(x+50, y)
                    print("right_hole_in_a_row1")
                if(jewel_color == right_hole_in_a_row2):
                    MouseClick(x+50, y+50)
                    MouseClick(x+50, y)
                    print("right_hole_in_a_row2")


            '''
             A
            aBa
             A
            '''

            if(jewel_color == down_jump_two_in_a_col):
                print("down jump two in a col")
                down_hole_in_a_col1 = pyg.pixel(x-50, y+50)
                down_hole_in_a_col2 = pyg.pixel(x+50, y+50)
                if(jewel_color == down_hole_in_a_col1):
                    print("down_hole_in_a_col1")
                    pyg.click(x-50, y+50)
                    pyg.click(x, y+50)
                if(jewel_color == down_hole_in_a_col2):
                    print("down_hole_in_a_col2")
                    pyg.click(x+50, y+50)
                    pyg.click(x, y+50)
            
            # pyg.moveTo(x, y)
            x += 50
            print("x: ", x, "y: ", y)
            
        x = START_X
        y += 50

    x = START_X
    y = START_Y