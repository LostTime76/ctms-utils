import config
import time
from pathlib import Path

from ctms.utils import bitops
from ctms.utils.coff import CoffImage, CoffSection

fpath = Path(Path(__file__).parent, 'test.out')

t1 = time.perf_counter_ns()

i = CoffImage(bytearray(fpath.read_bytes()))

b = bytearray(0x90000 << 1)

cs = i.sects['scn']

cs.write_n32(2, 0xdeadbeef)

i.sects.copy_to(0x80000 << 1, b)

bitops.rev16(b)

c = bitops.crc32(b)

t2 = time.perf_counter_ns()

print((t2 - t1) / 1000000)