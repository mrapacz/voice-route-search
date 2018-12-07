from jakdojade import search_jakdojade


def test_workflow_fetches_results():
    assert len(search_jakdojade("rondo ofiar katynia", "rondo matecznego")) > 1
