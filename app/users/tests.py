#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UserListTest(object):
    @classmethod
    def setup_class(cls):
        pass
    @classmethod
    def teardown_class(cls):
        pass

    def setUp(self):
        pass

    def teardown(self):
        pass

class UserDetailTest(object):
    pass

"""
class TestA(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""    
    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""    
    def setUp(self):
        """This method is run once before _each_ test method is executed"""    
    def teardown(self):
        """This method is run once after _each_ test method is executed"""    
    def test_init(self):
        a = A()
        assert_equal(a.value, "Some Value")
        assert_not_equal(a.value, "Incorrect Value")    
    def test_return_true(self):
        a = A()
        assert_equal(a.return_true(), True)
        assert_not_equal(a.return_true(), False)    
    def test_raise_exc(self):
        a = A()        assert_raises(KeyError, a.raise_exc, "A value")    @raises(KeyError)
    def test_raise_exc_with_decorator(self):
        a = A()
        a.raise_exc("A message")
"""