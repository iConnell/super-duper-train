import csv, hashlib, json, sys, os

def main():
    # check that a csv file was passed as argument
    if len(sys.argv) < 2:
        print("You must specify a csv file")
        exit()
        
    csv_file = sys.argv[1]
    output_csv_file_name = csv_file.split('.')[0]


    headers = []
    rows = []

    # create new csv file for the output
    new_csv = open(f"{output_csv_file_name}.output.csv", 'w', newline='')
    writer = csv.writer(new_csv)


    # open and read data from csv file
    with open('HNGi9.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        # get the headers
        headers = next(csv_reader)

        #add sha256 to headers
        headers.append("sha256")
        writer.writerow(headers)

        for row in csv_reader:
            rows.append(row)


    for row in rows:
        # skip rows that specify team names
        if row[0].startswith('TEAM'):
            writer.writerow(row)
            continue

        # The output dictionary
        output_dict = {
            "format": "CHIP-0007",
            "name": row[1],
            "description": row[3],
            "minting_tool": "",
            "sensitive_content": False,
            "series_number": row[0],
            "series_total": rows[-1][0],
            "attributes":[
                {
                    "trait_type": "gender",
                    "value": row[4]
                }
            ],
            "collection":{
                "name": "",
                "id": row[6],
                "attributes":[
                    {
                        "type": "description",
                        "value": "Rewards for accomplishments during HNGi9"
                    }
                ]
            }
        }

        # converts output dictionary to json
        json_object = json.dumps(output_dict, indent=4)

        # checks if json files directory exists, creates if it doesn't
        if not os.path.exists("./json_files/"):
            os.makedirs("./json_files")

        # creates a json file for the current row
        with open(f'json_files/{row[1]}.json', "w") as output_file:
            output_file.write(json_object)

        # generates sha256 has for the json file created above
        with open(f'json_files/{row[1]}.json', 'rb') as binary_file:
            output_bytes = binary_file.read()
            hash = hashlib.sha256(output_bytes).hexdigest()

            # add the hash to the row list
            row.append(hash)
        
        # write the row to the csv file
        writer.writerow(row)
        

if __name__ == "__main__":
    main()