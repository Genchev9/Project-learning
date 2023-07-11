import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
test_2=my_favorite_songs_dict['Waste a Moment']+my_favorite_songs_dict['New Salvation']+my_favorite_songs_dict['Out of Touch']
test_2=round(test_2,2)
print(f'три песни звучат {test_2}')
test_1=my_favorite_songs[1][1]+my_favorite_songs[4][1]+my_favorite_songs[5][1]
test_1=round(test_1,2)
print(f'три песни звучат {test_1}')
random.shuffle(my_favorite_songs)
random_songs=random.choice(my_favorite_songs)
random_songs_1=random.choice(my_favorite_songs)
random_songs_2=random.choice(my_favorite_songs)
print(f'три песни звучат {random_songs[1]+random_songs_1[1]+random_songs_2[1]}')