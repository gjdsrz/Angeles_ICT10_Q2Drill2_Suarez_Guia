import html
from js import document


# Sets for each club category
inte = {"Sultan Kudurat", "Peter Parker", "Kylian Mbappé"}

comms = {"Benjamin Tennyson", "Valentinez Sicidabohertz"}

advoc = {"Deion Decierto", "Loriz Santos", "Nataliya Pabale", "Sean Lee"}

acad = {"Master Oogway", "Michelangelo Buonarroti", "SpongeBob SquarePants", "Ludwig von Koopa"}


# Function to display all members
def show_members():

    # Combine the sets using union
    all_members = inte | comms | advoc | acad

    # Sort the names alphabetically
    member_list = sorted(all_members)

    # Display the names
    names = "<br>".join(map(html.escape, member_list))

    # Show the names and total number of members
    document.getElementById("output").innerHTML = f"""
        <h3>All members:</h3>
        {names}
        <br>
        Total members: {len(all_members)}
    """


# Function to add a new member
def add_member(event):
    global inte

    # Get the names from the text boxes
    first = document.getElementById("fname").value.strip()
    last = document.getElementById("lname").value.strip()

    # Combine first and last name
    full_name = f"{first} {last}".strip()

    # Add the new member using a set operator
    inte = inte | ({full_name} - {""})

    # Update the member list
    show_members()

    # Clear the text boxes
    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""


# Display the members when the page opens
show_members()
