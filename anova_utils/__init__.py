"""EFA Utilities (efa_utils)
Custom utility functions for conducting ANOVAs (or ANCOVAs).

Functions:
turkey_outliers: Function to identify outliers using the Tukey method.
qqs_over_groups_and_vars: Function to plot QQ subplots for each variable in a list of variables, over groups in a categorical variable.
check_homoscedacity: Function to check for homoscedacity using heuristics recommended by Blanca et al. (2018).
"""

from anova_utils.anova_utils_functions import