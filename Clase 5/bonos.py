#%%

import csv
import sys
import fileparse as fp
import matplotlib.pyplot as plt
import numpy as np


TVPP = fp.parse_csv('/home/emiliano/Desktop/Curso_UNSAM/bono_data/TVPP.csv',
                    select=["symbol", "date", "time", "open", "high", "low",
                            "close", "volume", "openint"],
                    types=[str, str, str, str, float, float, float, float,
                           float],
                    has_headers=True)

# TVPP = [bono['open'] for bono in TVPP]

TVPA = fp.parse_csv('/home/emiliano/Desktop/Curso_UNSAM/bono_data/TVPA.csv',
                    select=["symbol", "date", "time", "open", "high", "low",
                            "close", "volume", "openint"],
                    types=[str, str, str, str, float, float, float, float,
                           float], has_headers=True)
# TVPA = [bono['open'] for bono in TVPA]
TVPY = fp.parse_csv('/home/emiliano/Desktop/Curso_UNSAM/bono_data/TVPY.csv',
                    select=["symbol", "date", "time", "open", "high", "low",
                            "close", "volume", "openint"],
                    types=[str, str, str, str, float, float, float, float,
                           float], has_headers=True)

# TVPY = [bono['open'] for bono in TVPY]
TVPE = fp.parse_csv('/home/emiliano/Desktop/Curso_UNSAM/bono_data/TVPE.csv',
                    select=["symbol", "date", "time", "open", "high", "low",
                            "close", "volume", "openint"],
                    types=[str, str, str, str, float, float, float, float,
                           float], has_headers=True)

# TVPE = [bono['open'] for bono in TVPE]
DIAS_TVPP = [PP['date'] for PP in TVPP]
DIAS_TVPA = [PA['date'] for PA in TVPA]
DIAS_TVPY = [PY['date'] for PY in TVPY]
DIAS_TVPE = [PE['date'] for PE in TVPE]


DIAS_TVPE_TVPP = set(DIAS_TVPE).intersection(set(DIAS_TVPP))
DIAS_TVPE_TVPA = set(DIAS_TVPE).intersection(set(DIAS_TVPA))
DIAS_TVPE_TVPY = set(DIAS_TVPE).intersection(set(DIAS_TVPY))


CLOSE_TVPP = [PP['close'] for PP in TVPP if PP['date'] in DIAS_TVPE_TVPP]
CLOSE_TVPA = [PA['close'] for PA in TVPA if PA['date'] in DIAS_TVPE_TVPA]
CLOSE_TVPY = [PY['close'] for PY in TVPY if PY['date'] in DIAS_TVPE_TVPY]
CLOSE_TVPE_TVPP = [PE['close'] for PE in TVPE if PE['date'] in DIAS_TVPE_TVPP]
CLOSE_TVPE_TVPA = [PE['close'] for PE in TVPE if PE['date'] in DIAS_TVPE_TVPA]
CLOSE_TVPE_TVPY = [PE['close'] for PE in TVPE if PE['date'] in DIAS_TVPE_TVPY]


# plt.plot(CLOSE_TVPP)

# plt.plot(CLOSE_TVPA)
# plt.plot(CLOSE_TVPY)
# plt.show()

plt.subplot(3, 2, 1)
plt.plot(CLOSE_TVPA, 'r')
plt.plot(CLOSE_TVPE_TVPA, 'k')
plt.legend(['TVPP', 'TVPE'])
plt.subplot(3, 2, 2)
plt.plot(CLOSE_TVPA, CLOSE_TVPE_TVPA, '.')
