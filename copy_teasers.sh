#!/bin/bash
# copy_teasers.sh
# Run from the root of nrflynn2.github.io on the al-folio-rebuild branch
# after running: git checkout master -- files/publications images/noahflynn.jpg CNAME
#
# Maps old teaser images from files/publications/*/teaser.* to
# assets/img/publication_preview/ with names matching papers.bib preview fields.

set -e

SRC="files/publications"
DEST="assets/img/publication_preview"

mkdir -p "$DEST"

# --- Existing papers (14 from current site) ---
cp "$SRC/seacrowd_2024/teaser.png"         "$DEST/seacrowd_2024.png"
cp "$SRC/xenoscore_2023/teaser.jpeg"        "$DEST/xenoscore_2023.jpeg"
cp "$SRC/hydroxywarfarin_2022/teaser.png"   "$DEST/hydroxywarfarin_2022.png"
cp "$SRC/calnet_2021/teaser.png"            "$DEST/calnet_2021.png"
cp "$SRC/2021_bromo/teaser.png"             "$DEST/bromo_2021.png"
cp "$SRC/ehr_nsaid_2021/teaser.png"         "$DEST/ehr_nsaid_2021.png"
cp "$SRC/bioact_2021/teaser.jpeg"           "$DEST/bioact_2021.jpeg"
cp "$SRC/meclofenamate_2021/teaser.jpg"     "$DEST/meclofenamate_2021.jpg"
cp "$SRC/meloxicam_2021/teaser.png"         "$DEST/meloxicam_2021.png"
cp "$SRC/metfor_2020/teaser.jpeg"           "$DEST/metfor_2020.jpeg"
cp "$SRC/xenonet_2020/teaser.png"           "$DEST/xenonet_2020.png"
cp "$SRC/meloxicam_2020/teaser.png"         "$DEST/meloxicam_2020.png"
cp "$SRC/tbf_barnette_2019/teaser.png"      "$DEST/tbf_barnette_2019.png"
cp "$SRC/tbf_davis_2019/teaser.png"         "$DEST/tbf_davis_2019.png"

# --- Headshot ---
cp "images/noahflynn.jpg"                   "assets/img/prof_pic.jpg"

echo ""
echo "Done. Copied 14 teaser images to $DEST/"
echo "Copied headshot to assets/img/prof_pic.jpg"
echo ""
echo "Still needed (no existing teaser images — create or add placeholders):"
echo "  $DEST/gencircuit_2026.png"
echo "  $DEST/dreambench_2026.png"
echo "  $DEST/compass_2025.png"
echo "  $DEST/kinase_2025.png"
echo "  $DEST/nova_2024.png"
echo "  $DEST/book_cover.jpg"
echo ""
echo "You can create placeholders with:"
echo "  for f in gencircuit_2026 dreambench_2026 compass_2025 kinase_2025 nova_2024; do"
echo "    cp $DEST/xenonet_2020.png $DEST/\${f}.png"
echo "  done"
