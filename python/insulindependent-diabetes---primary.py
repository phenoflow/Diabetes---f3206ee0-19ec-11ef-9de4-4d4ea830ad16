# Evangelos Kontopantelis, David Springate, David Reeves, Darren M Ashcroft, Jose M Valderas, Tim Doran, 2024.

import sys, csv, re

codes = [{"code":"C109D00","system":"readv2"},{"code":"C108600","system":"readv2"},{"code":"C108C00","system":"readv2"},{"code":"C108.00","system":"readv2"},{"code":"C108400","system":"readv2"},{"code":"C109400","system":"readv2"},{"code":"C10E812","system":"readv2"},{"code":"C108800","system":"readv2"},{"code":"C108.11","system":"readv2"},{"code":"C109H00","system":"readv2"},{"code":"C109.00","system":"readv2"},{"code":"C109C00","system":"readv2"},{"code":"C108700","system":"readv2"},{"code":"C108H00","system":"readv2"},{"code":"66A5.00","system":"readv2"},{"code":"C108500","system":"readv2"},{"code":"C10E412","system":"readv2"},{"code":"C109500","system":"readv2"},{"code":"C108900","system":"readv2"},{"code":"C10E.12","system":"readv2"},{"code":"C108D00","system":"readv2"},{"code":"C109B00","system":"readv2"},{"code":"C100112","system":"readv2"},{"code":"C109A00","system":"readv2"},{"code":"C109G00","system":"readv2"},{"code":"C100011","system":"readv2"},{"code":"C108F00","system":"readv2"},{"code":"C109600","system":"readv2"},{"code":"C108B00","system":"readv2"},{"code":"C108E00","system":"readv2"},{"code":"C108J00","system":"readv2"},{"code":"250 AK","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulindependent-diabetes---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulindependent-diabetes---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulindependent-diabetes---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
