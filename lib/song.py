class Song:
    
    # define class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    # initialize the attributes
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # add the new instance to the count
        Song.add_song_to_count()
        
        # add the genre of the newly created song to the list of genres
        Song.add_to_genres(self.genre)
        
        # add the artist of the newly created song to the list of artists
        Song.add_to_artists(self.artist)
        
        # add count of the genre to the counts
        Song.add_to_genre_count(self.genre)
        
        # add the count of the artist of the current song to the counts
        Song.add_to_artist_count(self.artist)
        
    # define class methods
    ### count songs created ###
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
        
    ### add unique genres to the list ###
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            
    ### add unique artists to the list ###
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            
    ### count the number of songs per genre ###
    @classmethod
    def add_to_genre_count(cls, genre):
        # if key already exists, increase the count by 1, else set it to 1
        if genre in list(cls.genre_count.keys()):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
            
    ### count the number of songs produced by each artist ###
    @classmethod
    def add_to_artist_count(cls, artist):
        # if the key already exists, increase 
        if artist in list(cls.artist_count.keys()):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1