class Circle:
  def __init__(self):
    self.pi = 3.14

  def area( self, radius):

    area = self.pi * (radius/2) ** 2
    print(area)
    return area

circle = Circle()
pizza_area = circle.area(12)
teaching_table_area = circle.area(36)
round_room_area = circle.area(11460)

