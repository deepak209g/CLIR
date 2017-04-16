1. Compilation of Code:
	a) Go into project directory.
	b) Open the command prompt.
	c) Execute the following command:
		(i) python3 driver.py
	d) Choose 1 for using Translation Model.
	e) Choose 2 for computing Cosine Similarity between 2 documents.

2. Assumptions:
	Since we are processing the corpus in batches and training these batches via IBM model, it was observed that in each batch, only a few of the (e,f) pairs were converging. So we are assuming that the respective (e,f) pair will converge in atleast one of the batches and thus we can compute a consolidated model from these batches to get all the translation probabilities. 
	
	GitHub Repo Link : https://github.com/deepak209g/CLIR
