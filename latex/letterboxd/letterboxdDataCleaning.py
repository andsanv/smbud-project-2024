import os

def replace_backslash_quotes_in_folder(input_folder, output_folder):
   try:
       # Ensure the output folder exists
       os.makedirs(output_folder, exist_ok=True)

       # Iterate through all files in the input folder
       for filename in os.listdir(input_folder):
           if filename.endswith('.csv'):
               input_file = os.path.join(input_folder, filename)
               output_file = os.path.join(output_folder, filename)

               # Read and process the file
               with open(input_file, 'r') as infile:
                   content = infile.read()

               # Replace occurrences of \" with  and of \"" with ""
               updated_content = content.replace('\\""', '""')
               updated_content = updated_content.replace('\\"', '"')

               # Write the updated content to the output file
               with open(output_file, 'w') as outfile:
                   outfile.write(updated_content)

               print(f"Processed file: {input_file} -> {output_file}")

       print("All .csv files processed successfully.")
   except Exception as e:
       print(f"An error occurred: {e}")