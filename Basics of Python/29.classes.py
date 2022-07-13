class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point_1 = Point()
point_1.draw()
point_1.x = 10
point_1.y = 20
print(point_1.x)
