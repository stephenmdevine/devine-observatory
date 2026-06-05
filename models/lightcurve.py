from dataclasses import dataclass

import numpy as np

@dataclass
class LightCurve:
    time: np.ndarray
    flux: np.ndarray
    flux_error: np.ndarray | None = None

    @property
    def length(self) -> int:
        return len(self.time)