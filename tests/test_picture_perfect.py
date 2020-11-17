from picture_perfect import __version__
from picture_perfect.picture import Picture


def test_version():
    assert __version__ == "0.1.0"


def test_single_nail():
    picture = Picture(
        wall_width=123,
        line_of_sight=71,
        picture_width=35.25,
        picture_height=46,
        nail_top_offset=15,
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
    assert picture.nail_horizontal_position == 61.5


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
