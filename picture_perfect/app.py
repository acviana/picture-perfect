class Picture:

    def __init__(self,units="inches",**kwargs):
        self.wall_width = kwargs["wall_width"]
        self.line_of_sight = kwargs["line_of_sight"]
        self.picture_width = kwargs["picture_width"]
        self.picture_height = kwargs["picture_height"]
        # self.hanger_offset = kwargs["hanger_offset"]

    def calc(self):
        print(f"1/2 Wall Width: {self.wall_width / 2}")
        print(f"1/2 Picture Width: {self.picture_width / 2}")
        print(f"1/2 Picture Height: {self.picture_height / 2}")
        # print()


def main():
    picture = Picture(
        wall_width=123,
        line_of_sight=65,
        picture_width=35.25,
        picture_height=46,
        # hanger_offset=15
    )
    picture.calc()

if __name__ == '__main__':
    main()
