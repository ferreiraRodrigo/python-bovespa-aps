import bovespa
from classes.Company import Company
import numpy as np      

# Loop through all the records on the file and print in a format with the changes beetween the open price and close price(percentage)
def read_bovespa_files(file):
        bovespa_file = bovespa.File(file)
        for bovespa_record in bovespa_file.query():
                change = ((bovespa_record.price_close - bovespa_record.price_open) / bovespa_record.price_open) * 100
                print("{} | {} | Open Price: {} | Close Price: {} | Changes: {:.2f}%".format(
                        bovespa_record.date,
                        bovespa_record.company_name,
                        bovespa_record.price_open,
                        bovespa_record.price_close,
                        change
                        ))

# Split the company data and put it all in a matrix                       
def get_std_each_company(file):
        bovespa_file = bovespa.File(file)
        companys_index = []
        companys = []
        for bovespa_record in bovespa_file.query():
                if bovespa_record.company_name in companys_index:
                        companys[companys_index.index(bovespa_record.company_name)].add_price(bovespa_record.price_close)
                else:
                        new_company = Company(bovespa_record.company_name)
                        companys_index.append(bovespa_record.company_name)
                        companys.append(new_company)
                        companys[len(companys) - 1].add_price(bovespa_record.price_close)
        for company in companys:
                print(np.std(company.price_history))