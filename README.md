# AnaliseDadosSaudeMental_SIHSUS

### Introdução
---

### Extração dos Dados
---

### Análise Exploratória
---
**1. Importação da base de dados em formato Parquet e carregamento no dataframe com a biblioteca Pandas.**
   > _O dataframe resultante possui 326.910 registros e 113 colunas._

**2. Verificação das colunas com valores constantes em todos os registros.**
   > _Foram identificados 31 campos, dos quais X estavam evidenciados nos metadados._

    |   Campo    |  Valor Constante  |   |   Campo    |  Valor Constante  |
    |:----------:|:-----------------:| - |:----------:|:-----------------:|
    | UTI_MES_IN |      [' 0']       |   | UTI_MES_AN |      [' 0']       |
    | UTI_MES_AL |      [' 0']       |   | UTI_INT_IN |      [' 0']       |
    | UTI_INT_AN |      [' 0']       |   | UTI_INT_AL |      [' 0']       |
    | VAL_SADT   |     [' 0.00']     |   | VAL_RN     |     [' 0.00']     |
    | VAL_ACOMP  |     [' 0.00']     |   | VAL_ORTP   |     [' 0.00']     |
    | VAL_SANGUE |     [' 0.00']     |   | VAL_SADTSR |     [' 0.00']     |
    | VAL_TRANSP |     [' 0.00']     |   | VAL_OBSANG |     [' 0.00']     |
    | VAL_PED1AC |     [' 0.00']     |   | DIAG_SECUN |     ['0000']      |
    | NATUREZA   |     ['00']        |   | RUBRICA    |     [' 0']        |
    | NUM_PROC   |     ['']          |   | TOT_PT_SP  |     [' 0']        |
    | CPF_AUT    |     ['']          |   | SEQ_AIH5   |     ['000']       |
    | CBOR       |     ['000000']    |   | CNAER      |     ['000']       |
    | VINCPREV   |     ['0']         |   | GESTOR_DT  |     ['']          |
    | INFEHOSP   |     ['']          |   | CID_ASSO   |     ['0000']      |
    | CID_MORTE  |     ['0000']      |   | VAL_SH_GES |     [' 0.00']     |
    | VAL_SP_GES |     [' 0.00']     |

**3. Verificação dos campos com prevalência superior a 95% de registros com o mesmo valor.**
   > _Foram identificados 42 campos que atendem a essa condição._

    |   Campo    | % Prevalente | Valor Prevalente |   |   Campo    | % Prevalente | Valor Prevalente |
    |:----------:|:------------:|:----------------:| - |:----------:|:------------:|:----------------:|
    | UTI_MES_TO |   99.9043    |      ['0']       |   | MARCA_UTI  |   99.9043    |      ['00']      |
    | UTI_INT_TO |   99.9994    |      ['0']       |   | DIAR_ACOM  |   96.1405    |      ['0']       |
    | VAL_UTI    |   99.9043    |     ['0.00']     |   | IND_VDRL   |   99.9419    |      ['0']       |
    | MORTE      |   99.8498    |      ['0']       |   | HOMONIMO   |   99.9893    |      ['0']       |
    | NUM_FILHOS |   99.9997    |      ['0']       |   | INSTRU     |   99.9997    |      ['0']       |
    | CID_NOTIF  |   99.9997    |      ['']        |   | CONTRACEP1 |   99.9997    |      ['00']      |
    | CONTRACEP2 |   99.9997    |      ['00']      |   | GESTRISCO  |   99.9997    |      ['1']       |
    | INSC_PN    |   99.9985    | ['000000000000'] |   | GESTOR_COD |   99.2392    |   ['00000']      |
    | COMPLEX    |   99.9979    |      ['02']      |   | FINANC     |   99.9985    |      ['06']      |
    | FAEC_TP    |   99.9985    |      ['']        |   | ETNIA      |   99.9908    |    ['0000']      |
    | AUD_JUST   |   99.8743    |      ['']        |   | SIS_JUST   |    99.877    |      ['']        |
    | VAL_SH_FED |   99.9997    |     ['0.00']     |   | VAL_SP_FED |   99.9997    |     ['0.00']     |
    | VAL_UCI    |   99.9994    |     ['0.00']     |   | MARCA_UCI  |   99.9994    |      ['00']      |
    | DIAGSEC2   |   97.7226    |      ['']        |   | DIAGSEC3   |   99.3806    |      ['']        |
    | DIAGSEC4   |   99.7923    |      ['']        |   | DIAGSEC5   |   99.9192    |      ['']        |
    | DIAGSEC6   |   99.9746    |      ['']        |   | DIAGSEC7   |   99.9948    |      ['']        |
    | DIAGSEC8   |   99.9997    |      ['']        |   | DIAGSEC9   |   99.9997    |      ['']        |
    | TPDISEC2   |   97.7226    |      ['0']       |   | TPDISEC3   |   99.3806    |      ['0']       |
    | TPDISEC4   |   99.7923    |      ['0']       |   | TPDISEC5   |   99.9192    |      ['0']       |
    | TPDISEC6   |   99.9746    |      ['0']       |   | TPDISEC7   |   99.9948    |      ['0']       |
    | TPDISEC8   |   99.9997    |      ['0']       |   | TPDISEC9   |   99.9997    |      ['0']       |

**4. Identificação de possível campo agrupador**  
   > _Devido à anonimização obrigatória pela LGPD, os dados de identificação dos pacientes não estão disponíveis no repositório DataSUS._
   > _Para suprir essa necessidade, o campo **N_AIH** foi testado e pode ser utilizado para essa função._  

**4.1. Identificação de valores de **N_AIH** com maior número de ocorrências**
   > _Foram identificadas 34 ocorrências com mais de 70 registros para um mesmo **N_AIH**._  

**4.2. Análise das diferenças entre os registros de um mesmo **N_AIH****
   > _Foi realizada a análise das diferenças entre os registros de três amostras de **N_AIH**._  
   > _Os campos analisados foram: **MES_CMPT**, **ANO_CMPT**, **DT_INTER**, **DT_SAIDA**, **IDADE**, **SEXO** e **NASC**._  
   > _Os campos que apresentaram valores distintos foram: **MES_CMPT**, **ANO_CMPT**, **DT_SAIDA** e **IDADE**._  
   > _A hipótese é que cada registro representa uma ocorrência mensal da internação. Os campos **MES_CMPT** e **ANO_CMPT** indicam o período de referência, enquanto **DT_SAIDA** corresponde ao último dia do mês, nos casos de internação continuada. Além disso, a **IDADE** é atualizada anualmente._  
   > _Foi identificado um caso em que um **N_AIH** possui dois registros de internação no mês de janeiro de 2019, com data de saída em 30/11/2018. Supõe-se que se trate de um registro tardio no sistema._  

**5. Validação Global do campo N_AIH como agrupador**  
    > __ 