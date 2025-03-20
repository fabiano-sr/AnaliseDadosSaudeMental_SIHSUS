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

<div style="text-align: center;">
    <table style="font-size: 11px; border: 1px solid black; border-collapse: collapse; width: 100%;">
    <thead>
        <tr>
        <th style="text-align: center;">SEQ</th>
        <th style="text-align: center;">Campo</th>
        <th style="text-align: center;">Tipo e Tam</th>
        <th>Descrição/Observações</th>
        <th style="text-align: center;">Valor Contante</th>
        </tr>
    </thead>
    <tbody>
        <tr><td style="text-align: center;">12</td><td style="text-align: center;">UTI_MES_IN</td><td style="text-align: center;">numeric(2)</td><td>Zerado</td><td style="text-align: center;">[' 0']</td></tr>
        <tr><td style="text-align: center;">13</td><td style="text-align: center;">UTI_MES_AN</td><td style="text-align: center;">numeric(2)</td><td>Zerado</td><td style="text-align: center;">[' 0']</td></tr>
        <tr><td style="text-align: center;">14</td><td style="text-align: center;">UTI_MES_AL</td><td style="text-align: center;">numeric(2)</td><td>Zerado</td><td style="text-align: center;">[' 0']</td></tr>
        <tr><td style="text-align: center;">17</td><td style="text-align: center;">UTI_INT_IN</td><td style="text-align: center;">numeric(2)</td><td>Zerado</td><td style="text-align: center;">[' 0']</td></tr>
        <tr><td style="text-align: center;">18</td><td style="text-align: center;">UTI_INT_AN</td><td style="text-align: center;">numeric(2)</td><td>Zerado</td><td style="text-align: center;">[' 0']</td></tr>
        <tr><td style="text-align: center;">19</td><td style="text-align: center;">UTI_INT_AL</td><td style="text-align: center;">numeric(2)</td><td>Zerado</td><td style="text-align: center;">[' 0']</td></tr>
        <tr><td style="text-align: center;">27</td><td style="text-align: center;">VAL_SADT</td><td style="text-align: center;">numeric(13,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">28</td><td style="text-align: center;">VAL_RN</td><td style="text-align: center;">numeric(13,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">29</td><td style="text-align: center;">VAL_ACOMP</td><td style="text-align: center;">numeric(13,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">30</td><td style="text-align: center;">VAL_ORTP</td><td style="text-align: center;">numeric(13,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">31</td><td style="text-align: center;">VAL_SANGUE</td><td style="text-align: center;">numeric(13,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">32</td><td style="text-align: center;">VAL_SADTSR</td><td style="text-align: center;">numeric(11,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">33</td><td style="text-align: center;">VAL_TRANSP</td><td style="text-align: center;">numeric(13,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">34</td><td style="text-align: center;">VAL_OBSANG</td><td style="text-align: center;">numeric(11,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">35</td><td style="text-align: center;">VAL_PED1AC</td><td style="text-align: center;">numeric(11,2)</td><td>Zerado</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">42</td><td style="text-align: center;">DIAG_SECUN</td><td style="text-align: center;">char(4)</td><td>Código do diagnóstico secundário (CID10). Preenchido com zeros a partir de 201501.</td><td style="text-align: center;">['0000']</td></tr>
        <tr><td style="text-align: center;">44</td><td style="text-align: center;">NATUREZA</td><td style="text-align: center;">char(2)</td><td>Natureza jurídica do hospital (com conteúdo até maio/12). Era utilizada a classificação de Regime e Natureza.</td><td style="text-align: center;">['00']</td></tr>
        <tr><td style="text-align: center;">47</td><td style="text-align: center;">RUBRICA</td><td style="text-align: center;">numeric(5)</td><td>Zerado</td><td style="text-align: center;">[' 0']</td></tr>
        <tr><td style="text-align: center;">55</td><td style="text-align: center;">NUM_PROC</td><td style="text-align: center;">char(4)</td><td>Zerado</td><td style="text-align: center;">['']</td></tr>
        <tr><td style="text-align: center;">57</td><td style="text-align: center;">TOT_PT_SP</td><td style="text-align: center;">numeric(6)</td><td>Zerado</td><td style="text-align: center;">[' 0']</td></tr>
        <tr><td style="text-align: center;">58</td><td style="text-align: center;">CPF_AUT</td><td style="text-align: center;">char(11)</td><td>Zerado</td><td style="text-align: center;">['']</td></tr>
        <tr><td style="text-align: center;">67</td><td style="text-align: center;">SEQ_AIH5</td><td style="text-align: center;">char(3)</td><td>Sequencial de longa permanência (AIH tipo 5).</td><td style="text-align: center;">['000']</td></tr>
        <tr><td style="text-align: center;">68</td><td style="text-align: center;">CBOR</td><td style="text-align: center;">char(3)</td><td>Ocupação do paciente, segundo a Classificação Brasileira de Ocupações – CBO.</td><td style="text-align: center;">['000000']</td></tr>
        <tr><td style="text-align: center;">69</td><td style="text-align: center;">CNAER</td><td style="text-align: center;">char(3)</td><td>Código de acidente de trabalho.</td><td style="text-align: center;">['000']</td></tr>
        <tr><td style="text-align: center;">70</td><td style="text-align: center;">VINCPREV</td><td style="text-align: center;">char(1)</td><td>Vínculo com a Previdência.</td><td style="text-align: center;">['0']</td></tr>
        <tr><td style="text-align: center;">74</td><td style="text-align: center;">GESTOR_DT</td><td style="text-align: center;">char(8)</td><td>Data da autorização dada pelo Gestor (aaaammdd).</td><td style="text-align: center;">['']</td></tr>
        <tr><td style="text-align: center;">77</td><td style="text-align: center;">INFEHOSP</td><td style="text-align: center;">char(1)</td><td>Status de infecção hospitalar.</td><td style="text-align: center;">['']</td></tr>
        <tr><td style="text-align: center;">78</td><td style="text-align: center;">CID_ASSO</td><td style="text-align: center;">char(4)</td><td>CID causa.</td><td style="text-align: center;">['0000']</td></tr>
        <tr><td style="text-align: center;">79</td><td style="text-align: center;">CID_MORTE</td><td style="text-align: center;">char(4)</td><td>CID da morte.</td><td style="text-align: center;">['0000']</td></tr>
        <tr><td style="text-align: center;">92</td><td style="text-align: center;">VAL_SH_GES</td><td style="text-align: center;">numeric(10,2)</td><td>Valor do complemento do gestor (estadual ou municipal) de serviços hospitalares. Está incluído no valor total da AIH.</td><td style="text-align: center;">[' 0.00']</td></tr>
        <tr><td style="text-align: center;">93</td><td style="text-align: center;">VAL_SP_GES</td><td style="text-align: center;">numeric(10,2)</td><td>Valor do complemento do gestor (estadual ou municipal) de serviços profissionais. Está incluído no valor total da AIH.</td><td style="text-align: center;">[' 0.00']</td></tr>
    </tbody>
    </table>
</div>

**3. Verificação dos campos com prevalência superior a 95% de registros com o mesmo valor.**
   > _Foram identificados 42 campos que atendem a essa condição._

<div style="text-align: center;">
    <table style="font-size: 11px; border: 1px solid black; border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="text-align: center;">SEQ</th>
      <th style="text-align: center;">Campo</th>
      <th style="text-align: center;">Tipo e Tam</th>
      <th>Descrição/Observações</th>
      <th style="text-align: center;">% Prevalência</th>
      <th style="text-align: center;">Valor Prevalente</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align: center;">15</td><td style="text-align: center;">UTI_MES_TO</td><td style="text-align: center;">numeric(3)</td><td>Quantidade de dias de UTI no mês.</td><td style="text-align: center;">99,9043</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">16</td><td style="text-align: center;">MARCA_UTI</td><td style="text-align: center;">char(2)</td><td>Indica qual o tipo de UTI utilizada pelo paciente.</td><td style="text-align: center;">99,9043</td><td style="text-align: center;">['00']</td></tr>
    <tr><td style="text-align: center;">20</td><td style="text-align: center;">UTI_INT_TO</td><td style="text-align: center;">numeric(3)</td><td>Quantidade de diárias em unidade intermediária.</td><td style="text-align: center;">99,9994</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">21</td><td style="text-align: center;">DIAR_ACOM</td><td style="text-align: center;">numeric(3)</td><td>Quantidade de diárias de acompanhante.</td><td style="text-align: center;">96,1405</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">37</td><td style="text-align: center;">VAL_UTI</td><td style="text-align: center;">numeric(8,2)</td><td>Valor de UTI.</td><td style="text-align: center;">99,9043</td><td style="text-align: center;">['0.00']</td></tr>
    <tr><td style="text-align: center;">48</td><td style="text-align: center;">IND_VDRL</td><td style="text-align: center;">char(1)</td><td>Indica exame VDRL.</td><td style="text-align: center;">99,9419</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">53</td><td style="text-align: center;">MORTE</td><td style="text-align: center;">numeric(1)</td><td>Indica Óbito</td><td style="text-align: center;">99,8498</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">59</td><td style="text-align: center;">HOMONIMO</td><td style="text-align: center;">char(1)</td><td>Indicador se o paciente da AIH é homônimo do paciente de outra AIH.</td><td style="text-align: center;">99,9893</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">60</td><td style="text-align: center;">NUM_FILHOS</td><td style="text-align: center;">numeric(2)</td><td>Número de filhos do paciente.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">61</td><td style="text-align: center;">INSTRU</td><td style="text-align: center;">char(1)</td><td>Grau de instrução do paciente.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">62</td><td style="text-align: center;">CID_NOTIF</td><td style="text-align: center;">char(4)</td><td>CID de Notificação.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">63</td><td style="text-align: center;">CONTRACEP1</td><td style="text-align: center;">char(2)</td><td>Tipo de contraceptivo utilizado.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['00']</td></tr>
    <tr><td style="text-align: center;">64</td><td style="text-align: center;">CONTRACEP2</td><td style="text-align: center;">char(2)</td><td>Segundo tipo de contraceptivo utilizado.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['00']</td></tr>
    <tr><td style="text-align: center;">65</td><td style="text-align: center;">GESTRISCO</td><td style="text-align: center;">char(1)</td><td>Indicador se é gestante de risco.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['1']</td></tr>
    <tr><td style="text-align: center;">66</td><td style="text-align: center;">INSC_PN</td><td style="text-align: center;">char(12)</td><td>Número da gestante no pré-natal.</td><td style="text-align: center;">99,9985</td><td style="text-align: center;">['000000000000']</td></tr>
    <tr><td style="text-align: center;">71</td><td style="text-align: center;">GESTOR_COD</td><td style="text-align: center;">char(3)</td><td>Motivo de autorização da AIH pelo Gestor.</td><td style="text-align: center;">99,2392</td><td style="text-align: center;">['00000']</td></tr>
    <tr><td style="text-align: center;">80</td><td style="text-align: center;">COMPLEX</td><td style="text-align: center;">char(2)</td><td>Complexidade.</td><td style="text-align: center;">99,9979</td><td style="text-align: center;">['02']</td></tr>
    <tr><td style="text-align: center;">81</td><td style="text-align: center;">FINANC</td><td style="text-align: center;">char(2)</td><td>Tipo de financiamento.</td><td style="text-align: center;">99,9985</td><td style="text-align: center;">['06']</td></tr>
    <tr><td style="text-align: center;">82</td><td style="text-align: center;">FAEC_TP</td><td style="text-align: center;">char(6)</td><td>Subtipo de financiamento FAEC.</td><td style="text-align: center;">99,9985</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">85</td><td style="text-align: center;">ETNIA</td><td style="text-align: center;">char(4)</td><td>Etnia do paciente, se raça cor for indígena.</td><td style="text-align: center;">99,9908</td><td style="text-align: center;">['0000']</td></tr>
    <tr><td style="text-align: center;">88</td><td style="text-align: center;">AUD_JUST</td><td style="text-align: center;">char(50)</td><td>Justificativa do auditor para aceitação da AIH sem o número do Cartão Nacional de Saúde.</td><td style="text-align: center;">99,8743</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">89</td><td style="text-align: center;">SIS_JUST</td><td style="text-align: center;">char(50)</td><td>Justificativa do estabelecimento para aceitação da AIH sem o número do Cartão Nacional de Saúde.</td><td style="text-align: center;">99,877</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">90</td><td style="text-align: center;">VAL_SH_FED</td><td style="text-align: center;">numeric(10,2)</td><td>Valor do complemento federal de serviços hospitalares. Está incluído no valor total da AIH.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['0.00']</td></tr>
    <tr><td style="text-align: center;">91</td><td style="text-align: center;">VAL_SP_FED</td><td style="text-align: center;">numeric(10,2)</td><td>Valor do complemento federal de serviços profissionais. Está incluído no valor total da AIH.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['0.00']</td></tr>
    <tr><td style="text-align: center;">94</td><td style="text-align: center;">VAL_UCI</td><td style="text-align: center;">numeric(10,2)</td><td>Valor de UCI.</td><td style="text-align: center;">99,9994</td><td style="text-align: center;">['0.00']</td></tr>
    <tr><td style="text-align: center;">95</td><td style="text-align: center;">MARCA_UCI</td><td style="text-align: center;">char(2)</td><td>Tipo de UCI utilizada pelo paciente.</td><td style="text-align: center;">99,9994</td><td style="text-align: center;">['00']</td></tr>
    <tr><td style="text-align: center;">97</td><td style="text-align: center;">DIAGSEC2</td><td style="text-align: center;">char(4)</td><td>Diagnóstico secundário 2.</td><td style="text-align: center;">97,7226</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">98</td><td style="text-align: center;">DIAGSEC3</td><td style="text-align: center;">char(4)</td><td>Diagnóstico secundário 3.</td><td style="text-align: center;">99,3806</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">99</td><td style="text-align: center;">DIAGSEC4</td><td style="text-align: center;">char(4)</td><td>Diagnóstico secundário 4.</td><td style="text-align: center;">99,7923</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">100</td><td style="text-align: center;">DIAGSEC5</td><td style="text-align: center;">char(4)</td><td>Diagnóstico secundário 5.</td><td style="text-align: center;">99,9192</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">101</td><td style="text-align: center;">DIAGSEC6</td><td style="text-align: center;">char(4)</td><td>Diagnóstico secundário 6.</td><td style="text-align: center;">99,9746</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">102</td><td style="text-align: center;">DIAGSEC7</td><td style="text-align: center;">char(4)</td><td>Diagnóstico secundário 7.</td><td style="text-align: center;">99,9948</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">103</td><td style="text-align: center;">DIAGSEC8</td><td style="text-align: center;">char(4)</td><td>Diagnóstico secundário 8.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">104</td><td style="text-align: center;">DIAGSEC9</td><td style="text-align: center;">char(4)</td><td>Diagnóstico secundário 9.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['']</td></tr>
    <tr><td style="text-align: center;">107</td><td style="text-align: center;">TPDISEC2</td><td style="text-align: center;">char(1)</td><td>Tipo de diagnóstico secundário 2.</td><td style="text-align: center;">97,7226</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">108</td><td style="text-align: center;">TPDISEC3</td><td style="text-align: center;">char(1)</td><td>Tipo de diagnóstico secundário 3.</td><td style="text-align: center;">99,3806</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">109</td><td style="text-align: center;">TPDISEC4</td><td style="text-align: center;">char(1)</td><td>Tipo de diagnóstico secundário 4.</td><td style="text-align: center;">99,7923</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">110</td><td style="text-align: center;">TPDISEC5</td><td style="text-align: center;">char(1)</td><td>Tipo de diagnóstico secundário 5.</td><td style="text-align: center;">99,9192</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">111</td><td style="text-align: center;">TPDISEC6</td><td style="text-align: center;">char(1)</td><td>Tipo de diagnóstico secundário 6.</td><td style="text-align: center;">99,9746</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">112</td><td style="text-align: center;">TPDISEC7</td><td style="text-align: center;">char(1)</td><td>Tipo de diagnóstico secundário 7.</td><td style="text-align: center;">99,9948</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">113</td><td style="text-align: center;">TPDISEC8</td><td style="text-align: center;">char(1)</td><td>Tipo de diagnóstico secundário 8.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['0']</td></tr>
    <tr><td style="text-align: center;">114</td><td style="text-align: center;">TPDISEC9</td><td style="text-align: center;">char(1)</td><td>Tipo de diagnóstico secundário 9.</td><td style="text-align: center;">99,9997</td><td style="text-align: center;">['0']</td></tr>
  </tbody>
</table>
</div>

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