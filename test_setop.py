import setop

def setop_test_helper(tmpdir, operation, a_contents, b_contents):
    a = tmpdir.join('a.txt')
    b = tmpdir.join('b.txt')
    a.write(a_contents)
    b.write(b_contents)

    parser = setop.get_parser()
    args = parser.parse_args([operation, str(a), str(b)])

    return setop.get_result(args)

def test_intersect(tmpdir):
    for operation in ['i', 'intersect']:
        result = setop_test_helper(tmpdir, operation, 'a\nb\nc\n', 'b\nc\nd\n')

        assert 'c' in result
        assert 'b' in result
        assert len(result) == 2

def test_intersect_spaces(tmpdir):
    result = setop_test_helper(tmpdir, 'i', 'a\nb\nc\n', 'b\nc \nd\n')

    assert 'b' in result
    assert len(result) == 1

def test_union(tmpdir):
    for operation in ['u', 'union']:
        result = setop_test_helper(tmpdir, operation, 'a\nb\nc\n', 'b\nc\nd\n')

        assert 'a' in result
        assert 'b' in result
        assert 'c' in result
        assert 'd' in result
        assert len(result) == 4

def test_union_spaces(tmpdir):
    result = setop_test_helper(tmpdir, 'u', 'a\n', 'a \n')

    assert len(result) == 2
    assert 'a' in result
    assert 'a ' in result

def test_difference(tmpdir):
    result = setop_test_helper(tmpdir, 'd', 'a\nb\n', 'a\n')

    assert len(result) == 1
    assert 'b' in result

def test_difference_spaces(tmpdir):
    result = setop_test_helper(tmpdir, 'd', 'a\nb\n', 'a\nb \n')

    assert len(result) == 1
    assert 'b' in result

def test_rdifference(tmpdir):
    result = setop_test_helper(tmpdir, 'rd', 'a\n', 'a\nb\n')

    assert len(result) == 1
    assert 'b' in result

def test_rdifference_spaces(tmpdir):
    result = setop_test_helper(tmpdir, 'rd', 'a\nb \n', 'a\nb\n')

    assert len(result) == 1
    assert 'b' in result
