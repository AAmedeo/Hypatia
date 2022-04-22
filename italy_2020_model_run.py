from hypatia import Model
from hypatia import Plotter

## defalt parameters - single node
path = r"C:\Users\frac1\Politecnico di Milano\DENG-SESAM - Documenti\PROJECTS_Eni_Modelling Suite\Model\Hypatia-main\examples\Italian_energy_system_2020"
model = Model(path=path + "sets", mode="Operation")
model.read_input_data(path=path + "/parameters_scenario_2")
model.run(solver='scipy')
model.to_csv(path=path + '/results_italy_scenario_2', force_rewrite=True, postprocessing_module="it2020")

# cd C:\Users\frac1\OneDrive - Politecnico di Milano\Documents\GitHub\Hypatia
# venv\Scripts\activate