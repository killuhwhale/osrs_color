from enum import Enum

from utils import Constant


def grid(r, c, x, y, w, h, mx, my):
    ans = []
    for col in range(c):
        column = []
        for row in range(r):
            column.append([x + (col * mx), y + (row * my),
                           x + (col * mx) + w, y + (row * my) + h])
        ans.append(column)
    return ans


class DEFAULT_SPACES:

    INV = 1
    ROW_1 = 2
    ROW_2 = 3
    ROW_3 = 4
    ROW_4 = 5
    ROW_5 = 6
    ROW_6 = 7
    ROW_7 = 8
    COL_1 = 9
    COL_2 = 10
    COL_3 = 11
    COL_4 = 12
    N_A = 13   # North A (closer to player)
    N_B = 14   # North B (outside North A)
    E_A = 15
    E_B = 16
    S_A = 17
    S_B = 18
    W_A = 19
    W_B = 20
    INTF_HP = 21
    INTF_PRAYER = 22
    INTF_RUN = 23
    INTF_SPECIAL = 24
    SKILL_ATT = 25
    SKILL_STR = 26
    SKILL_DEF = 27
    SKILL_RNG = 28
    SKILL_PRY = 29
    SKILL_MAG = 30
    SKILL_RC = 31
    SKILL_CON = 32
    SKILL_HP = 33
    SKILL_AGL = 34
    SKILL_HRB = 35
    SKILL_THV = 36
    SKILL_CRA = 37
    SKILL_FLT = 38
    SKILL_SLA = 39
    SKILL_HUN = 40
    SKILL_MIN = 41
    SKILL_SMT = 42
    SKILL_FSH = 43
    SKILL_CK = 44
    SKILL_FMA = 45
    SKILL_WC = 46
    SKILL_FRM = 47
    SKILL_TLVL = 48
    PANEL_COMBAT = 49
    PANEL_SKILLS = 50
    PANEL_QUESTS = 51
    PANEL_INV = 52
    PANEL_GEAR = 53
    PANEL_PRAYER = 54
    PANEL_MAGIC = 55
    PANEL_CHAT = 56
    PANEL_FRIENDS = 57
    PANEL_ACCOUNT = 58
    PANEL_LOGOUT = 59
    PANEL_SETTINGS = 60
    PANEL_EMOTES = 61
    PANEL_MUSIC = 62

    PRAYER_DEF_5 = 63
    PRAYER_DEF_10 = 64
    PRAYER_PRO_ITEM = 65
    PRAYER_ATT_15 = 66
    PRAYER_MAG_15 = 67
    PRAYER_CHIV = 68
    PRAYER_STR_5 = 69
    PRAYER_STR_10 = 70
    PRAYER_RNG_10 = 71
    PRAYER_PRO_MAGE = 72
    PRAYER_RETRIBUTION = 73
    PRAYER_PIETY = 74
    PRAYER_ATT_5 = 75
    PRAYER_ATT_10 = 76
    PRAYER_MAG_10 = 77
    PRAYER_PRO_RNG = 78
    PRAYER_REDEMP = 79
    PRAYER_RIGOUR = 80
    PRAYER_RNG_5 = 81
    PRAYER_RAP_REST = 82
    PRAYER_DEF_15 = 83
    PRAYER_PRO_MELEE = 84
    PRAYER_SMITE = 85
    PRAYER_AUGURY = 86
    PRAYER_MAG_5 = 87
    PRAYER_RAP_HEAL = 88
    PRAYER_STR_15 = 89
    PRAYER_RNG_15 = 90
    PRAYER_PRESERVE = 91
    PRAYER_BLANK = 92

    MAGIC_HOME_TELE = 93
    MAGIC_WEAKEN = 94
    MAGIC_WATER_BOLT = 95
    MAGIC_FALLY_TELE = 96
    MAGIC_ENCHANT3 = 97
    MAGIC_CHARGE_WATER_ORB = 98
    MAGIC_CLAWS_GUTHIX = 99
    MAGIC_CHARGE_AIR_ORB = 100
    MAGIC_FIRE_WAVE = 101
    MAGIC_TELE_BLOCK = 102
    MAGIC_WIND_STK = 103
    MAGIC_FIRE_STK = 104
    MAGIC_VARROCK_TELE = 105
    MAGIC_CRUMBLE_UNDEAD = 106
    MAGIC_IBAN_BLAST = 107
    MAGIC_ENCHANT4 = 108
    MAGIC_FLAMES_ZAMMY = 109
    MAGIC_VULNER = 110
    MAGIC_ENTANGLE = 111
    MAGIC_TELE_2_TARGET = 112
    MAGIC_CONFUSE = 113
    MAGIC_BONES_2_BAN = 114
    MAGIC_ENCHANT2 = 115
    MAGIC_HOUSE_TELE = 116
    MAGIC_SNARE = 117
    MAGIC_WATCHTOWER_TELE = 118
    MAGIC_TROLLHEIM_TELE = 119
    MAGIC_ENChANT5 = 120
    MAGIC_STUN = 121
    MAGIC_ENCHANT6 = 122
    MAGIC_ENCHANT_CB = 123
    MAGIC__WIND_BOLT = 124
    MAGIC_EARTH_BOLT = 125
    MAGIC_WIND_BLAST = 126
    MAGIC_MAGIC_DART = 127
    MAGIC_FIRE_BLAST = 128
    MAGIC_WIND_WAVE = 129
    MAGIC_KOUREND_CASTLE = 130
    MAGIC_CHARGE = 131
    MAGIC_CAMMY_TELEOTHER = 132
    MAGIC_WATER_STK = 133
    MAGIC_CURSE = 134
    MAGIC_LUMBY_TELE = 135
    MAGIC_SUPERHEAT = 136
    MAGIC_ARDY_TELE = 137
    MAGIC_CHARGE_EARTH_ORB = 138
    MAGIC_CHARGE_FIRE_ORB = 139
    MAGIC_EARTH_WAVE = 140
    MAGIC_WIND_SURGE = 141
    MAGIC_EARTH_SURGE = 142
    MAGIC_ENCHANT1 = 143
    MAGIC_BIND = 144
    MAGIC_TELE_GRAB = 145
    MAGIC_CAMMY_TELE = 146
    MAGIC_EARTH_BLAST = 147
    MAGIC_BONES_2_PEACH = 148
    MAGIC_APEATOLL_TELE = 149
    MAGIC_ENFEEBLE = 150
    MAGIC_FALLY_TELEOTHER = 151
    MAGIC_ENCHANT7 = 152
    MAGIC_EARTH_STK = 153
    MAGIC_LOW_ALCH = 154
    MAGIC_FIRE_BOLT = 155
    MAGIC_WATER_BLAST = 156
    MAGIC_HIGH_ALCH = 157
    MAGIC_SARA_STK = 158
    MAGIC_WATER_WAVE = 159
    MAGIC_LUMBY_TELEOTHER = 160
    MAGIC_WATER_SURGE = 161
    MAGIC_FIRE_SURGE = 162

    GEAR_HEAD = 163
    GEAR_CAPE = 164
    GEAR_NECK = 165
    GEAR_QUIVER = 166
    GEAR_WEAPON = 167
    GEAR_BODY = 168
    GEAR_SHIELD = 169
    GEAR_LEGS = 170
    GEAR_GLOVES = 171
    GEAR_BOOTS = 172
    GEAR_RING = 173

    COMBAT_QUAD_1 = 174
    COMBAT_QUAD_2 = 175
    COMBAT_QUAD_3 = 176
    COMBAT_QUAD_4 = 177
    COMBAT_COL_1 = 178
    COMBAT_COL_2 = 179
    COMBAT_COL_3 = 180
    COMBAT_RETALIATE = 181

    COMBAT_SPELL_WIND_STK = 182
    COMBAT_SPELL_WIND_BOLT = 183
    COMBAT_SPELL_WIND_BLAST = 184
    COMBAT_SPELL_WIND_WAVE = 185
    COMBAT_SPELL_WIND_SURGE = 186
    COMBAT_SPELL_EARTH_STK = 187
    COMBAT_SPELL_EARTH_BOLT = 188
    COMBAT_SPELL_EARTH_BLAST = 189
    COMBAT_SPELL_EARTH_WAVE = 190
    COMBAT_SPELL_EARTH_SURGE = 191
    COMBAT_SPELL_WATER_STK = 192
    COMBAT_SPELL_WATER_BOLT = 193
    COMBAT_SPELL_WATER_BLAST = 194
    COMBAT_SPELL_WATER_WAVE = 195
    COMBAT_SPELL_WATER_SURGE = 196
    COMBAT_SPELL_FIRE_STK = 197
    COMBAT_SPELL_FIRE_BOLT = 198
    COMBAT_SPELL_FIRE_BLAST = 199
    COMBAT_SPELL_FIRE_WAVE = 200
    COMBAT_SPELL_FIRE_SURGE = 201

    GEAR_EQUIPMENT = 202
    GEAR_VALUE = 203
    GEAR_DEATH = 204
    GEAR_FOLLOWER = 205

    GEAR_EQUIPMENT_CLOSE = 206
    GEAR_VALUE_CLOSE = 207
    GEAR_DEATH_CLOSE = 208
    CHAT_HEAD = 209
    CHAT_HEAD_RIGHT = 210

    PLAYER_CENTER_SM = 211
    PLAYER_CENTER_MED = 212
    PLAYER_CENTER_LG = 213

    TUT_ISLAND_MINI_MAP_FISH_SPOT = 214

    NORTH = 215
    EAST = 216
    SOUTH = 217
    WEST = 218

    RESET_MAP = 219
    CLICK_HERE_TO_CONTINUE = 220

    SMELT_BAR_BRONZE = 223
    SMELT_BAR_IRON = 224
    SMELT_BAR_SILVER = 225
    SMELT_BAR_STEEL = 226
    SMELT_BAR_GOLD = 227
    SMELT_BAR_MITH = 228
    SMELT_BAR_ADAM = 229
    SMELT_BAR_RUNE = 230

    CLOSE_BANK = 221
    BANK_DEPOSIT_INV = 222
    BANK_TAB_ALL = 231
    BANK_TAB_1 = 232
    BANK_TAB_2 = 233
    BANK_TAB_3 = 234
    BANK_TAB_4 = 235
    BANK_TAB_5 = 236
    BANK_TAB_6 = 237
    BANK_TAB_7 = 238
    BANK_TAB_8 = 239
    BANK_TAB_9 = 240

    BANK_DEPOSIT_WORN_ITEMS = 241
    GE_HISTORY = 242
    CONTINUE = 243
    LOGIN_EXISTING_USER = 244
    LOGIN_LOGIN = 245

    '''
    
    
    
    
        Coords
    '''

   # Example of how to use grid. Manually find each var and plug in to the grid() method.
    SKILL_WIDTH = Constant(50)
    SKILL_HEIGHT = Constant(20)
    BASE_SKILL_X = Constant(555)
    BASE_SKILL_Y = Constant(211)
    SK_VT_MG = Constant(32)  # Skill vertical margin
    SK_HZ_MG = Constant(64)
    skills_grid = grid(8, 3, BASE_SKILL_X, BASE_SKILL_Y,
                       SKILL_WIDTH, SKILL_HEIGHT, SK_HZ_MG, SK_VT_MG)
    # Panels inv, prayer, magic, etc...
    panels_top_grid = grid(1, 7, 530, 176, 32, 20, 32, 1)
    panels_bottom_grid = grid(1, 7, 530, 473, 32, 20, 32, 1)
    prayer_grid = grid(6, 5, 551, 212, 33, 33, 37, 37)
    magic_grid = grid(10, 7, 552, 203, 23, 23, 26, 24)
    # Combat spells from combat menu (when staff equipped)
    combat_spells_grid = grid(5, 4, 570, 216,  23, 23, 41, 31)

    SPACES = {

        INV: [560, 210, 725, 465],
        ROW_1: [560, 210, 725, 250],
        ROW_2: [560, 245, 725, 285],  # h = 40
        ROW_3: [560, 280, 725, 320],
        ROW_4: [560, 315, 725, 355],
        ROW_5: [560, 350, 725, 390],
        ROW_6: [560, 385, 725, 425],
        ROW_7: [560, 425, 725, 465],
        COL_1: [560, 210, 600, 465],  # w = 40
        COL_2: [600, 210, 640, 465],
        COL_3: [642, 210, 683, 465],
        COL_4: [685, 210, 725, 465],
        N_A: [18, 87, 498, 167],
        N_B: [18, 7, 498, 87],
        E_A: [258, 7, 378, 327],
        E_B: [378, 7, 498, 327],
        S_A: [18, 167, 498, 247],
        S_B: [18, 247, 498, 327],
        W_A: [138, 7, 258, 327],
        W_B: [18, 7, 138, 327],

        INTF_HP: [520, 49, 540, 69],
        INTF_PRAYER: [520, 83, 540, 103],
        INTF_RUN: [530, 115, 550, 135],  # 20x20
        INTF_SPECIAL: [552, 140, 572, 160],

        SKILL_ATT: skills_grid[0][0],
        SKILL_STR: skills_grid[0][1],
        SKILL_DEF: skills_grid[0][2],
        SKILL_RNG: skills_grid[0][3],
        SKILL_PRY: skills_grid[0][4],
        SKILL_MAG: skills_grid[0][5],
        SKILL_RC: skills_grid[0][6],
        SKILL_CON: skills_grid[0][7],

        SKILL_HP: skills_grid[1][0],
        SKILL_AGL: skills_grid[1][1],
        SKILL_HRB: skills_grid[1][2],
        SKILL_THV: skills_grid[1][3],
        SKILL_CRA: skills_grid[1][4],
        SKILL_FLT: skills_grid[1][5],
        SKILL_SLA: skills_grid[1][6],
        SKILL_HUN: skills_grid[1][7],

        SKILL_MIN: skills_grid[2][0],
        SKILL_SMT: skills_grid[2][1],
        SKILL_FSH: skills_grid[2][2],
        SKILL_CK: skills_grid[2][3],
        SKILL_FMA: skills_grid[2][4],
        SKILL_WC: skills_grid[2][5],
        SKILL_FRM: skills_grid[2][6],
        SKILL_TLVL: skills_grid[2][7],


        PANEL_COMBAT: panels_top_grid[0][0],
        PANEL_SKILLS: panels_top_grid[1][0],
        PANEL_QUESTS: panels_top_grid[2][0],
        PANEL_INV: panels_top_grid[3][0],
        PANEL_GEAR: panels_top_grid[4][0],
        PANEL_PRAYER: panels_top_grid[5][0],
        PANEL_MAGIC: panels_top_grid[6][0],

        PANEL_CHAT: panels_bottom_grid[0][0],
        PANEL_FRIENDS: panels_bottom_grid[1][0],
        PANEL_ACCOUNT: panels_bottom_grid[2][0],
        PANEL_LOGOUT: panels_bottom_grid[3][0],
        PANEL_SETTINGS: panels_bottom_grid[4][0],
        PANEL_EMOTES: panels_bottom_grid[5][0],
        PANEL_MUSIC: panels_bottom_grid[6][0],


        PRAYER_DEF_5: prayer_grid[0][0],
        PRAYER_DEF_10: prayer_grid[0][1],
        PRAYER_PRO_ITEM: prayer_grid[0][2],
        PRAYER_ATT_15: prayer_grid[0][3],
        PRAYER_MAG_15: prayer_grid[0][4],
        PRAYER_CHIV: prayer_grid[0][5],

        PRAYER_STR_5: prayer_grid[1][0],
        PRAYER_STR_10: prayer_grid[1][1],
        PRAYER_RNG_10: prayer_grid[1][2],
        PRAYER_PRO_MAGE: prayer_grid[1][3],
        PRAYER_RETRIBUTION: prayer_grid[1][4],
        PRAYER_PIETY: prayer_grid[1][5],

        PRAYER_ATT_5: prayer_grid[2][0],
        PRAYER_ATT_10: prayer_grid[2][1],
        PRAYER_MAG_10: prayer_grid[2][2],
        PRAYER_PRO_RNG: prayer_grid[2][3],
        PRAYER_REDEMP: prayer_grid[2][4],
        PRAYER_RIGOUR: prayer_grid[2][5],

        PRAYER_RNG_5: prayer_grid[3][0],
        PRAYER_RAP_REST: prayer_grid[3][1],
        PRAYER_DEF_15: prayer_grid[3][2],
        PRAYER_PRO_MELEE: prayer_grid[3][3],
        PRAYER_SMITE: prayer_grid[3][4],
        PRAYER_AUGURY: prayer_grid[3][5],

        PRAYER_MAG_5: prayer_grid[4][0],
        PRAYER_RAP_HEAL: prayer_grid[4][1],
        PRAYER_STR_15: prayer_grid[4][2],
        PRAYER_RNG_15: prayer_grid[4][3],
        PRAYER_PRESERVE: prayer_grid[4][4],
        PRAYER_BLANK: prayer_grid[4][5],

        MAGIC_HOME_TELE: magic_grid[0][0],
        MAGIC_WEAKEN: magic_grid[0][1],
        MAGIC_WATER_BOLT: magic_grid[0][2],
        MAGIC_FALLY_TELE: magic_grid[0][3],
        MAGIC_ENCHANT3: magic_grid[0][4],
        MAGIC_CHARGE_WATER_ORB: magic_grid[0][5],
        MAGIC_CLAWS_GUTHIX: magic_grid[0][6],
        MAGIC_CHARGE_AIR_ORB: magic_grid[0][7],
        MAGIC_FIRE_WAVE: magic_grid[0][8],
        MAGIC_TELE_BLOCK: magic_grid[0][9],
        MAGIC_WIND_STK: magic_grid[1][0],
        MAGIC_FIRE_STK: magic_grid[1][1],
        MAGIC_VARROCK_TELE: magic_grid[1][2],
        MAGIC_CRUMBLE_UNDEAD: magic_grid[1][3],
        MAGIC_IBAN_BLAST: magic_grid[1][4],
        MAGIC_ENCHANT4: magic_grid[1][5],
        MAGIC_FLAMES_ZAMMY: magic_grid[1][6],
        MAGIC_VULNER: magic_grid[1][7],
        MAGIC_ENTANGLE: magic_grid[1][8],
        MAGIC_TELE_2_TARGET: magic_grid[1][9],
        MAGIC_CONFUSE: magic_grid[2][0],
        MAGIC_BONES_2_BAN: magic_grid[2][1],
        MAGIC_ENCHANT2: magic_grid[2][2],
        MAGIC_HOUSE_TELE: magic_grid[2][3],
        MAGIC_SNARE: magic_grid[2][4],
        MAGIC_WATCHTOWER_TELE: magic_grid[2][5],
        MAGIC_TROLLHEIM_TELE: magic_grid[2][6],
        MAGIC_ENChANT5: magic_grid[2][7],
        MAGIC_STUN: magic_grid[2][8],
        MAGIC_ENCHANT6: magic_grid[2][9],
        MAGIC_ENCHANT_CB: magic_grid[3][0],
        MAGIC__WIND_BOLT: magic_grid[3][1],
        MAGIC_EARTH_BOLT: magic_grid[3][2],
        MAGIC_WIND_BLAST: magic_grid[3][3],
        MAGIC_MAGIC_DART: magic_grid[3][4],
        MAGIC_FIRE_BLAST: magic_grid[3][5],
        MAGIC_WIND_WAVE: magic_grid[3][6],
        MAGIC_KOUREND_CASTLE: magic_grid[3][7],
        MAGIC_CHARGE: magic_grid[3][8],
        MAGIC_CAMMY_TELEOTHER: magic_grid[3][9],
        MAGIC_WATER_STK: magic_grid[4][0],
        MAGIC_CURSE: magic_grid[4][1],
        MAGIC_LUMBY_TELE: magic_grid[4][2],
        MAGIC_SUPERHEAT: magic_grid[4][3],
        MAGIC_ARDY_TELE: magic_grid[4][4],
        MAGIC_CHARGE_EARTH_ORB: magic_grid[4][5],
        MAGIC_CHARGE_FIRE_ORB: magic_grid[4][6],
        MAGIC_EARTH_WAVE: magic_grid[4][7],
        MAGIC_WIND_SURGE: magic_grid[4][8],
        MAGIC_EARTH_SURGE: magic_grid[4][9],
        MAGIC_ENCHANT1: magic_grid[5][0],
        MAGIC_BIND: magic_grid[5][1],
        MAGIC_TELE_GRAB: magic_grid[5][2],
        MAGIC_CAMMY_TELE: magic_grid[5][3],
        MAGIC_EARTH_BLAST: magic_grid[5][4],
        MAGIC_BONES_2_PEACH: magic_grid[5][5],
        MAGIC_APEATOLL_TELE: magic_grid[5][6],
        MAGIC_ENFEEBLE: magic_grid[5][7],
        MAGIC_FALLY_TELEOTHER: magic_grid[5][8],
        MAGIC_ENCHANT7: magic_grid[5][9],
        MAGIC_EARTH_STK: magic_grid[6][0],
        MAGIC_LOW_ALCH: magic_grid[6][1],
        MAGIC_FIRE_BOLT: magic_grid[6][2],
        MAGIC_WATER_BLAST: magic_grid[6][3],
        MAGIC_HIGH_ALCH: magic_grid[6][4],
        MAGIC_SARA_STK: magic_grid[6][5],
        MAGIC_WATER_WAVE: magic_grid[6][6],
        MAGIC_LUMBY_TELEOTHER: magic_grid[6][7],
        MAGIC_WATER_SURGE: magic_grid[6][8],
        MAGIC_FIRE_SURGE: magic_grid[6][9],


        GEAR_HEAD: [624, 207, 659, 242],
        GEAR_CAPE: [583, 246, 618, 281],
        GEAR_NECK: [624, 246, 659, 281],
        GEAR_QUIVER: [665, 246, 700, 281],
        GEAR_WEAPON: [568, 285, 603, 320],
        GEAR_BODY: [624, 285, 659, 320],
        GEAR_SHIELD: [680, 285, 715, 320],
        GEAR_LEGS: [624, 325, 659, 360],
        GEAR_GLOVES: [568, 365, 603, 400],
        GEAR_BOOTS: [624, 365, 659, 400],
        GEAR_RING: [680, 365, 715, 400],

        COMBAT_QUAD_1: [567, 248, 633, 291],
        COMBAT_QUAD_2: [651, 254, 714, 293],
        COMBAT_QUAD_3: [572, 308, 634, 346],
        COMBAT_QUAD_4: [651, 308, 713, 345],
        COMBAT_COL_1: [572, 254, 634, 277],
        COMBAT_COL_2: [572, 291, 634, 313],
        COMBAT_COL_3: [573, 326, 634, 349],
        COMBAT_RETALIATE: [572, 362, 713, 397],


        COMBAT_SPELL_WIND_STK: combat_spells_grid[0][0],
        COMBAT_SPELL_WIND_BOLT: combat_spells_grid[0][1],
        COMBAT_SPELL_WIND_BLAST: combat_spells_grid[0][2],
        COMBAT_SPELL_WIND_WAVE: combat_spells_grid[0][3],
        COMBAT_SPELL_WIND_SURGE: combat_spells_grid[0][4],

        COMBAT_SPELL_EARTH_STK: combat_spells_grid[1][0],
        COMBAT_SPELL_EARTH_BOLT: combat_spells_grid[1][1],
        COMBAT_SPELL_EARTH_BLAST: combat_spells_grid[1][2],
        COMBAT_SPELL_EARTH_WAVE: combat_spells_grid[1][3],
        COMBAT_SPELL_EARTH_SURGE: combat_spells_grid[1][4],

        COMBAT_SPELL_WATER_STK: combat_spells_grid[2][0],
        COMBAT_SPELL_WATER_BOLT: combat_spells_grid[2][1],
        COMBAT_SPELL_WATER_BLAST: combat_spells_grid[2][2],
        COMBAT_SPELL_WATER_WAVE: combat_spells_grid[2][3],
        COMBAT_SPELL_WATER_SURGE: combat_spells_grid[2][4],

        COMBAT_SPELL_FIRE_STK: combat_spells_grid[3][0],
        COMBAT_SPELL_FIRE_BOLT: combat_spells_grid[3][1],
        COMBAT_SPELL_FIRE_BLAST: combat_spells_grid[3][2],
        COMBAT_SPELL_FIRE_WAVE: combat_spells_grid[3][3],
        COMBAT_SPELL_FIRE_SURGE: combat_spells_grid[3][4],


        GEAR_EQUIPMENT: [558, 415, 590, 449],
        GEAR_VALUE: [604, 417, 634, 447],
        GEAR_DEATH: [648, 416, 680, 448],
        GEAR_FOLLOWER: [693, 416, 726, 449],

        GEAR_EQUIPMENT_CLOSE: [486, 19, 499, 33],
        GEAR_VALUE_CLOSE: [476, 24, 490, 39],
        GEAR_DEATH_CLOSE: [486, 20, 500, 35],


        CHAT_HEAD: [40, 365, 88, 453],  # 48 x 88
        CHAT_HEAD_RIGHT: [425, 365, 483, 453],  # 48 x 88

        PLAYER_CENTER_SM: [215, 130, 372, 202],
        PLAYER_CENTER_MED: [180, 100, 420, 240],
        PLAYER_CENTER_LG: [16, 70, 504, 302],

        TUT_ISLAND_MINI_MAP_FISH_SPOT: [692, 121, 711, 145],

        NORTH: [26, 39, 484, 176],
        EAST: [263, 39, 492, 307],
        SOUTH: [14, 184, 492, 307],
        WEST: [26, 39,  231, 307],
        RESET_MAP: [546, 4, 574, 32],

        CLICK_HERE_TO_CONTINUE: [21, 440, 496, 453],
        CLOSE_BANK: [482, 17, 491, 28],
        BANK_DEPOSIT_INV: [431, 300, 455, 326],

        SMELT_BAR_BRONZE: [22, 397, 65, 453],
        SMELT_BAR_IRON: [87, 397, 125, 452],
        SMELT_BAR_SILVER: [146, 396, 191, 454],
        SMELT_BAR_STEEL: [210, 396, 252, 455],
        SMELT_BAR_GOLD: [279, 408, 313, 451],
        SMELT_BAR_MITH: [351, 433, 377, 443],
        SMELT_BAR_ADAM: [408, 411, 437, 452],
        SMELT_BAR_RUNE: [466, 421, 498, 452],

        BANK_TAB_ALL: [75, 54, 96, 68, ],
        BANK_TAB_1: [114, 56, 133, 63, ],
        BANK_TAB_2: [165, 63, 180, 65, ],
        BANK_TAB_3: [194, 57, 213, 68, ],
        BANK_TAB_4: [229, 47, 254, 72, ],
        BANK_TAB_5: [268, 50, 302, 62, ],
        BANK_TAB_6: [308, 48, 338, 66, ],
        BANK_TAB_7: [347, 46, 372, 69, ],
        BANK_TAB_8: [402, 66, 410, 69, ],
        BANK_TAB_9: [447, 72, 452, 69, ],

        BANK_DEPOSIT_WORN_ITEMS: [472, 301, 493, 328],
        GE_HISTORY: [25, 26, 74, 46],
        CONTINUE: [115, 430, 464, 458],
        LOGIN_EXISTING_USER: [399, 293, 529, 322],
        LOGIN_LOGIN: [302, 335, 367, 349],



    }
