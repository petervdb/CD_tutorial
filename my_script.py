import datetime
today = datetime.date.today()
version = "1.0.4"
creation_date = "2020-02-15"
latest_update_date = "2020-02-17"
logfile="/log/history.log"
f = open(logfile, "a")
print ("This container version ", version, " created on ", creation_date, " and updated on ", latest_update_date, " was last executed on ", datetime.datetime.now())
f.write ("This container version " + version + " created on " + creation_date + " and updated on ")
f.write ( latest_update_date + " was last executed on " +  str(datetime.datetime.now()) + "\n")
print ("================================================================================")
f.write("================================================================================\n")
