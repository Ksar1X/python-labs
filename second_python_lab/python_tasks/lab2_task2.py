listaGene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                 'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']

genesToFind = ['FGFR4', 'FGERA4']

for gene in genesToFind:
    indices = [i for i, g in enumerate(listaGene1) if g == gene]
    if indices:
        print(f"{gene} has index: {indices}")
    else:
        print(f"{gene} Not in list!")
        

