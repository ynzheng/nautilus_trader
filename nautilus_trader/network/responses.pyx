#!/usr/bin/env python3
# -------------------------------------------------------------------------------------------------
# <copyright file="responses.pyx" company="Nautech Systems Pty Ltd">
#  Copyright (C) 2015-2019 Nautech Systems Pty Ltd. All rights reserved.
#  The use of this source code is governed by the license as found in the LICENSE.md file.
#  http://www.nautechsystems.io
# </copyright>
# -------------------------------------------------------------------------------------------------

# cython: language_level=3, boundscheck=False, wraparound=False, nonecheck=False

from cpython.datetime cimport datetime

from nautilus_trader.core.message cimport Response
from nautilus_trader.model.identifiers cimport GUID


cdef class DataResponse(Response):
    """
    Represents a response of historical tick data.
    """

    def __init__(self,
                 str data_type,
                 bytearray data,
                 GUID correlation_id,
                 GUID response_id,
                 datetime response_timestamp):
        """
        Initializes a new instance of the TickDataResponse class.

        :param data_type: The response data type.
        :param data: The response data.
        :param correlation_id: The correlation identifier.
        :param response_id: The response identifier.
        :param response_timestamp: The response timestamp.
        """
        super().__init__(correlation_id, response_id, response_timestamp)
        self.data_type = data_type
        self.data = data