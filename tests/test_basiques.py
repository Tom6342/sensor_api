from fake_data_app.sensor import VisitSensor
from datetime import date


def test_monday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2025, 3, 24))

def test_tuesday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2025, 3, 25))

def test_wednesday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2025, 3, 26))

def test_thursday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2025, 3, 27))

def test_friday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2025, 3, 28))


def test_saturday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2025, 3, 29))

def test_sunday_closed():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 == visit_sensor.simulate_visit_count(date(2025, 3, 30))


def test_with_break():
    visit_sensor = VisitSensor(1200, 300, perc_break=10)
    assert 0 == visit_sensor.get_visit_count(date(2025, 3, 29))

def test_without_break():
    visit_sensor = VisitSensor(1200, 300, perc_break=0)
    assert 0 != visit_sensor.get_visit_count(date(2025, 3, 29))

def test_with_malfunction():
    visit_sensor = VisitSensor(1200, 300, perc_malfunction=10)
    assert 1834 == visit_sensor.get_visit_count(date(2023, 11, 28))


def test_without_malfunction():
    visit_sensor = VisitSensor(1200, 300, perc_malfunction=0)
    assert 1192 == visit_sensor.get_visit_count(date(2023, 11, 28))


test_monday_open()
test_tuesday_open()
test_sunday_closed()
test_without_malfunction()