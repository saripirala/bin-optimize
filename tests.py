import unittest

from bin_optimize import optimize


class Testing(unittest.TestCase):
    def test_happy_path(self):
        test_set = [
            {'b1': [('a1', 600), ('a5', 250), ('a10', 400)],
             'b2': [('a2', 400), ('a6', 500), ('a11', 200)],
             'b3': [('a3', 700), ('a7', 200), ('a12', 300)],
             'b4': [('a4', 200), ('a8', 200), ('a13', 200),
                    ('a7', 200), ('a9', 400)]},
            {'b1': [('a1', 300), ('a5', 300), ('a9', 250), ('a12', 400)],
             'b2': [('a2', 400), ('a6', 500), ('a10', 200)],
             'b3': [('a3', 700), ('a7', 200), ('a11', 300)],
             'b4': [('a4', 800), ('a8', 400)]
             },
            {'b1': [('a1', 6), ('a5', 4.5), ('a9', 4)],
             'b2': [('a2', 4), ('a6', 5), ('a10', 2)],
             'b3': [('a3', 7), ('a7', 2), ('a11', 3)],
             'b4': [('a4', 2), ('a8', 2), ('a12', 2), ('a13', 2), ('a15', 4)]}
        ]
        expected =  \
            [{'b2': [('a2', 400), ('a6', 500), ('a11', 200), ('a1', 600)],
              'b3': [('a3', 700), ('a7', 200), ('a12', 300), ('a10', 400)],
              'b4': [('a4', 200), ('a8', 200), ('a13', 200), ('a7', 200),
                     ('a9', 400), ('a5', 250)]},
             {'b1': [('a1', 600), ('a5', 250), ('a10', 400), ('a6', 500)],
              'b3': [('a3', 700), ('a7', 200), ('a12', 300), ('a11', 200)],
              'b4': [('a4', 200), ('a8', 200), ('a13', 200), ('a7', 200),
                     ('a9', 400), ('a2', 400)]},
             {'b1': [('a1', 600), ('a5', 250), ('a10', 400), ('a7', 200)],
              'b2': [('a2', 400), ('a6', 500), ('a11', 200), ('a12', 300)],
              'b4': [('a4', 200), ('a8', 200), ('a13', 200), ('a7', 200),
                     ('a9', 400), ('a3', 700)]},
             {'b1': [('a1', 600), ('a5', 250), ('a10', 400), ('a7', 200)],
              'b2': [('a2', 400), ('a6', 500), ('a11', 200), ('a13', 200),
                     ('a8', 200)],
              'b3': [('a3', 700), ('a7', 200), ('a12', 300), ('a4', 200),
                     ('a9', 400)]},
             {'b2': [('a2', 400), ('a6', 500), ('a10', 200), ('a1', 300),
                     ('a9', 250)],
              'b3': [('a3', 700), ('a7', 200), ('a11', 300), ('a12', 400)],
              'b4': [('a4', 800), ('a8', 400), ('a5', 300)]},
             {'b1': [('a1', 300), ('a5', 300), ('a9', 250), ('a12', 400),
                     ('a6', 500)],
              'b3': [('a3', 700), ('a7', 200), ('a11', 300), ('a10', 200)],
              'b4': [('a4', 800), ('a8', 400), ('a2', 400)]},
             {'b1': [('a1', 300), ('a5', 300), ('a9', 250), ('a12', 400),
                     ('a7', 200)],
              'b2': [('a2', 400), ('a6', 500), ('a10', 200), ('a11', 300)],
              'b4': [('a4', 800), ('a8', 400), ('a3', 700)]},
             {'b1': [('a1', 300), ('a5', 300), ('a9', 250), ('a12', 400)],
              'b2': [('a2', 400), ('a6', 500), ('a10', 200), ('a4', 800)],
              'b3': [('a3', 700), ('a7', 200), ('a11', 300), ('a8', 400)]},
             {'b2': [('a2', 4), ('a6', 5), ('a10', 2), ('a1', 6)],
              'b3': [('a3', 7), ('a7', 2), ('a11', 3), ('a5', 4.5)],
              'b4': [('a4', 2), ('a8', 2), ('a12', 2), ('a13', 2), ('a15', 4),
                     ('a9', 4)]},
             {'b1': [('a1', 6), ('a5', 4.5), ('a9', 4)],
              'b3': [('a3', 7), ('a7', 2), ('a11', 3), ('a10', 2), ('a6', 5)],
              'b4': [('a4', 2), ('a8', 2), ('a12', 2), ('a13', 2), ('a15', 4),
                     ('a2', 4)]},
             {'b1': [('a1', 6), ('a5', 4.5), ('a9', 4)],
              'b2': [('a2', 4), ('a6', 5), ('a10', 2), ('a11', 3), ('a7', 2)],
              'b4': [('a4', 2), ('a8', 2), ('a12', 2), ('a13', 2), ('a15', 4),
                     ('a3', 7)]},
             {'b1': [('a1', 6), ('a5', 4.5), ('a9', 4), ('a8', 2)],
              'b2': [('a2', 4), ('a6', 5), ('a10', 2), ('a12', 2), ('a15', 4)],
              'b3': [('a3', 7), ('a7', 2), ('a11', 3), ('a13', 2), ('a4', 2)]}]

        result = []
        for rec in test_set:
            for k, _ in rec.items():
                resp = optimize(rec, k)
                result.append(resp)
        self.assertEqual(expected, result)

    def test_nbr_bins(self):
        bins = {123: [('a1', 6), ('a2', 4.5), ('a3', 4)],
                345: [('a4', 4), ('a5', 5), ('a6', 2)],
                567: [('a7', 7), ('a8', 2), ('a9', 3)],
                789: [('a10', 2), ('a11', 2),
                      ('a12', 2), ('a13', 2), ('a14', 4)]}

        expected = {345: [('a4', 4), ('a5', 5), ('a6', 2), ('a1', 6)],
                    567: [('a7', 7), ('a8', 2), ('a9', 3), ('a2', 4.5)],
                    789: [('a10', 2), ('a11', 2),
                          ('a12', 2), ('a13', 2), ('a14', 4), ('a3', 4)]}

        resp = optimize(bins, 123)
        self.assertEqual(expected, resp)

    def test_nbr_bins_empty_size(self):
        bins = {123: [('a1', 0), ('a2', 4.5), ('a3', )],
                345: [('a4', 4), ('a5', 5), ('a6', 2)],
                567: [('a7', 0), ('a8', 2), ('a9', 3)],
                789: [('a10', 2), ('a11', 2),
                      ('a12', 2), ('a13', 2), ('a14', 4)]}

        expected = {345: [('a4', 4), ('a5', 5), ('a6', 2)],
                    567: [('a7', 0), ('a8', 2), ('a9', 3), ('a1', 0),
                          ('a2', 4.5), ('a3', )],
                    789: [('a10', 2), ('a11', 2), ('a12', 2), ('a13', 2),
                          ('a14', 4)]}
        resp = optimize(bins, 123)
        self.assertEqual(expected, resp)

    def test_nbr_weights(self):
        bins = {123: [(102, 6), (107, 4.5), (112, 4)],
                345: [(103, 4), (108, 5), (113, 2)],
                567: [(104, 7), (109, 2), (114, 3)],
                789: [(105, 2), (110, 2),
                      (106, 2), (111, 2), (115, 4)]}

        expected = {345: [(103, 4), (108, 5), (113, 2), (102, 6)],
                    567: [(104, 7), (109, 2), (114, 3), (107, 4.5)],
                    789: [(105, 2), (110, 2),
                          (106, 2), (111, 2), (115, 4), (112, 4)]}

        resp = optimize(bins, 123)
        self.assertEqual(expected, resp)

    def test_incorrect_tuple(self):
        test_set = {'b1': [2], 'b2': 4}
        with self.assertRaises(TypeError):
            optimize(test_set, 'b1')

    def test_incorrect_bin(self):
        test_set = {'b1': [2], 'b2': [4]}
        with self.assertRaises(KeyError):
            optimize(test_set, 'E')

    def test_empty_bin(self):
        test_set = {'b1': [('a1', 2)], 'b2': []}
        self.assertEqual({'b1': [('a1', 2)]}, optimize(test_set, 'b2'))
