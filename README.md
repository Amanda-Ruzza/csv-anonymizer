# CSV Anonymizer
Python script that extracts a column from a CSV file, anonymizes the data from one specific column, and writes into a new CSV file

## Running Instructions:

- The original file needs to be either in the project folder, or a full path
- The original file needs to have a ``Header`` 
- To run the file, execute the following command:
    ```
    python anonymize_full_script.py -i <inputfilename> -o <outputfilename> -c <columnname>  
    ```
 ``-c, or --column`` is the name of the column which needs to be anonymized


## Future Improvements:
- Create a handle that defines weather if the file has a Header
- Create an exeption handling for when the file is not in the project folder