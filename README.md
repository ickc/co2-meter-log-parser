# Info

Supporting model: [Indoor CO2 Meter, Air Quality Monitor, Data Logger with NDIR Channel Sensor](https://www.amazon.com/dp/B0919CDYQ1). May also support [GZAIR CO2 Data Logger Monitor](https://www.amazon.com/gp/product/B0829ZWQVP) where the former seems to be a white label version of latter one.

# Usage

1.   With CO₂ meter not plugged in a computer (so that the filesystem is not mounted): History > Data Log Table > Save to file
2.   Plug CO₂ meter to computer.
3.   Copy `DATALOG.TXT` to `log`.
4.   CO₂ meter: History > Reset
5.   `make rename` to rename `DATALOG.TXT` automatically.
6.   Run `plot.ipynb` to explore.

Notes: you need to backup the data in the `log` directory yourself. It is git-ignored to not included here.

# Notes on calibration

In menu, choose

1. `Reset CO2 to factory setting`: The menu suggests leaving it to open air for 20 min. before calibration. At calibration, it assumes current level is 400 ppm.
2. `CO2 sensor calibration`: An offset can be configure too. To find your offset, you can check local CO₂ level, such as from these sites:

    - [Daily CO2](https://www.co2.earth/daily-co2)
    - [BEACO2N](http://beacon.berkeley.edu/about/)

3. `Reset` history to throw away data during calibration.
