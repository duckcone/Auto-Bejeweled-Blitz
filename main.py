from lib2to3.pgen2 import pgen
from operator import imod
from turtle import bgcolor, down, left
import pyautogui as pyg

DUR = 0.1
START_X = 465
START_Y = 395

x = START_X
y = START_Y

while(True):
    for row in range(8):
        for col in range(8):
            jewel_color = pyg.pixel(x, y) # the far left jewel in a row

            right_two_in_a_row = pyg.pixel(x+50, y)
            left_two_in_a_row = pyg.pixel(x-50, y)
            down_two_in_a_col = pyg.pixel(x, y+50)
            up_two_in_a_col = pyg.pixel(x, y-50)

            right_jump_two_in_a_row = pyg.pixel(x+100, y)
            left_jump_two_in_a_row = pyg.pixel(x-100, y)
            down_jump_two_in_a_col = pyg.pixel(x, y+100)
            up_jump_two_in_a_col = pyg.pixel(x, y-100)

            '''
              a
            AABa
              a
            '''
            if(jewel_color == right_two_in_a_row):
                right_third_in_the_row1 = pyg.pixel(x+100, y-50)
                right_third_in_the_row2 = pyg.pixel(x+150, y)
                right_third_in_the_row3 = pyg.pixel(x+100, y+50)
                if(jewel_color == right_third_in_the_row1):
                    pyg.moveTo(x+100, y-50)
                    pyg.click()
                    pyg.moveTo(x+100, y)
                    pyg.click()
                    # print("switch top jewel to button")
                if(jewel_color == right_third_in_the_row2):
                    pyg.moveTo(x+150, y)
                    pyg.click()
                    pyg.moveTo(x+100, y)
                    pyg.click()
                    # print("switch right jewel to left")
                if(jewel_color == right_third_in_the_row3):
                    pyg.moveTo(x+100, y+50)
                    pyg.click()
                    pyg.moveTo(x+100, y)
                    pyg.click()
                    # print("switch button jewel to top")

            '''
             a
            aBAA
             a
            '''
            if(jewel_color == left_two_in_a_row):
                left_third_in_the_row1 = pyg.pixel(x-100, y-50)
                left_third_in_the_row2 = pyg.pixel(x-150, y)
                left_third_in_the_row3 = pyg.pixel(x-100, y+50)
                if(jewel_color == left_third_in_the_row1):
                    pyg.moveTo(x-100, y-50)
                    pyg.click()
                    pyg.moveTo(x-100, y)
                    pyg.click()
                if(jewel_color == left_third_in_the_row2):
                    pyg.moveTo(x-150, y)
                    pyg.click()
                    pyg.moveTo(x-100, y)
                    pyg.click()
                if(jewel_color == left_third_in_the_row3):
                    pyg.moveTo(x-100, +50)
                    pyg.click()
                    pyg.moveTo(x-100, y)
                    pyg.click()


            '''
             A
             A
            aBa
             a
            '''
            if(jewel_color == down_two_in_a_col):
                down_third_in_the_col1 = pyg.pixel(x-50, y+100)
                down_third_in_the_col2 = pyg.pixel(x, y+150)
                dwon_third_in_the_col3 = pyg.pixel(x+50, y+100)
                if(jewel_color == down_third_in_the_col1):
                    pyg.moveTo(x-50, y+100)
                    pyg.click()
                    pyg.moveTo(x, y+100)
                    pyg.click()
                if(jewel_color == down_third_in_the_col2):
                    pyg.moveTo(x, y+150)
                    pyg.click()
                    pyg.moveTo(x, y+100)
                    pyg.click()
                if(jewel_color == dwon_third_in_the_col3):
                    pyg.moveTo(x+50, y+100)
                    pyg.click()
                    pyg.moveTo(x, y+100)
                    pyg.click()
            
            if(jewel_color == up_two_in_a_col):
                up_third_in_the_col1 = pyg.pixel(x-50, y-100)
                up_third_in_the_col2 = pyg.pixel(x, y-150)
                up_third_in_the_col3 = pyg.pixel(x+50, y-100)
                if(jewel_color == up_third_in_the_col1):
                    pyg.moveTo(x-50, y-100)
                    pyg.click()
                    pyg.moveTo(x, y-100)
                    pyg.click()
                if(jewel_color == up_third_in_the_col2):
                    pyg.moveTo(x, y-150)
                    pyg.click()
                    pyg.moveTo(x, y-100)
                    pyg.click()
                if(jewel_color == up_third_in_the_col3):
                    pyg.moveTo(x+50, y-100)
                    pyg.click()
                    pyg.moveTo(x, y-100)
                    pyg.click()

            '''
             a
            ABA
             a
            '''

            if(jewel_color == right_jump_two_in_a_row):
                right_hole_in_a_row1 = pyg.pixel(x+50, y-50)
                right_hole_in_a_row2 = pyg.pixel(x+50, y+50)
                if(jewel_color == right_hole_in_a_row1):
                    pyg.moveTo(x+50, y-50)
                    pyg.click()
                    pyg.moveTo(x+50, y)
                    pyg.click()
                if(jewel_color == right_hole_in_a_row2):
                    pyg.moveTo(x+50, y+50)
                    pyg.click()
                    pyg.moveTo(x+50, y)
                    pyg.click()
            
            if(jewel_color == left_jump_two_in_a_row):
                left_hole_in_a_row1 = pyg.pixel(x-50, y-50)
                left_hole_in_a_row2 = pyg.pixel(x-50, y+50)
                if(jewel_color == left_hole_in_a_row1):
                    pyg.moveTo(x-50, y-50)
                    pyg.click()
                    pyg.click(x-50, y)
                    pyg.click()
                if(jewel_color == left_hole_in_a_row2):
                    pyg.moveTo(x-50, y+50)
                    pyg.click()
                    pyg.moveTo(x-50, y)
                    pyg.click()

            '''
             A
            aBa
             A
            '''

            if(jewel_color == down_jump_two_in_a_col):
                down_hole_in_a_col1 = pyg.pixel(x-50, y+50)
                down_hole_in_a_col2 = pyg.pixel(x+50, y+50)
                if(jewel_color == down_hole_in_a_col1):
                    pyg.moveTo(x-50, y+50)
                    pyg.click()
                    pyg.moveTo(x, y+50)
                    pyg.click()
                if(jewel_color == down_hole_in_a_col2):
                    pyg.moveTo(x+50, y+50)
                    pyg.click()
                    pyg.moveTo(x, y+50)
                    pyg.click()
            if(jewel_color == up_jump_two_in_a_col):
                up_hole_in_a_col1 = pyg.pixel(x-50, y-50)
                up_hole_in_a_col2 = pyg.pixel(x+50, y-50)
                if(jewel_color == up_hole_in_a_col1):
                    pyg.moveTo(x-50, y-50)
                    pyg.click()
                    pyg.moveTo(x, y-50)
                    pyg.click()
                if(jewel_color == up_hole_in_a_col2):
                    pyg.moveTo(x+50, y-50)
                    pyg.click()
                    pyg.moveTo(x, y-50)
                    pyg.click()

            x += 50
            
        x = START_X
        y += 50

    x = START_X
    y = START_Y