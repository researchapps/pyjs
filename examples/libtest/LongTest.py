from UnitTest import UnitTest

class LongTest(UnitTest):

    def testAdd(self):
        x = 0
        y = 1
        x += y
        self.assertTrue(x == 1)

    def testType(self):

        # int shifted up ends up as a long
        x = 1<<64
        self.assertTrue(x == 18446744073709551616, "#302 - %s != 18446744073709551616L" % repr(x))
        self.assertTrue(isinstance(x, int))

        # long shifted up is still a long
        x = 1<<64
        self.assertTrue(x == 18446744073709551616, "%s != 18446744073709551616L" % repr(x))
        self.assertTrue(isinstance(x, int))

        x = 1<<20
        self.assertTrue(x == 1048576, "%s != 1048576" % repr(x))
        self.assertTrue(isinstance(x, int))

        x = 1<<20
        self.assertTrue(x == 1048576, "%s != 1048576L" % repr(x))
        self.assertTrue(isinstance(x, int))

        self.assertTrue(int(18446744073709551616) is 18446744073709551616, "No automatic int to long conversion")

        if int(18446744073709551616) == 18446744073709551616:
            # We do have long type

            x = 1<<64
            self.assertEqual(x, 18446744073709551616)

            x = 0x7fffffff + 1
            self.assertEqual(x, 2147483648)

            x = 0x7fffffff + 0x7fffffff
            self.assertEqual(x, 4294967294)

            x = -0x7fffffff - 2
            self.assertEqual(x, -2147483649)

            x = -0x7fffffff - 0x7fffffff
            self.assertEqual(x, -4294967294)

            x = 0x7fffffff * 2
            self.assertEqual(x, 4294967294)

            x = 0x7fffffff * -2
            self.assertEqual(x, -4294967294)

            x = 0x7ffff ** 2
            self.assertEqual(x, 274876858369)

            self.assertEqual(1 << 2, 4)
            self.assertEqual(6 >> 2, 1)

            x = 1
            x <<= 3
            self.assertEqual(x, 8)
            x = 8
            x >>= 1
            self.assertEqual(x, 4)

