# Info

Supporting model: [Indoor CO2 Meter, Air Quality Monitor, Data Logger with NDIR Channel Sensor](https://www.amazon.com/dp/B0919CDYQ1). May also support [GZAIR CO2 Data Logger Monitor](https://www.amazon.com/gp/product/B0829ZWQVP) where the former seems to be a white label version of latter one.

# Usage

-   CO~2~ meter: History > Data Log Table > Save to file
-   Plug CO~2~ meter to computer.
-   Copy `DATALOG.TXT` to `log`.
-   CO~2~ meter: History > Reset
-   `make rename` to rename `DATALOG.TXT` automatically.
-   Run `plot.ipynb` to explore.

Notes: you need to backup the data in the `log` directory yourself. It is git-ignored to not included here.
