// This program is intended to merge two customer files
start
    // Declare the input files, customer number, property size, last names,
    // and addresses from the 
    Declarations
        InputFile geraldineFile
        InputFile geraldFile
        OutputFile mergedFile
        num geraldCustomerNum
        num geraldineCustomerNum
        num geraldPropertySize
        num geraldinePropertySize
        string geraldLastName
        string geraldAddress
        string geraldineLastName
        string geraldineAddress
        string END = "endend"
        string bothAtEnd = "N"
    // Create getReady() function
    getReady()
    while bothAtEnd <> "Y"
        mergeRecords()
    endwhile
    finishUp()
stop

    // Use the getReady function to start the program by opening
    // files and reading the information inside 
    getReady()
        open geraldineFile
        open geraldFile
        open mergedFile
        readGerald()
        readGeraldine()
        checkEnd()
    return

    // Creating the readGerald function which inputs the file information
    // to wait to be processed into the merge file function
    readGerald()
        input geraldLastName, geraldCustomerNum, geraldPropertySize, geraldAddress from geraldFile
        if eof then
            geraldCustomerNum = END
        else
            input geraldLastName, geraldCustomerNum, geraldPropertySize, geraldAddress from geraldFile
        endif
    return

    // Creating the readGeraldine function which inputs the file information
    // to wait to be processed into the merge file function
    readGeraldine()
        input geraldineLastName, geraldineCustomerNum, geraldinePropertySize, geraldineAddress from geraldineFile
        if eof then
            geraldineCustomerNum = END
        else
            input geraldineLastName, geraldineCustomerNum, geraldinePropertySize, geraldineAddress from geraldineFile
        endif
    return

    // Creating the checkEnd function which compaires the files with
    // a string to see if it's the final value
    checkEnd()
        if geraldNames = END then
            if geraldineNames = END then
                bothAtEnd = "Y"
            endif
        endif
    return

    // Creating the mergeRecords function which compaires files to see which
    // will be merged. If they are equal, gerald will be chosen to merge
    mergeRecords()
        if geraldineCustomerNum > geraldCustomerNum then
            output geraldineLastName, geraldineCustomerNum, geraldinePropertySize, geraldineAddress to mergedFile
            readGeraldine()
        elif geraldineCustomerNum < geraldCustomerNum then
            output geraldLastName, geraldCustomerNum, geraldPropertySize, geraldAddress to mergedFile
            readGerald()
        else
            output geraldLastName, geraldCustomerNum, geraldPropertySize, geraldAddress to mergedFile
            readGeraldine()
            readGerald()
        endif
    return

    // Creating the finish up function which closes the program
    finishup()
        close geraldineFile
        close geraldFile 
        close mergeFile
    return
stop















