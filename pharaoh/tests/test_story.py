import engine

def test_levels():
    script = Script('script.json', JSONReader)
    story  = Story(script)
    levels = story.levels
    expect = {'level0', 'level1', 'level2'}
    assert levels == expect