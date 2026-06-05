from lightkurve import search_lightcurve

from models.lightcurve import LightCurve


def download_lightcurve(target: str) -> LightCurve:

    result = search_lightcurve(
        target,
        mission="TESS"
    )

    if len(result) == 0:
        raise ValueError(
            f"No TESS observations found for '{target}'"
        )
    
    lc = result.download()

    return LightCurve(
        time=lc.time.value,
        flux=lc.flux.value,
        flux_error=lc.flux_err.value
        if lc.flux_err is not None
        else None
    )