#!/usr/bin/env python3
correct_answers = {
        "Source IP": "10.1.10.172",
        "Destination IP": "10.1.10.80",
        "Destination MAC": "C0:B6:F9:66:D3:CE",
        "Source MAC": "c8:d9:d2:85:e8:af",
        "Malware file": "win_upadte.exe"
}

user_answers = {}

print("Please enter the answers for the following questions:")

for question in correct_answers:
    user_answers[question] = input(f"What is the {question.replace('_', ' ')}?\n")

if user_answers == correct_answers:
    print("Good job! SecurinetsTekUP{y0U_n41l3d_N3tw0rk_b4s1cs}")
else:
    print("Sorry, incorrect answers.")

