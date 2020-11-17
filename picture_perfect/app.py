import streamlit as st

from picture_perfect.picture import Picture, summary


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


if __name__ == "__main__":
    main()
