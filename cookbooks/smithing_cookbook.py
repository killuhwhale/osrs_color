from spaces import Spaces
from recipies import EdgeFurnace, GoToGE
import items
from spaces import Spaces
import meal

''' Define a list of recipies

'''


# item_to_make, items_to_withdraw, space_to_click_to_smelt, smelt_time
# item_to_make = str(Items.SILVER_BAR)
# items_to_withdraw = [Items.SILVER_ORE]
# space_to_click_to_smelt = Spaces.SMELT_BAR_SILVER
# smelt_time = 92  # seconds

'''
A list of tuples, with a tuple == (TaskClass, list(arguments for the class excluding client))

'''

recipie_tasks = [
    (
        EdgeFurnace.EdgeFurnace,
        [
            str(items.Items.BRONZE_BAR),
            [items.Items.TIN_ORE, items.Items.COPPER_ORE],
            Spaces.SMELT_BAR_BRONZE, 49
        ]
    ),
    # (GoToGE.GoToGE, ),
]


COOKBOOK = [
    meal.Meal(recipie_tasks)
    # give some static data
    # r_make_cbs.RECIPIE,   # Client 1 recipie
    # r_tut_island.RECIPIE  # Client 2 recipie
]
