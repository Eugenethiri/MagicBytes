#!/usr/bin/env python3

import sys

def corrupt_magic_number(input_file, output_file, file_type):
    with open(input_file, 'rb') as file:
        data = file.read()
                                                                                                                                                                      
    if file_type.lower() == 'jpeg' or file_type.lower() == 'jpg':
        corrupted_data = data[2:]
       
    elif file_type.lower() =='png' :
        corrupted_data = data[8:]
   
    else :
        raise ValueError("Unsupported file type. Use jpeg or png")
   
    with open(output_file, 'wb') as file:
        file.write(corrupted_data)
    
if __name__== "__main__":

    if len(sys.argv) != 5 or sys.argv[1] != '-i' or sys.argv[3] != '-m' :
        print("WRONG USAGE : ##python3 script.py -i /path/to/file -m jpeg/png/jpg")
        sys.exit(1)
    
    input_file = sys.argv[2] 
    file_type = sys.argv[4]
    output_file =  f"corrupted_{input_file.split('/')[-1]}" #automatic file naming
    
    try : 
         corrupt_magic_number(input_file, output_file, file_type)
         print(f"File Output saved as {output_file}")
         
    except Exception as e:
         print(f"Error: {e}")
