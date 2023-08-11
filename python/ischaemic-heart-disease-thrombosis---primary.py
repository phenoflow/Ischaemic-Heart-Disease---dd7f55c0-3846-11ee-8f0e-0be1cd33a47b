# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2023.

import sys, csv, re

codes = [{"code":"7A54700","system":"readv2"},{"code":"7A56000","system":"readv2"},{"code":"7A6S300","system":"readv2"},{"code":"G30..12","system":"readv2"},{"code":"G30..16","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ischaemic-heart-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ischaemic-heart-disease-thrombosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ischaemic-heart-disease-thrombosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ischaemic-heart-disease-thrombosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)