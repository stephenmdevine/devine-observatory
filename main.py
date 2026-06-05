from src.acquisition.tess import (
    download_lightcurve
)


def main():

    lc = download_lightcurve("TOI-700")

    print(f"Points: {lc.length}")

    print(f"First time: {lc.time[0]}")
    print(f"First flux: {lc.flux[0]}")


if __name__ == "__main__":
    main()