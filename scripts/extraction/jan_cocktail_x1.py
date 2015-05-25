'''
modifier: 01
'''
def main():
    info("Cocktail Pipette x1")
    gosub('obama:WaitForMiniboneAccess')
    gosub('obama:PrepareForCocktailShot')
    gosub('common:EvacPipette1')
    gosub('common:FillPipette1')
    gosub('obama:PrepareForCocktailShotExpansion')
    gosub('common:ExpandPipette1')
    close(description='Outer Pipette 1')
