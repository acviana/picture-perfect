class Picture:

    def __init__(self,units="inches",**kwargs):
        self.wall_width = kwargs["wall_width"]
        self.line_of_sight = kwargs["line_of_sight"]
        self.picture_width = kwargs["picture_width"]
        self.picture_height = kwargs["picture_height"]
        # self.hanger_top_offset = kwargs["hanger_top_offset"]

    def calc(self):
        self.half_wall_width = self.wall_width / 2
        self.half_picture_width = self.picture_width / 2
        self.half_picture_height = self.picture_height / 2

        self.distance_to_frame_bottom = self.line_of_sight - self.half_picture_height
        self.distance_to_frame_midpoint = self.line_of_sight
        self.distance_to_frame_top = self.line_of_sight + self.half_picture_height

    def summary(self):
        print(f"1/2 Wall Width: {self.half_wall_width}")
        print(f"1/2 Picture Width: {self.half_picture_width}")
        print(f"1/2 Picture Height: {self.half_picture_height}")


        print(f"Distance to Frame Bottom: {self.distance_to_frame_bottom}")
        print(f"Distance to Frame Midpoint: {self.distance_to_frame_midpoint}")
        print(f"Distance to Frame Top: {self.distance_to_frame_top}")

        # print(f"Distance to Bottom of Frame: {self.line_of_sight - }")
        # print(f"")


def main():
    picture = Picture(
        wall_width=123,
        line_of_sight=65,
        picture_width=35.25,
        picture_height=46,
        # hanger_top_offset=15
    )
    picture.calc()
    picture.summary()


if __name__ == '__main__':
    main()
