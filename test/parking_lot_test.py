#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../main")
import unittest
from parking_lot import ParkingLot
from parking_lot_full_exception import ParkingLotFullException
from car import Car
from car_not_found_exception import CarNotFoundException
from ticket import Ticket

class ParkingLotTest(unittest.TestCase):

    def test_should_get_ticket_when_park_car(self):
        parkingLot = ParkingLot(10)
        ticket = parkingLot.park(Car())
        self.assertIsNotNone(ticket)

    def test_should_throw_error_when_park_car_in_full_parking_lot(self):
        with self.assertRaises(ParkingLotFullException):
            parkingLot = ParkingLot(1)
            parkingLot.park(Car())
            parkingLot.park(Car())

    def test_should_get_car_when_pick_car_with_available_ticket(self):
        parkingLot = ParkingLot(10)
        car = Car()
        ticket = parkingLot.park(car)
        pickedCar = parkingLot.pick(ticket)
        self.assertEqual(car, pickedCar)

    def test_should_throw_error_when_pick_car_with_invalid_ticket(self):
        with self.assertRaises(CarNotFoundException):
            parkingLot = ParkingLot(10)
            parkingLot.pick(Ticket())

    def test_should_throw_error_when_pick_car_twice_with_same_ticket(self):
        with self.assertRaises(CarNotFoundException):
            parkingLot = ParkingLot(10)
            ticket = parkingLot.park(Car())
            parkingLot.pick(ticket)
            parkingLot.pick(ticket)
        


