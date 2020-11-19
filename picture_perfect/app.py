import matplotlib.patches as patches
import matplotlib.pyplot as plt
import streamlit as st

from picture_perfect.picture import Picture, summary


def plot_picture(picture):
    fig, ax = plt.subplots(1, 1)
    ax.set_xlim(0, picture.wall_width)
    ax.set_ylim(0, 200)  # TODO: fix this.
    rect = patches.Rectangle(
        picture.picture_bottom_left,
        picture.picture_width,
        picture.picture_height,
        linewidth=1,
        edgecolor="r",
        facecolor="none",
    )
    ax.add_patch(rect)
    return fig


def main():
    st.title("Picture Perfect")

    wall_width = st.sidebar.number_input("Width of Wall", min_value=0.0, step=0.25)
    line_of_sight = st.sidebar.number_input(
        "Vertical Midpoint", min_value=0.0, step=0.25
    )
    picture_width = st.sidebar.number_input(
        "Width of Picture", min_value=0.0, step=0.25
    )
    picture_height = st.sidebar.number_input(
        "Height of Picture", min_value=0.0, step=0.25
    )
    nail_top_offset = st.sidebar.number_input(
        "Nail Offset for top of Picture", min_value=0.0, step=0.25
    )

    picture = Picture(
        wall_width=wall_width,
        line_of_sight=line_of_sight,
        picture_width=picture_width,
        picture_height=picture_height,
        nail_top_offset=nail_top_offset,
    )

    picture.calc()
    st.text(summary(picture))

    st.pyplot(plot_picture(picture))


if __name__ == "__main__":
    main()
