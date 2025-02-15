DEF MODIFY_CONTENT(CONTENT):

    RETURN CONTENT.UPPER()  # MODIFY CONTENT AS NEEDED


DEF MAIN():
    # PROMPT USER FOR A FILENAME
    FILENAME = INPUT("ENTER THE FILENAME TO READ: ")

    TRY:
        # ATTEMPT TO OPEN AND READ THE FILE
        WITH OPEN(FILENAME, 'R') AS FILE:
            CONTENT = FILE.READ()

        # MODIFY THE CONTENT
        MODIFIED_CONTENT = MODIFY_CONTENT(CONTENT)

        # CREATE A NEW FILE AND WRITE THE MODIFIED CONTENT
        NEW_FILENAME = F"MODIFIED_{FILENAME}"
        WITH OPEN(NEW_FILENAME, 'W') AS NEW_FILE:
            NEW_FILE.WRITE(MODIFIED_CONTENT)

        PRINT(F"THE MODIFIED CONTENT HAS BEEN WRITTEN TO {NEW_FILENAME}")

    EXCEPT FILENOTFOUNDERROR:
        PRINT(F"ERROR: THE FILE '{FILENAME}' DOES NOT EXIST. PLEASE CHECK THE FILENAME AND TRY AGAIN.")
    EXCEPT PERMISSIONERROR:
        PRINT(F"ERROR: PERMISSION DENIED FOR READING THE FILE '{FILENAME}'.")
    EXCEPT EXCEPTION AS E:
        PRINT(F"AN UNEXPECTED ERROR OCCURRED: {E}")


IF __NAME__ == "__MAIN__":
    MAIN()
