# -*- coding: utf-8 -*-
"""
COMS W1002
Homework 3, Problem 4
Gregory Cuesta
10/31/2016

Mad Lib for 'Big Poppa' by The Notorious B.I.G. (1994)
G-Rated version
"""

def main():
    print('\nWelcome to the Notorious B.I.G. Rap Lib!\n\n'
    'You will be prompted to enter various names and words to produce your very own version of his hit song, "Juicy".')
    
    play = input('Are you ready to be a Rap Star?? Enter yes or no: ')
    while (play=='yes'):
          play_rapLib()
          play=input('Do you want to keep playing to improve your rap skills? Enter yes or no: ')
    print('\nGood. Stay in school and finish 1002.')
    
def play_rapLib():
    rapSong = ('\nIt was all a dream, I used to read PROGRAMMING_LANGUAGE magazine\n'
    'CLASSMATE1 and CLASSMATE2 up in the limousine\n'
    'Hangin\' PLURAL_NOUN1 on my wall\n'
    'Every Saturday MUSIC_APP, SINGER, Marley Marl\n'
    'I let my MOBILE_DEVICE rock \'til my MOBILE_DEVICE popped\n'
    'VERB1 ADJECTIVE1 on CANDY, sippin\' on ANIMAL Stock\n'
    'Way back, when I had the COLOR1 and COLOR2 lumberjack\n'
    'With the hat to match\n'
    'Remember Rappin\' PROFESSOR1? Duh-ha, duh-ha\n'
    'You never thought that FIELD_OF_STUDY would take it this far\n'
    'Now I\'m in the limelight cause I HOBBY tight\n'
    'Time to get paid, ACTIVITY at the World Trade\n'
    'Born sinner, the opposite of a winner\n'
    'Remember when I used to eat PLURAL_NOUN2 for dinner\n'
    'Peace to PROFESSOR2, FRIEND1, Kid Capri\n'
    'FRIEND2, Lovebug Starski\n'
    'I\'m VERB2 up like you thought I would\n'
    'Call the crib, same SOCIAL_MEDIA, same hood\n'
    'It\'s all good\n'
    'And if you don\'t know, now you know, DESCRIPTIVE_NOUN')
    
    progLang = input('Favorite programming language: ')
    progLang = progLang.upper()
    rapSong = rapSong.replace('PROGRAMMING_LANGUAGE', progLang)

    classmate1 = input('Name of a classmate: ')
    classmate1 = classmate1.upper()
    rapSong = rapSong.replace('CLASSMATE1', classmate1)

    classmate2 = input('Name of another classmate: ')
    classmate2 = classmate2.upper()
    rapSong = rapSong.replace('CLASSMATE2', classmate2)
    
    pNoun1 = input('Plural noun: ')
    pNoun1 = pNoun1.upper()
    rapSong = rapSong.replace('PLURAL_NOUN1', pNoun1)
    
    musicApp = input('Favorite music app: ')
    musicApp = musicApp.upper()
    rapSong = rapSong.replace('MUSIC_APP', musicApp)
    
    singer = input('Favorite singer: ')
    singer = singer.upper()
    rapSong = rapSong.replace('SINGER', singer)
    
    mobileDevice = input('Your mobile phone type: ')
    mobileDevice = mobileDevice.upper()
    rapSong = rapSong.replace('MOBILE_DEVICE', mobileDevice)
    
    verb1 = input('Verb + ing: ')
    verb1 = verb1.upper()
    rapSong = rapSong.replace('VERB1', verb1)
    
    adjective1 = input('Adjective: ')
    adjective1 = adjective1.upper()
    rapSong = rapSong.replace('ADJECTIVE1', adjective1)
    
    candy = input('Favorite candy: ')
    candy = candy.upper()
    rapSong = rapSong.replace('CANDY', candy)
    
    animal = input('Favorite animal: ')
    animal = animal.upper()
    rapSong = rapSong.replace('ANIMAL', animal)
    
    color1 = input('Color: ')
    color1 = color1.upper()
    rapSong = rapSong.replace('COLOR1', color1)
    
    color2 = input('Another color: ')
    color2 = color2.upper()
    rapSong = rapSong.replace('COLOR2', color2)
    
    professor1 = input('Name of our professor: ')
    professor1 = professor1.upper()
    rapSong = rapSong.replace('PROFESSOR1', professor1)
    
    field = input('Your field of study: ')
    field = field.upper()
    rapSong = rapSong.replace('FIELD_OF_STUDY', field)
    
    hobby = input('Favorite hobby: ')
    hobby = hobby.upper()
    rapSong = rapSong.replace('HOBBY', hobby)
    
    activity = input('Name of an activity: ')
    activity = activity.upper()
    rapSong = rapSong.replace('ACTIVITY', activity)
    
    pNoun2 = input('Another plural noun: ')
    pNoun2 = pNoun2.upper()
    rapSong = rapSong.replace('PLURAL_NOUN2', pNoun2)
    
    professor2 = input('Name of another professor: ')
    professor2 = professor2.upper()
    rapSong = rapSong.replace('PROFESSOR2', professor2)
    
    friend1 = input('Name of a close friend: ')
    friend1 = friend1.upper()
    rapSong = rapSong.replace('FRIEND1', friend1)
    
    friend2 = input('Name of another close friend: ')
    friend2 = friend2.upper()
    rapSong = rapSong.replace('FRIEND2', friend2 )
    
    verb2 = input('Another verb + ing: ')
    verb2 = verb2.upper()
    rapSong = rapSong.replace('VERB2', verb2)
    
    socMedia = input('Favorite social media platform: ')
    socMedia = socMedia.upper()
    rapSong = rapSong.replace('SOCIAL_MEDIA', socMedia)
    
    dNoun = input('Finally, your last word! Enter a descriptive noun to see your rap: ')
    dNoun = dNoun.upper()
    rapSong = rapSong.replace('DESCRIPTIVE_NOUN', dNoun)
    
    print('\nYou\'ve got skills!!')
    print(rapSong)

#run the game
main()

        
        