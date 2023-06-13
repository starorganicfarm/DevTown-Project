#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Using HardCoded

def show_trailer(title, youtube_url):
    # Open Browser and play trailer
    print(f"Playing trailer for {title}")
    print(f"Trailer URL: {youtube_url}")
    # Add code to open the browser and play the trailer

show_trailer("Avengers: Endgame", "https://youtu.be/TcMBFSGVi1c")

def show_info(title, storyline, release_date, rating, youtube_url, director, box_office):
    # Print movie information
    print("Movie Information:")
    print(f"Title: {title}")
    print(f"Storyline: {storyline}")
    print(f"Release Date: {release_date}")
    print(f"Rating: {rating}")
    print(f"Trailer URL: {youtube_url}")
    print(f"Director: {director}")
    print(f"Box Office: {box_office}")

    
show_info("Avengers: Endgame", "The remaining Avengers join forces with allies to reverse the damage caused by Thanos and bring back the fallen heroes."
         , "April 26, 2019", "10/10", "https://youtu.be/TcMBFSGVi1c", "Anthony Russo, Joe Russo", "$2.798 billion USD")


# In[ ]:





# In[2]:


#Using WebBrowser

import webbrowser

def show_trailer(title, youtube_url):
    # Open Browser and play trailer
    webbrowser.open(youtube_url)
    show_info(title, "The remaining Avengers join forces with allies to reverse the damage caused by Thanos and bring back the fallen heroes."
         , "April 26, 2019", "10/10", youtube_url, "Anthony Russo, Joe Russo", "$2.798 billion USD")
    
def show_info(title, storyline, release_date, rating, youtube_url, director, box_office):
    # Print movie information
    print(f"Title: {title}")
    print(f"Storyline: {storyline}")
    print(f"Release Date: {release_date}")
    print(f"Rating: {rating}")
    print(f"Trailer URL: {youtube_url}")
    print(f"Director: {director}")
    print(f"Box Office: {box_office}")
    
show_trailer("Avengers: Endgame", "https://youtu.be/TcMBFSGVi1c")


# In[ ]:





# In[3]:


#Using Classes

class Movie:
    def __init__(self, title, storyline, release_date, rating, youtube_url, director, box_office):
        self.title = title
        self.youtube_url = youtube_url
        self.storyline = storyline
        self.release_date = release_date
        self.rating = rating
        self.youtube_url = youtube_url
        self.director = director
        self.box_office = box_office

    def show_trailer(self):
        # Open Browser and play trailer
        print(f"Playing trailer for {self.title}")
        print(f"Trailer URL: {self.youtube_url}")
        # Add code to open the browser and play the trailer

    def show_info(self):
        # Print movie information
        print("Movie Information:")
        print(f"Title: {self.title}")
        print(f"Storyline: {self.storyline}")
        print(f"Release Date: {self.release_date}")
        print(f"Rating: {self.rating}")
        print(f"Trailer URL: {self.youtube_url}")
        print(f"Director: {self.director}")
        print(f"Box Office: {self.box_office}")


# Creating instances of Movie class
avengers = Movie("Avengers: Endgame", "The remaining Avengers join forces with allies to reverse the damage caused by Thanos and bring back the fallen heroes.",
         "April 26, 2019", "10/10", "https://youtu.be/TcMBFSGVi1c", "Anthony Russo, Joe Russo", "$2.798 billion USD")
inception = Movie("Inception", "A thief enters people's dreams to steal information", "September 11, 2010", "9/10", 
                  "https://youtu.be/YoHD9XEInc0", "Christopher Nolan", "836.8 million USD")

# Example usage:
avengers.show_trailer()
avengers.show_info()
print('\n')
inception.show_trailer()
inception.show_info()


# In[ ]:




