from unittest import TestCase
from find_duplicated_photos import folder_pair

__author__ = 'jason'

class TestFolderPair(TestCase):
    def test_group_by_folder_pair(self):
        input = [('/xxx/yyy/a', '/xxx/ooo/a'),
                 ('/xxx/ooo/k', '/xxx/yyy/k'),
                 ('/xxx/zzz/t', '/xxx/yyy/t'),
                 ('/xxx/zzz/k', '/xxx/yyy/k')
                 ]
        out = folder_pair.group_by_folder_pair(input)
        self.assertEquals(out, [({'/xxx/yyy', '/xxx/ooo'}, ['a', 'k']), ({'/xxx/yyy', '/xxx/zzz'}, ['t', 'k'])])