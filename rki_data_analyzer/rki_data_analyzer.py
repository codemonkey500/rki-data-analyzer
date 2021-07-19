#!/usr/bin/env python3

import argparse
import sys
import rki_data_bund
import rki_data_bundeslaender
import rki_data_landkreise

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-bl", help="7-Tage-Inzidenz/100.000 Einw. (Bundeslaender)", action="store_true")
    parser.add_argument("-lk", help="7-Tage-Inzidenz/100.000 Einw. (Landkreise)", action="store_true")
    parser.add_argument("-age", help="7-Tage-Inzidenz/100.000 Einw. in den Altersgruppen (DE)", action="store_true")

    args = parser.parse_args()

    if args.bl:
        data_bundeslaender = rki_data_bundeslaender.RkiDataBundeslaender()
        data_bundeslaender.plot_c7_per_100k()

    elif args.lk:
        data_landkreise = rki_data_landkreise.RkiDataLandkreise()
        data_landkreise.plot_c7_per_100k()

    elif args.age:
        data_age_groups = rki_data_bund.RkiDataBund()
        data_age_groups.plot_incidence_age_groups()
    else:
        parser.print_help(sys.stderr)
