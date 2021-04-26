import json, csv


def is_admin(message, role_name):
    return role_name.lower() in [role.name.lower() for role in message.author.roles]


def parse_student_info(filename):
    reader = csv.DictReader(open(filename, "r"))
    parsed_student_data = {}
    for row in reader:
        student_id = row["Student ID"]
        surname = row["Surname"]
        first_name = row["First name"]
        preferred_name = row["Preferred name"]
        email = row["Email address"]
        discord_key = row["Discord Key"]

        parsed_student_data[discord_key] = {
            "student_id": student_id,
            "surname": surname,
            "first_name": first_name,
            "preferred_name": preferred_name,
            "email": email,
        }

    print(parsed_student_data)

    # Write data as json
    with open("parsed_student_data.json", "w+") as f:
        json.dump(parsed_student_data, f)


def get_student_info(discord_key):
    filename = "parsed_student_data.json"
    with open(filename, "r") as f:
        parsed_student_data = json.load(f)
        try:
            return parsed_student_data[discord_key]
        except Exception as e:
            print(e)
            return false


if __name__ == "__main__":
    parse_student_info("student_data.csv")
