

# def check_triangle(sides):
#     a, b, c = sorted(sides) 
#     return a > 0 and a+b >= c



# def equilateral(sides):
#     if not check_triangle(sides):
#         return False
#     else:
#         return sides[0] == sides[1] == sides[2]


# def isosceles(sides):
#     pass


# def scalene(sides):
#     pass

def check_triangle(sides):
    a, b, c = sorted(sides)  # Sorting makes inequality checks simpler
    return a > 0 and a + b >= c  # Ensures all sides are positive and valid
def equilateral(sides):
    if not check_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]
def isosceles(sides):
    if not check_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
def scalene(sides):
    if not check_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]