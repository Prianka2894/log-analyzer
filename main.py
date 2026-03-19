file_name = input("Enter log file name: ")

error_count = 0
warning_count = 0
total_lines = 0

with open(file_name, "r") as file:
    for line in file:
        total_lines += 1

        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1

print("Total lines:", total_lines)
print("ERROR count:", error_count)
print("WARNING count:", warning_count)
