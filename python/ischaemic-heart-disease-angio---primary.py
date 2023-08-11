# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2023.

import sys, csv, re

codes = [{"code":"5533","system":"readv2"},{"code":"7927500","system":"readv2"},{"code":"7928","system":"readv2"},{"code":"7928.11","system":"readv2"},{"code":"7928000","system":"readv2"},{"code":"7928100","system":"readv2"},{"code":"7928200","system":"readv2"},{"code":"7928300","system":"readv2"},{"code":"7928y00","system":"readv2"},{"code":"7928z00","system":"readv2"},{"code":"7929000","system":"readv2"},{"code":"7929300","system":"readv2"},{"code":"793G.00","system":"readv2"},{"code":"793G300","system":"readv2"},{"code":"793Gy00","system":"readv2"},{"code":"793Gz00","system":"readv2"},{"code":"7A54000","system":"readv2"},{"code":"7A54500","system":"readv2"},{"code":"7A56400","system":"readv2"},{"code":"7A6G100","system":"readv2"},{"code":"7A6H300","system":"readv2"},{"code":"7A6H400","system":"readv2"},{"code":"8L41.00","system":"readv2"},{"code":"8LF..00","system":"readv2"},{"code":"ZV45800","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ischaemic-heart-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ischaemic-heart-disease-angio---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ischaemic-heart-disease-angio---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ischaemic-heart-disease-angio---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
