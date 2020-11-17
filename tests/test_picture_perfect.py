from picture_perfect import __version__
from picture_perfect.app import Picture


def test_version():
    assert __version__ == "0.1.0"


def test_app():
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
