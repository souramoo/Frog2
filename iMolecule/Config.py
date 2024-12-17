"""
   This software is part of Frog, a chemo informatics class able to build 
   3D coordinates for small compounds
    Copyright (C) 2006-2007 P. Tuffery, B.O. Villoutreix, Th. Bohme Leite, D. Gomes, M. Miteva, J. Chomilier

    Frog2 (C) 2009-2010 by P. Tuffery, M. Miteva, F. Guyon

    Using this software, please cite:
        Frog2: Efficient 3D conformation ensemble generator for small compounds.
        Miteva MA, Guyon F, Tuffery P.
        Nucleic Acids Res. 2010 Jul;38(Web Server issue):W622-7. Epub 2010 May 5.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# The root of the distribution
FROGHOME = "/data/lib/Frog2"
FROGHOME = "/home/coder/Frog2/"

# could superseded by e.g. :
# FROGHOME = "/home/wrk/Frog/Frog/iMoleculeDist/"

# The path to the ring library
# End that one by a /
LIBRARY_PATH = FROGHOME+"/librairieNEW/"

# BABEL_PATH =  FROGHOME+"/openbabel-2.0.2/src/babel" # path to Babel 2.0.2
# BABEL_PATH =  FROGHOME+"/bin/babel" # path to Babel 2.0.2
# BABEL_PATH =  "/data/lib/openbabel2.2.3/bin/babel"
BABEL_PATH =  FROGHOME+"/openbabel2.3-install/bin/babel" # path to Babel 2.3.0
# BABEL_PATH =  FROGHOME+"/bin/babel" # path to Babel 2.3.0

# Babel version MUST BE CORRECT.
# DO NOT PUT LETTERS. JUST CONSIDER "2.3.0", NOT "2.3.0a23".
# DO NOT PUT JUST "2.3" or "2".  DO SPECIFY: "2.3.0", i.e. 3 numbers, 2 dots
BABEL_VERSION = "2.3.0" 
# BABEL_VERSION = "2.0.2" 

# DO NOT REMOVE NEXT LINE
# Frog will take the 2.3.0 and put as an int so as to get a comparision for versions
BABEL_VERSION = int(BABEL_VERSION.replace(".",""))


# Path to pymol to generate images on the fly
PYMOL="/usr/local/bin/pymol"

# From here you should not touch anything

ANCILLARY_PATH = FROGHOME+"/iMolecule/code_c"

MONOCONF  = ANCILLARY_PATH+"/monoconfV2"
MONOCONFv2  = ANCILLARY_PATH+"/monoconfV3"
MULTICONF_EXPLORE_SOME = ANCILLARY_PATH+"/multiconfV2_ReducedExploration"
MULTICONF_EXPLORE_ALL = ANCILLARY_PATH+"/multiconfV2_CompleteExploration"
CLUSTCMD = ANCILLARY_PATH+"/mol2clusterize"

AMMOSHOME =  FROGHOME+"/AMMOS"
DGAMMOSHOME = FROGHOME+"/AMMOS/DG-AMMOS"
AMMOSBUILD = DGAMMOSHOME+"/bin/dg-ammos.py"
AMMOSMINIHOME = AMMOSHOME+"/AMMOS_mac_linux_chimera_Dec2008_onVLS3D/AMMOS_SmallMol"
AMMOSMINI  = AMMOSMINIHOME+"/bin/AMMOS_SmallMol_sp4.py"
AMMOSQUICKMINI  = AMMOSMINIHOME+"/bin/AMMOS_SmallMol_quickrefine.py"
AMMOSENE   = AMMOSMINIHOME+"/bin/AMMOS_SmallMol_ene.py"
# AMMOS MINIMISATION PARAMETERS ARE IN: AMMOSMINIHOME/progs/vls_min/min_ligand.ammp
# See: cngdel 500 0 0.015; -> cngdel 250 0 0.015

MAXWARNRINGSIZE = 25      # Size of rings Frog is likely not to gener properly
MAXWARNRINGAROMATIC = 20  # Minimal aromatic atoms for rings Frog is likely not to gener properly

