#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Find names
"""
import random

MALE = ["Abel", "Artemis", "August", "Eli", "Giovanni", "Ivan", "Jack", "Jefferson",
"Jonas", "Leo", "Logan", "Malachi", "Mario", "Micah", "Nahum", "Noah", "Orlence", "Oscar", "Samuel",
"Silas", "Victor", "Vlad", "Wester"]

FEMALE = ["Alice", "Ardent", "Ashlyn", "Caess", "Clare", "Elena", "Eveline", "Fiona",
"Grace", "Hannah", "Hazel", "Hester", "Isabel", "Krista", "Jezebel", "Leah", "Lucile", "Lydia",
"Seraphina", "Sonya", "Sophie", "Veronica", "Violet"]

SURNAME = ["Bell", "Bowen", "Canter", "Carson", "Cross", "Harwood", "Hollas",
"Hunter", "Kalra", "Keel", "Moreau", "Morgan", "Porter", "Pickett", "Quinn", "Sidhu", "Soto",
"Torrez", "Vakharia", "Walker", "Winter", "Wright"]

NOBLE = ["Ash", "Blackbird", "Firefly", "Mooncloud", "Nightsong", "Snow",
"Twilight", "Whitethorn"]

if __name__ == '__main__':
    male = raw_input('Male or Female? (m/F) ').lower() == 'm'
    noble = raw_input('Noble? (y/N) ').lower() == 'y'
    nb = int(raw_input('How many? [1] ') or 1)
    for i in xrange(1, nb + 1):
        if male:
            first_name = random.choice(MALE)
        else:
            first_name = random.choice(FEMALE)
        if noble:
            surname = random.choice(NOBLE)
        else:
            surname = random.choice(SURNAME)

        print("%s %s" % (first_name, surname))
