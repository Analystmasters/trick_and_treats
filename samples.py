#pass all vars as params to a function without specifying each and every one as a dictionary

return {
    'img': img,
    'initial_lsf': initial_lsf,
    'timestep': 5,  # time step
    'iter_inner': 5,
    'iter_outer': 40,
    'lmda': 5,  # coefficient of the weighted length term L(phi)
    'alfa': 1.5,  # coefficient of the weighted area term A(phi)
    'epsilon': 1.5,  # parameter that specifies the width of the DiracDelta function
    'sigma': 1.5,  # scale parameter in Gaussian kernel
    'potential_function': DOUBLE_WELL,
}
params = gourd_params()
phi = find_lsf(**params)


# 
