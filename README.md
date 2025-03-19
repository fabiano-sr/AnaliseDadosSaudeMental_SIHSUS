# AnaliseDadosSaudeMental_SIHSUS

### Introdução
---

### Extração dos Dados
---

### Análise Exploratória
---
1. Unificação dos dados em data frame utilizando pandas.
2. Realizada verificação dos campos que continham o mesmo valor em todos os registros.
    > _Foram identificados 31 campos, destes X estavam evidenciados nos metadados._
    > |   Campo    |  Valor Constante  |   |   Campo    |  Valor Constante  |
    > |-----------:|:-----------------:| - |-----------:|:-----------------:|
    > | UTI_MES_IN |      [' 0']       |   | UTI_MES_AN |      [' 0']       |
    > | UTI_MES_AL |      [' 0']       |   | UTI_INT_IN |      [' 0']       |
    > | UTI_INT_AN |      [' 0']       |   | UTI_INT_AL |      [' 0']       |
    > | VAL_SADT   |     [' 0.00']     |   | VAL_RN     |     [' 0.00']     |
    > | VAL_ACOMP  |     [' 0.00']     |   | VAL_ORTP   |     [' 0.00']     |
    > | VAL_SANGUE |     [' 0.00']     |   | VAL_SADTSR |     [' 0.00']     |
    > | VAL_TRANSP |     [' 0.00']     |   | VAL_OBSANG |     [' 0.00']     |
    > | VAL_PED1AC |     [' 0.00']     |   | DIAG_SECUN |     ['0000']      |
    > | NATUREZA   |     ['00']        |   | RUBRICA    |     [' 0']        |
    > | NUM_PROC   |     ['']          |   | TOT_PT_SP  |     [' 0']        |
    > | CPF_AUT    |     ['']          |   | SEQ_AIH5   |     ['000']       |
    > | CBOR       |     ['000000']    |   | CNAER      |     ['000']       |
    > | VINCPREV   |     ['0']         |   | GESTOR_DT  |     ['']          |
    > | INFEHOSP   |     ['']          |   | CID_ASSO   |     ['0000']      |
    > | CID_MORTE  |     ['0000']      |   | VAL_SH_GES |     [' 0.00']     |
    > | VAL_SP_GES |     [' 0.00']     |

3. Realizada verificação dos campos que continham prevalência maior de 95% de registros com o mesmo valor.
    > _Foram identificados 31 campos, destes X estavam evidenciados nos metadados._
    > |   Campo    | % Prevalente | Valor Prevalente |   |   Campo    | % Prevalente | Valor Prevalente |
    > |------------|--------------|------------------|   |------------|--------------|------------------|
    > | UTI_MES_TO |   99.9043    |      ["0"]       |   | MARCA_UTI  |   99.9043    |      ["00"]      |
    > | UTI_INT_TO |   99.9994    |      ["0"]       |   | DIAR_ACOM  |   96.1405    |      ["0"]       |
    > | VAL_UTI    |   99.9043    |     ["0.00"]     |   | IND_VDRL   |   99.9419    |      ["0"]       |
    > | MORTE      |   99.8498    |      ["0"]       |   | HOMONIMO   |   99.9893    |      ["0"]       |
    > | NUM_FILHOS |   99.9997    |      ["0"]       |   | INSTRU     |   99.9997    |      ["0"]       |
    > | CID_NOTIF  |   99.9997    |      [""]        |   | CONTRACEP1 |   99.9997    |      ["00"]      |
    > | CONTRACEP2 |   99.9997    |      ["00"]      |   | GESTRISCO  |   99.9997    |      ["1"]       |
    > | INSC_PN    |   99.9985    | ["000000000000"] |   | GESTOR_COD |   99.2392    |   ["00000"]      |
    > | COMPLEX    |   99.9979    |      ["02"]      |   | FINANC     |   99.9985    |      ["06"]      |
    > | FAEC_TP    |   99.9985    |      [""]        |   | ETNIA      |   99.9908    |    ["0000"]      |
    > | AUD_JUST   |   99.8743    |      [""]        |   | SIS_JUST   |    99.877    |      [""]        |
    > | VAL_SH_FED |   99.9997    |     ["0.00"]     |   | VAL_SP_FED |   99.9997    |     ["0.00"]     |
    > | VAL_UCI    |   99.9994    |     ["0.00"]     |   | MARCA_UCI  |   99.9994    |      ["00"]      |
    > | DIAGSEC2   |   97.7226    |      [""]        |   | DIAGSEC3   |   99.3806    |      [""]        |
    > | DIAGSEC4   |   99.7923    |      [""]        |   | DIAGSEC5   |   99.9192    |      [""]        |
    > | DIAGSEC6   |   99.9746    |      [""]        |   | DIAGSEC7   |   99.9948    |      [""]        |
    > | DIAGSEC8   |   99.9997    |      [""]        |   | DIAGSEC9   |   99.9997    |      [""]        |
    > | TPDISEC2   |   97.7226    |      ["0"]       |   | TPDISEC3   |   99.3806    |      ["0"]       |
    > | TPDISEC4   |   99.7923    |      ["0"]       |   | TPDISEC5   |   99.9192    |      ["0"]       |
    > | TPDISEC6   |   99.9746    |      ["0"]       |   | TPDISEC7   |   99.9948    |      ["0"]       |
    > | TPDISEC8   |   99.9997    |      ["0"]       |   | TPDISEC9   |   99.9997    |      ["0"]       |


