#!/usr/bin/env python3

"""
Changes made to this file will affect the main programm.
Use this file to configure the plot output.
Population data for the different bundelaender will be downloaded automatically.
Population data must be added manually for each landkreise. -> "SK Regensburg": Population of 153094
"""

RKI_FILE_RELATIV_PATH = "data/RKI_COVID19.csv"
RKI_FILE_NAME = "RKI_COVID19.csv"

# (typ, name, population) population based on Bevölkerungsstatistik mit Stand 31.12.2019
LANDKREISE_LIST = [("LK", "Heinsberg", 255555),
                   ("SK", "Wiesbaden", 278474),
                   ("SK", "Regensburg", 153094),
                   ("LK", "Regensburg", 194070),
                   ("SK", "München", 1471508),
                   ("SK", "Weiden i.d.OPf.", 42743),
                   ("SK", "Leipzig", 593145),
                   ("LK", "Neustadt a.d.Waldnaab", 94450),
                   ("LK", "Tirschenreuth", 72046)]

BUNDESLAENDER_LIST = ["Thüringen",
                      "Sachsen",
                      "Berlin",
                      "Brandenburg",
                      "Bayern",
                      "Nordrhein-Westfalen",
                      "Niedersachsen",
                      "Sachsen-Anhalt",
                      "Hamburg",
                      "Bremen",
                      "Hessen",
                      "Rheinland-Pfalz",
                      "Baden-Württemberg",
                      "Saarland",
                      "Mecklenburg-Vorpommern",
                      "Schleswig-Holstein"]

ALTERSGRUPPE_LIST = [("A00-A04", 3926397), ("A05-A14", 7364418), ("A15-A34", 19213113), ("A35-A59", 29137839),
                     ("A60-A79", 17988340), ("A80+", 5389106)]  # (Age group, estimated population for this age group)

POPULATION_BUNDESLAENDER_URL = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/" \
                               "rest/services/Coronaf%C3%A4lle_in_den_Bundesl%C3%A4ndern/" \
                               "FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"

POPULATION_LANDKREISE_URL = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/" \
                            "FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
