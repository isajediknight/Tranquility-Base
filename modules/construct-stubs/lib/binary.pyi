def integer2bits(number: int, width: int, signed: bool = ...) -> bytes: ...
def integer2bytes(number: int, width: int, signed: bool = ...) -> bytes: ...
def bits2integer(data: bytes, signed: bool = ...) -> int: ...
def bytes2integer(data: bytes, signed: bool = ...) -> int: ...
def bytes2bits(data: bytes) -> bytes: ...
def bits2bytes(data: bytes) -> bytes: ...
def swapbytes(data: bytes) -> bytes: ...
def swapbytesinbits(data: bytes) -> bytes: ...
def swapbitsinbytes(data: bytes) -> bytes: ...
def hexlify(data: bytes) -> bytes: ...
def unhexlify(data: bytes) -> bytes: ...
