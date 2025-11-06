def get_applicant_info():
    name = input("Enter applicant's name: ").strip()
    gender = input("Enter applicant's gender (M/F): ").strip().upper()
    return name, gender

def approve_loan(name, gender):
    # Simple approval logic based on gender
    if gender == 'M':
        print(f"Loan approved for Mr. {name}.")
    elif gender == 'F':
        print(f"Loan approved for Ms. {name}.")
    else:
        print("Loan approval failed: Invalid gender.")

def main():
    print("=== Loan Approval System ===")
    name, gender = get_applicant_info()
    approve_loan(name, gender)

if __name__ == "__main__":
    main()