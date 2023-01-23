# CSV Anonymizer
Python script that extracts a column from a CSV file, anonymizes the data from one specific column, and writes into a new CSV file.
Can hash multiple columns in one operation.

## Running Instructions

- The original file needs to be either in the project folder, or a full path
- The original file needs to have a ``Header`` 
- To run the file, execute the following command:
    ```
    python anonymize_full_script.py -i <inputfilename> -o <outputfilename> -c <columnname>  
    ```
 ``-c, or --column`` is the name of the column which needs to be anonymized
 Important: There cannot be spaces in between column names!
 Example on how to execute this code:
    ```
    python anonymize_full_script.py -i people-100.csv -o people-hash1.csv -c 'Job Title','First Name'
    ```


## Future Improvements
- Create a handle that defines weather if the file has a ``Header`` or not
- Create a loop that handles files without a ``Header``
- Create an exeption handling for when the file is not in the project folder
- Implement the ``click`` package instead of the ``sys`` aiming to create a more dynamic CLI for the user