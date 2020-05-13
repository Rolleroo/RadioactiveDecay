import re
from app.businesslogic.Nuclide import Nuclide

class DataRow:
    def __init__(self):
        self.COLUMN_NAMES = [
            'nuclide_name',
            'halflife',
            'decay_mode',
            'pointer_1',
            'pointer_2',
            'pointer_3',
            'pointer_4',
            'daughter_nuclide_1_name',
            'daughter_nuclide_1_record_i',
            'daughter_nuclide_1_branch_i',
            'daughter_nuclide_2_name',
            'daughter_nuclide_2_record_i',
            'daughter_nuclide_2_branch_i',
            'daughter_nuclide_3_name',
            'daughter_nuclide_3_record_i',
            'daughter_nuclide_3_branch_i',
            'daughter_nuclide_4_name',
            'daughter_nuclide_4_record_i',
            'daughter_nuclide_4_branch_i',
            'energy_alpha',
            'energy_electron',
            'energy_photon',
            'number_1',
            'number_2',
            'number_3',
            'number_4',
            'number_5',
            'atomic_mass',
            'air_kerma_rate_constant',
            'air_kerma_rate_coefficient'
        ]

        self.COLUMN_COL = [
            1,
            8,
            18,
            27,
            34,
            41,
            48,
            54,
            63,
            68,
            79,
            87,
            93,
            104,
            112,
            118,
            129,
            138,
            143,
            154,
            161,
            169,
            177,
            181,
            185,
            189,
            194,
            198,
            209,
            218
        ]

        self.nuclide_name = None
        self.halflife = None
        self.decay_mode = None
        self.pointer_1 = None
        self.pointer_2 = None
        self.pointer_3 = None
        self.pointer_4 = None
        self.daughter_nuclide_1_name = None
        self.daughter_nuclide_1_record_i = None
        self.daughter_nuclide_1_branch_i = None
        self.daughter_nuclide_2_name = None
        self.daughter_nuclide_2_record_i = None
        self.daughter_nuclide_2_branch_i = None
        self.daughter_nuclide_3_name = None
        self.daughter_nuclide_3_record_i = None
        self.daughter_nuclide_3_branch_i = None
        self.daughter_nuclide_4_name = None
        self.daughter_nuclide_4_record_i = None
        self.daughter_nuclide_4_branch_i = None
        self.energy_alpha = None
        self.energy_electron = None
        self.energy_photon = None
        self.number_1 = None
        self.number_2 = None
        self.number_3 = None
        self.number_4 = None
        self.number_5 = None
        self.atomic_mass = None
        self.air_kerma_rate_constant = None
        self.air_kerma_rate_coefficient = None

    def __repr__(self):
        return str(
            {
                column_name: getattr(self, column_name) 
                for column_name in self.COLUMN_NAMES
            }
        )

    def __extract_halflife(self):
        halflife_regex = r"([-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)([a-z]+)"
        halflife_groups = re.match(halflife_regex, self.halflife, re.I).groups()
        return {
            'value': float(halflife_groups[0]),
            'unit': halflife_groups[2]
        }

    def get_nuclide(self):
        extracted_halflife = self.__extract_halflife()

        nuclide = Nuclide(
            name=self.nuclide_name,
            halflife_value=extracted_halflife.get('value'),
            halflife_unit=extracted_halflife.get('unit'),
            decay_mode=self.decay_mode,
            daughter_nuclide_names=[],
            daughter_nuclide_ratios=[]
        )

        if self.daughter_nuclide_1_name:
            nuclide.daughter_nuclide_names.append(self.daughter_nuclide_1_name)
            nuclide.daughter_nuclide_ratios.append(float(self.daughter_nuclide_1_branch_i))
        if self.daughter_nuclide_2_name:
            nuclide.daughter_nuclide_names.append(self.daughter_nuclide_2_name)
            nuclide.daughter_nuclide_ratios.append(float(self.daughter_nuclide_2_branch_i))
        if self.daughter_nuclide_3_name:
            nuclide.daughter_nuclide_names.append(self.daughter_nuclide_3_name)
            nuclide.daughter_nuclide_ratios.append(float(self.daughter_nuclide_3_branch_i))
        if self.daughter_nuclide_4_name:
            nuclide.daughter_nuclide_names.append(self.daughter_nuclide_4_name)
            nuclide.daughter_nuclide_ratios.append(float(self.daughter_nuclide_4_branch_i))

        return nuclide


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.nuclides = {}

    def get_nuclides_dict(self):
        with open(self.filename, encoding='latin-1') as ro:
            for i, line in enumerate(ro.readlines()):
                # skip first line (no data)
                if i > 0:
                    self.__process_line(line)
        return self.nuclides
        
    def __process_line(self, line):
        row = DataRow()

        for i, item_start_col in enumerate(row.COLUMN_COL):
            item_end_col = row.COLUMN_COL[i+1] if (i + 1) < len(row.COLUMN_COL) else 10000
            column_name = row.COLUMN_NAMES[i]
            line_item = line[item_start_col - 1 : item_end_col - 1]
            setattr(row, column_name, line_item.strip())
        
        nuclide_name = getattr(row, row.COLUMN_NAMES[0])
        nuclide = row.get_nuclide()

        self.nuclides[nuclide_name] = nuclide
