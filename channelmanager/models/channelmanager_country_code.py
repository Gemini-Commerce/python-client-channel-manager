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


class ChannelmanagerCountryCode(str, Enum):
    """
    ChannelmanagerCountryCode
    """

    """
    allowed enum values
    """
    COUNTRY_CODE_UNKNOWN = 'COUNTRY_CODE_UNKNOWN'
    COUNTRY_CODE_AD = 'COUNTRY_CODE_AD'
    COUNTRY_CODE_AE = 'COUNTRY_CODE_AE'
    COUNTRY_CODE_AF = 'COUNTRY_CODE_AF'
    COUNTRY_CODE_AG = 'COUNTRY_CODE_AG'
    COUNTRY_CODE_AI = 'COUNTRY_CODE_AI'
    COUNTRY_CODE_AL = 'COUNTRY_CODE_AL'
    COUNTRY_CODE_AM = 'COUNTRY_CODE_AM'
    COUNTRY_CODE_AO = 'COUNTRY_CODE_AO'
    COUNTRY_CODE_AQ = 'COUNTRY_CODE_AQ'
    COUNTRY_CODE_AR = 'COUNTRY_CODE_AR'
    COUNTRY_CODE_AS = 'COUNTRY_CODE_AS'
    COUNTRY_CODE_AT = 'COUNTRY_CODE_AT'
    COUNTRY_CODE_AU = 'COUNTRY_CODE_AU'
    COUNTRY_CODE_AW = 'COUNTRY_CODE_AW'
    COUNTRY_CODE_AX = 'COUNTRY_CODE_AX'
    COUNTRY_CODE_AZ = 'COUNTRY_CODE_AZ'
    COUNTRY_CODE_BA = 'COUNTRY_CODE_BA'
    COUNTRY_CODE_BB = 'COUNTRY_CODE_BB'
    COUNTRY_CODE_BD = 'COUNTRY_CODE_BD'
    COUNTRY_CODE_BE = 'COUNTRY_CODE_BE'
    COUNTRY_CODE_BF = 'COUNTRY_CODE_BF'
    COUNTRY_CODE_BG = 'COUNTRY_CODE_BG'
    COUNTRY_CODE_BH = 'COUNTRY_CODE_BH'
    COUNTRY_CODE_BI = 'COUNTRY_CODE_BI'
    COUNTRY_CODE_BJ = 'COUNTRY_CODE_BJ'
    COUNTRY_CODE_BL = 'COUNTRY_CODE_BL'
    COUNTRY_CODE_BM = 'COUNTRY_CODE_BM'
    COUNTRY_CODE_BN = 'COUNTRY_CODE_BN'
    COUNTRY_CODE_BO = 'COUNTRY_CODE_BO'
    COUNTRY_CODE_BQ = 'COUNTRY_CODE_BQ'
    COUNTRY_CODE_BR = 'COUNTRY_CODE_BR'
    COUNTRY_CODE_BS = 'COUNTRY_CODE_BS'
    COUNTRY_CODE_BT = 'COUNTRY_CODE_BT'
    COUNTRY_CODE_BV = 'COUNTRY_CODE_BV'
    COUNTRY_CODE_BW = 'COUNTRY_CODE_BW'
    COUNTRY_CODE_BY = 'COUNTRY_CODE_BY'
    COUNTRY_CODE_BZ = 'COUNTRY_CODE_BZ'
    COUNTRY_CODE_CA = 'COUNTRY_CODE_CA'
    COUNTRY_CODE_CC = 'COUNTRY_CODE_CC'
    COUNTRY_CODE_CD = 'COUNTRY_CODE_CD'
    COUNTRY_CODE_CF = 'COUNTRY_CODE_CF'
    COUNTRY_CODE_CG = 'COUNTRY_CODE_CG'
    COUNTRY_CODE_CH = 'COUNTRY_CODE_CH'
    COUNTRY_CODE_CI = 'COUNTRY_CODE_CI'
    COUNTRY_CODE_CK = 'COUNTRY_CODE_CK'
    COUNTRY_CODE_CL = 'COUNTRY_CODE_CL'
    COUNTRY_CODE_CM = 'COUNTRY_CODE_CM'
    COUNTRY_CODE_CN = 'COUNTRY_CODE_CN'
    COUNTRY_CODE_CO = 'COUNTRY_CODE_CO'
    COUNTRY_CODE_CR = 'COUNTRY_CODE_CR'
    COUNTRY_CODE_CU = 'COUNTRY_CODE_CU'
    COUNTRY_CODE_CV = 'COUNTRY_CODE_CV'
    COUNTRY_CODE_CW = 'COUNTRY_CODE_CW'
    COUNTRY_CODE_CX = 'COUNTRY_CODE_CX'
    COUNTRY_CODE_CY = 'COUNTRY_CODE_CY'
    COUNTRY_CODE_CZ = 'COUNTRY_CODE_CZ'
    COUNTRY_CODE_DE = 'COUNTRY_CODE_DE'
    COUNTRY_CODE_DJ = 'COUNTRY_CODE_DJ'
    COUNTRY_CODE_DK = 'COUNTRY_CODE_DK'
    COUNTRY_CODE_DM = 'COUNTRY_CODE_DM'
    COUNTRY_CODE_DO = 'COUNTRY_CODE_DO'
    COUNTRY_CODE_DZ = 'COUNTRY_CODE_DZ'
    COUNTRY_CODE_EC = 'COUNTRY_CODE_EC'
    COUNTRY_CODE_EE = 'COUNTRY_CODE_EE'
    COUNTRY_CODE_EG = 'COUNTRY_CODE_EG'
    COUNTRY_CODE_EH = 'COUNTRY_CODE_EH'
    COUNTRY_CODE_ER = 'COUNTRY_CODE_ER'
    COUNTRY_CODE_ES = 'COUNTRY_CODE_ES'
    COUNTRY_CODE_ET = 'COUNTRY_CODE_ET'
    COUNTRY_CODE_FI = 'COUNTRY_CODE_FI'
    COUNTRY_CODE_FJ = 'COUNTRY_CODE_FJ'
    COUNTRY_CODE_FK = 'COUNTRY_CODE_FK'
    COUNTRY_CODE_FM = 'COUNTRY_CODE_FM'
    COUNTRY_CODE_FO = 'COUNTRY_CODE_FO'
    COUNTRY_CODE_FR = 'COUNTRY_CODE_FR'
    COUNTRY_CODE_GA = 'COUNTRY_CODE_GA'
    COUNTRY_CODE_GB = 'COUNTRY_CODE_GB'
    COUNTRY_CODE_GD = 'COUNTRY_CODE_GD'
    COUNTRY_CODE_GE = 'COUNTRY_CODE_GE'
    COUNTRY_CODE_GF = 'COUNTRY_CODE_GF'
    COUNTRY_CODE_GG = 'COUNTRY_CODE_GG'
    COUNTRY_CODE_GH = 'COUNTRY_CODE_GH'
    COUNTRY_CODE_GI = 'COUNTRY_CODE_GI'
    COUNTRY_CODE_GL = 'COUNTRY_CODE_GL'
    COUNTRY_CODE_GM = 'COUNTRY_CODE_GM'
    COUNTRY_CODE_GN = 'COUNTRY_CODE_GN'
    COUNTRY_CODE_GP = 'COUNTRY_CODE_GP'
    COUNTRY_CODE_GQ = 'COUNTRY_CODE_GQ'
    COUNTRY_CODE_GR = 'COUNTRY_CODE_GR'
    COUNTRY_CODE_GS = 'COUNTRY_CODE_GS'
    COUNTRY_CODE_GT = 'COUNTRY_CODE_GT'
    COUNTRY_CODE_GU = 'COUNTRY_CODE_GU'
    COUNTRY_CODE_GW = 'COUNTRY_CODE_GW'
    COUNTRY_CODE_GY = 'COUNTRY_CODE_GY'
    COUNTRY_CODE_HK = 'COUNTRY_CODE_HK'
    COUNTRY_CODE_HM = 'COUNTRY_CODE_HM'
    COUNTRY_CODE_HN = 'COUNTRY_CODE_HN'
    COUNTRY_CODE_HR = 'COUNTRY_CODE_HR'
    COUNTRY_CODE_HT = 'COUNTRY_CODE_HT'
    COUNTRY_CODE_HU = 'COUNTRY_CODE_HU'
    COUNTRY_CODE_ID = 'COUNTRY_CODE_ID'
    COUNTRY_CODE_IE = 'COUNTRY_CODE_IE'
    COUNTRY_CODE_IL = 'COUNTRY_CODE_IL'
    COUNTRY_CODE_IM = 'COUNTRY_CODE_IM'
    COUNTRY_CODE_IN = 'COUNTRY_CODE_IN'
    COUNTRY_CODE_IO = 'COUNTRY_CODE_IO'
    COUNTRY_CODE_IQ = 'COUNTRY_CODE_IQ'
    COUNTRY_CODE_IR = 'COUNTRY_CODE_IR'
    COUNTRY_CODE_IS = 'COUNTRY_CODE_IS'
    COUNTRY_CODE_IT = 'COUNTRY_CODE_IT'
    COUNTRY_CODE_JE = 'COUNTRY_CODE_JE'
    COUNTRY_CODE_JM = 'COUNTRY_CODE_JM'
    COUNTRY_CODE_JO = 'COUNTRY_CODE_JO'
    COUNTRY_CODE_JP = 'COUNTRY_CODE_JP'
    COUNTRY_CODE_KE = 'COUNTRY_CODE_KE'
    COUNTRY_CODE_KG = 'COUNTRY_CODE_KG'
    COUNTRY_CODE_KH = 'COUNTRY_CODE_KH'
    COUNTRY_CODE_KI = 'COUNTRY_CODE_KI'
    COUNTRY_CODE_KM = 'COUNTRY_CODE_KM'
    COUNTRY_CODE_KN = 'COUNTRY_CODE_KN'
    COUNTRY_CODE_KP = 'COUNTRY_CODE_KP'
    COUNTRY_CODE_KR = 'COUNTRY_CODE_KR'
    COUNTRY_CODE_KW = 'COUNTRY_CODE_KW'
    COUNTRY_CODE_KY = 'COUNTRY_CODE_KY'
    COUNTRY_CODE_KZ = 'COUNTRY_CODE_KZ'
    COUNTRY_CODE_LA = 'COUNTRY_CODE_LA'
    COUNTRY_CODE_LB = 'COUNTRY_CODE_LB'
    COUNTRY_CODE_LC = 'COUNTRY_CODE_LC'
    COUNTRY_CODE_LI = 'COUNTRY_CODE_LI'
    COUNTRY_CODE_LK = 'COUNTRY_CODE_LK'
    COUNTRY_CODE_LR = 'COUNTRY_CODE_LR'
    COUNTRY_CODE_LS = 'COUNTRY_CODE_LS'
    COUNTRY_CODE_LT = 'COUNTRY_CODE_LT'
    COUNTRY_CODE_LU = 'COUNTRY_CODE_LU'
    COUNTRY_CODE_LV = 'COUNTRY_CODE_LV'
    COUNTRY_CODE_LY = 'COUNTRY_CODE_LY'
    COUNTRY_CODE_MA = 'COUNTRY_CODE_MA'
    COUNTRY_CODE_MC = 'COUNTRY_CODE_MC'
    COUNTRY_CODE_MD = 'COUNTRY_CODE_MD'
    COUNTRY_CODE_ME = 'COUNTRY_CODE_ME'
    COUNTRY_CODE_MF = 'COUNTRY_CODE_MF'
    COUNTRY_CODE_MG = 'COUNTRY_CODE_MG'
    COUNTRY_CODE_MH = 'COUNTRY_CODE_MH'
    COUNTRY_CODE_MK = 'COUNTRY_CODE_MK'
    COUNTRY_CODE_ML = 'COUNTRY_CODE_ML'
    COUNTRY_CODE_MM = 'COUNTRY_CODE_MM'
    COUNTRY_CODE_MN = 'COUNTRY_CODE_MN'
    COUNTRY_CODE_MO = 'COUNTRY_CODE_MO'
    COUNTRY_CODE_MP = 'COUNTRY_CODE_MP'
    COUNTRY_CODE_MQ = 'COUNTRY_CODE_MQ'
    COUNTRY_CODE_MR = 'COUNTRY_CODE_MR'
    COUNTRY_CODE_MS = 'COUNTRY_CODE_MS'
    COUNTRY_CODE_MT = 'COUNTRY_CODE_MT'
    COUNTRY_CODE_MU = 'COUNTRY_CODE_MU'
    COUNTRY_CODE_MV = 'COUNTRY_CODE_MV'
    COUNTRY_CODE_MW = 'COUNTRY_CODE_MW'
    COUNTRY_CODE_MX = 'COUNTRY_CODE_MX'
    COUNTRY_CODE_MY = 'COUNTRY_CODE_MY'
    COUNTRY_CODE_MZ = 'COUNTRY_CODE_MZ'
    COUNTRY_CODE_NA = 'COUNTRY_CODE_NA'
    COUNTRY_CODE_NC = 'COUNTRY_CODE_NC'
    COUNTRY_CODE_NE = 'COUNTRY_CODE_NE'
    COUNTRY_CODE_NF = 'COUNTRY_CODE_NF'
    COUNTRY_CODE_NG = 'COUNTRY_CODE_NG'
    COUNTRY_CODE_NI = 'COUNTRY_CODE_NI'
    COUNTRY_CODE_NL = 'COUNTRY_CODE_NL'
    COUNTRY_CODE_NO = 'COUNTRY_CODE_NO'
    COUNTRY_CODE_NP = 'COUNTRY_CODE_NP'
    COUNTRY_CODE_NR = 'COUNTRY_CODE_NR'
    COUNTRY_CODE_NU = 'COUNTRY_CODE_NU'
    COUNTRY_CODE_NZ = 'COUNTRY_CODE_NZ'
    COUNTRY_CODE_OM = 'COUNTRY_CODE_OM'
    COUNTRY_CODE_PA = 'COUNTRY_CODE_PA'
    COUNTRY_CODE_PE = 'COUNTRY_CODE_PE'
    COUNTRY_CODE_PF = 'COUNTRY_CODE_PF'
    COUNTRY_CODE_PG = 'COUNTRY_CODE_PG'
    COUNTRY_CODE_PH = 'COUNTRY_CODE_PH'
    COUNTRY_CODE_PK = 'COUNTRY_CODE_PK'
    COUNTRY_CODE_PL = 'COUNTRY_CODE_PL'
    COUNTRY_CODE_PM = 'COUNTRY_CODE_PM'
    COUNTRY_CODE_PN = 'COUNTRY_CODE_PN'
    COUNTRY_CODE_PR = 'COUNTRY_CODE_PR'
    COUNTRY_CODE_PS = 'COUNTRY_CODE_PS'
    COUNTRY_CODE_PT = 'COUNTRY_CODE_PT'
    COUNTRY_CODE_PW = 'COUNTRY_CODE_PW'
    COUNTRY_CODE_PY = 'COUNTRY_CODE_PY'
    COUNTRY_CODE_QA = 'COUNTRY_CODE_QA'
    COUNTRY_CODE_RE = 'COUNTRY_CODE_RE'
    COUNTRY_CODE_RO = 'COUNTRY_CODE_RO'
    COUNTRY_CODE_RS = 'COUNTRY_CODE_RS'
    COUNTRY_CODE_RU = 'COUNTRY_CODE_RU'
    COUNTRY_CODE_RW = 'COUNTRY_CODE_RW'
    COUNTRY_CODE_SA = 'COUNTRY_CODE_SA'
    COUNTRY_CODE_SB = 'COUNTRY_CODE_SB'
    COUNTRY_CODE_SC = 'COUNTRY_CODE_SC'
    COUNTRY_CODE_SD = 'COUNTRY_CODE_SD'
    COUNTRY_CODE_SE = 'COUNTRY_CODE_SE'
    COUNTRY_CODE_SG = 'COUNTRY_CODE_SG'
    COUNTRY_CODE_SH = 'COUNTRY_CODE_SH'
    COUNTRY_CODE_SI = 'COUNTRY_CODE_SI'
    COUNTRY_CODE_SJ = 'COUNTRY_CODE_SJ'
    COUNTRY_CODE_SK = 'COUNTRY_CODE_SK'
    COUNTRY_CODE_SL = 'COUNTRY_CODE_SL'
    COUNTRY_CODE_SM = 'COUNTRY_CODE_SM'
    COUNTRY_CODE_SN = 'COUNTRY_CODE_SN'
    COUNTRY_CODE_SO = 'COUNTRY_CODE_SO'
    COUNTRY_CODE_SR = 'COUNTRY_CODE_SR'
    COUNTRY_CODE_SS = 'COUNTRY_CODE_SS'
    COUNTRY_CODE_ST = 'COUNTRY_CODE_ST'
    COUNTRY_CODE_SV = 'COUNTRY_CODE_SV'
    COUNTRY_CODE_SX = 'COUNTRY_CODE_SX'
    COUNTRY_CODE_SY = 'COUNTRY_CODE_SY'
    COUNTRY_CODE_SZ = 'COUNTRY_CODE_SZ'
    COUNTRY_CODE_TC = 'COUNTRY_CODE_TC'
    COUNTRY_CODE_TD = 'COUNTRY_CODE_TD'
    COUNTRY_CODE_TF = 'COUNTRY_CODE_TF'
    COUNTRY_CODE_TG = 'COUNTRY_CODE_TG'
    COUNTRY_CODE_TH = 'COUNTRY_CODE_TH'
    COUNTRY_CODE_TJ = 'COUNTRY_CODE_TJ'
    COUNTRY_CODE_TK = 'COUNTRY_CODE_TK'
    COUNTRY_CODE_TL = 'COUNTRY_CODE_TL'
    COUNTRY_CODE_TM = 'COUNTRY_CODE_TM'
    COUNTRY_CODE_TN = 'COUNTRY_CODE_TN'
    COUNTRY_CODE_TO = 'COUNTRY_CODE_TO'
    COUNTRY_CODE_TR = 'COUNTRY_CODE_TR'
    COUNTRY_CODE_TT = 'COUNTRY_CODE_TT'
    COUNTRY_CODE_TV = 'COUNTRY_CODE_TV'
    COUNTRY_CODE_TW = 'COUNTRY_CODE_TW'
    COUNTRY_CODE_TZ = 'COUNTRY_CODE_TZ'
    COUNTRY_CODE_UA = 'COUNTRY_CODE_UA'
    COUNTRY_CODE_UG = 'COUNTRY_CODE_UG'
    COUNTRY_CODE_UM = 'COUNTRY_CODE_UM'
    COUNTRY_CODE_US = 'COUNTRY_CODE_US'
    COUNTRY_CODE_UY = 'COUNTRY_CODE_UY'
    COUNTRY_CODE_UZ = 'COUNTRY_CODE_UZ'
    COUNTRY_CODE_VA = 'COUNTRY_CODE_VA'
    COUNTRY_CODE_VC = 'COUNTRY_CODE_VC'
    COUNTRY_CODE_VE = 'COUNTRY_CODE_VE'
    COUNTRY_CODE_VG = 'COUNTRY_CODE_VG'
    COUNTRY_CODE_VI = 'COUNTRY_CODE_VI'
    COUNTRY_CODE_VN = 'COUNTRY_CODE_VN'
    COUNTRY_CODE_VU = 'COUNTRY_CODE_VU'
    COUNTRY_CODE_WF = 'COUNTRY_CODE_WF'
    COUNTRY_CODE_WS = 'COUNTRY_CODE_WS'
    COUNTRY_CODE_YE = 'COUNTRY_CODE_YE'
    COUNTRY_CODE_YT = 'COUNTRY_CODE_YT'
    COUNTRY_CODE_ZA = 'COUNTRY_CODE_ZA'
    COUNTRY_CODE_ZM = 'COUNTRY_CODE_ZM'
    COUNTRY_CODE_ZW = 'COUNTRY_CODE_ZW'
    COUNTRY_CODE_XK = 'COUNTRY_CODE_XK'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ChannelmanagerCountryCode from a JSON string"""
        return cls(json.loads(json_str))


