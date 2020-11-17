class Picture:
    def __init__(self, units="inches", **kwargs):
        self.wall_width = kwargs["wall_width"]
        self.line_of_sight = kwargs["line_of_sight"]
        self.picture_width = kwargs["picture_width"]
        self.picture_height = kwargs["picture_height"]
        self.nail_top_offset = kwargs["nail_top_offset"]

    def calc(self):
        self.half_wall_width = self.wall_width / 2
        self.half_picture_width = self.picture_width / 2
        self.half_picture_height = self.picture_height / 2

        self.distance_to_frame_bottom = self.line_of_sight - self.half_picture_height
        self.distance_to_frame_midpoint = self.line_of_sight
        self.distance_to_frame_top = self.line_of_sight + self.half_picture_height

        self.nail_midline_offset = self.half_picture_height - self.nail_top_offset
        self.nail_final_height = self.line_of_sight + self.nail_midline_offset

    def summary(self):
        print(f"1/2 Wall Width: {self.half_wall_width}")
        print(f"1/2 Picture Width: {self.half_picture_width}")
        print(f"1/2 Picture Height: {self.half_picture_height}")

        print(f"Distance to Frame Bottom: {self.distance_to_frame_bottom}")
        print(f"Distance to Frame Midpoint: {self.distance_to_frame_midpoint}")
        print(f"Distance to Frame Top: {self.distance_to_frame_top}")

        print(f"Distance from Midline to Nail: {self.nail_midline_offset}")
        print(f"Final Nail Height: {self.nail_final_height}")


def main():
    picture = Picture(
        wall_width=123,
        line_of_sight=71,
        picture_width=35.25,
        picture_height=46,
        nail_top_offset=15,
    )
    picture.calc()
    picture.summary()


if __name__ == "__main__":
    main()
