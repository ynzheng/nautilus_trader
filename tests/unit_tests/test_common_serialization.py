#!/usr/bin/env python3
# -------------------------------------------------------------------------------------------------
# <copyright file="test_common_serialization.py" company="Invariance Pte">
#  Copyright (C) 2018-2019 Invariance Pte. All rights reserved.
#  The use of this source code is governed by the license as found in the LICENSE.md file.
#  http://www.invariance.com
# </copyright>
# -------------------------------------------------------------------------------------------------

import unittest

from inv_trader.common.clock import *
from inv_trader.network.msgpack import *
from inv_trader.common.serialization import *
from test_kit.stubs import *

UNIX_EPOCH = TestStubs.unix_epoch()


class SerializationFunctionTests(unittest.TestCase):

    def test_can_parse_symbol_from_string(self):
        # Arrange
        symbol = Symbol('AUDUSD', Venue.FXCM)

        # Act
        result = parse_symbol(symbol.value)

        # Assert
        self.assertEqual(symbol, result)

    def test_can_parse_bar_spec_from_string(self):
        # Arrange
        bar_spec = BarSpecification(1, Resolution.MINUTE, QuoteType.MID)

        # Act
        result = parse_bar_spec(str(bar_spec))

        # Assert
        self.assertEqual(bar_spec, result)

    def test_can_convert_price_to_string_from_none(self):
        # Arrange
        # Act
        result = convert_price_to_string(None)

        # Assert
        self.assertEqual('NONE', result)

    def test_can_convert_price_to_string_from_decimal(self):
        # Arrange
        # Act
        result = convert_price_to_string(Price('1.00000'))

        # Assert
        self.assertEqual('1.00000', result)

    def test_can_convert_string_to_price_from_none(self):
        # Arrange
        # Act
        result = convert_string_to_price('NONE')

        # Assert
        self.assertEqual(None, result)

    def test_can_convert_string_to_price_from_decimal(self):
        # Arrange
        # Act
        result = convert_string_to_price('1.00000')

        # Assert
        self.assertEqual(Price('1.00000'), result)

    def test_can_convert_datetime_to_string_from_none(self):
        # Arrange
        # Act
        result = convert_datetime_to_string(None)

        # Assert
        self.assertEqual('NONE', result)

    def test_can_convert_datetime_to_string(self):
        # Arrange
        # Act
        result = convert_datetime_to_string(UNIX_EPOCH)

        # Assert
        self.assertEqual('1970-01-01T00:00:00.000Z', result)

    def test_can_convert_string_to_time_from_datetime(self):
        # Arrange
        # Act
        result = convert_string_to_datetime('1970-01-01T00:00:00.000Z')

        # Assert
        self.assertEqual(UNIX_EPOCH, result)

    def test_can_convert_string_to_time_from_none(self):
        # Arrange
        # Act
        result = convert_string_to_datetime('NONE')

        # Assert
        self.assertEqual(None, result)