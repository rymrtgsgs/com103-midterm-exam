section = ""
while section == "":
    s_in = input("Class section: ")
    is_blank = True
    has_symbol = False
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
    for char in s_in:
        if char != " ":
            is_blank = False
        if char not in valid_chars:
            has_symbol = True
            
    if s_in == "" or is_blank or has_symbol:
        print("Invalid! Section cannot be blank or contain special symbols.")
    else:
        section = s_in.upper()

coordinator = ""
while coordinator == "":
    c_in = input("Coordinator name: ")
    is_blank = True
    for char in c_in:
        if char != " ":
            is_blank = False
            
    if c_in == "" or is_blank:
        print("Invalid! Coordinator name cannot be blank or only whitespace.")
    else:
        coordinator = c_in.upper()

print("\n==========================================")
print("   INTRAMURALS -- SPORTS EVENTS")
print("==========================================")
print(" 1. Basketball    [Team]")
print(" 2. Volleyball    [Team]")
print(" 3. Badminton     [Individual]")
print(" 4. Chess         [Individual]")
print(" 5. Table Tennis  [Individual]")
print("==========================================")

total_pts = 0
logs = ""
game_count = 1
log_display_num = 1
num_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

while game_count <= 4:
    print("\n--- GAME " + num_map[game_count] + " ---")
    
    choice = ""
    while choice == "":
        c_val = input("Sport number (0 to skip): ")
        if c_val in ["0", "1", "2", "3", "4", "5"]:
            choice = c_val
        else:
            print("INVALID! Enter 0-5 only (no signs, symbols, or spaces).")

    if choice == "0":
        game_count = game_count + 1
    else:
        opposing = ""
        while opposing == "":
            o_val = input("Opposing section: ")
            is_o_blank = True
            for char in o_val:
                if char != " ":
                    is_o_blank = False
            if o_val == "" or is_o_blank:
                print("Invalid! Opposing team cannot be blank.")
            else:
                opposing = o_val.upper()

        result = ""
        while result == "":
            r_val = input("Result (W/L): ")
            upper_r = r_val.upper()
            if upper_r == "W" or upper_r == "L":
                result = upper_r
            else:
                print("Invalid! Enter W or L only.")

        if choice == "1":
            s_name = "Basketball  [Team]"
        elif choice == "2":
            s_name = "Volleyball  [Team]"
        elif choice == "3":
            s_name = "Badminton   [Individual]"
        elif choice == "4":
            s_name = "Chess       [Individual]"
        else:
            s_name = "Table Tennis  [Individual]"

        pts = 0
        res_text = "LOSS"
        if result == "W":
            pts = 3
            res_text = "WIN "
        
        total_pts = total_pts + pts
        
        logs = logs + "[" + num_map[log_display_num] + "] " + s_name + "\n"
        logs = logs + "    vs " + opposing + "  |  Result: " + res_text + "  |  Points: " + num_map[pts] + "\n\n"
        
        game_count = game_count + 1
        log_display_num = log_display_num + 1

standing = "KEEP FIGHTING"
if total_pts >= 9:
    standing = "GOLD CONTENDER"
elif total_pts >= 6:
    standing = "SILVER PUSH"

print("\n=============================================")
print("     " + section + " -- GAME RESULTS BOARD")
print("=============================================")
print("Coordinator : " + coordinator)
print("---------------------------------------------")
print(logs, end="")
print("---------------------------------------------")
print("Total Points   : " + num_map[total_pts])
print("Standing       : " + standing)
print("=============================================")
