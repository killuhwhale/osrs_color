# from recipies.<new_file> import RECIPIES as <New letter>
from recipies.r_make_cbs import RECIPIES as A
from recipies.r_tut_island import RECIPIES as B


ALL_RECIPIES = {}


def get_all_recipies():
    ALL_RECIPIES.update(A)
    ALL_RECIPIES.update(B)
    # ALL_RECIPIES.update(<Add Imported Here>)

    return ALL_RECIPIES
