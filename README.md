# Install
Create a python environment with `conda create -n mmdet python=3.6`.

Install python libraries with `pip install -r requirements.txt`.

# Dataset preparation
We get data from FakeNewsNet, and format it to a `.csv` file, with the `data_process/generate_csv.py`. 

Details are written in the comments in the python file.

# Dataset analysis
Sentiment analysis is done by `data_process/sentiment_analysis.py`, and is visualized by  `data_process/sentiment_plot.py`. `data_process/tsne.py` is used to visualize tsne result.

# Run the model
Models are implemented in the `infor/infer.py`.

Use `infer/grid_tuning.py` to search for hyper parameters.

# Model results
Images are stored in `img/.`.
