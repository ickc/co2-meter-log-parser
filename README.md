# Info

Supporting model: [Indoor CO2 Meter, Air Quality Monitor, Data Logger with NDIR Channel Sensor](https://www.amazon.com/dp/B0919CDYQ1). May also support [GZAIR CO2 Data Logger Monitor](https://www.amazon.com/gp/product/B0829ZWQVP) where the former seems to be a white label version of latter one.

# Usage

-   With CO~2~ meter not plugged in a computer (so that the filesystem is not mounted): History > Data Log Table > Save to file
-   Plug CO~2~ meter to computer.
-   Copy `DATALOG.TXT` to `log`.
-   CO~2~ meter: History > Reset
-   `make rename` to rename `DATALOG.TXT` automatically.
-   Run `plot.ipynb` to explore.

Notes: you need to backup the data in the `log` directory yourself. It is git-ignored to not included here.

# Notes on calibration

The menu suggests leaving it to open air for 20 min. before calibration.

At calibration, it assumes current level is 400 ppm.

An offset can be configure too. To find your offset, you can check local CO~2~ level, such as from these sites:

* [Daily CO2](https://www.co2.earth/daily-co2)
* [BEACO2N](http://beacon.berkeley.edu/about/)
