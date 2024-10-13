from circle import Circle
from rectangle import Rectangle
from right_triangle import RightTriangle
from square import Square


def main_menu():
    print("1. Add new shape\n2. List all shapes\n3. Sum all circumferences\n"
          "4. Sum all areas\n5. Find biggest circumferences\n6. Find biggest area\n7. Exit")


def select_shape_menu():
    print("1. Square\n2. Rectangle\n3. Circle\n4. Right triangle")


def print_list_of_all_shapes(shape_list):
    if shape_list:
        print("********************************************************\n")
        for shape in shape_list:
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


def sum_all_areas(shap_list):
    if not shap_list:
        print("The shape list is empty")
    else:
        area = 0.0
        for shape in shap_list:
            area = shape.calc_area()
        return area


# list of all shapes
shapes_list = []
choice = 1

while choice >= 1:
    main_menu()
    choice = int(input("Please select one of the options:\n"))
    if choice == 1:
        shape_color = input("Shape color:\n")
        select_shape_menu()
        try:
            shape_type = int(input("Please select type of shape:\n"))
            if shape_type == 1:
                width = float(input("What is the square width?\n"))
                shapes_list.append(Square(shape_color, width))
            elif shape_type == 2:
                width = float(input("What is the rectangle width?\n"))
                height = float(input("What is the rectangle height?\n"))
                shapes_list.append(Rectangle(shape_color, width, height))
            elif shape_type == 3:
                radius = float(input("What is the circle radius ?\n"))
                shapes_list.append(Circle(shape_color, radius))
            elif shape_type == 4:
                width = float(input("What is the rectangle width?\n"))
                height = float(input("What is the rectangle height?\n"))
                shapes_list.append(RightTriangle(shape_color, width, height))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
    elif choice == 2:
        print_list_of_all_shapes(shapes_list)
    elif choice == 3:
        print(sum_all_circumferences(shapes_list))
    elif choice == 4:
        print(sum_all_areas(shapes_list))
    # Find the biggest circumference:
    elif int(choice) == 5:
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
    # Find the biggest area:
    elif int(choice == 6):
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
    # Exit Program
    elif choice == 7:
        break
