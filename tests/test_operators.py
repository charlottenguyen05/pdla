from arithmp.parser import Parser
      
def test_add():
    parser = Parser()
    assert parser.parse(None, "1 + 1") == 2
    assert parser.parse(None, "0 + 3") == 3