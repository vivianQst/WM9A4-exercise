"""
Speeding Ticket Function

Objective:
Write a function named 'speeding_ticket' that evaluates whether a driver should receive a speeding ticket based on their driving speed and a special condition (their birthday).

Function Parameters:
1. speed (integer): The driver's speed in mph (miles per hour).
2. is_birthday (boolean): A flag indicating whether the driver is driving on their birthday.

Instructions:
- The function should return one of three strings based on the driver's speed: "No Ticket", "Small Ticket", or "Big Ticket".
- If the driver's speed is 60 mph or less, they should receive "No Ticket".
- If the driver's speed is between 61 and 80 mph inclusive, they should receive a "Small Ticket".
- If the driver's speed is 81 mph or more, they should receive a "Big Ticket".
- On the driver's birthday, the speed limits for each ticket category are increased by 5 mph. For example, they can go up to 65 mph and still receive "No Ticket" if is_birthday is True.

Example Test Cases:
1. speeding_ticket(60, False) should return "No Ticket".
2. speeding_ticket(75, False) should return "Small Ticket".
3. speeding_ticket(85, False) should return "Big Ticket".
4. speeding_ticket(65, True) should return "No Ticket".
5. speeding_ticket(85, True) should return "Small Ticket".
"""


def speeding_ticket(speed, is_birthday):
    if is_birthday:
        speed -= 5

    # Check the driver's speed and return the appropriate ticket
    if speed <= 60:
        return "No Ticket"
    elif 61 <= speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"
    # Your code goes here
    # Implement the logic based on the driver's speed and birthday condition
    pass  # Delete this after implementing some code inside this function


# Test cases
print("Test1:",speeding_ticket(60, False))  # Expected output: "No Ticket"
print("Test2:",speeding_ticket(75, False))  # Expected output: "Small Ticket"
print("Test3:",speeding_ticket(85, False))  # Expected output: "Big Ticket"
print("Test4:",speeding_ticket(65, True))  # Expected output: "No Ticket"
print("Test5:",speeding_ticket(85, True))  # Expected output: "Small Ticket