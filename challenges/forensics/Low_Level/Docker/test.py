def main():
    # Define the correct answers
    correct_answers = {
        "source_ip": "10.1.10.172",
        "destination_ip": "10.1.10.80",
        "destination_mac": "C0:B6:F9:66:D3:CE",
        "source_mac": "c8:d9:d2:85:e8:af",
        "malware_file": "win_upadte.exe"
    }

    # Prompt the user to enter answers
    user_answers = {}
    print("Please enter the answers for the following questions:")
    for question in correct_answers:
        user_answers[question] = input(f"What is the {question.replace('_', ' ')}? ")

    # Check if user answers match the correct answers
    if user_answers == correct_answers:
        print("SecurinetsTekUP{y0U_n41l3d_N3tw0rk_b4s1cs}")
    else:
        print("Sorry, incorrect answers.")

if __name__ == "__main__":
    main()
