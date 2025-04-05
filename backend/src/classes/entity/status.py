


class Status:
    def __init__(self, hp, hp_rgn, mp, mp_rgn, sp, sp_rgn, atk, atk_m, df, df_m, res, res_m, spd, crit, crit_max, sanity, load):
        self.hp = hp
        self.maxHp = self.hp
        self.regenHp = hp_rgn
        self.mp = mp
        self.maxMp = self.mp
        self.regenMp = mp_rgn
        self.sp = sp
        self.maxSp = self.sp
        self.regenSp = sp_rgn
        self.atk = atk
        self.atkM = atk_m
        self.df = df
        self.dfM = df_m
        self.res = res
        self.resM = res_m
        self.spd = spd
        self.crit = crit
        self.maxCrit = crit_max
        self.sanity = sanity
        self.maxSanity = self.sanity

        self.load = load


    def get_info_dict(self):

        data = {
            "status": {
                "hp": self.hp,
                "max_hp": self.maxHp,
                "regen_hp": self.regenHp,
                "mp": self.mp,
                "max_mp": self.maxMp,
                "regen_mp": self.regenMp,
                "sp": self.sp,
                "max_sp": self.maxSp,
                "regen_sp": self.regenSp,
                "atk": self.atk,
                "atk_m": self.atkM,
                "df": self.df,
                "df_m": self.dfM,
                "res": self.res,
                "res_m": self.resM,
                "spd": self.spd,
                "crit": self.crit,
                "max_crit": self.maxCrit,
                "sanity": self.sanity,
                "max_sanity": self.maxSanity,
                "load": self.load
            }
        }



        return data