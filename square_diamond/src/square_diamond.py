from pathlib import Path

import matplotlib.pyplot
import numpy as np
import skimage
from matplotlib.backends.backend_pdf import PdfPages
from reportlab.pdfbase.pdfdoc import PDFPages
from tqdm import tqdm


class SquareDiamondDMCColor:
    def __init__(self, floss, r, g, b):
        self.__floss = floss
        self.__rgb = [r/255, g/255, b/255]

    def color(self):
        return self.__rgb

    def floss(self):
        return self.__floss


class SquareDiamondDMCColors:
    def __init__(self):
        self.colors = [
            SquareDiamondDMCColor(3713, 255, 226, 226),
            SquareDiamondDMCColor(761, 255,	201, 201),
            SquareDiamondDMCColor(760, 245,	173, 173),
            SquareDiamondDMCColor(3712, 241, 135, 135),
            SquareDiamondDMCColor(3328, 227, 109, 109),
            SquareDiamondDMCColor(347, 191,	45,	45),

            SquareDiamondDMCColor(353, 254, 215, 204),
            SquareDiamondDMCColor(352, 253,  156, 151),
            SquareDiamondDMCColor(351, 233, 106, 103),
            SquareDiamondDMCColor(350, 224, 72, 72),
            SquareDiamondDMCColor(349, 210, 16, 53),
            SquareDiamondDMCColor(817, 187, 5, 31),
            SquareDiamondDMCColor(3708, 255, 203, 213),
            SquareDiamondDMCColor(3706, 255, 173, 188),
            SquareDiamondDMCColor(3705, 255, 121, 146),
            SquareDiamondDMCColor(3801, 231, 73, 103),
            SquareDiamondDMCColor(666, 227, 29,  66),
            SquareDiamondDMCColor(321, 199, 43,  59),
            SquareDiamondDMCColor(304, 183, 31,  51),
            SquareDiamondDMCColor(498, 167, 19,  43),
            SquareDiamondDMCColor(816, 151, 11,  35),
            SquareDiamondDMCColor(815, 135, 7,  31),
            SquareDiamondDMCColor(814, 123, 0,  27),
            SquareDiamondDMCColor(894, 255, 178,  187),
            SquareDiamondDMCColor(893, 252, 144,  162),
            SquareDiamondDMCColor(892, 255, 121,  140),
            SquareDiamondDMCColor(891, 255, 87,  115),
            SquareDiamondDMCColor(818, 255, 223,  217),
            SquareDiamondDMCColor(957, 253, 181,  181),
            SquareDiamondDMCColor(956, 255, 145,  145),
            SquareDiamondDMCColor(309, 214, 43,  91),
            SquareDiamondDMCColor(963, 255, 215,  215),
            SquareDiamondDMCColor(3716, 255,    189,    189),
            SquareDiamondDMCColor(962, 230,    138,    138),
            SquareDiamondDMCColor(961, 207,    115,    115),
            SquareDiamondDMCColor(3833, 234,    134,    153),
            SquareDiamondDMCColor(3832, 219,    85,    110),
            SquareDiamondDMCColor(3831, 179,    47,    72),
            SquareDiamondDMCColor(777, 145,    53,    70),
            SquareDiamondDMCColor(819, 255,    238,    235),
            SquareDiamondDMCColor(3326, 251,    173,    180),
            SquareDiamondDMCColor(776, 252,    176,    185),
            SquareDiamondDMCColor(899, 242,    118,    136),
            SquareDiamondDMCColor(335, 238,    84,    110),
            SquareDiamondDMCColor(326, 179,    59,    75),
            SquareDiamondDMCColor(151, 240,    206,    212),
            SquareDiamondDMCColor(3354, 228,    166,    172),
            SquareDiamondDMCColor(3733, 232,    135,    155),
            SquareDiamondDMCColor(3731, 218,    103,    131),
            SquareDiamondDMCColor(3350, 188,    67,    101),
            SquareDiamondDMCColor(150, 171, 2,    73),
            SquareDiamondDMCColor(3689, 251, 191,    194),
            SquareDiamondDMCColor(3688, 231, 169,    172),
            SquareDiamondDMCColor(3687, 201, 107,    112),
            SquareDiamondDMCColor(3803, 171, 51,    87),
            SquareDiamondDMCColor(3685, 136, 21,    49),
            SquareDiamondDMCColor(605, 255, 192,    205),
            SquareDiamondDMCColor(604, 255, 176,    190),
            SquareDiamondDMCColor(603, 255, 164,    190),
            SquareDiamondDMCColor(602, 226, 72,    116),
            SquareDiamondDMCColor(601, 209, 40,    106),
            SquareDiamondDMCColor(600, 205, 47,    99),
            SquareDiamondDMCColor(3806, 255,    140,    174),
            SquareDiamondDMCColor(3805, 243,    71,    139),
            SquareDiamondDMCColor(3804, 224,    40,   118),
            SquareDiamondDMCColor(3609, 244,    174,    213),
            SquareDiamondDMCColor(3608, 234,    156,    196),
            SquareDiamondDMCColor(3607, 197,    73,    137),
            SquareDiamondDMCColor(718, 156,    36,    98),
            SquareDiamondDMCColor(917, 155,    19,    89),
            SquareDiamondDMCColor(915, 130,    0,    67),
            SquareDiamondDMCColor(225, 255,    223,    213),
            SquareDiamondDMCColor(224, 235,    183,    175),
            SquareDiamondDMCColor(152, 226,    160,    153),
            SquareDiamondDMCColor(223, 204,    132,    124),
            SquareDiamondDMCColor(3722, 188,    108,    100),
            SquareDiamondDMCColor(3721, 161,    75,    81),
            SquareDiamondDMCColor(221, 136,    62,    67),
            SquareDiamondDMCColor(778, 223,    179,    187),
            SquareDiamondDMCColor(3727, 219,    169,    178),
            SquareDiamondDMCColor(316, 183,    115,    127),
            SquareDiamondDMCColor(3726, 155,    91,    102),
            SquareDiamondDMCColor(315, 129,    73,    82),
            SquareDiamondDMCColor(3802, 113,    65,    73),
            SquareDiamondDMCColor(902, 130,    38,    55),
            SquareDiamondDMCColor(3743, 215,    203,    211),
            SquareDiamondDMCColor(3042, 183,    157,    167),
            SquareDiamondDMCColor(3041, 149,    111,    124),
            SquareDiamondDMCColor(3740, 120,    87,    98),
            SquareDiamondDMCColor(3836, 186,    145,    170),
            SquareDiamondDMCColor(3835, 148,    96,    131),
            SquareDiamondDMCColor(3834, 114,    55,    93),
            SquareDiamondDMCColor(154, 87,    36,    51),
            SquareDiamondDMCColor(211, 227,    203,    227),
            SquareDiamondDMCColor(210, 195,    159,    195),
            SquareDiamondDMCColor(209, 163,    123,    167),
            SquareDiamondDMCColor(208, 131,    91,    139),
            SquareDiamondDMCColor(3837, 108,    58,    110),
            SquareDiamondDMCColor(327, 99,    54,    102),
            SquareDiamondDMCColor(153, 230,    204,    217),
            SquareDiamondDMCColor(554, 219,    179,    203),
            SquareDiamondDMCColor(553, 163,    99,    139),
            SquareDiamondDMCColor(552, 128,    58,    107),
            SquareDiamondDMCColor(550, 92,    24,    78),
            SquareDiamondDMCColor(3747, 211,    215,    237),
            SquareDiamondDMCColor(341, 183,    191,    221),
            SquareDiamondDMCColor(156, 163,   174,    209),
            SquareDiamondDMCColor(340, 173,    167,    199),
            SquareDiamondDMCColor(155, 152,    145,    182),
            SquareDiamondDMCColor(3746, 119,    107,    152),
            SquareDiamondDMCColor(333, 92,    84,    120),
            SquareDiamondDMCColor(157, 187,    195,    217),
            SquareDiamondDMCColor(794, 143,    156,    193),
            SquareDiamondDMCColor(793, 112,    125,    162),
            SquareDiamondDMCColor(3807, 96,    103,    140),
            SquareDiamondDMCColor(792, 85,    91,    123),
            SquareDiamondDMCColor(158, 76,    82,    110),
            SquareDiamondDMCColor(791, 70,    69,    99),
            SquareDiamondDMCColor(3840, 176,    192,    218),
            SquareDiamondDMCColor(3839, 123,    142,    171),
            SquareDiamondDMCColor(3838, 92,    114,    148),
            SquareDiamondDMCColor(800, 192,    204,    222),
            SquareDiamondDMCColor(809, 148,    168,    198),
            SquareDiamondDMCColor(799, 116,    142,    182),
            SquareDiamondDMCColor(798, 70,    106,    142),
            SquareDiamondDMCColor(797, 19,    71,    125),
            SquareDiamondDMCColor(796, 17,    65,    109),
            SquareDiamondDMCColor(820, 14,    54,    92),
            SquareDiamondDMCColor(162, 219,    236,    245),
            SquareDiamondDMCColor(827, 189,    221,    237),
            SquareDiamondDMCColor(813, 161,    194,    215),
            SquareDiamondDMCColor(826, 107,    158,    191),
            SquareDiamondDMCColor(825, 71,    129,    165),
            SquareDiamondDMCColor(824, 57,    105,    135),
            SquareDiamondDMCColor(996, 48,    194,    236),
            SquareDiamondDMCColor(3843, 20,    170,    208),
            SquareDiamondDMCColor(995, 38,    150,    182),
            SquareDiamondDMCColor(3846, 6,    227,    230),
            SquareDiamondDMCColor(3845, 4,    196,    202),
            SquareDiamondDMCColor(3844, 18,    174,    186),
            SquareDiamondDMCColor(159, 199,    202,    215),
            SquareDiamondDMCColor(160, 153,    159,    183),
            SquareDiamondDMCColor(161, 120,    128,    164),
            SquareDiamondDMCColor(3756, 238,    252,    252),
            SquareDiamondDMCColor(775, 217,    235,    241),
            SquareDiamondDMCColor(3841, 205,    223,    237),
            SquareDiamondDMCColor(3325, 184,    210,    230),
            SquareDiamondDMCColor(3755, 147,    180,    206),
            SquareDiamondDMCColor(334, 115,    159,    193),
            SquareDiamondDMCColor(322, 90,    143,    184),
            SquareDiamondDMCColor(312, 53,    102,    139),
            SquareDiamondDMCColor(803, 44,    89,    124),
            SquareDiamondDMCColor(336, 37,    59,    115),
            SquareDiamondDMCColor(823, 33,    48,    99),
            SquareDiamondDMCColor(939, 27,    40,    83),
            SquareDiamondDMCColor(3753, 219,    226,    233),
            SquareDiamondDMCColor(3752, 199,    209,    219),
            SquareDiamondDMCColor(932, 162,    181,    198),
            SquareDiamondDMCColor(931, 106,    133,    158),
            SquareDiamondDMCColor(930, 69,    92,    113),
            SquareDiamondDMCColor(3750, 56,    76,    94),
            SquareDiamondDMCColor(828, 197,    232,    237),
            SquareDiamondDMCColor(3761, 172,    216,    226),
            SquareDiamondDMCColor(519, 126,    177,    200),
            SquareDiamondDMCColor(518, 79,    147,    167),
            SquareDiamondDMCColor(3760, 62,    133,    162),
            SquareDiamondDMCColor(517, 59,    118,    143),
            SquareDiamondDMCColor(3842, 50,    102,    124),
            SquareDiamondDMCColor(311, 28,    80,    102),
            SquareDiamondDMCColor(747, 229,    252,    253),
            SquareDiamondDMCColor(3766, 153,    207,    217),
            SquareDiamondDMCColor(807, 100,    171,    186),
            SquareDiamondDMCColor(806, 61,    149,    165),
            SquareDiamondDMCColor(3765, 52,    127,    140),
            SquareDiamondDMCColor(3811, 188,    227,    230),
            SquareDiamondDMCColor(598, 144,    195,    204),
            SquareDiamondDMCColor(597, 91,    163,    179),
            SquareDiamondDMCColor(3810, 72,    142,    154),
            SquareDiamondDMCColor(3809, 63,    124,    133),
            SquareDiamondDMCColor(3808, 54,    105,    112),
            SquareDiamondDMCColor(928, 221,    227,    227),
            SquareDiamondDMCColor(927, 189,    203,    203),
            SquareDiamondDMCColor(926, 152,    174,    174),
            SquareDiamondDMCColor(3768, 101,    127,    127),
            SquareDiamondDMCColor(924, 86,    106,    106),
            SquareDiamondDMCColor(3849, 82,    179,    164),
            SquareDiamondDMCColor(3848, 85,    147,    146),
            SquareDiamondDMCColor(3847, 52,    125,    117),
            SquareDiamondDMCColor(964, 169,    226,    216),
            SquareDiamondDMCColor(959, 89,    199,    180),
            SquareDiamondDMCColor(958, 62,    182,    161),
            SquareDiamondDMCColor(3812, 47,    140,    132),
            SquareDiamondDMCColor(3851, 73,    179,    161),
            SquareDiamondDMCColor(943, 61,    147,    132),
            SquareDiamondDMCColor(3850, 55,    132,    119),
            SquareDiamondDMCColor(993, 144,    192,    180),
            SquareDiamondDMCColor(992, 111,    174,    159),
            SquareDiamondDMCColor(3814, 80,    139,    125),
            SquareDiamondDMCColor(991, 71,    123,    110),
            SquareDiamondDMCColor(966, 185,    215,    192),
            SquareDiamondDMCColor(564, 167,    205,    175),
            SquareDiamondDMCColor(563, 143,    192,    152),
            SquareDiamondDMCColor(562, 83,    151,    106),
            SquareDiamondDMCColor(505, 51,    131,    98),
            SquareDiamondDMCColor(3817, 153,    195,    170),
            SquareDiamondDMCColor(3816, 101,    165,    125),
            SquareDiamondDMCColor(163, 77,    131,    97),
            SquareDiamondDMCColor(3815, 71,    119,    89),
            SquareDiamondDMCColor(561, 44,    106,    69),
            SquareDiamondDMCColor(504, 196,    222,    204),
            SquareDiamondDMCColor(3813, 178,    212,    189),
            SquareDiamondDMCColor(503, 123,    172,    148),
            SquareDiamondDMCColor(502, 91,    144,    113),
            SquareDiamondDMCColor(501, 57,    111,    82),
            SquareDiamondDMCColor(500, 4,    77,    51),
            SquareDiamondDMCColor(955, 162,    214,    173),
            SquareDiamondDMCColor(954, 136,    186,    145),
            SquareDiamondDMCColor(913, 109,    171,    119),
            SquareDiamondDMCColor(912, 27,    157,    107),
            SquareDiamondDMCColor(911, 24,    144,    101),
            SquareDiamondDMCColor(910, 24,    126,    86),
            SquareDiamondDMCColor(909, 21,    111,    73),
            SquareDiamondDMCColor(3818, 17,    90,    59),
            SquareDiamondDMCColor(369, 215,    237,    204),
            SquareDiamondDMCColor(368, 166,    194,    152),
            SquareDiamondDMCColor(320, 105,    136,    90),
            SquareDiamondDMCColor(367, 97,    122,    82),
            SquareDiamondDMCColor(319, 32,    95,    46),
            SquareDiamondDMCColor(890, 23,    73,    35),
            SquareDiamondDMCColor(164, 200,    216,    184),
            SquareDiamondDMCColor(989, 141,    166,    117),
            SquareDiamondDMCColor(988, 115,    139,    91),
            SquareDiamondDMCColor(987, 88,    113,    65),
            SquareDiamondDMCColor(986, 64,    82,    48),
            SquareDiamondDMCColor(772, 228,    236,    212),
            SquareDiamondDMCColor(3348, 204,    217,    177),
            SquareDiamondDMCColor(3347, 113,    147,    92),
            SquareDiamondDMCColor(3346, 64,    106,    58),
            SquareDiamondDMCColor(3345, 27,    89,    21),
            SquareDiamondDMCColor(895, 27,    83,    0),
            SquareDiamondDMCColor(704, 158,    207,    52),
            SquareDiamondDMCColor(703, 123,    181,    71),
            SquareDiamondDMCColor(702, 71,    167,    47),
            SquareDiamondDMCColor(701, 63,    143,    41),
            SquareDiamondDMCColor(700, 7,    115,    27),
            SquareDiamondDMCColor(699, 5,   101,   23),
            SquareDiamondDMCColor(907, 199,    230,    102),
            SquareDiamondDMCColor(906, 127,    179,    53),
            SquareDiamondDMCColor(905, 98,    138,    40),
            SquareDiamondDMCColor(904, 85,    120,    34),
            SquareDiamondDMCColor(472, 216,    228,    152),
            SquareDiamondDMCColor(471, 174,    191,    121),
            SquareDiamondDMCColor(470, 148,    171,    79),
            SquareDiamondDMCColor(469, 114,    132,    60),
            SquareDiamondDMCColor(937, 98,    113,    51),
            SquareDiamondDMCColor(936, 76,    88,    38),
            SquareDiamondDMCColor(935, 66,    77,    33),
            SquareDiamondDMCColor(934, 49,    57,    25),
            SquareDiamondDMCColor(523, 171,    177,    151),
            SquareDiamondDMCColor(3053, 156,    164,    130),
            SquareDiamondDMCColor(3052, 136,    146,    104),
            SquareDiamondDMCColor(3051, 95,   102,    72),
            SquareDiamondDMCColor(524, 196,    205,    172),
            SquareDiamondDMCColor(522, 150,    158,    126),
            SquareDiamondDMCColor(520, 102,    109,    79),
            SquareDiamondDMCColor(3364, 131,    151,    95),
            SquareDiamondDMCColor(3363, 114,    130,    86),
            SquareDiamondDMCColor(3362, 94,    107,    71),
            SquareDiamondDMCColor(165, 239,    244,    164),
            SquareDiamondDMCColor(3819, 224,    232,    104),
            SquareDiamondDMCColor(166, 192,    200,    64),
            SquareDiamondDMCColor(581, 167,    174,    56),
            SquareDiamondDMCColor(580, 136,    141,    51),
            SquareDiamondDMCColor(734, 199,    192,    119),
            SquareDiamondDMCColor(733, 188,    179,    76),
            SquareDiamondDMCColor(732, 148,    140,    54),
            SquareDiamondDMCColor(731, 147,    139,    55),
            SquareDiamondDMCColor(730, 130,    123,    48),
            SquareDiamondDMCColor(3013, 185,    185,    130),
            SquareDiamondDMCColor(3012, 166,    167,    93),
            SquareDiamondDMCColor(3011, 137,    138,    88),
            SquareDiamondDMCColor(372, 204,    183,    132),
            SquareDiamondDMCColor(371, 191,    166,    113),
            SquareDiamondDMCColor(370, 184,    157,    100),
            SquareDiamondDMCColor(834, 219,    190,    127),
            SquareDiamondDMCColor(833, 200,    171,    108),
            SquareDiamondDMCColor(832, 189,    155,    81),
            SquareDiamondDMCColor(831, 170,    143,    86),
            SquareDiamondDMCColor(830, 141,    120,    75),
            SquareDiamondDMCColor(829, 126,    107,    66),
            SquareDiamondDMCColor(613, 220,    196,    170),
            SquareDiamondDMCColor(612, 188,    154,    120),
            SquareDiamondDMCColor(611, 150,    118,    86),
            SquareDiamondDMCColor(610, 121,    96,    71),
            SquareDiamondDMCColor(3047, 231,    214,    193),
            SquareDiamondDMCColor(3046, 216,    188,    154),
            SquareDiamondDMCColor(3045, 188,    150,    106),
            SquareDiamondDMCColor(167, 167,    124,    73),
            SquareDiamondDMCColor(746, 252,    252,    238),
            SquareDiamondDMCColor(677, 245,    236,    203),
            SquareDiamondDMCColor(422, 198,    159,    123),
            SquareDiamondDMCColor(3828, 183,    139,    97),
            SquareDiamondDMCColor(420, 160,    112,    66),
            SquareDiamondDMCColor(869, 131,    94,    57),
            SquareDiamondDMCColor(728, 228,    180,    104),
            SquareDiamondDMCColor(783, 206,    145,    36),
            SquareDiamondDMCColor(782, 174,    119,    32),
            SquareDiamondDMCColor(781, 162,    109,    32),
            SquareDiamondDMCColor(780, 148,    99,    26),
            SquareDiamondDMCColor(676, 229,    206,    151),
            SquareDiamondDMCColor(729, 208,    165,    62),
            SquareDiamondDMCColor(680, 188,    141,    14),
            SquareDiamondDMCColor(3829, 169,    130,    4),
            SquareDiamondDMCColor(3822, 246,    220,    152),
            SquareDiamondDMCColor(3821, 243,    206,    117),
            SquareDiamondDMCColor(3820, 223,    182,    95),
            SquareDiamondDMCColor(3852, 205,    157,    55),
            SquareDiamondDMCColor(445, 255,    251,    139),
            SquareDiamondDMCColor(307, 253,    237,    84),
            SquareDiamondDMCColor(973, 255,    227,    0),
            SquareDiamondDMCColor(444, 255,    214,    0),
            SquareDiamondDMCColor(3078, 253,    249,    205),
            SquareDiamondDMCColor(727, 255,    241,    175),
            SquareDiamondDMCColor(726, 253,    215,    85),
            SquareDiamondDMCColor(725, 255,    200,    64),
            SquareDiamondDMCColor(972, 255,    181,    21),
            SquareDiamondDMCColor(745, 255,    233,    173),
            SquareDiamondDMCColor(744, 255,    231,    147),
            SquareDiamondDMCColor(743, 254,    211,    118),
            SquareDiamondDMCColor(742, 255,    191,    87),
            SquareDiamondDMCColor(741, 255,    163,    43),
            SquareDiamondDMCColor(740, 255,    139,    0),
            SquareDiamondDMCColor(970, 247,    139,    19),
            SquareDiamondDMCColor(971, 246,    127,    0),
            SquareDiamondDMCColor(947, 255,    123,    77),
            SquareDiamondDMCColor(946, 235,    99,    7),
            SquareDiamondDMCColor(900, 209,    88,    7),
            SquareDiamondDMCColor(967, 255,    222,    213),
            SquareDiamondDMCColor(3824, 254,    205,    194),
            SquareDiamondDMCColor(3341, 252,    171,    152),
            SquareDiamondDMCColor(3340, 255,    131,    111),
            SquareDiamondDMCColor(608, 253,    93,    53),
            SquareDiamondDMCColor(606, 250, 50, 3),
            SquareDiamondDMCColor(951, 255,        226,        207),
            SquareDiamondDMCColor(3856, 255,        211,        181),
            SquareDiamondDMCColor(722, 247,        151,        111),
            SquareDiamondDMCColor(721, 242,        120,        66),
            SquareDiamondDMCColor(720, 229,        92,        31),
            SquareDiamondDMCColor(3825, 253,        189,        150),
            SquareDiamondDMCColor(922, 226,        115,        35),
            SquareDiamondDMCColor(921, 198,        98,        24),
            SquareDiamondDMCColor(920, 172,        84,        20),
            SquareDiamondDMCColor(919, 166,        69,        16),
            SquareDiamondDMCColor(918, 130,        52,        10),
            SquareDiamondDMCColor(3770, 255,        238,        227),
            SquareDiamondDMCColor(945, 251,        213,        187),
            SquareDiamondDMCColor(402, 247,        167,        119),
            SquareDiamondDMCColor(3776, 207,        121,        57),
            SquareDiamondDMCColor(301, 179,        95,        43),
            SquareDiamondDMCColor(400, 143,        67,        15),
            SquareDiamondDMCColor(300, 111,        47,        0),
            SquareDiamondDMCColor(3823, 255,        253,        227),
            SquareDiamondDMCColor(3855, 250,        211,        150),
            SquareDiamondDMCColor(3854, 242,        175,        104),
            SquareDiamondDMCColor(3853, 242,        151,        70),
            SquareDiamondDMCColor(3827, 247,        187,        119),
            SquareDiamondDMCColor(977, 220,        156,        86),
            SquareDiamondDMCColor(976, 194,        129,        66),
            SquareDiamondDMCColor(3826, 173,        114,        57),
            SquareDiamondDMCColor(975, 145,        79,        18),
            SquareDiamondDMCColor(948, 254,        231,        218),
            SquareDiamondDMCColor(754, 247,        203,        191),
            SquareDiamondDMCColor(3771, 244,        187,        169),
            SquareDiamondDMCColor(758, 238,        170,        155),
            SquareDiamondDMCColor(3778, 217,        137,        120),
            SquareDiamondDMCColor(356, 197,        106,        91),
            SquareDiamondDMCColor(3830, 185,        85,        68),
            SquareDiamondDMCColor(355, 152,        68,        54),
            SquareDiamondDMCColor(3777, 134,        48,        34),
            SquareDiamondDMCColor(3779, 248 ,      202 ,       200),
            SquareDiamondDMCColor(3859, 186 ,      139 ,       124),
            SquareDiamondDMCColor(3858, 150 ,      74  ,      63),
            SquareDiamondDMCColor(3857, 104 ,      37  ,      26),
            SquareDiamondDMCColor(3774,  243,       225,        215),
            SquareDiamondDMCColor(950 , 238 ,      211 ,       196),
            SquareDiamondDMCColor(3064, 196 ,      142 ,       112),
            SquareDiamondDMCColor(407 , 187 ,      129 ,       97),
            SquareDiamondDMCColor(3773, 182 ,      117 ,       82),
            SquareDiamondDMCColor(3772, 160 ,      108 ,       80),
            SquareDiamondDMCColor(632 , 135 ,      85  ,      57),
            SquareDiamondDMCColor(453 , 215 ,      206 ,       203),
            SquareDiamondDMCColor(452 , 192 ,      179 ,       174),
            SquareDiamondDMCColor(451 , 145 ,      123 ,       115),
            SquareDiamondDMCColor(3861, 166 ,      136 ,       129),
            SquareDiamondDMCColor(3860, 125 ,       93  ,      87  ),
            SquareDiamondDMCColor(779 , 98  ,      75   ,     69   ),
            SquareDiamondDMCColor(712 , 255 ,       251 ,       239),
            SquareDiamondDMCColor(739 , 248 ,       228 ,       200),
            SquareDiamondDMCColor(738 , 236 ,       204 ,       158),
            SquareDiamondDMCColor(437 , 228 ,       187 ,       142),
            SquareDiamondDMCColor(436 , 203 ,       144 ,       81 ),
            SquareDiamondDMCColor(435 , 184 ,       119 ,       72 ),
            SquareDiamondDMCColor(434 , 152 ,       94  ,      51  ),
            SquareDiamondDMCColor(433 , 122 ,       69  ,      31  ),
            SquareDiamondDMCColor(801 , 101 ,       57  ,      25  ),
            SquareDiamondDMCColor(898 , 73  ,      42   ,     19   ),
            SquareDiamondDMCColor(938 , 54  ,      31   ,     14   ),
            SquareDiamondDMCColor(3371, 30  ,      17   ,     8    ),
            SquareDiamondDMCColor(543 , 242 ,       227 ,       206),
            SquareDiamondDMCColor(3864, 203 ,       182 ,       156),
            SquareDiamondDMCColor(3863, 164 ,       131 ,       92 ),
            SquareDiamondDMCColor(3862, 138 ,       110 ,       78 ),
            SquareDiamondDMCColor(3031, 75  ,      60   ,     42   ),
            SquareDiamondDMCColor('C5200', 255 ,       255 ,       255),
            SquareDiamondDMCColor('White',252,        251,        248),
            SquareDiamondDMCColor(3865, 249,        247,        241),
            SquareDiamondDMCColor('Ecru', 240,        234,        218),
            SquareDiamondDMCColor(822, 231,        226,        211),
            SquareDiamondDMCColor(644, 221,        216,        203),
            SquareDiamondDMCColor(642, 164,        152,        120),
            SquareDiamondDMCColor(640, 133,        123,        97),
            SquareDiamondDMCColor(3787, 98,        93,        80),
            SquareDiamondDMCColor(3021, 79,        75,        65),
            SquareDiamondDMCColor(3024, 235,        234,        231),
            SquareDiamondDMCColor(3023, 177,        170,        151),
            SquareDiamondDMCColor(3022, 142,        144,        120),
            SquareDiamondDMCColor(535, 99,        100,        88),
            SquareDiamondDMCColor(3033, 227,        216,        204),
            SquareDiamondDMCColor(3782, 210,        188,        166),
            SquareDiamondDMCColor(3032, 179,        159,        139),
            SquareDiamondDMCColor(3790, 127,        106,        85),
            SquareDiamondDMCColor(3781, 107,        87,        67),
            SquareDiamondDMCColor(3866, 250,        246,        240),
            SquareDiamondDMCColor(842, 209,        186,        161),
            SquareDiamondDMCColor(841, 182,        155,        126),
            SquareDiamondDMCColor(840, 154,        124,        92),
            SquareDiamondDMCColor(839, 103,        85,        65),
            SquareDiamondDMCColor(838, 89,        73,        55),
            SquareDiamondDMCColor(3072, 230,        232,        232),
            SquareDiamondDMCColor(648, 188,        180,        172),
            SquareDiamondDMCColor(647, 176,        166,        156),
            SquareDiamondDMCColor(646, 135,        125,        115),
            SquareDiamondDMCColor(645, 110,        101,        92),
            SquareDiamondDMCColor(844, 72,        72,        72),
            SquareDiamondDMCColor(762, 236,        236,        236),
            SquareDiamondDMCColor(415, 211,        211,        214),
            SquareDiamondDMCColor(318, 171,        171,        171),
            SquareDiamondDMCColor(414, 140,        140,        140),
            SquareDiamondDMCColor(168, 209,        209,        209),
            SquareDiamondDMCColor(169, 132,        132,        132),
            SquareDiamondDMCColor(317, 108,        108,        108),
            SquareDiamondDMCColor(413, 86,       86,        86),
            SquareDiamondDMCColor(3799, 66,        66,        66),
            SquareDiamondDMCColor(310, 0,       0,       0)
        ]

    def get_colors(self):
        return [color.color() for color in self.colors]

    def get_dmc(self, index):
        return self.colors[index].floss()


class SquareDiamondPaper:
    def __init__(self, size_x_mm, size_y_mm):
        self.__size_x = size_x_mm * 3.7795275591
        self.__size_y = size_y_mm * 3.7795275591

    def size(self):
        return self.__size_y, self.__size_x


class SquareDiamond:
    def __init__(self, paper: SquareDiamondPaper):
        self.__paper = paper
        self.__square_size = 2.5

    def closest(self, colors, color):
        colors = np.array(colors)
        color = np.array(color)
        distances = np.sqrt(np.sum((colors - color) ** 2, axis=1))
        index_of_smallest = np.where(distances == np.amin(distances))
        smallest_distance = colors[index_of_smallest]
        return smallest_distance, index_of_smallest[0][0]

    def dmc_color(self):
        pass

    def load_image(self, filename, save_image):
        img_array = skimage.io.imread(filename)
        height, width, depth = img_array.shape
        # scale = self.__paper.size()[0] / width #if  self.__paper.size()[0] / width > self.__paper.size()[1] / height else self.__paper.size()[1] / height
        # print(scale)
        # img_array = skimage.transform.rescale(img_array, scale) # , channel_axis=2)
        ratio = self.__paper.size()[0] / height, self.__paper.size()[1] / width
        size = self.__paper.size()[0] * ratio[0], self.__paper.size()[1] * ratio[1]
        img_array = skimage.transform.resize(img_array, size)
        # print(img_array[0:10][0:10])
        height, width, depth = img_array.shape
        sq_size = int(self.__square_size * 3.7795275591)
        rows = int(height/sq_size)
        columns = int(width / sq_size)

        _colors = SquareDiamondDMCColors()
        colors = _colors.get_colors()
        progress = tqdm(total=rows*columns, leave=False)

        squares = []
        table_color = {}
        for row in range(rows):
            sq_row = []
            for col in range(columns):
                slic_image = skimage.segmentation.slic(img_array[row*sq_size:(row+1)*sq_size, col*sq_size:(col+1)*sq_size, :], n_segments=1, compactness=1)
                img_array[row * sq_size:(row + 1) * sq_size, col*sq_size:(col+1)*sq_size, :] = skimage.color.label2rgb(slic_image, img_array[row*sq_size:(row+1)*sq_size, col*sq_size:(col+1)*sq_size, :], kind='avg')

                color, index = self.closest(colors, img_array[row * sq_size, col*sq_size])
                sq_row.append(_colors.get_dmc(index))

                if save_image:
                    img_array[row * sq_size:(row+1) * sq_size, col*sq_size:(col+1)*sq_size] = color

                rgb = ((255*color[0][0]).astype(np.uint8) << 16) | ((255*color[0][1]).astype(np.uint8) << 8) | (255*color[0][2]).astype(np.uint8)
                if rgb not in table_color:
                    table_color[rgb] = {'color': color, 'count': 1, 'dmc': _colors.get_dmc(index)}
                else:
                    table_color[rgb]['count'] += 1

                progress.update()
            squares.append(sq_row)
            # skimage.io.imshow(img_array[row*sq_size:(row+1)*sq_size, 0:sq_size, :])
            # skimage.io.show()

        color_in_row = 4
        table = {'data':[[]], 'color':[[]], 'label': ['Color', 'DMC', 'Count',
                                                      'Color', 'DMC', 'Count',
                                                      'Color', 'DMC', 'Count',
                                                      'Color', 'DMC', 'Count']}
        for color in table_color:
            if len(table['data'][-1]) < color_in_row * 3:
                table['data'][-1].append('')
                table['data'][-1].append(table_color[color]['dmc'])
                table['data'][-1].append(table_color[color]['count'])

                table['color'][-1].append(table_color[color]['color'])
                table['color'][-1].append([1.0, 1.0, 1.0])
                table['color'][-1].append([1.0, 1.0, 1.0])
            else:
                table['data'].append([])
                table['color'].append([])

        if not len(table['data'][-1]):
            del table['data'][-1]
            del table['color'][-1]
        elif len(table['data'][-1]) < color_in_row * 3:
            table['data'][-1] += ['' for i in range(color_in_row * 3 - len(table['data'][-1]))]
            table['color'][-1] += [[1.0, 1.0, 1.0] for i in range(color_in_row * 3 - len(table['color'][-1]))]

        fig, ax = matplotlib.pyplot.subplots(figsize=(8.27,11.7))
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=table['data'], cellColours=table['color'], colLabels=table['label'])
        matplotlib.pyplot.savefig("tablepdf.pdf", bbox_inches='tight')

        pdf_file = f'{Path(filename).parent}/{Path(filename).stem}.pdf'
        with PdfPages(pdf_file) as pdf:
            row_in_page = 60
            col_in_page = 20
            full_rows = int(len(squares)/row_in_page)
            extra_rows = len(squares) - full_rows * row_in_page
            full_cols = int(len(squares[0])/col_in_page)
            extra_cols = len(squares[0]) - full_cols * col_in_page
            pages = (full_rows + 1 if extra_rows else full_rows) * (full_cols + 1 if extra_cols else full_cols)
            print(f'Pages:{pages} full_rows:{full_rows} fullcols:{full_cols} extra_rows:{extra_rows} extra_cols:{extra_cols}')
            progress = tqdm(total=pages, leave=False)
            row = 0

            fig, ax = matplotlib.pyplot.subplots(figsize=(8.27, 11.7))
            ax.axis('off')
            ax.table(cellText=table['data'], cellColours=table['color'], colLabels=table['label'], loc='top', bbox=[0, 0, 1, 1])
            pdf.savefig()
            matplotlib.pyplot.close()

            while row < len(squares):
                row_size = row_in_page
                if len(squares) - row < row_size:
                    row_size = len(squares) - row
                col = 0
                while col < len(squares[0]):
                    size = col_in_page
                    if len(squares[0]) - col < col_in_page:
                        size = len(squares[0]) - col
                    fig, ax = matplotlib.pyplot.subplots(figsize=(8.27, 11.7))
                    ax.axis('off')
                    data = [[''] + [idx for idx in range(col, col+size)]]

                    for idx in range(row_size):
                        data_row = squares[row+idx]
                        data.append([row+idx] + data_row[col:col+size])

                    ax.table(cellText=data, loc='top', bbox=[0, 0, 1, 1])
                    pdf.savefig()
                    matplotlib.pyplot.close()

                    progress.update()

                    col += size
                row += row_size

        if save_image:
            skimage.io.imsave(f'{Path(filename).parent}/{Path(filename).stem}_final.jpg', (255*img_array).astype(np.uint8))


if __name__ == "__main__":
    paper = SquareDiamondPaper(450, 300)
    prog = SquareDiamond(paper)
    # prog.load_image('../img/people.jpg', True)
    prog.load_image('../img/tree.jpg', True)