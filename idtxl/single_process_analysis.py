"""Parent class for analysis of single processes in the network.

@author: patricia
"""
from .network_analysis import NetworkAnalysis


class SingleProcessAnalysis(NetworkAnalysis):
    def __init__(self):
        super().__init__()
