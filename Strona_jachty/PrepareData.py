from DbConnect import ConnectionConfig

CN = ConnectionConfig()

def PrepareAll():
    return CN.DownloadData("SELECT * FROM jachty")

def List():
    return CN.DownloadData("SELECT nazwa, linkjpg, t.typ, j.id FROM `jachty`AS j JOIN typy AS t ON j.idtyp = t.Id;")

def BoatData(Id):
    return CN.DownloadData("SELECT nazwa, linkjpg, t.typ, j.opis FROM `jachty`AS j "
                           "JOIN typy AS t ON j.idtyp = t.Id "
                           "WHERE j.id = "+str(Id))

def BoatReservation(Id):
    return CN.DownloadData("SELECT DATE_FORMAT(od, '%d-%m-%Y') AS od, "
                           "DATE_FORMAT(do, '%d-%m-%Y') AS do FROM rezerwacje WHERE IdJacht = "+str(Id))


