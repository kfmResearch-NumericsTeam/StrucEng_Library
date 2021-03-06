def outputer(result_data, result_element,step):
# updatet result_data dictionary (OUTPUTER)
    result_data[str(step)]["element"]["as_xi_bot"].update({result_element[0] : {"ip1_sp0" : result_element[1][0]}})
    result_data[str(step)]["element"]["as_xi_top"].update({result_element[0] : {"ip1_sp0" : result_element[1][1]}})
    result_data[str(step)]["element"]["as_eta_bot"].update({result_element[0] : {"ip1_sp0" : result_element[2][0]}})
    result_data[str(step)]["element"]["as_eta_top"].update({result_element[0] : {"ip1_sp0" : result_element[2][1]}})
    result_data[str(step)]["element"]["as_z"].update({result_element[0] : {"ip1_sp0" : result_element[3]}})
    result_data[str(step)]["element"]["Fall_bot"].update({result_element[0] : {"ip1_sp0" : result_element[4][0]}})
    result_data[str(step)]["element"]["Fall_top"].update({result_element[0] : {"ip1_sp0" : result_element[4][1]}})
    result_data[str(step)]["element"]["CC_bot"].update({result_element[0] : {"ip1_sp0" : result_element[5][0]}})
    result_data[str(step)]["element"]["CC_top"].update({result_element[0] : {"ip1_sp0" : result_element[5][1]}})
    result_data[str(step)]["element"]["t_bot"].update({result_element[0] : {"ip1_sp0" : result_element[6][0]}})
    result_data[str(step)]["element"]["t_top"].update({result_element[0] : {"ip1_sp0" : result_element[6][1]}})
    result_data[str(step)]["element"]["k_bot"].update({result_element[0] : {"ip1_sp0" : result_element[7][0]}})
    result_data[str(step)]["element"]["k_top"].update({result_element[0] : {"ip1_sp0" : result_element[7][1]}})
    result_data[str(step)]["element"]["psi_bot"].update({result_element[0] : {"ip1_sp0" : result_element[8][0]}})
    result_data[str(step)]["element"]["psi_top"].update({result_element[0] : {"ip1_sp0" : result_element[8][1]}})
    result_data[str(step)]["element"]["m_shear_c"].update({result_element[0] : {"ip1_sp0" : result_element[9]}})
    result_data[str(step)]["element"]["m_cc_bot"].update({result_element[0] : {"ip1_sp0" : result_element[10][0]}})
    result_data[str(step)]["element"]["m_cc_top"].update({result_element[0] : {"ip1_sp0" : result_element[10][1]}})
    result_data[str(step)]["element"]["m_c_total"].update({result_element[0] : {"ip1_sp0" : result_element[11]}})


    result_data[str(step)]["element"]["xyz"].update({result_element[0] : result_element[12][0]})
    result_data[str(step)]["element"]["ex"].update({result_element[0] : result_element[12][1]})
    result_data[str(step)]["element"]["ey"].update({result_element[0] : result_element[12][2]})
    result_data[str(step)]["element"]["ez"].update({result_element[0] : result_element[12][3]})
    result_data[str(step)]["element"]["e_xi_bot"].update({result_element[0] : result_element[12][4]})
    result_data[str(step)]["element"]["e_xi_top"].update({result_element[0] : result_element[12][5]})
    result_data[str(step)]["element"]["e_eta_bot"].update({result_element[0] : result_element[12][6]})
    result_data[str(step)]["element"]["e_eta_top"].update({result_element[0] : result_element[12][7]})

    return result_data