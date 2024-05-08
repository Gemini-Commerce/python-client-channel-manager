# coding: utf-8

"""
    Channel Manager Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ChannelmanagerLanguageCode(str, Enum):
    """
    ChannelmanagerLanguageCode
    """

    """
    allowed enum values
    """
    LANGUAGE_CODE_UNKNOWN = 'LANGUAGE_CODE_UNKNOWN'
    LANGUAGE_CODE_AA = 'LANGUAGE_CODE_AA'
    LANGUAGE_CODE_AB = 'LANGUAGE_CODE_AB'
    LANGUAGE_CODE_AE = 'LANGUAGE_CODE_AE'
    LANGUAGE_CODE_AF = 'LANGUAGE_CODE_AF'
    LANGUAGE_CODE_AK = 'LANGUAGE_CODE_AK'
    LANGUAGE_CODE_AM = 'LANGUAGE_CODE_AM'
    LANGUAGE_CODE_AN = 'LANGUAGE_CODE_AN'
    LANGUAGE_CODE_AR = 'LANGUAGE_CODE_AR'
    LANGUAGE_CODE_AS = 'LANGUAGE_CODE_AS'
    LANGUAGE_CODE_AV = 'LANGUAGE_CODE_AV'
    LANGUAGE_CODE_AY = 'LANGUAGE_CODE_AY'
    LANGUAGE_CODE_AZ = 'LANGUAGE_CODE_AZ'
    LANGUAGE_CODE_BA = 'LANGUAGE_CODE_BA'
    LANGUAGE_CODE_BE = 'LANGUAGE_CODE_BE'
    LANGUAGE_CODE_BG = 'LANGUAGE_CODE_BG'
    LANGUAGE_CODE_BH = 'LANGUAGE_CODE_BH'
    LANGUAGE_CODE_BM = 'LANGUAGE_CODE_BM'
    LANGUAGE_CODE_BI = 'LANGUAGE_CODE_BI'
    LANGUAGE_CODE_BN = 'LANGUAGE_CODE_BN'
    LANGUAGE_CODE_BO = 'LANGUAGE_CODE_BO'
    LANGUAGE_CODE_BR = 'LANGUAGE_CODE_BR'
    LANGUAGE_CODE_BS = 'LANGUAGE_CODE_BS'
    LANGUAGE_CODE_CA = 'LANGUAGE_CODE_CA'
    LANGUAGE_CODE_CE = 'LANGUAGE_CODE_CE'
    LANGUAGE_CODE_CH = 'LANGUAGE_CODE_CH'
    LANGUAGE_CODE_CO = 'LANGUAGE_CODE_CO'
    LANGUAGE_CODE_CR = 'LANGUAGE_CODE_CR'
    LANGUAGE_CODE_CS = 'LANGUAGE_CODE_CS'
    LANGUAGE_CODE_CU = 'LANGUAGE_CODE_CU'
    LANGUAGE_CODE_CV = 'LANGUAGE_CODE_CV'
    LANGUAGE_CODE_CY = 'LANGUAGE_CODE_CY'
    LANGUAGE_CODE_DA = 'LANGUAGE_CODE_DA'
    LANGUAGE_CODE_DE = 'LANGUAGE_CODE_DE'
    LANGUAGE_CODE_DV = 'LANGUAGE_CODE_DV'
    LANGUAGE_CODE_DZ = 'LANGUAGE_CODE_DZ'
    LANGUAGE_CODE_EE = 'LANGUAGE_CODE_EE'
    LANGUAGE_CODE_EL = 'LANGUAGE_CODE_EL'
    LANGUAGE_CODE_EN = 'LANGUAGE_CODE_EN'
    LANGUAGE_CODE_EO = 'LANGUAGE_CODE_EO'
    LANGUAGE_CODE_ES = 'LANGUAGE_CODE_ES'
    LANGUAGE_CODE_ET = 'LANGUAGE_CODE_ET'
    LANGUAGE_CODE_EU = 'LANGUAGE_CODE_EU'
    LANGUAGE_CODE_FA = 'LANGUAGE_CODE_FA'
    LANGUAGE_CODE_FF = 'LANGUAGE_CODE_FF'
    LANGUAGE_CODE_FI = 'LANGUAGE_CODE_FI'
    LANGUAGE_CODE_FJ = 'LANGUAGE_CODE_FJ'
    LANGUAGE_CODE_FO = 'LANGUAGE_CODE_FO'
    LANGUAGE_CODE_FR = 'LANGUAGE_CODE_FR'
    LANGUAGE_CODE_FY = 'LANGUAGE_CODE_FY'
    LANGUAGE_CODE_GA = 'LANGUAGE_CODE_GA'
    LANGUAGE_CODE_GD = 'LANGUAGE_CODE_GD'
    LANGUAGE_CODE_GL = 'LANGUAGE_CODE_GL'
    LANGUAGE_CODE_GN = 'LANGUAGE_CODE_GN'
    LANGUAGE_CODE_GU = 'LANGUAGE_CODE_GU'
    LANGUAGE_CODE_GV = 'LANGUAGE_CODE_GV'
    LANGUAGE_CODE_HA = 'LANGUAGE_CODE_HA'
    LANGUAGE_CODE_HE = 'LANGUAGE_CODE_HE'
    LANGUAGE_CODE_HI = 'LANGUAGE_CODE_HI'
    LANGUAGE_CODE_HO = 'LANGUAGE_CODE_HO'
    LANGUAGE_CODE_HR = 'LANGUAGE_CODE_HR'
    LANGUAGE_CODE_HT = 'LANGUAGE_CODE_HT'
    LANGUAGE_CODE_HU = 'LANGUAGE_CODE_HU'
    LANGUAGE_CODE_HY = 'LANGUAGE_CODE_HY'
    LANGUAGE_CODE_HZ = 'LANGUAGE_CODE_HZ'
    LANGUAGE_CODE_IA = 'LANGUAGE_CODE_IA'
    LANGUAGE_CODE_ID = 'LANGUAGE_CODE_ID'
    LANGUAGE_CODE_IE = 'LANGUAGE_CODE_IE'
    LANGUAGE_CODE_IG = 'LANGUAGE_CODE_IG'
    LANGUAGE_CODE_II = 'LANGUAGE_CODE_II'
    LANGUAGE_CODE_IK = 'LANGUAGE_CODE_IK'
    LANGUAGE_CODE_IO = 'LANGUAGE_CODE_IO'
    LANGUAGE_CODE_IS = 'LANGUAGE_CODE_IS'
    LANGUAGE_CODE_IT = 'LANGUAGE_CODE_IT'
    LANGUAGE_CODE_IU = 'LANGUAGE_CODE_IU'
    LANGUAGE_CODE_JA = 'LANGUAGE_CODE_JA'
    LANGUAGE_CODE_JV = 'LANGUAGE_CODE_JV'
    LANGUAGE_CODE_KA = 'LANGUAGE_CODE_KA'
    LANGUAGE_CODE_KG = 'LANGUAGE_CODE_KG'
    LANGUAGE_CODE_KI = 'LANGUAGE_CODE_KI'
    LANGUAGE_CODE_KJ = 'LANGUAGE_CODE_KJ'
    LANGUAGE_CODE_KK = 'LANGUAGE_CODE_KK'
    LANGUAGE_CODE_KL = 'LANGUAGE_CODE_KL'
    LANGUAGE_CODE_KM = 'LANGUAGE_CODE_KM'
    LANGUAGE_CODE_KN = 'LANGUAGE_CODE_KN'
    LANGUAGE_CODE_KO = 'LANGUAGE_CODE_KO'
    LANGUAGE_CODE_KR = 'LANGUAGE_CODE_KR'
    LANGUAGE_CODE_KS = 'LANGUAGE_CODE_KS'
    LANGUAGE_CODE_KU = 'LANGUAGE_CODE_KU'
    LANGUAGE_CODE_KV = 'LANGUAGE_CODE_KV'
    LANGUAGE_CODE_KW = 'LANGUAGE_CODE_KW'
    LANGUAGE_CODE_KY = 'LANGUAGE_CODE_KY'
    LANGUAGE_CODE_LA = 'LANGUAGE_CODE_LA'
    LANGUAGE_CODE_LB = 'LANGUAGE_CODE_LB'
    LANGUAGE_CODE_LG = 'LANGUAGE_CODE_LG'
    LANGUAGE_CODE_LI = 'LANGUAGE_CODE_LI'
    LANGUAGE_CODE_LN = 'LANGUAGE_CODE_LN'
    LANGUAGE_CODE_LO = 'LANGUAGE_CODE_LO'
    LANGUAGE_CODE_LT = 'LANGUAGE_CODE_LT'
    LANGUAGE_CODE_LU = 'LANGUAGE_CODE_LU'
    LANGUAGE_CODE_LV = 'LANGUAGE_CODE_LV'
    LANGUAGE_CODE_MG = 'LANGUAGE_CODE_MG'
    LANGUAGE_CODE_MH = 'LANGUAGE_CODE_MH'
    LANGUAGE_CODE_MI = 'LANGUAGE_CODE_MI'
    LANGUAGE_CODE_MK = 'LANGUAGE_CODE_MK'
    LANGUAGE_CODE_ML = 'LANGUAGE_CODE_ML'
    LANGUAGE_CODE_MN = 'LANGUAGE_CODE_MN'
    LANGUAGE_CODE_MR = 'LANGUAGE_CODE_MR'
    LANGUAGE_CODE_MS = 'LANGUAGE_CODE_MS'
    LANGUAGE_CODE_MT = 'LANGUAGE_CODE_MT'
    LANGUAGE_CODE_MY = 'LANGUAGE_CODE_MY'
    LANGUAGE_CODE_NA = 'LANGUAGE_CODE_NA'
    LANGUAGE_CODE_NB = 'LANGUAGE_CODE_NB'
    LANGUAGE_CODE_ND = 'LANGUAGE_CODE_ND'
    LANGUAGE_CODE_NE = 'LANGUAGE_CODE_NE'
    LANGUAGE_CODE_NG = 'LANGUAGE_CODE_NG'
    LANGUAGE_CODE_NL = 'LANGUAGE_CODE_NL'
    LANGUAGE_CODE_NN = 'LANGUAGE_CODE_NN'
    LANGUAGE_CODE_NO = 'LANGUAGE_CODE_NO'
    LANGUAGE_CODE_NR = 'LANGUAGE_CODE_NR'
    LANGUAGE_CODE_NV = 'LANGUAGE_CODE_NV'
    LANGUAGE_CODE_NY = 'LANGUAGE_CODE_NY'
    LANGUAGE_CODE_OC = 'LANGUAGE_CODE_OC'
    LANGUAGE_CODE_OJ = 'LANGUAGE_CODE_OJ'
    LANGUAGE_CODE_OM = 'LANGUAGE_CODE_OM'
    LANGUAGE_CODE_OR = 'LANGUAGE_CODE_OR'
    LANGUAGE_CODE_OS = 'LANGUAGE_CODE_OS'
    LANGUAGE_CODE_PA = 'LANGUAGE_CODE_PA'
    LANGUAGE_CODE_PI = 'LANGUAGE_CODE_PI'
    LANGUAGE_CODE_PL = 'LANGUAGE_CODE_PL'
    LANGUAGE_CODE_PS = 'LANGUAGE_CODE_PS'
    LANGUAGE_CODE_PT = 'LANGUAGE_CODE_PT'
    LANGUAGE_CODE_QU = 'LANGUAGE_CODE_QU'
    LANGUAGE_CODE_RM = 'LANGUAGE_CODE_RM'
    LANGUAGE_CODE_RN = 'LANGUAGE_CODE_RN'
    LANGUAGE_CODE_RO = 'LANGUAGE_CODE_RO'
    LANGUAGE_CODE_RU = 'LANGUAGE_CODE_RU'
    LANGUAGE_CODE_RW = 'LANGUAGE_CODE_RW'
    LANGUAGE_CODE_SA = 'LANGUAGE_CODE_SA'
    LANGUAGE_CODE_SC = 'LANGUAGE_CODE_SC'
    LANGUAGE_CODE_SD = 'LANGUAGE_CODE_SD'
    LANGUAGE_CODE_SE = 'LANGUAGE_CODE_SE'
    LANGUAGE_CODE_SG = 'LANGUAGE_CODE_SG'
    LANGUAGE_CODE_SI = 'LANGUAGE_CODE_SI'
    LANGUAGE_CODE_SK = 'LANGUAGE_CODE_SK'
    LANGUAGE_CODE_SL = 'LANGUAGE_CODE_SL'
    LANGUAGE_CODE_SM = 'LANGUAGE_CODE_SM'
    LANGUAGE_CODE_SN = 'LANGUAGE_CODE_SN'
    LANGUAGE_CODE_SO = 'LANGUAGE_CODE_SO'
    LANGUAGE_CODE_SQ = 'LANGUAGE_CODE_SQ'
    LANGUAGE_CODE_SR = 'LANGUAGE_CODE_SR'
    LANGUAGE_CODE_SS = 'LANGUAGE_CODE_SS'
    LANGUAGE_CODE_ST = 'LANGUAGE_CODE_ST'
    LANGUAGE_CODE_SU = 'LANGUAGE_CODE_SU'
    LANGUAGE_CODE_SV = 'LANGUAGE_CODE_SV'
    LANGUAGE_CODE_SW = 'LANGUAGE_CODE_SW'
    LANGUAGE_CODE_TA = 'LANGUAGE_CODE_TA'
    LANGUAGE_CODE_TE = 'LANGUAGE_CODE_TE'
    LANGUAGE_CODE_TG = 'LANGUAGE_CODE_TG'
    LANGUAGE_CODE_TH = 'LANGUAGE_CODE_TH'
    LANGUAGE_CODE_TI = 'LANGUAGE_CODE_TI'
    LANGUAGE_CODE_TK = 'LANGUAGE_CODE_TK'
    LANGUAGE_CODE_TL = 'LANGUAGE_CODE_TL'
    LANGUAGE_CODE_TN = 'LANGUAGE_CODE_TN'
    LANGUAGE_CODE_TO = 'LANGUAGE_CODE_TO'
    LANGUAGE_CODE_TR = 'LANGUAGE_CODE_TR'
    LANGUAGE_CODE_TS = 'LANGUAGE_CODE_TS'
    LANGUAGE_CODE_TT = 'LANGUAGE_CODE_TT'
    LANGUAGE_CODE_TW = 'LANGUAGE_CODE_TW'
    LANGUAGE_CODE_TY = 'LANGUAGE_CODE_TY'
    LANGUAGE_CODE_UG = 'LANGUAGE_CODE_UG'
    LANGUAGE_CODE_UK = 'LANGUAGE_CODE_UK'
    LANGUAGE_CODE_UR = 'LANGUAGE_CODE_UR'
    LANGUAGE_CODE_UZ = 'LANGUAGE_CODE_UZ'
    LANGUAGE_CODE_VE = 'LANGUAGE_CODE_VE'
    LANGUAGE_CODE_VI = 'LANGUAGE_CODE_VI'
    LANGUAGE_CODE_VO = 'LANGUAGE_CODE_VO'
    LANGUAGE_CODE_WA = 'LANGUAGE_CODE_WA'
    LANGUAGE_CODE_WO = 'LANGUAGE_CODE_WO'
    LANGUAGE_CODE_XH = 'LANGUAGE_CODE_XH'
    LANGUAGE_CODE_YI = 'LANGUAGE_CODE_YI'
    LANGUAGE_CODE_YO = 'LANGUAGE_CODE_YO'
    LANGUAGE_CODE_ZA = 'LANGUAGE_CODE_ZA'
    LANGUAGE_CODE_ZH = 'LANGUAGE_CODE_ZH'
    LANGUAGE_CODE_ZU = 'LANGUAGE_CODE_ZU'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ChannelmanagerLanguageCode from a JSON string"""
        return cls(json.loads(json_str))

