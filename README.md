# Species Info Collector: A Python Function for Collecting Taxonomic Information based on ete3 package
This repository contains one Python script: taxonomy.py

The function get_taxonomy_info retrieves taxonomy information from NCBI Taxonomy database for a given species. It returns a Pandas DataFrame with columns for the species name, order, family, and subfamily.

The function takes two arguments: the species name as a string and an optional boolean argument update_taxonomy. If update_taxonomy is set to True, the NCBI Taxonomy database will be updated before retrieving the taxonomy information.

The function uses the NCBITaxa module from the ete3 package to retrieve the taxonomy information. It assigns a taxonomic identifier (taxid) for the given species and uses it to get lineage, rank, and name information for the species.

The function then extracts the order, family, and subfamily information from the rank and name information, respectively. If the information is not available, the function sets the value as "Unknown".

Finally, the function creates a dictionary with the taxonomy information for each species and uses it to create a Pandas DataFrame with the species name, order, family, and subfamily as columns. The DataFrame is returned as output.

## Requirements
To ue de taxonomy.py script you need to have Python 3.x installed, along with the following Python modules:

- re
- os
- pandas
