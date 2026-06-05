# condition1 and condition2
# both of conditions are needed to be true
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")

# condition1 or condition2
# any one condition is true then it is true
has_ticket = False
is_vip = True

if has_ticket or is_vip:
    print("Entry Allowed")


# not True -> becomes False , not False becomes -> True
logged_in = False
if not logged_in:
    print("Please Login")

