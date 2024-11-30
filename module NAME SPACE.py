def test_function () :
    print("I`m in TEST FUNC level")
    def inner_function () :
        print("I`m in INNER FUNC level")
    inner_function()

# MAIN BLOCK

test_function()
# inner_function() Unresolved reference 'inner_function'