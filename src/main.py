from _class import Triangle

def main():
    side_a = int(input("Lado 1: "))
    side_b = int(input("Lado 2: "))
    side_c = int(input("Lado 3: "))

    triangle = Triangle(side_a, side_b, side_c)
    print(triangle.triangle_type())

if __name__ == "__main__":
    main()

