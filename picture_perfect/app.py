import matplotlib.patches as patches
import matplotlib.pyplot as plt
import streamlit as st

from picture_perfect.picture import Picture
from picture_perfect.picture import summary


def plot_picture(picture):
    fig, ax = plt.subplots(1, 1)
    plt.gca().set_aspect("equal", adjustable="box")
    ax.set_xlim(0, picture.wall_width)
    ax.set_ylim(0, 120)  # TODO: fix this.

    rect = patches.Rectangle(
        xy=picture.picture_bottom_left,
        width=picture.picture_width,
        height=picture.picture_height,
        linewidth=1,
        edgecolor="r",
        facecolor="none",
    )
    ax.add_patch(rect)

    for nail_position in picture.nail_position:
        ax.plot(nail_position[0], nail_position[1], "x")
        ax.text(nail_position[0] + 2, nail_position[1] + 2, nail_position, rotation=45)

    ax.axvline(picture.half_wall_width, linestyle=":")
    ax.axhline(picture.line_of_sight, linestyle=":")
    return fig


def main():
    st.title("Picture Perfect")

    wall_width = st.sidebar.number_input(
        label="Width of Wall", min_value=0.0, step=0.25, value=123.0
    )
    line_of_sight = st.sidebar.number_input(
        label="Vertical Midpoint", min_value=0.0, step=0.25, value=71.0
    )
    picture_width = st.sidebar.number_input(
        label="Width of Picture", min_value=0.0, step=0.25, value=35.25
    )
    picture_height = st.sidebar.number_input(
        label="Height of Picture", min_value=0.0, step=0.25, value=46.0
    )
    nail_top_offset = st.sidebar.number_input(
        label="Nail Offset for top of Picture", min_value=0.0, step=0.25, value=15.0
    )
    nails = int(st.sidebar.radio("Nails", [1, 2]))
    if nails == 1:
        nail_separation = None
    elif nails == 2:
        nail_separation = st.sidebar.number_input(
            label="Distance Between Nails", min_value=0.0, step=0.25, value=18.0
        )

    picture = Picture(
        wall_width=wall_width,
        line_of_sight=line_of_sight,
        picture_width=picture_width,
        picture_height=picture_height,
        nail_top_offset=nail_top_offset,
        nails=nails,
        nail_separation=nail_separation,
    )

    picture.calc()
    st.text(summary(picture))
    st.pyplot(plot_picture(picture))


if __name__ == "__main__":
    main()
