import openpyxl

# Load the Excel file, skipping the first row (header)
file_path = "Test1.xlsx"
workbook = openpyxl.load_workbook(filename=file_path, data_only=True)  # Assuming UTF-8 encoding
sheet = workbook.active

punjabi_to_english = {}
for row in sheet.iter_rows(min_row=2):  # Skip the header row (row 1)
  punjabi_word = row[1].value
  english_word = row[0].value
  punjabi_to_english[punjabi_word] = english_word

def search_english_word():
  punjabi_word = input("Enter a Punjabi word: ")

  print(f"Entered Punjabi word: {punjabi_word}")

  english_word = punjabi_to_english.get(punjabi_word, "Word not found")
  print(f'The English word for "{punjabi_word}" is "{english_word}"')

# Call the function to perform the search
search_english_word()
