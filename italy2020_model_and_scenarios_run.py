from hypatia import Model
from hypatia import italy2020_merge_results

# base_path = "C:/Users/frac1/Politecnico di Milano/PROJECTS_Eni_Modelling Suite/Model/Hypatia-main/examples/Italian_energy_system_2020"
base_path = r"C:\Users\frac1\Politecnico di Milano\DENG-SESAM - Documenti\PROJECTS_Eni_Modelling Suite\Model\examples\Italian_energy_system_2020"


# SCENARIO 1

# load sets
model = Model(path=base_path + "/sets/", mode="Operation")

# read parameters data
model.read_input_data(base_path + "/parameters/")

# solve model
model.run(solver='scipy')

# write result to csv in the it2020 format
model.to_csv(path=base_path + "/result_scenario_1/", force_rewrite=True, postprocessing_module="it2020")



# SCENARIO 2

# load sets
model2 = Model(path=base_path + "/sets/", mode="Operation")

# write default parameters data
# model2.create_data_excels(base_path + "/parameters_scenario_2", force_rewrite=True)

# read parameters data
model2.read_input_data(base_path + "/parameters_scenario_2/")

# solve model
model2.run(solver='scipy')

# write result to csv in the it2020 format
model2.to_csv(path=base_path + "/result_scenario_2/", force_rewrite=True, postprocessing_module="it2020")



# Merge result csv for different scenarios
italy2020_merge_results(
    scenarios={
        "scenario1": base_path + "/result_scenario_1/",
        "scenario2": base_path + "/result_scenario_2/"
    },
    path=base_path + "/merged_results",
    force_rewrite=True
)

# AGGREGATION FILE
# generate aggregation for the 2 models.
# Since the 2 models sets are the same the generated file from the 2 models will be the same. Therefore I generate only 1 aggregation file
# which can be shared between the 2 models
model.create_aggregation_config_file(path=base_path + "/aggregation_config.xlsx")
