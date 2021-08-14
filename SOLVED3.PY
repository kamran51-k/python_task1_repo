import csv
def gdp():
    year = input("Please enter a year")
    with open('./unemp.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[0] == year:
                print(row)
                average = sum(list(map(float, row[1:13])))/12
                print(f"Yearly average unemployment {average}")
    gdp_file = open("./gdp.txt", "r")
    total = 0
    for line in gdp_file:
        if line[:4] == year:
            total += float(line.strip().split()[1])
    print(f"GDP average is {total/4}")
gdp()