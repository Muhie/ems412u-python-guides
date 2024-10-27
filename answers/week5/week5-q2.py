# Muhie Al Haimus
# 24/09/2024
'''Explanation: 3D rotations: Ask the user to input an 
XYZ point and then ask which axis the user would
 like to rotate around. Then output the rotated point to the screen.'''
import numpy as np
import math

def get_rotation_axis():
    axis = input("Please enter the axis you would like to rotate around ie. x y z all lowercase please ")
    angle = float(input("Please enter the value of the angle in degrees in which you would like to rotate by "))
    angle = angle * math.pi/180
    return axis, angle

""" FOR THIS QUESTION WE ASSUME CORRECT INPUT DATA HOWEVER COULD YOU MODIFY THIS CODE TO MAKE SURE DATA IS VALID?"""
def get_single_point():
    axis_array = ["x", "y", "z"]
    matrix = np.zeros((3, 1))
    for i in range(0, 3):
        value = float(input("Please enter the {} value of the point you want to rotate ".format(axis_array[i])))
        matrix[i][0] = value
    return matrix



""" A function that calculates the final, rotated XYZ point"""
def do_rotations(angle, axis, matrix): 
    anti_clockwise_x_axis = np.matrix([[1, 0, 0],
                                    [0, math.cos(angle), -math.sin(angle)],
                                    [0, math.sin(angle), math.cos(angle)]])

    anti_clockwise_y_axis = np.matrix([[math.cos(angle), 0 , math.sin(angle)],
                                        [0, 1, 0],
                                        [-math.sin(angle), 0 , math.cos(angle)]])

    anti_clockwise_z_axis = np.matrix([[math.cos(angle), -math.sin(angle), 0],
                                        [math.sin(angle), math.cos(angle), 0],
                                        [0, 0, 1]])
    if axis == "x":
        rotated_point = anti_clockwise_x_axis * matrix
    if axis == "y":
        rotated_point = anti_clockwise_y_axis * matrix
    if axis == "z":
        rotated_point = anti_clockwise_z_axis * matrix

    return rotated_point


if __name__ == "__main__":
    axis_and_angle = get_rotation_axis()
    point = get_single_point()
    rotated_point = do_rotations(axis_and_angle[1], axis_and_angle[0], point)
    print(rotated_point)