import os
import pandas as pd
from ete3 import NCBITaxa

def get_taxonomy_info(species: list, update_taxonomy: bool = False):
 """
    Get taxonomy information for a list of species.

    Parameters
    ----------
    species : list
        List of species to retrieve information. Species names should match
        those present in the NCBI Taxonomy database.
    update_taxonomy : bool, optional
        If True, the NCBI Taxonomy database will be updated before retrieving
        information. Defaults to False.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the following columns:
        'Specie': name of the species
        'Order': order name of the species
        'Family': family name of the species
        'Subfamily': subfamily name of the species
    """
    
    ncbi = NCBITaxa()
    
    if update_taxonomy:
        ncbi.update_taxonomy_database()

    # atribuindo taxid para cada espécies
    taxid = ncbi.get_name_translator(species)

    # código
    lineage = [ncbi.get_lineage_translator(i) for i in taxid.values()]

    # rank
    rank = [ncbi.get_rank(ncbi.get_lineage(i[0])) for i in taxid.values()]

    # nome comum
    name = [ncbi.get_taxid_translator(ncbi.get_lineage(i[0])) for i in taxid.values()]

    order  = []
    family = []
    subfamily = []
    order_name  = []
    family_name = []
    subfamily_name = []
    specie = [k for k,v in taxid.items()]
    dicio = {}

    for i in range(len(taxid)):

        order.append([k for k,v in rank[i].items() if v == 'order'])
        family.append([k for k,v in rank[i].items() if v == 'family'])
        subfamily.append([k for k,v in rank[i].items() if v == 'subfamily'])

        if order[i] == []:
            order[i] = ['Unknow']

        if family[i] == []:
            family[i] = ['Unknow']
        
        if subfamily[i] == []:
            subfamily[i] = ['Unknow']

        order_name.append([v for k,v in name[i].items() if k == order[i][0]])
        family_name.append([v for k,v in name[i].items() if k == family[i][0]])
        subfamily_name.append([v for k,v in name[i].items() if k == subfamily[i][0]])


        if order_name[i] == []:
            order_name[i] = ['Unknow']

        if family_name[i] == []:
            family_name[i] = ['Unknow']
        
        if subfamily_name[i] == []:
            subfamily_name[i] = ['Unknow']

        dicio[specie[i]] = [order_name[i][0],family_name[i][0],subfamily_name[i][0]]
        
    df = pd.DataFrame({'Specie': specie,
                       'Order': [v[0] for k,v in dicio.items()],
                       'Family': [v[1] for k,v in dicio.items()],
                       'Subfamily': [v[2] for k,v in dicio.items()]})
    
    return df