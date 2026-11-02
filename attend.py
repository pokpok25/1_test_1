import csv
import os


FILE_NAME = "attendance.csv"


def load_attendance():
    """
    attendance.csv 파일에서 출석 기록을 읽어 옵니다.

    반환값 예:
    [
        {"date": "2026-11-02", "name": "홍길동"},
        {"date": "2026-11-02", "name": "김철수"}
    ]
    """
    attendance = []

    if not os.path.exists(FILE_NAME):
        return attendance

    with open(FILE_NAME, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            attendance.append({
                "date": row["date"],
                "name": row["name"]
            })

    return attendance


def save_attendance(attendance):
    """
    출석 기록 전체를 attendance.csv 파일에 저장합니다.
    """
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["date", "name"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for record in attendance:
            writer.writerow(record)


def add_attendance(attendance):
    """
    날짜와 이름을 입력받아 출석 기록을 추가합니다.
    """
    date = input("날짜를 입력하세요 예: 2026-11-02: ").strip()
    name = input("이름을 입력하세요: ").strip()

    if date == "":
        print("날짜를 입력해야 합니다.")
        return

    if name == "":
        print("이름을 입력해야 합니다.")
        return

    record = {
        "date": date,
        "name": name
    }

    attendance.append(record)
    save_attendance(attendance)

    print("출석이 기록되었습니다.")


def show_attendance(attendance):
    """
    저장된 출석 목록을 화면에 보여 줍니다.
    """
    if len(attendance) == 0:
        print("아직 출석 기록이 없습니다.")
        return

    print()
    print("===== 출석 목록 =====")

    for index, record in enumerate(attendance, start=1):
        print(f"{index}. {record['date']} - {record['name']}")

    print("====================")
    print()


def show_menu():
    """
    사용자가 선택할 수 있는 메뉴를 보여 줍니다.
    """
    print()
    print("===== 스터디 출석부 =====")
    print("1. 출석 기록 추가")
    print("2. 출석 목록 보기")
    print("3. 종료")
    print("========================")


def main():
    attendance = load_attendance()

    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            add_attendance(attendance)
        elif choice == "2":
            show_attendance(attendance)
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 1, 2, 3 중에서 골라 주세요.")


if __name__ == "__main__":
    main()
