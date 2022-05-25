from hypatia import Model
from hypatia import Plotter

## defalt parameters - single node
path = r"/Users/afa/Desktop/italy2020/"
model = Model(path=path + "sets2", mode="Operation")
model.create_data_excels(path=path + "/parameters1", force_rewrite=True)
model.read_input_data(path=path + "/parameters1")
model.run(solver='scipy')
model.to_csv(path=path + '/results_italy_scenario_2', force_rewrite=True, postprocessing_module="it2020")

# cd C:\Users\frac1\OneDrive - Politecnico di Milano\Documents\GitHub\Hypatia
# venv\Scripts\activate
