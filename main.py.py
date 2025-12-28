from datetime import datetime, timedelta

def smart_study_planner():
    print("\n SMART STUDY PLANNER \n")

    subjects = {}
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input(f"Enter subject {i+1} name: ")
        while True:
            priority = int(input(f"Enter priority for {subject} (1-5, 5 = highest): "))
            if 1 <= priority <= 5:
                break
            else:
                print(" Priority must be between 1 and 5.")

        subjects[subject] = priority

    daily_hours = float(input("\nEnter available study hours per day: "))

    exam_date_input = input("Enter exam date (YYYY-MM-DD): ")
    exam_date = datetime.strptime(exam_date_input, "%Y-%m-%d").date()
    today = datetime.today().date()

    days_left = (exam_date - today).days

    if days_left <= 0:
        print(" Exam date must be a future date.")
        return

    total_priority = sum(subjects.values())

    print(f"\n🗓 Days left until exam: {days_left}")
    print("\n DAILY STUDY PLAN\n")

    current_date = today

    with open("study_plan.txt", "w") as file:
        file.write("SMART STUDY PLAN\n\n")

        for day in range(days_left):
            print(f"📌 Date: {current_date}")
            file.write(f"Date: {current_date}\n")

            for subject, priority in subjects.items():
                hours = (priority / total_priority) * daily_hours
                print(f"  • {subject}: {hours:.2f} hours")
                file.write(f"{subject}: {hours:.2f} hours\n")

            print("-" * 30)
            file.write("-" * 30 + "\n")
            current_date += timedelta(days=1)

    print("\n Study plan saved successfully as 'study_plan.txt'")

if __name__ == "__main__":
    smart_study_planner()