import pygame
import sys
import random

# Initialize screen dimensions and pygame
screen_dimensions = [1300, 680]
pygame.init()

# Initialize array and another array to reset it later on
h = 0
number_of_elements = 500 - h
array = random.sample(range(number_of_elements), number_of_elements)
array2 = random.sample(range(number_of_elements), number_of_elements)

# Starting pygame screen
screen = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("Data Structures Sorting Assignment")

# Scale on sidebar
Scale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Buttons
number_of_buttons = 5
start_point = (100, 20)
spacing = 40
button_width = (screen_dimensions[0] - 2 * start_point[0] - spacing * (number_of_buttons - 1)) / number_of_buttons
button_height = 40

sidebar = 30

# A class for buttons to be displayed on screen
class Button():
    # location and size
    def __init__(self, button_width, button_height,button_x,button_y,text_string, text_size,color = 'black'):
        self.button_width = button_width
        self.button_height = button_height
        self.button_x = button_x
        self.button_y = button_y
        self.text_string = text_string
        self.text_size = text_size
        self.color = color

    def draw_button(self):
        pygame.draw.rect(screen, self.color, (self.button_x,self.button_y,self.button_width,self.button_height),4,100)
        font = pygame.font.Font('freesansbold.ttf', self.text_size)
        text = font.render(f'{self.text_string}', False, (250, 250, 250))
        screen.blit(text, (self.button_x + self.button_width/10, self.button_y+10))
        pygame.display.update()

    def is_pressed(self,mouse_location_x, mouse_location_y):
        if self.button_x < mouse_location_x < self.button_x + self.button_width and self.button_y < mouse_location_y < self.button_y + self.button_height:
            return True


insertion_button = Button(button_width, button_height, start_point[0] + 0, start_point[1],'Insertion Sort',20 )
selection_button = Button(button_width, button_height, start_point[0] + (spacing+button_width), start_point[1], 'Selection Sort',20)
bubble_button = Button(button_width, button_height, start_point[0] + (spacing+button_width)*2, start_point[1], 'Bubble Sort',20)
quick_button = Button(button_width, button_height, start_point[0] + (spacing+button_width)*3, start_point[1], 'Quick Sort', 20)


# This function finds the median of three numbers(middle) by calculating the difference between the numbers
# For example if the difference between the first and middle number is positive and the difference between the middle
# and the last number is positive then the first is larger than the middle and the latter is larger than the last number
def median_of_three(f, m, l):
    diff1 = f - m
    diff2 = m - l
    diff3 = f - l
    if diff1*diff2 > 0:
        return m
    if diff1*diff3 > 0:
        return l
    return f


# Partitioning is used in quick sort function
def partition(left, u):
    # Finding the median of three numbers
    middle_index = median_of_three(left, int((left + u) / 2), u)
    # Selecting the pivot and placing it at the end of the array to be partitioned
    piv = array[middle_index]
    array[middle_index] = array[u]
    array[u] = piv
    i = left - 1
    # iterating i and j over the array and applying the concept of partitioning
    for j in range(left, u):
        if array[j] <= array[u]:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        draw_array()
    temp = array[i+1]
    array[i+1] = array[u]
    array[u] = temp
    return i+1


# This function runs recursively and the condition is to stop when the part of array to be sorted doesn't contain numbs
def quick_sort(first, last):
    if first >= last:
        return
    pivot = partition(first, last)
    quick_sort(first, pivot-1)
    quick_sort(pivot+1, last)
    return array


# Additional sorting algorithm to show in visualizer
# This algorithm takes the largest number and places it at the end of the array
def selection_sort():
    counter = 1
    while counter < len(array)+1:
        largest = array[0]
        location = 0

        for i in array[:len(array) - counter + 1]:
            if i > largest:
                largest = i
                location = array.index(largest)
        if location == len(array)-counter:
            pass
        else:
            temp = largest
            array[location] = array[-counter]
            array[-counter] = temp
        draw_array()

        counter += 1
        if counter == len(array):
            return array


def bubble_sort():
    # Initializing counter1 and counter to compare 2 elements at a time

    for counter1 in range(len(array)):
        for counter in range(len(array) - counter1 -1):
            if array[counter] > array[counter+1]:
                temp = array[counter]
                array[counter] = array[counter+1]
                array[counter + 1] = temp
        draw_array()
    return array


def insertion_sort():
    i = 1
    while i < len(array):
        insert = array[i]
        j = i
        while j > 0 and array[j-1] > insert:
            array[j] = array[j-1]
            j -= 1
        array[j] = insert
        i += 1
        draw_array()
    return array


def check_events(): # Check if the pygame window was quit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            k = pygame.mouse.get_pos()
            if 75 < k[1] < 75 + sidebar:
                global array, h
                array = random.sample(range(int(k[0]*0.5)+1), int(k[0]*0.5)+1)
                draw_array()
                h = k[0]+1
                draw_sidebar()
            if insertion_button.is_pressed(k[0], k[1]):
                insertion_sort()
            elif selection_button.is_pressed(k[0], k[1]):
                selection_sort()
            elif bubble_button.is_pressed(k[0], k[1]):
                bubble_sort()
            elif quick_button.is_pressed(k[0],k[1]):
                quick_sort(0, len(array)-1)


# Draws the sidebar on screen to show the the number of elements in the array
def draw_sidebar():
    pygame.draw.rect(screen, (250, 250, 250), (0,75, screen_dimensions[0], sidebar))
    pygame.draw.rect(screen, "blue", (0, 75, h, sidebar))


# Draws the array
def draw_array():
    screen.fill("black")
    rect_width = int(screen_dimensions[0] / len(array))
    for a in array:
        height = ((screen_dimensions[1]/len(array))*a)*0.8
        pygame.draw.rect(screen, "blue", ((screen_dimensions[0]-rect_width*len(array))/2+rect_width*array.index(a), screen_dimensions[1] - height, rect_width, height))

    pygame.display.update()
    check_events()


draw_array()

# Infinite loop to run pygame
while True:

    draw_sidebar()
    insertion_button.draw_button()
    selection_button.draw_button()
    bubble_button.draw_button()
    quick_button.draw_button()
    check_events()
