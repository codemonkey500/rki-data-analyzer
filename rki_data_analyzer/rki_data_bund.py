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


class RkiDataBund:

    def __init__(self):
        try:
            self.__data = pd.read_csv(os.path.join(os.path.dirname(__file__), constants.RKI_FILE_RELATIV_PATH))
            logging.info(constants.RKI_FILE_NAME + " found! Reading file...")
            logging.info("Dropping unused columns...")
            self.__data.drop(self.__data.columns.difference(["Bundesland", "Meldedatum",
                                                             "AnzahlFall", "Altersgruppe",
                                                             "AnzahlTodesfall",
                                                             "NeuerTodesfall"]), axis=1, inplace=True)

        except IOError as e:
            logging.error("\n" + "\"" + constants.RKI_FILE_NAME + "\"" +
                          " must be stored in the data directory of the current project!")
            sys.exit(e)

    def get_data(self):
        return self.__data

    def plot_incidence_age_groups(self):

        df = self.get_data().groupby(by=["Altersgruppe", "Meldedatum"], sort=True)["AnzahlFall"].sum().reset_index()
        df.drop(df[df["Altersgruppe"] == "unbekannt"].index, inplace=True)

        lines = ["-", "dashdot", "--"]
        linecycler = cycle(lines)

        months = mdates.MonthLocator()  # every month
        days = mdates.DayLocator()
        formatter = mdates.DateFormatter("%b %Y")

        fig, ax = plt.subplots()

        for altersgruppe in constants.ALTERSGRUPPE_LIST:
            df_ak = pd.DataFrame(df[df.Altersgruppe == altersgruppe[0]])
            df_ak["7Tage"] = df_ak.iloc[:, 2].rolling(window=7).sum() / altersgruppe[1] * 100000
            df_ak.fillna(0)
            ax.plot(pd.to_datetime(df_ak["Meldedatum"]),
                    df_ak["7Tage"],
                    label=altersgruppe[0], linestyle=next(linecycler))

        # format the ticks
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_minor_locator(days)
        ax.xaxis.set_major_formatter(formatter)

        # format the coords message box
        # ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        ax.grid(True)

        # rotates and right aligns the x labels
        fig.autofmt_xdate()
        plt.legend()
        plt.xlabel("Datum")
        plt.ylabel("7-Tage-Inzidenz/100.000 Einw.")
        fig.suptitle("7-Tage-Inzidenz der Altersgruppen", fontsize=16)
        plt.show()
