class Picture:
    def __init__(self, units="inches", nails=1, **kwargs):
        self.wall_width = kwargs["wall_width"]
        self.line_of_sight = kwargs["line_of_sight"]
        self.picture_width = kwargs["picture_width"]
        self.picture_height = kwargs["picture_height"]
        self.nail_top_offset = kwargs["nail_top_offset"]
        self.nails = nails
        if self.nails == 2:
            self.nail_separation = kwargs["nail_separation"]
        if units == "inches":
            self.unit_abbreviation = '"'

    def calc(self):
        self._calc_lengths()
        self._calc_distances()
        self._calc_positions()

    def _calc_distances(self):
        self.distance_to_frame_bottom = self.line_of_sight - self.half_picture_height
        self.distance_to_frame_midpoint = self.line_of_sight
        self.distance_to_frame_top = self.line_of_sight + self.half_picture_height

    def _calc_lengths(self):
        self.half_wall_width = self.wall_width / 2
        self.half_picture_width = self.picture_width / 2
        self.half_picture_height = self.picture_height / 2
        if self.nails == 2:
            self.half_nail_separation = self.nail_separation / 2

    def _calc_positions(self):
        self.wall_bottom_midpoint = (self.half_wall_width, 0)
        self.picture_bottom_left = (
            self.half_wall_width - self.half_picture_width,
            self.line_of_sight - self.half_picture_height,
        )
        self.picture_bottom_right = (
            self.half_wall_width + self.half_picture_width,
            self.line_of_sight - self.half_picture_height,
        )
        self.picture_top_left = (
            self.half_wall_width - self.half_picture_width,
            self.line_of_sight + self.half_picture_height,
        )
        self.picture_top_right = (
            self.half_wall_width + self.half_picture_width,
            self.line_of_sight + self.half_picture_height,
        )
        self.picture_bottom_midpoint = (
            self.half_wall_width,
            self.line_of_sight - self.half_picture_height,
        )

        self.nail_midline_offset = self.half_picture_height - self.nail_top_offset
        self.nail_vertical_position = self.line_of_sight + self.nail_midline_offset
        if self.nails == 1:
            self.nail_position = [
                (
                    self.half_wall_width,
                    self.line_of_sight
                    + (self.half_picture_height - self.nail_top_offset),
                )
            ]
        elif self.nails == 2:
            self.nail_position = [
                (
                    self.half_wall_width - self.half_nail_separation,
                    self.line_of_sight
                    + (self.half_picture_height - self.nail_top_offset),
                ),
                (
                    self.half_wall_width + self.half_nail_separation,
                    self.line_of_sight
                    + (self.half_picture_height - self.nail_top_offset),
                ),
            ]

    def _rectilinear_distance(self, coord_1, coord_2):
        return (abs(coord_1[0] - coord_2[0]), abs(coord_1[1] - coord_1[1]))


def summary(picture):
    output = ""
    output += f"1/2 Wall Width: {picture.half_wall_width}{picture.unit_abbreviation}\n"
    output += (
        f"1/2 Picture Width: {picture.half_picture_width}{picture.unit_abbreviation}\n"
    )
    output += f"1/2 Picture Height: {picture.half_picture_height}{picture.unit_abbreviation}\n"

    output += f"Distance to Frame Bottom: {picture.distance_to_frame_bottom}{picture.unit_abbreviation}\n"
    output += f"Distance to Frame Midpoint: {picture.distance_to_frame_midpoint}{picture.unit_abbreviation}\n"
    output += f"Distance to Frame Top: {picture.distance_to_frame_top}{picture.unit_abbreviation}\n"

    output += f"Distance from Midline to Nail: {picture.nail_midline_offset}{picture.unit_abbreviation}\n"
    output += f"Final Nail Height: {picture.nail_vertical_position}{picture.unit_abbreviation}\n"
    return output


def main():
    picture = Picture(
        wall_width=123,
        line_of_sight=71,
        picture_width=35.25,
        picture_height=46,
        nail_top_offset=15,
    )
    picture.calc()
    print(summary(picture))


if __name__ == "__main__":
    main()
