from picture_perfect import __version__
from picture_perfect.picture import Picture


def test_version():
    assert __version__ == "0.1.0"


def test__distance():
    picture = Picture(
        wall_width=123,
        line_of_sight=71,
        picture_width=35.25,
        picture_height=46,
        nail_top_offset=15,
    )
    picture._rectilinear_distance((0, 0), (3, 3)) == (3, 3)


def test_single_nail():
    picture = Picture(
        wall_width=123,
        line_of_sight=71,
        picture_width=35.25,
        picture_height=46,
        nail_top_offset=15,
    )
    picture.calc()

    # Set by _calc_lengths
    assert picture.half_wall_width == 61.5
    assert picture.half_picture_width == 17.625
    assert picture.half_picture_height == 23.0

    # Set by _cacl_distances
    assert picture.distance_to_frame_bottom == 48.0
    assert picture.distance_to_frame_midpoint == 71
    assert picture.distance_to_frame_top == 94.0

    # TODO
    assert picture.nail_midline_offset == 8
    assert picture.nail_vertical_position == 79
    assert picture.nail_horizontal_position == 61.5

    # Set by _calc_positions
    assert picture.wall_bottom_midpoint == (61.5, 0)
    assert picture.picture_bottom_left == (43.875, 48.0)
    assert picture.picture_bottom_right == (79.125, 48.0)
    assert picture.picture_top_left == (43.875, 94.0)
    assert picture.picture_top_right == (79.125, 94.0)
    assert picture.picture_bottom_midpoint == (61.5, 48.0)


def test_double_nail():
    picture = Picture(
        wall_width=123,
        line_of_sight=71,
        picture_width=35.25,
        picture_height=46,
        nail_top_offset=15,
        nails=2,
        nail_separation=18,
    )
    picture.calc()

    assert picture.half_wall_width == 61.5
    assert picture.half_picture_width == 17.625
    assert picture.half_picture_height == 23.0
    assert picture.distance_to_frame_bottom == 48.0
    assert picture.distance_to_frame_midpoint == 71
    assert picture.distance_to_frame_top == 94.0
    assert picture.nail_midline_offset == 8
    assert picture.nail_vertical_position == 79
    assert picture.nail_horizontal_position == [52.5, 70.5]
