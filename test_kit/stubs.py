# -------------------------------------------------------------------------------------------------
# <copyright file="stubs.py" company="Nautech Systems Pty Ltd">
#  Copyright (C) 2015-2020 Nautech Systems Pty Ltd. All rights reserved.
#  The use of this source code is governed by the license as found in the LICENSE.md file.
#  https://nautechsystems.io
# </copyright>
# -------------------------------------------------------------------------------------------------

import uuid

from datetime import datetime, timedelta, timezone

from nautilus_trader.core.types import GUID, ValidString
from nautilus_trader.common.clock import TestClock
from nautilus_trader.model.enums import (
    BarStructure,
    PriceType,
    Currency,
    SecurityType,
    AccountType,
    OrderSide)
from nautilus_trader.model.objects import (
    Quantity,
    Decimal,
    Money,
    Price,
    Tick,
    BarSpecification,
    BarType,
    Bar,
    Instrument)
from nautilus_trader.model.identifiers import (
    Venue,
    Symbol,
    IdTag,
    TraderId,
    AccountId,
    StrategyId,
    OrderIdBroker,
    ExecutionId,
    PositionIdBroker)
from nautilus_trader.model.generators import PositionIdGenerator
from nautilus_trader.model.order import Order, OrderFactory
from nautilus_trader.model.position import Position
from nautilus_trader.model.events import (
    AccountStateEvent,
    OrderInitialized,
    OrderSubmitted,
    OrderAccepted,
    OrderRejected,
    OrderWorking,
    OrderExpired,
    OrderModified,
    OrderCancelled,
    OrderCancelReject,
    OrderPartiallyFilled,
    OrderFilled,
    PositionOpened,
    PositionModified,
    PositionClosed)

# Unix epoch is the UTC time at 00:00:00 on 1/1/1970
UNIX_EPOCH = datetime(1970, 1, 1, 0, 0, 0, 0, timezone.utc)
AUDUSD_FXCM = Symbol('AUDUSD', Venue('FXCM'))
GBPUSD_FXCM = Symbol('GBPUSD', Venue('FXCM'))
USDJPY_FXCM = Symbol('USDJPY', Venue('FXCM'))


class TestStubs:

    @staticmethod
    def unix_epoch(offset_mins: int=0) -> datetime:
        """
        Generate a stub datetime based on the given offset from Unix epoch time.

        Unix time (also known as POSIX time or epoch time) is a system for
        describing instants in time, defined as the number of seconds that have
        elapsed since 00:00:00 Coordinated Universal Time (UTC), on Thursday,
        1 January 1970, minus the number of leap seconds which have taken place
        since then.

        :return The unix epoch datetime plus any offset.
        """
        return UNIX_EPOCH + timedelta(minutes=offset_mins)

    @staticmethod
    def symbol_audusd_fxcm() -> Symbol:
        return Symbol('AUDUSD', Venue('FXCM'))

    @staticmethod
    def symbol_gbpusd_fxcm() -> Symbol:
        return Symbol('GBPUSD', Venue('FXCM'))

    @staticmethod
    def symbol_usdjpy_fxcm() -> Symbol:
        return Symbol('USDJPY', Venue('FXCM'))

    @staticmethod
    def instrument_gbpusd() -> Instrument:
        return Instrument(
            Symbol('GBPUSD', Venue('FXCM')),
            'GBP/USD',
            Currency.USD,
            SecurityType.FOREX,
            tick_precision=5,
            tick_size=Decimal(0.00001, 5),
            round_lot_size=Quantity(1000),
            min_stop_distance_entry=0,
            min_limit_distance_entry=0,
            min_stop_distance=0,
            min_limit_distance=0,
            min_trade_size=Quantity(1),
            max_trade_size=Quantity(50000000),
            rollover_interest_buy=Decimal(0, 0),
            rollover_interest_sell=Decimal(0, 0),
            timestamp=UNIX_EPOCH)

    @staticmethod
    def instrument_usdjpy() -> Instrument:
        return Instrument(
            Symbol('USDJPY', Venue('FXCM')),
            'USD/JPY',
            Currency.JPY,
            SecurityType.FOREX,
            tick_precision=3,
            tick_size=Decimal(0.001, 3),
            round_lot_size=Quantity(1000),
            min_stop_distance_entry=0,
            min_limit_distance_entry=0,
            min_stop_distance=0,
            min_limit_distance=0,
            min_trade_size=Quantity(1),
            max_trade_size=Quantity(50000000),
            rollover_interest_buy=Decimal(0, 0),
            rollover_interest_sell=Decimal(0, 0),
            timestamp=UNIX_EPOCH)

    @staticmethod
    def bar_spec_1min_bid() -> BarSpecification:
        return BarSpecification(1, BarStructure.MINUTE, PriceType.BID)

    @staticmethod
    def bar_spec_1min_ask() -> BarSpecification:
        return BarSpecification(1, BarStructure.MINUTE, PriceType.ASK)

    @staticmethod
    def bar_spec_1min_mid() -> BarSpecification:
        return BarSpecification(1, BarStructure.MINUTE, PriceType.MID)

    @staticmethod
    def bar_spec_1sec_mid() -> BarSpecification:
        return BarSpecification(1, BarStructure.SECOND, PriceType.MID)

    @staticmethod
    def bartype_audusd_1min_bid() -> BarType:
        return BarType(AUDUSD_FXCM, TestStubs.bar_spec_1min_bid())

    @staticmethod
    def bartype_audusd_1min_ask() -> BarType:
        return BarType(AUDUSD_FXCM, TestStubs.bar_spec_1min_ask())

    @staticmethod
    def bartype_gbpusd_1min_bid() -> BarType:
        return BarType(GBPUSD_FXCM, TestStubs.bar_spec_1min_bid())

    @staticmethod
    def bartype_gbpusd_1min_ask() -> BarType:
        return BarType(GBPUSD_FXCM, TestStubs.bar_spec_1min_ask())

    @staticmethod
    def bartype_gbpusd_1sec_mid() -> BarType:
        return BarType(GBPUSD_FXCM, TestStubs.bar_spec_1sec_mid())

    @staticmethod
    def bartype_usdjpy_1min_bid() -> BarType:
        return BarType(USDJPY_FXCM, TestStubs.bar_spec_1min_bid())

    @staticmethod
    def bartype_usdjpy_1min_ask() -> BarType:
        return BarType(USDJPY_FXCM, TestStubs.bar_spec_1min_ask())

    @staticmethod
    def bar_5decimal() -> Bar:
        return Bar(Price(1.00002, 5),
                   Price(1.00004, 5),
                   Price(1.00001, 5),
                   Price(1.00003, 5),
                   100000,
                   UNIX_EPOCH)

    @staticmethod
    def bar_3decimal() -> Bar:
        return Bar(Price(90.002, 3),
                   Price(90.004, 3),
                   Price(90.001, 3),
                   Price(90.003, 3),
                   100000,
                   UNIX_EPOCH)

    @staticmethod
    def tick_3decimal(symbol) -> Tick:
        return Tick(symbol,
                    Price(90.002, 3),
                    Price(90.003, 3),
                    UNIX_EPOCH)

    @staticmethod
    def trader_id() -> TraderId:
        return TraderId('TESTER', '000')

    @staticmethod
    def account_id() -> AccountId:
        return AccountId('NAUTILUS', '000', AccountType.SIMULATED)

    @staticmethod
    def account_event(account_id=None) -> AccountStateEvent:
        if account_id is None:
            account_id = TestStubs.account_id()
        return AccountStateEvent(
            account_id,
            Currency.USD,
            Money(1000000),
            Money(1000000),
            Money(0),
            Money(0),
            Money(0),
            Decimal(0, 0),
            ValidString('N'),
            GUID(uuid.uuid4()),
            UNIX_EPOCH)

    @staticmethod
    def event_order_filled(order, fill_price=Price(1.00000, 5)) -> OrderFilled:
        return OrderFilled(
            TestStubs.account_id(),
            order.id,
            ExecutionId('E-' + order.id.value),
            PositionIdBroker('T-' + order.id.value),
            order.symbol,
            order.side,
            order.quantity,
            order.price if fill_price is None else fill_price,
            Currency.USD,
            UNIX_EPOCH,
            GUID(uuid.uuid4()),
            UNIX_EPOCH)

    @staticmethod
    def event_order_working(order, working_price=Price(1.00000, 5)) -> OrderWorking:
        return OrderWorking(
            TestStubs.account_id(),
            order.id,
            OrderIdBroker('B-' + order.id.value),
            order.symbol,
            order.label,
            order.side,
            order.type,
            order.quantity,
            order.price if working_price is None else working_price,
            order.time_in_force,
            UNIX_EPOCH,
            GUID(uuid.uuid4()),
            UNIX_EPOCH,
            order.expire_time)

    @staticmethod
    def event_position_opened(position) -> PositionOpened:
        return PositionOpened(
            position,
            StrategyId('SCALPER', '001'),
            position.last_event,
            GUID(uuid.uuid4()),
            UNIX_EPOCH)

    @staticmethod
    def event_position_modified(position) -> PositionModified:
        return PositionModified(
            position,
            StrategyId('SCALPER', '001'),
            position.last_event,
            GUID(uuid.uuid4()),
            UNIX_EPOCH)

    @staticmethod
    def event_position_closed(position) -> PositionClosed:
        return PositionClosed(
            position,
            StrategyId('SCALPER', '001'),
            position.last_event,
            GUID(uuid.uuid4()),
            UNIX_EPOCH)

    @staticmethod
    def position(number=1, entry_price=Price(1.00000, 5)) -> Position:
        clock = TestClock()

        generator = PositionIdGenerator(
            id_tag_trader=IdTag('001'),
            id_tag_strategy=IdTag('001'),
            clock=clock)

        for i in range(number - 1):
            generator.generate()

        order_factory = OrderFactory(
            id_tag_trader=IdTag('001'),
            id_tag_strategy=IdTag('001'),
            clock=clock)

        order = order_factory.market(
            AUDUSD_FXCM,
            OrderSide.BUY,
            Quantity(100000))

        order_filled = TestStubs.event_order_filled(order, entry_price)

        position_id = generator.generate()
        position = Position(position_id=position_id, event=order_filled)

        return position

    @staticmethod
    def position_which_is_closed(number=1, close_price=Price(1.00010, 5)) -> Position:
        clock = TestClock()

        position = TestStubs.position(number=number)

        order_factory = OrderFactory(
            id_tag_trader=IdTag('001'),
            id_tag_strategy=IdTag('001'),
            clock=clock)

        order = order_factory.market(
            AUDUSD_FXCM,
            OrderSide.SELL,
            Quantity(100000))

        order_filled = OrderFilled(
            TestStubs.account_id(),
            order.id,
            ExecutionId('E-' + order.id.value),
            PositionIdBroker('T-' + position.id.value),
            order.symbol,
            order.side,
            order.quantity,
            close_price,
            Currency.USD,
            UNIX_EPOCH + timedelta(minutes=5),
            GUID(uuid.uuid4()),
            UNIX_EPOCH + timedelta(minutes=5))

        position.apply(order_filled)

        return position
