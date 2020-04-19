import os
import numpy


@DATASETS.register_module
class FakeNewsDataset():
    def __init__(self, news_type='politifact', **kwargs):
        self.
