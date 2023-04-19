import csv

morse_data = []

old_light_value = 0
THRESHOLD = 120
with open('morse_light_raw.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # For each row in our data:
    for row in csv_reader:
        # Read the raw light value as an integer
        raw_light_value = int(row[1])

        # Here, you need to write code that stores a thresholded value into the current_light_value variable.
        if(raw_light_value > THRESHOLD):
          current_light_value = 1
        else:
          current_light_value = 0
          
        # Paste your code from the previous sketch that counts pulses of thresholded data using current_light_value here:

        
        morse_data.append([row[0],current_light_value])
        line_count += 1
    print(f'Processed {line_count} lines.')

# Now that we have processed the raw data, create a new CSV file that has the blade count vs. time data
f = open("morse_data_output.csv", "w")
for row in blade_data:
  f.write("{0},{1}\n".format(row[0], row[1]))
f.close()
