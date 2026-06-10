import matplotlib.pyplot as plt


def plot_lightcurve(lightcurve):

    plt.figure(figsize=(10, 5))

    plt.plot(
        lightcurve.time,
        lightcurve.flux,
        ".",
        markersize=1
    )

    plt.xlabel("Time")
    plt.ylabel("Flux")

    plt.title("Raw Light Curve")

    plt.show()