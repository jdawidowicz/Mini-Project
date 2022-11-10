from Menu import add_new, delete_from, update
statuslist = ["Preparing", "Delivered", "Out for Delivery"]


def test_add_new():
    testlist = [{"Product":"Test1","Price":"Test1"}]
    expected = [{"Product":"Test1","Price":"Test1"},{"Product":"Test2","Price":"Test2"}]

    def mock_input(string):
        return "Test2"


    add_new(testlist, input=mock_input)
    actual = testlist
    assert actual == expected

def test_delete_from():
    testlist = [{"Product":"Test1","Price":"Test1"}]
    expected = []

    def mock_input(String):
        return 0


    delete_from(testlist, input = mock_input)
    actual = testlist
    assert actual == expected

def test_update():
    testlist = [{"Product":"Test1","Price":"Test1"}]
    expected = [{"Product":"Test2","Price":"Test2"}]

    def mock_index_input(string):
        return 0


    def mock_input(string):
        return "Test2"


    update(testlist, status = False, input1 = mock_index_input, input2 = mock_input)
    actual = testlist
    assert actual == expected

def test_status_update():
    testlist = [{"Status":"Delivered"}]
    expected = [{"Status":"Preparing"}]

    def mock_index_input(string):
        return 0
    
    update(testlist, status = True, input1=mock_index_input, input2=mock_index_input)
    actual = testlist
    assert actual == expected
    





test_add_new()
test_delete_from()
test_update()
test_status_update()