#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../main")
import unittest
from parking_lot import ParkingLot
from parking_lot_full_exception import ParkingLotFullException
from car import Car

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


