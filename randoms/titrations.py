from math import sqrt, log


# calculating the ph of a weak acid titrated with a string base
def ph_weak_acid_with_strong_base(vol, acid, base, pka, added):
    acid_m = acid * vol
    base_m = base * added
    if acid_m < base_m:
        base_con = (base_m - acid_m) / (vol + added)
        return - log(1e-14 / base_con, 10)
    acid_con = (acid_m - base_m) / (vol + added)
    oh = base_m / (vol + added)
    x = 10 ** (-pka) / oh * acid_con
    return - log(x, 10)


# calculating the ph of a weak acid titrated with a string base
def ph_weak_base_with_strong_acid(base_v, base_m, acid_m, pkb, added_acid_v):
    base_moles = base_v * base_m
    acid_moles = acid_m * added_acid_v
    if base_moles < acid_moles:
        acid_con = (acid_moles - base_moles) / (base_v + added_acid_v)
        return - log(acid_con, 10)
    acid_con = (base_moles - acid_moles) / (base_v + added_acid_v)
    h3o = acid_moles / (base_v + added_acid_v)
    x = 10 ** (-pkb) * acid_con / h3o
    return - log(1e-14 / x, 10)


def equivalence_ph_given_base(base_vol, base_m, acid_m, pkb):
    base_mol = base_vol * base_m
    acid_needed = base_mol / acid_m
    base_m_after = base_mol / (base_vol + acid_needed)
    ka = 1e-14 / (10 ** (-pkb))
    x = sqrt(ka * base_m_after)
    return - log(x, 10)


def equivalence_ph_given_acid(acid_vol, acid_m, base_m, pka):
    acid_mol = acid_vol * acid_m
    base_needed = acid_mol / base_m
    acid_m_after = acid_mol / (acid_vol + base_needed)
    kb = 1e-14 / (10 ** (-pka))
    x = sqrt(kb * acid_m_after)
    h3o = 1e-14 / x
    return - log(h3o, 10)


vol = .2098
acid = .26
base = .98
pka = 3.35
added = .06248
# print(ph_weak_acid_with_strong_base(vol, acid, base, pka, added))

base_vol = .09
base_m = .1051
acid_m = .6933
pkb = 8.77
# print(equivalence_ph_given_base(base_vol, base_m, acid_m, pkb))

acid_vol = .180
acid_m = .1758
base_m = .9
pka = 4.76
# print(equivalence_ph_given_acid(acid_vol, acid_m, base_m, pka))

base_vol = .0874
base_m = .26
acid_m = .23
pkb = 9.37
added_acid_v = .109
print(ph_weak_base_with_strong_acid(base_vol, base_m, acid_m, pkb, added_acid_v))
