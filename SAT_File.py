

def get_opt_solution_value(filename):
    """
"./data/wuf20-78-R/wuf20-017.mwcnf"
    (example: wuf20-78-R)
    :param clause_amount:   (example: 20)
    :param var_amount:      (example: 78)
    :param instance_type:   (example: R)
    :param instance_id:     (example: 1)
    :return:
    """
    _, _, folder_name, file_name = filename.split('/')
    file_name = file_name.split('.')[0].replace('-A','')
    with open(f'./data/{folder_name}-opt.dat') as opt_file:
        for line in opt_file:
            if line.startswith(f'{file_name[1:]} '):
                _, weight, *_ = line.split()
                return int(weight)

    return -1