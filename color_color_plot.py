
# JWST COSMOS-Web color–color diagram
# Figure 2 style


from astropy.io import fits
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt


# Global plot style
plt.rcParams.update({
    "font.size": 11,
    "axes.linewidth": 1.0,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.size": 4,
    "ytick.major.size": 4,
    "font.family": "serif"
})


# Load catalog

catalog_path = "../data/raw/COSMOSWeb_mastercatalog_v1.fits"

with fits.open(catalog_path) as hdul:
    data = hdul[1].data


# Extract magnitudes (AB)

f115 = data["mag_model_f115w"]
f277 = data["mag_model_f277w"]
f444 = data["mag_model_f444w"]


# Sanity filtering

valid = (
    np.isfinite(f115) &
    np.isfinite(f277) &
    np.isfinite(f444) &
    (f115 > 0) & (f115 < 35) &
    (f277 > 0) & (f277 < 35) &
    (f444 > 0) & (f444 < 35)
)

f115 = f115[valid]
f277 = f277[valid]
f444 = f444[valid]
data_clean = data[valid]


# Colours

x = f277 - f444
y = f115 - f277


# Brown dwarf colour selection

bd_mask = (x > 0.9) & (y + 1.0 < x)

print("Number of brown dwarf candidates:", bd_mask.sum())


# Save candidates

Table(data_clean[bd_mask]).write(
    "../output/brown_dwarf_candidates.fits",
    overwrite=True
)


# Plot

fig, ax = plt.subplots(figsize=(5.8, 5.8))




hb = ax.hexbin(
    x,
    y,
    gridsize=170,        
    bins="log",
    cmap="Greys",
    mincnt=1,
    linewidths=0,
    zorder=1
)



ax.scatter(
    x[bd_mask],
    y[bd_mask],
    s=20,               
    marker="o",
    color="#d62728",
    edgecolor="white",
    linewidth=0.25,
    alpha=0.95,
    zorder=5,
    label="BD candidates"
)


# Selection boundaries

x_line = np.linspace(0.0, 5.2, 500)

ax.axvline(
    0.9,
    color="black",
    linestyle="--",
    linewidth=0.9,
    label="Colour criteria"
)

ax.plot(
    x_line,
    x_line - 1.0,
    color="black",
    linestyle="--",
    linewidth=0.9
)


# Axes, limits, labels 

ax.set_xlabel("F277W − F444W (AB mag)")
ax.set_ylabel("F115W − F277W (AB mag)")

ax.set_xlim(-0.1, 5.2)     # slight zoom-out
ax.set_ylim(-3.2, 1.1)     # slight zoom-out

ax.grid(False)


# Legend 

leg = ax.legend(
    loc="upper right",
    fontsize=10,
    frameon=True,
    handlelength=1.6,
    borderpad=0.6
)

leg.get_frame().set_facecolor("0.9")
leg.get_frame().set_edgecolor("0.5")
leg.get_frame().set_linewidth(0.8)
leg.get_frame().set_alpha(0.95)


# Caption 

fig.text(
    0.5, -0.15,
    "Figure 1. F277W − F444W versus F115W − F277W colour–colour diagram for sources in the JWST COSMOS-Web field.\n"
    "Grey hexagonal bins show the distribution of all detected sources in the survey area.\n"
    "Red circles indicate brown dwarf candidates selected using the colour criteria F277W − F444W > 0.9 and F115W − F277W + 1 < F277W − F444W.\n"
    "These colour cuts are designed to isolate objects with strong 2.7 µm H₂O and CH₄ absorption features characteristic of cool brown dwarfs.",
    ha="center",
    fontsize=10
)


# Save

plt.tight_layout()
plt.savefig(
    "../figures/figure2_like_color_color.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

