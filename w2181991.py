"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w2181991
 4. Date: 22/11/2025
****************************************************************************

"""
from graphics import *
import csv
import math

data_list = []   # data_list An empty list to load and hold data from csv file

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)
##################################################################################################################################3

#TASK_A
airport_codes = ["LHR", "MAD", "CDG", "IST", "AMS", "LIS", "FRA", "FCO", "MUC", "BCN"]
full_airport_name = ["London Heathrow", "Madrid Adolfo Suárez-Barajas", "Charles De Gaulle International", "Istanbul Airport International",
                     "Amsterdam Schiphol", "Lisbon Portela", "Frankfurt Main", "Rome Fiumicino", "Munich International", "Barcelona International"]
iata_codes = ["BA", "AF", "AY", "KL", "SK", "TP", "TK", "W6", "U2", "FR", "A3", "SN", "EK", "QR", "IB", "LH"]
airline_names = [
    "British Airways", "Air France", "Finnair", "KLM", "Scandinavian Airlines",
    "TAP Air Portugal", "Turkish Airlines", "Wizz Air", "easyJet", "Ryanair",
    "Aegean Airlines", "Brussels Airlines", "Emirates", "Qatar Airways", "Iberia", "Lufthansa"
]


while True:
        # ---- city code ----
        city_code = input("Please enter a three-letter city code: ").strip().upper()
        while len(city_code) != 3:
            city_code = input("Wrong code length – please enter a three-letter city code: ").strip().upper()
        while city_code not in airport_codes:
            if len(city_code) != 3:
                city_code = input("Wrong code length – please enter a three-letter city code: ").strip().upper()
            else:
                city_code = input("Unavailable city code – please enter a valid city code: ").strip().upper()

        # ---- year (validate format first, then range) ----
        year_str = input("Please enter the year required in the format YYYY: ").strip()
        while not (len(year_str) == 4 and year_str.isdigit()):
            year_str = input("Wrong data type - please enter a four-digit year value: ").strip()

        year = int(year_str)
        while year not in range(2000, 2026):  # 2000–2025 inclusive
            year_str = input("Out of range - please enter a value from 2000 to 2025: ").strip()
            if len(year_str) == 4 and year_str.isdigit():
                year = int(year_str)
                

        # ---- file check ----
        selected_data_file = f"{city_code}{year}.csv"
        p = airport_codes.index(city_code)

        try:
            with open(selected_data_file, 'r', encoding='utf-8') as file:  # Open the file to check if it exists
                print("************************************************************************************************************")
                print(f"{selected_data_file} selected - Planes departing {full_airport_name[p]} {year}")
                print("************************************************************************************************************")
            break  # Exit the main loop if file exists
        except FileNotFoundError:
            pass
              
        
load_csv(selected_data_file)     #calls the function "load_csv" sending the variable 'selected_data_file" as a parameter

#Task_B
def task_B(): 
    print("************************************************************************************************************")
    print(f"File {selected_data_file} selected - Planes departing {full_airport_name[p]} {year}")
    print("************************************************************************************************************")
    

    #1. The total number of flights from this airport was (CORRECTED)
    print (f"The total number of flights from this airport was {len(data_list)}")

    #2. The total number of flights departing Terminal Two was (CORRECTED)
    count = sum(1 for row in data_list if row[8].strip() == "2")
    print (f"The total number of flights departing Terminal Two was {count}")

    #3. The total number of departures on flights under 600 miles was (CORRECTED)
    Under600 = sum(1 for row in data_list if int(row[5].strip()) < 600) 
    print(f"The total number of departures on flights under 600 miles was {Under600}")

    #4. The total number of departure flights by Air France aircraft (CORRECTED)
    AF = sum(1 for row in data_list if row[1].strip().startswith("AF"))
    print (f"There were {AF} Air France flights from this airport")

    #5. The total number of flights departing in temperatures below 15C (CORRECTED)
    TB = sum(1 for row in data_list if row[10].strip() < "15")
    print(f"There were {TB} flights departing in temperatures below 15 degrees")

    #6. The average number of British Airways departures per hour (rounded to two decimal places) (CORRECTED)
    BA = sum(1 for row in data_list if row[1].strip().startswith("BA"))
    average_per_hour = BA / 12  
    print(f"There was an average of {average_per_hour:.2f} British Airways flights per hour from this airport.")

    #7. The percentage of total departures that are British Airways aircraft
    Total_Depature = len(data_list)
    Percentage_Total_BA = BA/Total_Depature
    print (f"British Airways planes made up {(Percentage_Total_BA)*100:.2f}% of all departures")

    #8. The percentage of Air France flights with a delayed departure
    Delay_AF = sum(1 for row in data_list if row[1].strip().startswith("AF") and row[3].strip() > row[2].strip())
    Percentage_AF_delay = Delay_AF/AF
    print (f"{(Percentage_AF_delay)*100:.2f}% of Air France departures were delayed")
    
    #9 . The total number of hours of rain in the twelve hours.
    rainy_hours = set()
    for row in data_list:
        try:
            hour = int(str(row[2]).strip().split(":")[0])  # row[2] = ScheduledDepature
        except Exception:
            continue
        if 0 <= hour <= 11 and "rain" in str(row[10]).lower():
            rainy_hours.add(hour)

    rain_hours = len(rainy_hours)
    print(f"There were {rain_hours} hours in which rain fell")

    #10 . Least common destination with full names
    destinations = [row[4].strip() for row in data_list]
    least_count = min(destinations.count(d) for d in destinations)
    least_common = [d for d in set(destinations) if destinations.count(d) == least_count]

    full_names = [full_airport_name[airport_codes.index(code)] for code in least_common if code in airport_codes]

    print(f"The least common destinations are {full_names}")

task_B() 


# Task C. Save Results as a Text File (10 Marks)
def task_C():
    original_stdout = sys.stdout # Store the original stdout
    with open("results.txt", 'a', encoding="utf-8") as f:
        sys.stdout = f # Redirect stdout to the file
        task_B() # Call the function, all prints will go to the file
    sys.stdout = original_stdout # Restore original stdout
    return
task_C()

def task_D():
    while True:
        ALcode_His = input("Enter a two-character Airline code to plot a histogram: ").upper().strip()
        while ALcode_His not in iata_codes:
            print("Unavailable Airline code, please try again.")
            ALcode_His = input("Enter the two-character Airline code to plot a histogram: ").upper().strip()
        IntexAL = iata_codes.index(ALcode_His)
        break

    # Create window
    win = GraphWin("Histogram", 800, 500)
    win.setBackground(color_rgb(244, 240, 232))  # Light cream background

    # Title
    title_text = f"Departures by hour for {airline_names[IntexAL]} from {full_airport_name[p]} {year}"
    title = Text(Point(400, 30), title_text)  # Centered in logical coords
    title.setSize(12)
    title.setStyle("bold")
    title.draw(win)

    # Y-axis label
    y_label = Text(Point(40, 250), "Hours\n\n00:00\nto\n12:00")
    y_label.setSize(10)
    y_label.setStyle("bold")
    y_label.draw(win)

    # -------------------- ADDITIONS START HERE --------------------
    # 1) Filter rows for selected airline 
    filtered_flights = [row for row in data_list if row[1].strip().upper().startswith(ALcode_His)]

    # 2) Count flights per hour using ScheduledDepature 
    hourly = [0] * 12  
    for row in filtered_flights:
        sched = row[2].strip()
        try:
            hr = int(sched.split(":")[0])
        except (ValueError, IndexError):
            continue
        if 0 <= hr <= 11:
            hourly[hr] += 1

    # 3) Simple horizontal histogram bars 
    left_margin = 150    
    right_margin = 40
    top_margin = 70     
    bar_h = 20
    gap = 12

    # Compute drawable width and scale to max value 
    drawable_w = 800 - left_margin - right_margin
    max_val = max(hourly) if hourly else 0
    scale = (drawable_w - 40) / max_val if max_val > 0 else 1

    # Draw an axis line for reference
    axis = Line(Point(left_margin, top_margin - 8), Point(left_margin, top_margin + 12 * (bar_h + gap) - gap + 8))
    axis.setWidth(2)
    axis.draw(win)

    # 4) Render each hour row: label, bar, and numeric value
    for h in range(12):
        # Vertical placement for this row
        y_top = top_margin + h * (bar_h + gap)
        y_mid = y_top + bar_h / 2

        # Hour label (e.g., "00:00")
        lab = Text(Point(left_margin - 50, y_mid), f"{h:02d}:00")
        lab.setSize(10)
        lab.draw(win)

        # Bar length
        bar_len = hourly[h] * scale

        # Bar rectangle (use a pleasant blue tone; grey for zero)
        bar = Rectangle(Point(left_margin + 1, y_top),
                        Point(left_margin + 1 + max(bar_len, 2), y_top + bar_h))
        bar.setFill("pink")
        bar.setOutline(color_rgb(50, 50, 50))
        bar.setWidth(1)
        bar.draw(win)

        # Numeric value just to the right of the bar
        val_x = left_margin + 1 + (bar_len if hourly[h] > 0 else 8) + 10
        val = Text(Point(val_x, y_mid), str(hourly[h]))
        val.setSize(10)
        val.draw(win)
    win.getMouse()
    win.close()
task_D()

# Task E.
def task_E():
    while True:
        New_CSV = input("Do you want to select a new data file? Y/N: ").upper().strip()

        if New_CSV == "Y":
            data_list.clear()
            # --- File selection process ---
            while True:
                # City code
                city_code = input("Please enter a three-letter city code: ").strip().upper()
                while len(city_code) != 3:
                    city_code = input("Wrong code length – please enter a three-letter city code: ").strip().upper()
                while city_code not in airport_codes:
                    if len(city_code) != 3:
                        city_code = input("Wrong code length – please enter a three-letter city code: ").strip().upper()
                    else:
                        city_code = input("Unavailable city code – please enter a valid city code: ").strip().upper()

                # Year
                year_str = input("Please enter the year required in the format YYYY: ").strip()
                while not (len(year_str) == 4 and year_str.isdigit()):
                    year_str = input("Wrong data type - please enter a four-digit year value: ").strip()

                year = int(year_str)
                while year not in range(2000, 2026):
                    year_str = input("Out of range - please enter a value from 2000 to 2025: ").strip()
                    if len(year_str) == 4 and year_str.isdigit():
                        year = int(year_str)

                selected_data_file = f"{city_code}{year}.csv"
                p = airport_codes.index(city_code)

                # Try to open the file; if not found, loop back to re-enter
                try:
                    with open(selected_data_file, 'r', encoding='utf-8') as file:
                        print("************************************************************************************************************")
                        print(f"{selected_data_file} selected - Planes departing {full_airport_name[p]} {year}")
                        print("************************************************************************************************************")
                    break
                except FileNotFoundError:
                    pass

            # Load data and run the tasks once
            load_csv(selected_data_file)
            task_B()
            task_C()
            task_D()

            return True

        elif New_CSV == "N":
            print("Thank you. End of run")
            return False
        else:
            pass
            continue


# ---- Main loop ----
while True:
    # task_E() controls whether we continue or stop
    keep_going = task_E()
    if not keep_going:
        break


