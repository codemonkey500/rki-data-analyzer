#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import constants
import logging
import sys
from itertools import cycle

logging.basicConfig(level=logging.INFO)


class RkiDataLandkreise:

    def __init__(self):
        try:
            self.__data = pd.read_csv(os.path.join(os.path.dirname(__file__), constants.RKI_FILE_RELATIV_PATH))
            logging.info(constants.RKI_FILE_NAME + " found! Reading file...")
            logging.info("Dropping unused columns...")
            self.__data.drop(self.__data.columns.difference(["Landkreis", "Meldedatum",
                                                             "AnzahlFall"]), axis=1, inplace=True)

        except IOError as e:
            logging.error("\n" + "\"" + constants.RKI_FILE_NAME + "\"" +
                          " must be stored in the data directory of the current project!")
            sys.exit(e)

    def get_data(self):
        return self.__data

    def plot_c7_per_100k(self):

        df = self.get_data().groupby(by=["Landkreis", "Meldedatum"], sort=True)["AnzahlFall"].sum().reset_index()

        lines = ["-", "--", "dotted"]
        linecycler = cycle(lines)

        months = mdates.MonthLocator()  # every month
        days = mdates.DayLocator()
        formatter = mdates.DateFormatter("%b %Y")

        fig, ax = plt.subplots()

        for tupel in constants.LANDKREISE_LIST:
            landkreis = str(tupel[0] + " " + tupel[1])
            df_landkreis = pd.DataFrame(df[df.Landkreis == landkreis])
            df_landkreis["7Tage"] = self.calculate_c7_per_100k(df_landkreis, tupel)
            df_landkreis.fillna(0)
            ax.plot(pd.to_datetime(df_landkreis["Meldedatum"]),
                    df_landkreis["7Tage"],
                    label=landkreis, linestyle=next(linecycler))

        # format the ticks
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_minor_locator(days)
        ax.xaxis.set_major_formatter(formatter)

        # format the coords message box
        ax.grid(True)

        # Horizontal line to mark the critical 200 incidence
        ax.axhline(y=200, color="r")

        # Horizontal line to mark the goal incidence
        ax.axhline(y=50, color="g")

        # rotates and right aligns the x labels
        fig.autofmt_xdate()
        plt.legend()
        plt.xlabel("Datum")
        plt.ylabel("7-Tage-Inzidenz/100.000 Einw.")
        fig.suptitle("7-Tage-Inzidenz/100.000 Einw. für Landkreise", fontsize=16)
        plt.show()

    @staticmethod
    def calculate_c7_per_100k(df, tupel):
        population = tupel[2]
        return df.iloc[:, 2].rolling(window=7).sum() / population * 100000

    @staticmethod
    def convert_typ(typ):
        output = ""
        if typ == "LK":
            output = "Landkreis"
        elif typ == "SK":
            output = "Kreisfreie Stadt"
        return output
