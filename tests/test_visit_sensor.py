from fake_data_app.sensor import VisitSensor
import unittest
from datetime import date


class TestVisitSensor(unittest.TestCase):
    def test_weekdays_open(self):
        for test_day in range(24,30):
            with self.subTest(i=test_day):
                visit_sensor = VisitSensor(1200,300)
                visit_count = visit_sensor.simulate_visit_count(date(2025,3,test_day))
                self.assertFalse(visit_count == -1)

    def test_sunday_closed(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2025, 3, 30))

        self.assertEqual(visit_count, -1)

    def test_with_break(self):
        visit_sensor = VisitSensor(1200, 300, perc_break=10)
        visit_count = visit_sensor.get_visit_count(date(2025, 3, 29))
        self.assertEqual(visit_count, 0)

    def test_with_malfunction(self):
        visit_sensor = VisitSensor(1200, 300, perc_malfunction=10)
        visit_count = visit_sensor.get_visit_count(date(2025, 3, 28))
        self.assertEqual(visit_count, 254)

if __name__ == '__main__':
    unittest.main()