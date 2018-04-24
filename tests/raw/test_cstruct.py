import unittest

from powerpy.raw import *

DOS_MAGIC = 0x4D5A
DOS_CIGAM = 0x5A4D
DOS_HEADER = b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00\x00\x00\x00\x00\x00\x00@\x00\x00' \
             b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
             b'\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00'


class DosHeaderParser(metaclass=CStruct):
    e_magic = USHORT  # 00: MZ Header signature
    e_cblp = USHORT  # 02: Bytes on last page of file
    e_cp = USHORT  # 04: Pages in file
    e_crlc = USHORT  # 06: Relocations
    e_cparhdr = USHORT  # 08: Size of header in paragraphs
    e_minalloc = USHORT  # 0a: Minimum extra paragraphs needed
    e_maxalloc = USHORT  # 0c: Maximum extra paragraphs needed
    e_ss = USHORT  # 0e: Initial (relative) SS value
    e_sp = USHORT  # 10: Initial SP value
    e_csum = USHORT  # 12: Checksum
    e_ip = USHORT  # 14: Initial IP value
    e_cs = USHORT  # 16: Initial (relative) CS value
    e_lfarlc = USHORT  # 18: File address of relocation table
    e_ovno = USHORT  # 1a: Overlay number
    e_res = "8s"  # 1c: Reserved words
    e_oemid = USHORT  # 24: OEM identifier (for e_oeminfo)
    e_oeminfo = USHORT  # 26: OEM information=0 e_oemid specific
    e_res2 = "20s"  # 28: Reserved words
    e_lfanew = "I"  # 3c: Offset to extended header


class TestCStruct(unittest.TestCase):
    def setUp(self):
        endianness = struct.unpack("H", DOS_HEADER[0:2])[0]
        self.header = DosHeaderParser()
        self.header.set_endianness('big' if endianness == DOS_MAGIC else 'little')

    def test_cstruct_base(self):
        self.header.unpack(DOS_HEADER)
        self.assertTrue(self.header.e_magic == DOS_MAGIC or self.header.e_magic == DOS_CIGAM)
        self.assertEqual(self.header.e_cblp, 144)
        self.assertEqual(len(self.header.e_res), 8)
        self.assertEqual(self.header.e_maxalloc, 65535)
        self.assertEqual(self.header.e_lfanew, 248)

    def test_cstruct_packer(self):
        self.header.unpack(DOS_HEADER)
        bytez = bytes(self.header)
        self.assertEqual(bytez, DOS_HEADER)
