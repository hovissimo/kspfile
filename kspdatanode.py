''' A serialization module for Kerbal Space Program data files.

This module is responsible for serializing and deserializing the data files
(.sfs, .cfg, .craft) of Kerbal Space Program. It is not the role of this module
to make that data meaningful or to have rich classes for the KSP data.

Notes and observations:
 - As of KSP v1.0.4 data files consist of a tree of nodes.
 - The nodes have 0+ key/value pairs of data, and 0+ node children.
 - As far as I can tell, there is an implicit and anonymous root node
   (.craft files start with data pairs).
 - These files can contain comments, any text after '//' should be ignored.

I have found _some_ documentation for these files.
See: http://anatid.github.io/XML-Documentation-for-the-KSP-API/class_config_node.html
     http://wiki.kerbalspaceprogram.com/wiki/CFG_File_Documentation
     https://github.com/Anatid/XML-Documentation-for-the-KSP-API/blob/master/src/ConfigNode.cs
'''  # nopep8

from collections import namedtuple


NodeValue = namedtuple('NodeValue', ['name', 'value'])


class KSPDataNode():
    '''A representation of a data node in a KSP file.'''
    def __init__(self, name):
        self.name = name
        self.values = ()
        self.nodes = ()
        self.parent = None
        pass

    def add_value(self, name, value):
        '''Add a named value to this node.

        Order of added values should be maintained. Uniqueness is not required.
        '''
        self.values += (NodeValue(name, value), )

    def add_node(self, child_node):
        '''Add a node to this node's children.

        Order of added nodes should be maintained.'''
        self.nodes += (child_node, )
        child_node.parent = self
        return child_node
