kata = (2019, 9, 25, 3, 3)

year = str(kata[0])
month = str(kata[1])
day = str(kata[2])
hour = str(kata[3])
minutes = str(kata[4])

print(year.zfill(4) + "/" + month.zfill(2) + "/" + day.zfill(2) + " " + hour.zfill(2) + ":" + minutes.zfill(2))