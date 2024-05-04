#!/usr/bin/env python3
correct_answers = {
    'What is the android version?': '9',
    'What is the OS build version?': '6736742',
    'What is the Andoid HostSpot ESSID?': 'AndroidAP_1409',
    'What is the HostSpot password?': '5dd82a4b7509',
    'Who is the Victim?': 'LING LOY',
    'What is the suspicious phone number?': '+214 92 227 393',
    'Who is blackmailing him?': 'Kcah',
    "What's the full name of the hacker?": 'kcah GAMBINO',
    'How much to pay?': '350.000.000 DNT',
    'What is the malware hash?': '7628f8e5d5fad40ebf06232050c845d7ed1bc31b3045bd0a37b5a05db1dcf9d7',
    "Voice Mail config what's the VVM port number?": '1808',
    'How much the android system spent to cleaned up Restart Fixes?': '1695243811',
    'Where was the victim killed?': '36.809485,10.302189',
    'Who ordered the kill?':'El CAPO'
}

user_answers = {}

print("== 1NV3ST1G4T0R ==\nPlease enter the answers for the following questions:\n")

for question in correct_answers:
    user_answers[question] = input(f"{question}\n> ")


if user_answers == correct_answers:
    print("Good job! \nFlag: Securinets{w0w_You_4re_The_b3st_1nvestigat0r!!}")
else:
    print("Sorry, incorrect answers.")

