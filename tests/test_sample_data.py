import json
import os


def test_sample_graph_chart_exists():
    base = os.path.dirname(__file__)
    path = os.path.join(base, '../data/sample-graph-chart.json')
    assert os.path.exists(path)
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    assert isinstance(data, dict) or isinstance(data, list)
