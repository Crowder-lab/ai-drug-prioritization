# -------------------------------------------------------------------------

# Using R with the 2022 National Ambulatory Medical Care Survey Health Center
# (NAMCS HC) Component Public Use Data File
#
# Please follow the steps below to load the 2022 NAMCS HC Component public use
# data file into R.
#
# 1. Create a new folder on your local workstation, for example, C:\namcshc2022.
#
# 2. Download the namcshc2022_r.rds file from the website and save to the folder
# C:\namcshc2022.
#
# Please note that this program will replace the dataset in the default
# directory, if one is present.
#
# For details and guidance on how to properly conduct statistical analyses
# with these data, including the appropriate use of weights to create
# nationally representative estimates, please refer to the technical
# documentation that accompanies the 2022 NAMCS Health Center Component.
#
# For any questions, suggestions, or comments concerning NAMCS HC Component data
# please contact the Division of Health Care Statistics at ambcare@cdc.gov.

# -------------------------------------------------------------------------

# Install and Load Packages
library("tidyverse")

# Read in NAMCS HC 2022  Public Use File R Dataset
namcshc2022 <- read_rds("namcshc2022_r.rds")

# Display Contents of Data File
names(namcshc2022)
