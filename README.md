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
   > _Foram identificados 31 campos, dos quais 20 estavam evidenciados nos metadados._

| SEQ | Campo | Tipo e Tam | Descrição/Observações | Valor Contante |
| :---: | :---: | :---: | :---- | :---: |
| 12 | UTI_MES_IN | numeric(2) | Zerado | [' 0'] |
| 13 | UTI_MES_AN | numeric(2) | Zerado | [' 0'] |
| 14 | UTI_MES_AL | numeric(2) | Zerado | [' 0'] |
| 17 | UTI_INT_IN | numeric(2) | Zerado | [' 0'] |
| 18 | UTI_INT_AN | numeric(2) | Zerado | [' 0'] |
| 19 | UTI_INT_AL | numeric(2) | Zerado | [' 0'] |
| 27 | VAL_SADT | numeric(13,2) | Zerado | [' 0.00'] |
| 28 | VAL_RN | numeric(13,2) | Zerado | [' 0.00'] |
| 29 | VAL_ACOMP | numeric(13,2) | Zerado | [' 0.00'] |
| 30 | VAL_ORTP | numeric(13,2) | Zerado | [' 0.00'] |
| 31 | VAL_SANGUE | numeric(13,2) | Zerado | [' 0.00'] |
| 32 | VAL_SADTSR | numeric(11,2) | Zerado | [' 0.00'] |
| 33 | VAL_TRANSP | numeric(13,2) | Zerado | [' 0.00'] |
| 34 | VAL_OBSANG | numeric(11,2) | Zerado | [' 0.00'] |
| 35 | VAL_PED1AC | numeric(11,2) | Zerado | [' 0.00'] |
| 42 | DIAG_SECUN | char(4) | Código do diagnostico secundário (CID10). Preenchido com zeros a partir de 201501. | ['0000'] |
| 44 | NATUREZA | char(2) | Natureza jurídica do hospital (com conteúdo até maio/12). Era utilizada a classificação de Regime e Natureza. | ['00'] |
| 47 | RUBRICA | numeric(5) | Zerado | [' 0'] |
| 55 | NUM_PROC | char(4) | Zerado | [''] |
| 57 | TOT_PT_SP | numeric(6) | Zerado | [' 0'] |
| 58 | CPF_AUT | char(11) | Zerado | [''] |
| 67 | SEQ_AIH5 | char(3) | Sequencial de longa permanência (AIH tipo 5). | ['000'] |
| 68 | CBOR | char(3) | Ocupação do paciente, segundo a Classificação Brasileira de Ocupações – CBO. | ['000000'] |
| 69 | CNAER | char(3) | Código de acidente de trabalho. | ['000'] |
| 70 | VINCPREV | char(1) | Vínculo com a Previdência. | ['0'] |
| 74 | GESTOR_DT | char(8) | Data da autorização dada pelo Gestor (aaaammdd). | [''] |
| 77 | INFEHOSP | char(1) | Status de infecção hospitalar. | [''] |
| 78 | CID_ASSO | char(4) | CID causa. | ['0000'] |
| 79 | CID_MORTE | char(4) | CID da morte. | ['0000'] |
| 92 | VAL_SH_GES | numeric (10, 2) | Valor do complemento do gestor (estadual ou municipal) de  serviços hospitalares. Está incluído no valor total da AIH. | [' 0.00'] |
| 93 | VAL_SP_GES | numeric (10, 2) | Valor do complemento do gestor (estadual ou municipal) de  serviços profissionais. Está incluído no valor total da AIH. | [' 0.00'] |

**3. Verificação dos campos com prevalência superior a 95% de registros com o mesmo valor.**
   > _Foram identificados 42 campos que atendem a essa condição._

| SEQ | Campo | Tipo e Tam | Descrição/Observações | % Prevalência | Valor Prevalente |
| :---: | :---: | :---: | :----- | :---: | :---: |
| 15 | UTI_MES_TO | numeric(3) | Quantidade de dias de UTI no mês. | 99,9043 | ['0'] |
| 16 | MARCA_UTI | char(2) | Indica qual o tipo de UTI utilizada pelo paciente. | 99,9043 | ['00'] |
| 20 | UTI_INT_TO | numeric(3) | Quantidade de diárias em unidade intermediaria. | 99,9994 | ['0'] |
| 21 | DIAR_ACOM | numeric(3) | Quantidade de diárias de acompanhante. | 96,1405 | ['0'] |
| 37 | VAL_UTI | numeric(8,2) | Valor de UTI. | 99,9043 | ['0.00'] |
| 48 | IND_VDRL | char(1) | Indica exame VDRL. | 99,9419 | ['0'] |
| 53 | MORTE | numeric(1) | Indica Óbito | 99,8498 | ['0'] |
| 59 | HOMONIMO | char(1) | Indicador se o paciente da AIH é homônimo do paciente de  outra AIH. | 99,9893 | ['0'] |
| 60 | NUM_FILHOS | numeric(2) | Número de filhos do paciente. | 99,9997 | ['0'] |
| 61 | INSTRU | char(1) | Grau de instrução do paciente. | 99,9997 | ['0'] |
| 62 | CID_NOTIF | char(4) | CID de Notificação. | 99,9997 | [''] |
| 63 | CONTRACEP1 | char(2) | Tipo de contraceptivo utilizado. | 99,9997 | ['00'] |
| 64 | CONTRACEP2 | char(2) | Segundo tipo de contraceptivo utilizado. | 99,9997 | ['00'] |
| 65 | GESTRISCO | char(1) | Indicador se é gestante de risco. | 99,9997 | ['1'] |
| 66 | INSC_PN | char(12) | Número da gestante no pré-natal. | 99,9985 | ['000000000000'] |
| 71 | GESTOR_COD | char(3) | Motivo de autorização da AIH pelo Gestor. | 99,2392 | ['00000'] |
| 80 | COMPLEX | char(2) | Complexidade. | 99,9979 | ['02'] |
| 81 | FINANC | char(2) | Tipo de financiamento. | 99,9985 | ['06'] |
| 82 | FAEC_TP | char(6) | Subtipo de financiamento FAEC. | 99,9985 | [''] |
| 85 | ETNIA | char(4) | Etnia do paciente, se raça cor for indígena. | 99,9908 | ['0000'] |
| 88 | AUD_JUST | char (50) | Justificativa do auditor para aceitação da AIH sem o número do Cartão Nacional de Saúde. | 99,8743 | [''] |
| 89 | SIS_JUST | char (50) | Justificativa do estabelecimento para aceitação da AIH sem o  número do Cartão Nacional de Saúde. | 99,877 | [''] |
| 90 | VAL_SH_FED | numeric (10, 2) | Valor do complemento federal de serviços hospitalares. Está  incluído no valor total da AIH. | 99,9997 | ['0.00'] |
| 91 | VAL_SP_FED | numeric (10, 2) | Valor do complemento federal de serviços profissionais. Está  incluído no valor total da AIH. | 99,9997 | ['0.00'] |
| 94 | VAL_UCI | numeric (10, 2) | Valor de UCI. | 99,9994 | ['0.00'] |
| 95 | MARCA_UCI | char (2) | Tipo de UCI utilizada pelo paciente. | 99,9994 | ['00'] |
| 97 | DIAGSEC2 | char (4) | Diagnóstico secundário 2. | 97,7226 | [''] |
| 98 | DIAGSEC3 | char (4) | Diagnóstico secundário 3. | 99,3806 | [''] |
| 99 | DIAGSEC4 | char (4) | Diagnóstico secundário 4. | 99,7923 | [''] |
| 100 | DIAGSEC5 | char (4) | Diagnóstico secundário 5. | 99,9192 | [''] |
| 101 | DIAGSEC6 | char (4) | Diagnóstico secundário 6. | 99,9746 | [''] |
| 102 | DIAGSEC7 | char (4) | Diagnóstico secundário 7. | 99,9948 | [''] |
| 103 | DIAGSEC8 | char (4) | Diagnóstico secundário 8. | 99,9997 | [''] |
| 104 | DIAGSEC9 | char (4) | Diagnóstico secundário 9. | 99,9997 | [''] |
| 107 | TPDISEC2 | char(1) | Tipo de diagnóstico secundário 2. | 97,7226 | ['0'] |
| 108 | TPDISEC3 | char(1) | Tipo de diagnóstico secundário 3. | 99,3806 | ['0'] |
| 109 | TPDISEC4 | char(1) | Tipo de diagnóstico secundário 4. | 99,7923 | ['0'] |
| 110 | TPDISEC5 | char(1) | Tipo de diagnóstico secundário 5. | 99,9192 | ['0'] |
| 111 | TPDISEC6 | char(1) | Tipo de diagnóstico secundário 6. | 99,9746 | ['0'] |
| 112 | TPDISEC7 | char(1) | Tipo de diagnóstico secundário 7. | 99,9948 | ['0'] |
| 113 | TPDISEC8 | char(1) | Tipo de diagnóstico secundário 8. | 99,9997 | ['0'] |
| 114 | TPDISEC9 | char(1) | Tipo de diagnóstico secundário 9. | 99,9997 | ['0'] |

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

| SEQ | NOME DO CAMPO | TIPO E TAM | Descrição/Observações |
| :---: | :---: | :---: | :---: |
| 1 | UF_ZI | char(6) | Município Gestor. |