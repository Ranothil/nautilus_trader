# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2022 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

from typing import Literal, Optional

from ib_insync import Contract

from nautilus_trader.config import LiveDataClientConfig
from nautilus_trader.config import LiveExecClientConfig
from nautilus_trader.config.common import InstrumentFilter


class InteractiveBrokersInstrumentFilter(InstrumentFilter, frozen=True):  # type: ignore
    """Interactive brokers instrument filter"""

    secType: Optional[str] = None
    symbol: Optional[str] = None
    exchange: Optional[str] = None
    primaryExchange: Optional[str] = None
    load_futures: bool = False
    load_options: bool = False
    option_kwargs: Optional[dict] = None

    @classmethod
    def from_instrument_id(cls, value: str, **kwargs):
        local_symbol, primary_exchange = value.rsplit(".", maxsplit=1)
        return cls(symbol=local_symbol, primaryExchange=primary_exchange, **kwargs)

    @classmethod
    def stock(cls, value):
        return cls.from_instrument_id(secType="STK", value=value)

    @classmethod
    def forex(cls, value):
        return cls.from_instrument_id(secType="CASH", value=value)

    @classmethod
    def future(cls, value):
        return cls.from_instrument_id(secType="FUT", value=value)

    def to_contract(self) -> Contract:
        return Contract(
            secType=self.secType,
            symbol=self.symbol,
            exchange=self.exchange or self.primaryExchange,
            primaryExchange=self.primaryExchange,
        )


class InteractiveBrokersDataClientConfig(LiveDataClientConfig):
    """
    Configuration for ``InteractiveBrokersDataClient`` instances.

    Parameters
    ----------
    username : str, optional
        The Interactive Brokers account username.
        If ``None`` then will source the `TWS_USERNAME`
    password : str, optional
        The Interactive Brokers account password.
        If ``None`` then will source the `TWS_PASSWORD`
    account_id : str, optional
        The Interactive Brokers account id.
        If ``None`` then will source the `TWS_ACCOUNT`
    trading_mode: str
        paper or live
    account_id : str, optional
        The account_id to use for nautilus
    gateway_host : str, optional
        The hostname for the gateway server
    gateway_port : int, optional
        The port for the gateway server
    client_id: int, optional
        The client_id to be passed into connect call
    start_gateway: bool, optional
        Start or not internal tws docker container
    read_only_api: bool, optional, default True
        Read only; no execution. Set read_only_api=False to allow executing live orders
    """

    username: Optional[str] = None
    password: Optional[str] = None
    trading_mode: Literal["paper", "live"] = "paper"
    account_id: Optional[str] = None
    gateway_host: str = "127.0.0.1"
    gateway_port: Optional[int] = None
    client_id: int = 1
    start_gateway: bool = True
    read_only_api: bool = True


class InteractiveBrokersExecClientConfig(LiveExecClientConfig):
    """
    Configuration for ``InteractiveBrokersExecClient`` instances.

    Parameters
    ----------
    username : str, optional
        The Interactive Brokers account username.
        If ``None`` then will source the `TWS_USERNAME`
    password : str, optional
        The Interactive Brokers account password.
        If ``None`` then will source the `TWS_PASSWORD`
    account_id : str, optional
        The Interactive Brokers account id.
        If ``None`` then will source the `TWS_ACCOUNT`
    trading_mode: str
        paper or live
    account_id : str, optional
        The account_id to use for nautilus
    gateway_host : str, optional
        The hostname for the gateway server
    gateway_port : int, optional
        The port for the gateway server
     client_id: int, optional
        The client_id to be passed into connect call
    start_gateway: bool, optional
        Start or not internal tws docker container
    read_only_api: bool, optional, default True
        Read only; no execution. Set read_only_api=False to allow executing live orders
    """

    username: Optional[str] = None
    password: Optional[str] = None
    account_id: Optional[str] = None
    trading_mode: Literal["paper", "live"] = "paper"
    gateway_host: str = "127.0.0.1"
    gateway_port: Optional[int] = None
    client_id: int = 1
    start_gateway: bool = True
    read_only_api: bool = True
