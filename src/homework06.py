#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 06
Sergey Streltsov 2019-11-17
Simplest object of a Room
"""

import hashlib


class Room(object):

    def __init__(self, room_number, bed_number, is_lux=False):
        self._room_number = room_number
        self._bed_number = bed_number
        self._is_lux = is_lux
        self._booking_history = dict()

    def book_room(self, checkin_date, checkout_date):
        if self.check_booking_interval(
                checkin_date=checkin_date,
                checkout_date=checkout_date) and not self.is_booked():
            confirm_obj = hashlib.md5((checkin_date + checkout_date).encode())
            confirmation_number = confirm_obj.hexdigest()
            print('Booking Ok, checkin: {}, checkout: {}'.format(checkin_date,
                                                                 checkout_date))
            print('Conf. number: {}'.format(confirmation_number))
            self._booking_history[confirmation_number] = [checkin_date, checkout_date]
        else:
            print('Error: {}-{} not available'.format(checkin_date, checkout_date))
            return -1
        return confirmation_number

    def cancel_booking(self, confirmation_number):
        if confirmation_number in self._booking_history.keys():
            dates = self._booking_history.pop(confirmation_number)
            print('{}, booking canceled'.format(dates))
        else:
            print('Error: booking with conf. number {} not found'.format(confirmation_number))

    def check_booking_interval(self, checkin_date, checkout_date):
        # check is interval valid
        return bool(checkin_date and checkout_date)

    def is_booked(self, mock_obj=False):
        # check is booked
        return mock_obj

    def info(self, extended_info=False):
        print('Room: {}'.format(self._room_number))
        print('Lux - {}'.format(self._is_lux))
        print('Has {} bed(s)'.format(self._bed_number))
        print('Booked now: {}'.format(self.is_booked(mock_obj=True)))
        if extended_info:
            print('Booking history: {}'.format(self._booking_history))


if __name__ == '__main__':
    room82 = Room(room_number=82, bed_number=2)
    room33 = Room(room_number=33, bed_number=4)
    room101 = Room(room_number=33, bed_number=2, is_lux=True)
    book01 = room101.book_room(checkin_date='2019-11-19',
                               checkout_date='2019-11-22')
    room101.cancel_booking(confirmation_number=book01)
    room101.info(extended_info=True)
    room82.info()
    room33.cancel_booking(confirmation_number='dc2dd32873650bf8a490d82e')
