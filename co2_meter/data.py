from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

import numpy as np
import pandas as pd


@dataclass
class Data:
    dataframe: pd.DataFrame
    units: tuple[str, str, str]
    columns: ClassVar[tuple[str, str, str]] = ("CO2", "Tempature", "Humidity")

    @classmethod
    def from_file(cls, path: Path) -> Data:
        with path.open() as f:
            raw = list(csv.reader(f))

        assert raw[0] == [" Date", " Time", " CO2", " Temp", " RH"]

        n = len(raw) - 1
        co2 = np.empty(n, dtype=np.int16)
        temp = np.empty(n, dtype=np.int8)
        rh = np.empty(n, dtype=np.int8)

        temp_unit = raw[1][4]
        dt_str: list[str] = []
        for i, row in enumerate(raw[1:]):
            assert len(row) == 6
            assert row[4] == temp_unit
            dt_str.append("".join((row[0].replace("/", "-"), "T", row[1])))
            co2[i] = int(row[2])
            temp[i] = int(row[3])
            assert row[5][-1] == "%"
            rh[i] = int(row[5][:-1])

        dt = np.array(dt_str, dtype=np.datetime64)

        units = ("ppm", temp_unit.replace("'", "º"), r"%")

        df = pd.DataFrame(
            {
                f"{col} ({unit})": value
                for col, unit, value in zip(cls.columns, units, (co2, temp, rh))
            },
            index=dt,
        )
        assert df.index.is_monotonic_decreasing
        return Data(
            df,
            units,
        )

    @classmethod
    def from_dir(cls, directory: Path, ext: str = "csv") -> Data:
        datas = [
            Data.from_file(path)
            for path in sorted(directory.glob(f"*.{ext}"), reverse=True)
        ]
        units = datas[0].units
        dfs = []
        for data in datas:
            assert data.units == units
            dfs.append(data.dataframe)
        df = pd.concat(dfs, axis=0)
        assert df.index.is_monotonic_decreasing
        return Data(df, units)

    @property
    def duration(self) -> pd.Timedelta:
        return self.dataframe.index[-1] - self.dataframe.index[0]

    @property
    def start_time(self) -> str:
        return self.strftime(self.dataframe.index[0])

    @property
    def end_time(self) -> str:
        return self.strftime(self.dataframe.index[-1])

    @staticmethod
    def strftime(dt: np.datetime64) -> str:
        return dt.strftime("%Y%m%d_%H%M")

    def rename_file(self, path: Path) -> None:
        parent = path.parent
        name = f"{self.start_time}-{self.end_time}.csv"
        path.rename(parent / name)

    def plot(self, *args, **kwargs):
        return self.dataframe.plot(*args, **kwargs)
