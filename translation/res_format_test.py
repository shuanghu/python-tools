# coding:utf-8

import unittest
import resource_format


class TestResourceFormat(unittest.TestCase):
    def test_js_format_normal(self):
        res = resource_format.js_format("Satellite_id: '卫星编号',")
        self.assertEqual(res[0], 'Satellite_id')
        self.assertEqual(res[1], '卫星编号')

    def test_js_format_escape(self):
        res = resource_format.js_format("Satellite_id: '卫星\'编号',")
        self.assertEqual(res[0], 'Satellite_id')
        self.assertEqual(res[1], '卫星\'编号')

    def test_js_empty(self):
        res = resource_format.js_format(" Satellite_id:'卫星编号', ")
        self.assertEqual(res[0], 'Satellite_id')
        self.assertEqual(res[1], '卫星编号')

        res = resource_format.js_format(" Satellite_id:'te st', ")
        self.assertEqual(res[0], 'Satellite_id')
        self.assertEqual(res[1], 'te st')


if __name__ == '__main__':
    unittest.main()
