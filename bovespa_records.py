import bovespa

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