"""Task: Event Guest List Manager
Description: You are organizing an event and need to manage guest lists using sets. You have two groups of people:
invited guests and confirmed attendees. Create a program to perform the following:

Create a set called invited_guests with at least 5 names of people you invited to the event.
Create a set called confirmed_attendees with at least 3 names of people who confirmed their attendance
 (some may overlap with invited_guests).
Print the following:

The list of all invited guests.
The list of confirmed attendees.
The names of guests who were invited but did not confirm (use the appropriate set operation).
The names of guests who confirmed but were not on the invited list (use the appropriate set operation).



Requirements:

Use at least one set method (e.g., union, intersection, difference, etc.) or operator (e.g., , &, -).
Ensure your sets contain unique names (no duplicates).
Use print() to display the results with clear labels (e.g., "Invited Guests:", etc.)"""

invited_guests = {"Joe Biden", "Donald Trump", "JPT Morgan", "Henry Ford", "Ronaldo"}
confirmed_attendees = {"Donald Trump", "Ronaldo", "Joe Biden", "putin", "Makron", "Mendela"}
unconfirmed_attendees = invited_guests.difference(confirmed_attendees)
not_listGuests = confirmed_attendees.difference(invited_guests)
allList = f"The list of all invited guests: {invited_guests} "
all_attendees = f"The list of all confirmed attendees: {confirmed_attendees}"
not_confirm = f"The names of guests who were invited but did not confirm: {unconfirmed_attendees}"
not_invited = f"The names of guests who confirmed but were not on the invited list: {not_listGuests}"
print(allList)
print(all_attendees)
print(not_confirm)
print(not_invited)
print()