class Manga():
    """Represents a manga with its title, author, genre, number of volumes, description, and optional cover image.

    Provides methods for accessing and modifying manga information.
    """
    
    def __init__(self, title, author, genre, volumes,description,image=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.volumes = volumes
        self.description = description
        self.image = image
        
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nVolumes: {self.volumes}\n"
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def volumes(self):
        return self._volumes

    @property
    def description(self):
        return self._description
    
    @property
    def image(self):
        return self._image
    
    @title.setter
    def title(self, title):
        self._title = title
        
    @author.setter
    def author(self, author):
        self._author = author
    
    @genre.setter
    def genre(self, genre):
        self._genre = genre
        
    @volumes.setter
    def volumes(self, volumes):
        self._volumes = volumes
        

    @description.setter
    def description(self, description):
        self._description = description
        
    @image.setter
    def image(self, image):
        self._image = image
        
    