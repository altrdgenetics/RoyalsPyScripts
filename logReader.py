import os
import time

filePath = str(input("Enter Full File Path: "))
defaultSearchTermTCP = str("Blocked incoming TCP connection request")
defaultSearchTermUDP = str("Blocked incoming UDP connection request")
print("Default Search Terms: '" + defaultSearchTermTCP + "' & '" + defaultSearchTermUDP + "'")
'''print("Enter Additional Search Terms -> 'OR' ")
searchTerm = str(input("(separate terms with space): "))'''
exists = os.path.isfile(filePath)

if exists:
    startDate = str("")
    startTime = str("")
    endDate = str("")
    endTime = str("")
    firstLine = True
    '''searchTermSplit = searchTerm.upper().split()'''
    logfile = open(os.path.abspath(filePath), 'r')
    result_file = open('results_' + str(time.time()).replace('.', '') + '.txt', 'w+')
    with logfile as f:
        for line in f:
            if (line.__contains__(defaultSearchTermUDP)) or (line.__contains__(defaultSearchTermTCP)):
                '''if any(x in line.upper() for x in searchTermSplit):'''
                date = str(line[0:6]).replace("  ", " ").strip()
                time = str(line[7:15]).strip()
                proto = str(line[94:97]).strip()
                ip = "{:<15}".format(str(line.split("from", 1)[1].split(":")[0]).strip())
                port = str(line.rsplit(":", 1)[1]).strip()
                result_file.write("DATE= " + date + "   TIME= " + time + "    PROTO= " + proto + "    IP= " + ip
                                  + "    PORT= " + port + "\n")
                if firstLine:
                    startDate = date.replace(" ", "_")
                    startTime = time
                    firstLine = False
                endDate = date.replace(" ", "_")
                endTime = time
    logfile.close()
    result_file.close()
    newName = str("results_" + startDate + "_" + startTime + "_" + endDate + "_" + endTime + ".txt")
    os.rename(result_file.name, newName.replace(":", "_"))
else:
    print("File Does not Exist")



