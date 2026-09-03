#!/usr/bin/env python3
"""Generate the MEAP v12 book-map figure for the InfoArk blog post.

matplotlib is not installed system-wide on this machine. Run with the
interpreter that has it:

    /home/noahr/ml-drug-discovery/.venv/bin/python bin/make-meap-v12-figure.py

Writes assets/img/blog/meap-v12/book-map.png at 1800 px wide. The matching
.webp is produced separately with the same ffmpeg settings that
bin/optimize-target-discovery-images uses.

Palette is sampled from assets/img/blog/data-repositories/hero.png so the
figure sits in the same visual family as the existing blog figures.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

CREAM      = "#FAF9F4"
CARD_FILL  = "#E0E8EB"
CARD_EDGE  = "#A8B6C4"
TEAL       = "#306E85"
TEAL_DARK  = "#245B6E"
WARM       = "#F8F1E1"
INK        = "#354252"
MUTED      = "#6B7B8C"
MINT       = "#A8D7DD"

W, H = 1800, 1000

# (label, [title lines], status, tag)
PART1 = [
    ("1",  ["The Drug Discovery Process"],                              "revised", None),
    ("2",  ["Ligand-based Screening:", "Filtering & Similarity Searching"], "revised", None),
    ("3",  ["Ligand-based Screening:", "Machine Learning"],             "revised", "theory to E"),
    ("4",  ["Solubility Deep Dive with", "Linear Models"],              "revised", "theory to E"),
    ("5",  ["Classification: Cytochrome", "P450 Inhibition"],           "revised", None),
    ("6",  ["Small Molecule Binding to", "an RNA Target"],              "revised", None),
    ("7",  ["Unsupervised Learning:", "Repurposing, Curating, Screening"], "revised", None),
]

PART2 = [
    ("8",  ["Introduction to Deep Learning"],                           "revised", None),
    ("9",  ["Structure-based Drug Design", "with Active Learning"],     "revised", "theory to E"),
    ("10", ["Generative Models for", "De Novo Design"],                 "revised", "theory to E"),
    ("11", ["Graph Neural Networks for", "Drug Target Affinity"],       "revised", "theory to E"),
    ("12", ["Transformer Architectures for", "Protein Structure Prediction"], "revised", None),
    ("13", ["Multimodal AI Systems for", "End-to-End Pipelines"],       "revised", "notebook added"),
]

APPX = [
    ("A", ["Glossary"],                              "rebuilt", "107 to 718 entries"),
    ("B", ["Chemical Data Repositories"],            "rebuilt", "19 to 84 resources"),
    ("C", ["Knowledge Distillation"],                "revised", None),
    ("D", ["Protein Structure Prediction", "Deep Dive"], "revised", None),
    ("E", ["Extended Technical Material"],           "new",     "relocated theory"),
    ("F", ["Chapter References"],                    "new",     "202 references"),
    ("G", ["Chapter Exercises"],                     "new",     "87 exercises"),
    ("H", ["Computational Drug Target", "Discovery"], "new",    "21 figures"),
    ("I", ["Diffusion & Flow Matching"],             "new",     "5 notebooks"),
]

STYLE = {
    "new":     dict(face=TEAL,      edge=TEAL_DARK, lw=1.4, text="#FFFFFF", tag="#BFDDE6"),
    "rebuilt": dict(face=WARM,      edge=TEAL,      lw=2.0, text=INK,       tag=TEAL),
    "revised": dict(face=CARD_FILL, edge=CARD_EDGE, lw=1.2, text=INK,       tag=MUTED),
}

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")
fig.patch.set_facecolor(CREAM)
ax.add_patch(plt.Rectangle((0, 0), W, H, color=CREAM, zorder=0))


def card(x, y_top, w, entry):
    label, lines, status, tag = entry
    s = STYLE[status]
    h = 74
    ax.add_patch(FancyBboxPatch(
        (x, y_top - h), w, h,
        boxstyle="round,pad=0,rounding_size=9",
        facecolor=s["face"], edgecolor=s["edge"], linewidth=s["lw"], zorder=2))
    ax.text(x + 26, y_top - h / 2 + 2, label, color=s["text"], fontsize=17,
            fontweight="bold", ha="left", va="center", zorder=3)
    tx = x + 74
    if len(lines) == 1:
        ys = [y_top - h / 2 + 1]
    else:
        ys = [y_top - 28, y_top - 49]
    for ly, line in zip(ys, lines):
        ax.text(tx, ly, line, color=s["text"], fontsize=13.5, ha="left",
                va="center", zorder=3)
    if tag:
        ax.text(x + w - 22, y_top - h / 2 + 1, tag, color=s["tag"], fontsize=10.5,
                style="italic", ha="right", va="center", zorder=3)
    return y_top - h


def column(x, w, heading, sub, entries, y_top):
    ax.text(x, y_top + 46, " ".join(heading), color=INK, fontsize=15, fontweight="bold",
            ha="left", va="center")
    ax.text(x, y_top + 22, sub, color=MUTED, fontsize=11.5, ha="left", va="center")
    ax.plot([x, x + w], [y_top + 6, y_top + 6], color=CARD_EDGE, lw=1.2, zorder=1)
    y = y_top - 8
    for e in entries:
        y = card(x, y, w, e) - 12
    return y


COL_W = 540
XS = [60, 630, 1200]
TOP = 830

ax.text(60, H - 62, "Build AI Drug Discovery Pipelines", color=INK,
        fontsize=27, fontweight="bold", ha="left", va="center")
column(XS[0], COL_W, "PART 1",
       "Fundamentals of cheminformatics and machine learning", PART1, TOP)
column(XS[1], COL_W, "PART 2",
       "Deep learning for molecules and structural biology", PART2, TOP)
y_end = column(XS[2], COL_W, "APPENDICES",
               "Reference material, exercises, and two new deep dives", APPX, TOP)

# legend, placed in the gap under the two chapter columns
LY = 158
items = [
    ("new",     "New in v12"),
    ("rebuilt", "Rebuilt in v12"),
    ("revised", "Revised in v12"),
]
lx = 60
for status, text in items:
    s_ = STYLE[status]
    ax.add_patch(FancyBboxPatch(
        (lx, LY - 13), 30, 26, boxstyle="round,pad=0,rounding_size=6",
        facecolor=s_["face"], edgecolor=s_["edge"], linewidth=s_["lw"], zorder=2))
    ax.text(lx + 42, LY, text, color=INK, fontsize=12.5, ha="left", va="center")
    lx += 42 + len(text) * 8 + 44

out = "assets/img/blog/meap-v12/book-map.png"
os.makedirs(os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=CREAM)
print("wrote", out)

# WebP companion, using the same settings as bin/optimize-target-discovery-images
webp = out.replace(".png", ".webp")
rc = os.system(
    f"ffmpeg -y -i {out} -vf \"scale='min(1800,iw)':-2:flags=lanczos\" "
    f"-c:v libwebp -quality 88 -compression_level 6 {webp} "
    ">/dev/null 2>&1"
)
print("wrote", webp, "(ffmpeg rc=%d)" % rc)
