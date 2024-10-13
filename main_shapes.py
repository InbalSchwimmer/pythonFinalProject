from circle import Circle
from rectangle import Rectangle
from right_triangle import RightTriangle
from square import Square


def main_menu():
    print("1. Add new shape\n2. List all shapes\n3. Sum all circumferences\n"
          "4. Sum all areas\n5. Find biggest circumferences\n6. Find biggest area\n7. Exit")


def select_shape_menu():
    print("1. Square\n2. Rectangle\n3. Circle\n4. Right triangle")


def get_valid_color():
    while True:
        valid_color = input("Please enter color:\n")
        if not valid_color.isdigit():
            return valid_color
        else:
            print("Invalid input. Color should be a string. Please try again.")


def print_list_of_all_shapes(shape_list):
    if shape_list:
        print("********************************************************\n")
        for shape in shapes_list:
            shape.display_shape_parameters()
        print("\n********************************************************\n")
    else:
        print("\nThe shape list is empty\n")


def sum_all_circumferences(shape_list):
    if not shape_list:
        print("Shapes list is empty")
    else:
        circumferences = 0.0
        for shape in shape_list:
            circumferences += shape.calc_circumference()
        return circumferences


def sum_all_areas(shape_list):
    if not shape_list:
        print("The shape list is empty")
    else:
        areas = 0.0
        for shape in shapes_list:
            areas += float(shape.calc_area())
        return areas


def biggest_circumferences(shape_list):
    if not shapes_list:
        print("The shape list is empty")
    else:
        max_circumference = 0
        max_shape = None
        for shape in shapes_list:
            if float(shape.calc_circumference()) > float(max_circumference):
                max_circumference = float(shape.calc_circumference())
                max_shape = shape
        if max_shape:
            max_shape.display_shape_parameters()
            print(f"The biggest circumference: {max_circumference}\n")


def biggest_area(shape_list):
    if not shapes_list:
        print("The shape list is empty")
    else:
        max_area = 0
        max_shape = None
        for shape in shapes_list:
            if shape.calc_area() > max_area:
                max_area = shape.calc_area()
                max_shape = shape
        if max_shape:
            max_shape.display_shape_parameters()
            print(f"The biggest area: {max_area}\n")


# list of all shapes
shapes_list = []
choice = 1

while choice >= 1:
    main_menu()
    choice = int(input("Please select one of the options:\n"))
    # Add new shape
    if choice == 1:
        shape_color = get_valid_color()
        select_shape_menu()
        try:
            shape_type = int(input("Please select type of shape:\n"))
            # Square
            if shape_type == 1:
                width = float(input("What is the square width?\n"))
                shapes_list.append(Square(shape_color, width))
            # Rectangle
            elif shape_type == 2:
                width = float(input("What is the rectangle width?\n"))
                height = float(input("What is the rectangle height?\n"))
                shapes_list.append(Rectangle(shape_color, width, height))
            # Circle
            elif shape_type == 3:
                radius = float(input("What is the circle radius ?\n"))
                shapes_list.append(Circle(shape_color, radius))
            # Right triangle
            elif shape_type == 4:
                width = float(input("What is the rectangle width?\n"))
                height = float(input("What is the rectangle height?\n"))
                shapes_list.append(RightTriangle(shape_color, width, height))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
    # Print list of shapes
    elif choice == 2:
        print_list_of_all_shapes(shapes_list)
    # Print the sum of all circumferences
    elif choice == 3:
        print(sum_all_circumferences(shapes_list))
    # Print the sum of all areas
    elif choice == 4:
        print(sum_all_areas(shapes_list))
    # Find and print the biggest circumference:
    elif int(choice) == 5:
        biggest_circumferences(shapes_list)
    # Find and print the biggest area:
    elif int(choice == 6):
        biggest_area(shapes_list)
    # Exit Program
    elif choice == 7:
        break
