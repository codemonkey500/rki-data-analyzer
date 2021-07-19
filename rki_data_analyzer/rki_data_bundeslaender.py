#!/usr/bin/env python3

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import constants
import logging
import sys
from itertools import cycle
import requests

logging.basicConfig(level=logging.INFO)


class RkiDataBundeslaender:

    def __init__(self):
        try:
            self.__data = pd.read_csv(os.path.join(os.path.dirname(__file__), constants.RKI_FILE_RELATIV_PATH))
            logging.info(constants.RKI_FILE_NAME + " found! Reading file...")
            logging.info("Dropping unused columns...")
            self.__data.drop(self.__data.columns.difference(["Bundesland", "Meldedatum",
                                                             "AnzahlFall", "Altersgruppe",
                                                             "AnzahlTodesfall"]), axis=1, inplace=True)
            logging.info("Downloading population data from RKI...")
            self.__population = self.download_population_data(constants.POPULATION_BUNDESLAENDER_URL)

        except IOError as e:
            logging.error("\n" + "\"" + constants.RKI_FILE_NAME + "\"" +
                          " must be stored in the data directory of the current project!")
            sys.exit(e)

    def get_data(self):
        return self.__data

    def get_population_data(self):
        return self.__population

    def plot_c7_per_100k(self):

        df = self.get_data().groupby(by=["Bundesland", "Meldedatum"], sort=True)["AnzahlFall"].sum().reset_index()

        lines = ["-", "--", "dotted"]
        linecycler = cycle(lines)

        months = mdates.MonthLocator()  # every month
        days = mdates.DayLocator()
        formatter = mdates.DateFormatter("%b %Y")

        fig, ax = plt.subplots()

        for bundesland in constants.BUNDESLAENDER_LIST:
            df_bundesland = pd.DataFrame(df[df.Bundesland == bundesland])
            df_bundesland["7Tage"] = self.calculate_c7_per_100k(df_bundesland, bundesland)
            df_bundesland.fillna(0)
            ax.plot(pd.to_datetime(df_bundesland["Meldedatum"]),
                    df_bundesland["7Tage"],
                    label=bundesland, linestyle=next(linecycler))

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
        fig.suptitle("7-Tage-Inzidenz/100.000 Einw. der Bundesländer", fontsize=16)
        plt.show()

    def calculate_c7_per_100k(self, df, bundesland):
        df_population = self.get_population_data()
        population = df_population[df_population["attributes.LAN_ew_GEN"] == bundesland].iloc[0, 1]
        return df.iloc[:, 2].rolling(window=7).sum() / population * 100000

    @staticmethod
    def download_population_data(url):
        try:
            response = requests.get(url, verify=True)
            data = json.loads(response.content)
            df = pd.json_normalize(data["features"])
            df.drop(df.columns.difference(["attributes.LAN_ew_EWZ", "attributes.LAN_ew_GEN"]), 1, inplace=True)
            logging.info("Dropping unused columns...")
            return df

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
