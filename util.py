import json, csv


def is_admin(ctx, admin_role_name):
    """Check if the user has a role with a particular name, aka an admin role

    Args:
        ctx (context): The context where the command was called from ex. discord.Message
        admin_role_name (str): Name of the Admin role

    Returns:
        boolean: Return true if the user is an admin, false otherwise
    """
    return admin_role_name.lower() in [role.name.lower() for role in ctx.author.roles]


def parse_student_data(filename): 
    """Parse .csv file containing student data

    Args:
        filename (str): Name of the file (must be a .csv file)
    """
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
            "Student ID": student_id,
            "Surname": surname,
            "First name": first_name,
            "Preferred name": preferred_name,
            "Email address": email,
        }

    # Write data as json
    with open("parsed_student_data.json", "w+") as f:
        json.dump(parsed_student_data, f)


def get_student_data(discord_key):
    """Returns the data of the student using the discord key

    Args:
        discord_key (str): Discord key of the student

    Returns:
        [Student|None]: Returns Student object or None if the student was not found
    """
    filename = "parsed_student_data.json"
    with open(filename, "r") as f:
        parsed_student_data = json.load(f)
        try:
            return parsed_student_data[discord_key]
        except Exception as err:
            print(err)
    return None


if __name__ == "__main__":
    parse_student_data("student_data.csv")
