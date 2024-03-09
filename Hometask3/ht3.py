class MediaFile:
    def __init__(self, file_name, size, creation_date, owner, format, color_scheme):
        self.file_name = file_name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner
        self.format = format
        self.color_scheme = color_scheme

    def create(self):
        # create
        pass

    def delete(self):
        # delete
        pass

    def open(self):
        # open
        pass

    def close(self):
        # close
        pass

    def save(self):
        # save
        pass

    def crop(self):
        # crop
        pass

    def change_color_scheme(self):
        # change the color scheme
        pass


class Video(MediaFile):
    def __init__(self, file_name, size, creation_date, owner, format, color_scheme, duration):
        super().__init__(file_name, size, creation_date, owner, format, color_scheme)
        self.duration = duration

    def play(self):
        # play
        pass

    def pause(self):
        # pause
        pass

    def splitting(self):
        # splitting into frames
        pass


class Audio(MediaFile):
    def __init__(self, file_name, size, creation_date, owner, format, color_scheme, duration, volume, resolution):
        super().__init__(file_name, size, creation_date, owner, format, color_scheme)
        self.duration = duration
        self.volume = volume
        self.resolution = resolution

    def play(self):
        # play
        pass

    def pause(self):
        # pause
        pass

    def boost_bass(self):
        # boost the bass
        pass

    def rotate(self):
        # rotate
        pass


class Photo(MediaFile):
    def __init__(self, file_name, size, creation_date, owner, format, color_scheme, resolution):
        super().__init__(file_name, size, creation_date, owner, format, color_scheme)
        self.resolution = resolution

    def rotate(self):
        # rotate
        pass
