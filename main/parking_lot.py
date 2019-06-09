#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ticket import Ticket
from car import Car
from parking_lot_full_exception import ParkingLotFullException

class ParkingLot:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__parkingRecord = {}

    def park(self, car):
        if (self.__capacity - len(self.__parkingRecord) <= 0):
            raise ParkingLotFullException()
        ticket = Ticket()
        self.__parkingRecord[ticket] = car
        return ticket