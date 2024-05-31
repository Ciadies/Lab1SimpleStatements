'''
Created on Sep. 19, 2023
Asks for an episode in a composed structure and returns it as a full name
@author: Sebastian
'''
episode = input("Please enter an episode: ")

e_idx = episode.find("_E")
season = episode[1:e_idx]

title_idx = episode.find("_", e_idx+1)
number = episode[e_idx+2:title_idx]

title = episode[title_idx+1:-1] + episode[-1]

print(f"Season {season}, Episode {number}: {title} (The Simpsons)")