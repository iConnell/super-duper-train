# HNG CSV TASK

This script takes the CSV provided by the teams, and generate a [CHIP-0007 compatible json](https://github.com/Chia-Network/chips/blob/main/assets/chip-0007/example.json), calculate the sha256 of the json file and append it to each line in the csv (as a filename.output.csv)

## Usage

```
# Clone this repo
git clone https://github.com/iConnell/super-duper-train.git

# change into the super-duper-train directory
cd super-duper-train

# run the python file with a csv file as filename
python main.py <filename.csv>
```

Json files for all columns will be found in `root/json_files/`
and a `filename.output.csv` file in the root directory
