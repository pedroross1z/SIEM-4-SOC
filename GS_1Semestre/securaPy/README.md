# SecuraPy SIEM — Trabalho Fina

## Como usar este projeto

Este projeto contém a **casca** (esqueleto) do sistema SecuraPy SIEM. Todos os
arquivos `.py` dos módulos já existem com as funções definidas, mas o corpo de
cada função contém apenas `pass` — ou seja, **nada funciona ainda**.

Seu trabalho é **implementar o código** dentro de cada função, seguindo as
docstrings e dicas que já estão escritas nos arquivos.

### Verificando seu progresso com os testes

O projeto inclui **testes automatizados** que validam se sua implementação está
correta. Quando você começar, **todos os testes vão falhar**. Conforme você
implementa as funções, os testes vão passando.

#### Instalando as dependências

```bash
# Na pasta securaPy/
pip install pytest requests
```

#### Rodando todos os testes

```bash
# Na pasta securaPy/
python -m pytest testes/ -v
```

#### Rodando testes de um módulo específico

```bash
# Testar apenas o coletor
python -m pytest testes/test_coletor.py -v

# Testar apenas as regras
python -m pytest testes/test_regras.py -v

# Testar apenas o detector
python -m pytest testes/test_detector.py -v

# Testar apenas o enriquecimento
python -m pytest testes/test_enriquecimento.py -v

# Testar apenas o servidor de alertas
python -m pytest testes/test_servidor.py -v

# Testar apenas os relatórios
python -m pytest testes/test_relatorios.py -v

# Testar apenas a integração (ponta a ponta)
python -m pytest testes/test_integracao.py -v
```

#### Rodando um teste específico

```bash
# Rodar apenas um teste por nome
python -m pytest testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_retorna_dict -v
```

#### Vendo quantos testes passam vs falham

```bash
python -m pytest testes/ --tb=no -q
```

Saída esperada no início (tudo falhando):
```
182 failed, 15 passed
```
(os 15 que passam de cara são testes de entrada inválida/vazia — como as funções
ainda não fazem nada, retornar `None` coincide com o comportamento esperado para
entradas inválidas)

Saída esperada quando tudo estiver implementado:
```
197 passed, 0 failed
```

### Ordem recomendada de implementação

Comece pelo módulo que os outros dependem e vá subindo:

1. **`coletor.py`** — base de tudo (rode `test_coletor.py`)
2. **`regras.py`** — precisa do coletor (rode `test_regras.py`)
3. **`detector.py`** — precisa do coletor (rode `test_detector.py`)
4. **`enriquecimento.py`** — independente (rode `test_enriquecimento.py`)
5. **`relatorios.py`** — precisa de todos (rode `test_relatorios.py`)
6. **`servidor_alertas.py` + `cliente_alertas.py`** — independente (rode `test_servidor.py`)
7. **`main.py`** — integra tudo (rode `test_integracao.py`)

### Estrutura do projeto

```
securaPy/
├── main.py                  # Ponto de entrada — menu principal
├── coletor.py               # Módulo 1 — Leitura e parsing de logs
├── regras.py                # Módulo 2 — Motor de regras de detecção
├── detector.py              # Módulo 3 — Detecção de anomalias
├── servidor_alertas.py      # Módulo 4a — Servidor TCP de alertas
├── cliente_alertas.py       # Módulo 4b — Cliente TCP de alertas
├── enriquecimento.py        # Módulo 5 — Consulta API de geolocalização
├── relatorios.py            # Módulo 6 — Dashboard CLI e relatórios
├── logs/                    # Arquivos de log para teste
│   ├── auth.log
│   ├── firewall.log
│   └── web_access.log
├── config/
│   └── regras.json          # Configuração das regras de detecção
├── saida/                   # Relatórios gerados (pasta de saída)
├── testes/                  # Testes automatizados
│   ├── conftest.py          # Fixtures compartilhadas
│   ├── test_coletor.py      # Testes do módulo 1
│   ├── test_regras.py       # Testes do módulo 2
│   ├── test_detector.py     # Testes do módulo 3
│   ├── test_servidor.py     # Testes do módulo 4
│   ├── test_enriquecimento.py  # Testes do módulo 5
│   ├── test_relatorios.py   # Testes do módulo 6
│   └── test_integracao.py   # Testes ponta a ponta
└── README.md                # Este arquivo
```

### Mapa de testes por módulo

| Módulo | Arquivo de teste | Testes | O que valida |
|--------|-----------------|--------|-------------|
| coletor.py | test_coletor.py | 47 | Parsing dos 3 formatos de log, normalização, erros de arquivo |
| regras.py | test_regras.py | 37 | Carregamento JSON, classificação severidade, avaliação de cada regra |
| detector.py | test_detector.py | 38 | Brute force, port scan, blacklist, resumo consolidado |
| enriquecimento.py | test_enriquecimento.py | 26 | IP privado/público, cache, mock de API, tratamento de erros |
| servidor_alertas.py | test_servidor.py | 7 | Formatação de alertas, conexão TCP, broadcast |
| relatorios.py | test_relatorios.py | 30 | Filtros, top IPs, exportação JSON, menu |
| integração | test_integracao.py | 12 | Fluxo completo ponta a ponta |
| | | **197** | **Total** |

---

## Para a entrega: preencha as seções abaixo

> **IMPORTANTE:** Antes de entregar, substitua tudo abaixo deste ponto
> com as informações do seu grupo.

---

# SecuraPy SIEM — Hackers da Fiap

## Integrantes

| Nome | RM | Responsabilidade |
|------|-----|-----------------|
| Elias de Aguiar Matos Junior | 568932 | [Módulos que implementou] |
| Guilherme costa Praxedes | 569990 | [Módulos que implementou] |
| Gustavo Cesar Dutra Batista | 569964 | [Módulos que implementou] |
| Italo Henrique Passos Bastos | 573624 | [Módulos que implementou] |
| Pedro Rossi de Macedo | 571590 | [Módulos que implementou] |

## Descrição

[Descreva em 2-3 parágrafos o que o sistema faz, quais problemas ele resolve
e como os módulos se integram.]

## Como executar

```bash
# 1. Instalar dependências
pip install requests

# 2. Rodar o sistema
cd securaPy
python main.py

# 3. Rodar os testes
python -m pytest testes/ -v
```

## Resultado dos testes

```
collected 197 items                                                                                                                                           

testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_retorna_dict PASSED                                                                       [  0%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_campos_obrigatorios PASSED                                                                [  1%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_timestamp PASSED                                                                          [  1%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_fonte PASSED                                                                              [  2%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_tipo PASSED                                                                               [  2%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_ip PASSED                                                                                 [  3%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_detalhes_contem_usuario PASSED                                                            [  3%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_fail_linha_original PASSED                                                                     [  4%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_ok PASSED                                                                                      [  4%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_invalida_retorna_none PASSED                                                                   [  5%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_vazia_retorna_none PASSED                                                                      [  5%]
testes/test_coletor.py::TestParsearLinhaAuth::test_linha_parcial_retorna_none PASSED                                                                    [  6%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_block_retorna_dict PASSED                                                                  [  6%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_block_campos_obrigatorios PASSED                                                           [  7%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_block_timestamp PASSED                                                                     [  7%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_block_fonte PASSED                                                                         [  8%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_block_tipo PASSED                                                                          [  8%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_block_ip_origem PASSED                                                                     [  9%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_block_detalhes_contem_dport PASSED                                                         [  9%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_allow PASSED                                                                               [ 10%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_invalida_retorna_none PASSED                                                               [ 10%]
testes/test_coletor.py::TestParsearLinhaFirewall::test_linha_vazia_retorna_none PASSED                                                                  [ 11%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_get_retorna_dict PASSED                                                                         [ 11%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_get_campos_obrigatorios PASSED                                                                  [ 12%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_get_timestamp PASSED                                                                            [ 12%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_get_fonte PASSED                                                                                [ 13%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_get_tipo_metodo_http PASSED                                                                     [ 13%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_get_ip PASSED                                                                                   [ 14%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_get_detalhes_contem_url PASSED                                                                  [ 14%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_get_detalhes_contem_status PASSED                                                               [ 15%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_xss_preserva_caracteres_especiais PASSED                                                        [ 15%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_traversal PASSED                                                                                [ 16%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_invalida_retorna_none PASSED                                                                    [ 16%]
testes/test_coletor.py::TestParsearLinhaWeb::test_linha_vazia_retorna_none PASSED                                                                       [ 17%]
testes/test_coletor.py::TestCarregarLog::test_carregar_auth_log PASSED                                                                                  [ 17%]
testes/test_coletor.py::TestCarregarLog::test_carregar_firewall_log PASSED                                                                              [ 18%]
testes/test_coletor.py::TestCarregarLog::test_carregar_web_log PASSED                                                                                   [ 18%]
testes/test_coletor.py::TestCarregarLog::test_todos_eventos_sao_dicts PASSED                                                                            [ 19%]
testes/test_coletor.py::TestCarregarLog::test_arquivo_inexistente_retorna_lista_vazia PASSED                                                            [ 19%]
testes/test_coletor.py::TestCarregarLog::test_arquivo_vazio_retorna_lista_vazia PASSED                                                                  [ 20%]
testes/test_coletor.py::TestCarregarLog::test_linhas_invalidas_sao_ignoradas PASSED                                                                     [ 20%]
testes/test_coletor.py::TestCarregarLog::test_fonte_correta_em_todos_eventos PASSED                                                                     [ 21%]
testes/test_coletor.py::TestCarregarTodosOsLogs::test_retorna_lista PASSED                                                                              [ 21%]
testes/test_coletor.py::TestCarregarTodosOsLogs::test_carrega_todas_as_fontes PASSED                                                                    [ 22%]
testes/test_coletor.py::TestCarregarTodosOsLogs::test_total_de_eventos PASSED                                                                           [ 22%]
testes/test_coletor.py::TestCarregarTodosOsLogs::test_pasta_inexistente_retorna_lista_vazia PASSED                                                      [ 23%]
testes/test_coletor.py::TestCarregarTodosOsLogs::test_ignora_arquivos_nao_log PASSED                                                                    [ 23%]
testes/test_detector.py::TestDetectarBruteForce::test_retorna_dicionario PASSED                                                                         [ 24%]
testes/test_detector.py::TestDetectarBruteForce::test_detecta_ip_com_11_falhas PASSED                                                                   [ 24%]
testes/test_detector.py::TestDetectarBruteForce::test_detecta_ip_com_5_falhas PASSED                                                                    [ 25%]
testes/test_detector.py::TestDetectarBruteForce::test_nao_detecta_abaixo_threshold PASSED                                                               [ 25%]
testes/test_detector.py::TestDetectarBruteForce::test_nao_detecta_ips_internos PASSED                                                                   [ 26%]
testes/test_detector.py::TestDetectarBruteForce::test_contagem_tentativas PASSED                                                                        [ 26%]
testes/test_detector.py::TestDetectarBruteForce::test_lista_usuarios_tentados PASSED                                                                    [ 27%]
testes/test_detector.py::TestDetectarBruteForce::test_severidade_alta_para_muitas_tentativas PASSED                                                     [ 27%]
testes/test_detector.py::TestDetectarBruteForce::test_threshold_customizado PASSED                                                                      [ 28%]
testes/test_detector.py::TestDetectarBruteForce::test_threshold_1_detecta_todos PASSED                                                                  [ 28%]
testes/test_detector.py::TestDetectarBruteForce::test_ignora_eventos_ok PASSED                                                                          [ 29%]
testes/test_detector.py::TestDetectarBruteForce::test_ignora_eventos_firewall PASSED                                                                    [ 29%]
testes/test_detector.py::TestDetectarBruteForce::test_lista_vazia_retorna_dict_vazio PASSED                                                             [ 30%]
testes/test_detector.py::TestDetectarPortScan::test_retorna_dicionario PASSED                                                                           [ 30%]
testes/test_detector.py::TestDetectarPortScan::test_detecta_ip_com_7_portas PASSED                                                                      [ 31%]
testes/test_detector.py::TestDetectarPortScan::test_detecta_ip_com_3_portas PASSED                                                                      [ 31%]
testes/test_detector.py::TestDetectarPortScan::test_nao_detecta_abaixo_threshold PASSED                                                                 [ 32%]
testes/test_detector.py::TestDetectarPortScan::test_portas_sao_unicas PASSED                                                                            [ 32%]
testes/test_detector.py::TestDetectarPortScan::test_quantidade_portas PASSED                                                                            [ 33%]
testes/test_detector.py::TestDetectarPortScan::test_severidade_para_muitas_portas PASSED                                                                [ 34%]
testes/test_detector.py::TestDetectarPortScan::test_ignora_allow PASSED                                                                                 [ 34%]
testes/test_detector.py::TestDetectarPortScan::test_threshold_customizado PASSED                                                                        [ 35%]
testes/test_detector.py::TestDetectarPortScan::test_lista_vazia_retorna_dict_vazio PASSED                                                               [ 35%]
testes/test_detector.py::TestVerificarBlacklist::test_retorna_tupla PASSED                                                                              [ 36%]
testes/test_detector.py::TestVerificarBlacklist::test_encontra_ips_da_blacklist PASSED                                                                  [ 36%]
testes/test_detector.py::TestVerificarBlacklist::test_nao_encontra_ip_ausente_dos_logs PASSED                                                           [ 37%]
testes/test_detector.py::TestVerificarBlacklist::test_ips_internos_nao_na_blacklist PASSED                                                              [ 37%]
testes/test_detector.py::TestVerificarBlacklist::test_contagem_por_ip PASSED                                                                            [ 38%]
testes/test_detector.py::TestVerificarBlacklist::test_usa_intersecao_de_sets PASSED                                                                     [ 38%]
testes/test_detector.py::TestVerificarBlacklist::test_blacklist_vazia PASSED                                                                            [ 39%]
testes/test_detector.py::TestVerificarBlacklist::test_eventos_vazios PASSED                                                                             [ 39%]
testes/test_detector.py::TestGerarResumoAmeacas::test_retorna_lista PASSED                                                                              [ 40%]
testes/test_detector.py::TestGerarResumoAmeacas::test_contem_todos_ips_suspeitos PASSED                                                                 [ 40%]
testes/test_detector.py::TestGerarResumoAmeacas::test_ip_com_3_deteccoes_mais_grave PASSED                                                              [ 41%]
testes/test_detector.py::TestGerarResumoAmeacas::test_lista_deteccoes PASSED                                                                            [ 41%]
testes/test_detector.py::TestGerarResumoAmeacas::test_ordenado_por_pontuacao PASSED                                                                     [ 42%]
testes/test_detector.py::TestGerarResumoAmeacas::test_cada_ameaca_tem_campos PASSED                                                                     [ 42%]
testes/test_detector.py::TestGerarResumoAmeacas::test_tudo_vazio PASSED                                                                                 [ 43%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_10_0_0_1_privado PASSED                                                                            [ 43%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_10_255_255_255_privado PASSED                                                                      [ 44%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_10_0_0_5_privado PASSED                                                                            [ 44%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_172_16_0_1_privado PASSED                                                                          [ 45%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_172_31_255_255_privado PASSED                                                                      [ 45%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_172_32_0_1_publico PASSED                                                                          [ 46%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_172_15_0_1_publico PASSED                                                                          [ 46%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_192_168_1_1_privado PASSED                                                                         [ 47%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_192_168_1_10_privado PASSED                                                                        [ 47%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_192_168_255_255_privado PASSED                                                                     [ 48%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_127_0_0_1_privado PASSED                                                                           [ 48%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_8_8_8_8_publico PASSED                                                                             [ 49%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_185_220_101_1_publico PASSED                                                                       [ 49%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_91_240_118_172_publico PASSED                                                                      [ 50%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_45_33_32_156_publico PASSED                                                                        [ 50%]
testes/test_enriquecimento.py::TestEhIpPrivado::test_1_1_1_1_publico PASSED                                                                             [ 51%]
testes/test_enriquecimento.py::TestConsultarIp::test_consulta_ip_publico PASSED                                                                         [ 51%]
testes/test_enriquecimento.py::TestConsultarIp::test_retorno_contem_campos PASSED                                                                       [ 52%]
testes/test_enriquecimento.py::TestConsultarIp::test_usa_cache_na_segunda_consulta PASSED                                                               [ 52%]
testes/test_enriquecimento.py::TestConsultarIp::test_ip_privado_nao_consulta_api PASSED                                                                 [ 53%]
testes/test_enriquecimento.py::TestConsultarIp::test_salva_no_cache PASSED                                                                              [ 53%]
testes/test_enriquecimento.py::TestConsultarIp::test_trata_timeout PASSED                                                                               [ 54%]
testes/test_enriquecimento.py::TestConsultarIp::test_trata_erro_conexao PASSED                                                                          [ 54%]
testes/test_enriquecimento.py::TestEnriquecerAlertas::test_adiciona_geolocalizacao PASSED                                                               [ 55%]
testes/test_enriquecimento.py::TestEnriquecerAlertas::test_ip_privado_marca_rede_interna PASSED                                                         [ 55%]
testes/test_enriquecimento.py::TestEnriquecerAlertas::test_lista_vazia PASSED                                                                           [ 56%]
testes/test_integracao.py::TestFluxoCarregarEAnalisar::test_carregar_e_aplicar_regras PASSED                                                            [ 56%]
testes/test_integracao.py::TestFluxoCarregarEAnalisar::test_regras_detectam_todos_os_ataques PASSED                                                     [ 57%]
testes/test_integracao.py::TestFluxoDeteccao::test_deteccao_completa PASSED                                                                             [ 57%]
testes/test_integracao.py::TestFluxoEnriquecimento::test_ips_dos_logs_classificados_corretamente PASSED                                                 [ 58%]
testes/test_integracao.py::TestFluxoRelatorios::test_filtrar_e_top_ips PASSED                                                                           [ 58%]
testes/test_integracao.py::TestFluxoRelatorios::test_exportar_relatorio_completo PASSED                                                                 [ 59%]
testes/test_integracao.py::TestFluxoBuscaIp::test_ip_malicioso_completo PASSED                                                                          [ 59%]
testes/test_integracao.py::TestFluxoBuscaIp::test_ip_interno_sem_alertas PASSED                                                                         [ 60%]
testes/test_integracao.py::TestConsistenciaDados::test_todos_alertas_referem_eventos_reais PASSED                                                       [ 60%]
testes/test_integracao.py::TestConsistenciaDados::test_todos_ips_brute_force_sao_do_auth PASSED                                                         [ 61%]
testes/test_integracao.py::TestConsistenciaDados::test_todos_ips_port_scan_sao_do_firewall PASSED                                                       [ 61%]
testes/test_integracao.py::TestConsistenciaDados::test_severidades_validas PASSED                                                                       [ 62%]
testes/test_regras.py::TestCarregarRegras::test_carrega_arquivo_valido PASSED                                                                           [ 62%]
testes/test_regras.py::TestCarregarRegras::test_todas_regras_sao_dicts PASSED                                                                           [ 63%]
testes/test_regras.py::TestCarregarRegras::test_regras_tem_campos_obrigatorios PASSED                                                                   [ 63%]
testes/test_regras.py::TestCarregarRegras::test_carrega_5_regras PASSED                                                                                 [ 64%]
testes/test_regras.py::TestCarregarRegras::test_arquivo_inexistente_retorna_lista_vazia PASSED                                                          [ 64%]
testes/test_regras.py::TestCarregarRegras::test_json_invalido_retorna_lista_vazia PASSED                                                                [ 65%]
testes/test_regras.py::TestCarregarRegras::test_filtra_regras_inativas PASSED                                                                           [ 65%]
testes/test_regras.py::TestCarregarRegras::test_todas_inativas_retorna_lista_vazia PASSED                                                               [ 66%]
testes/test_regras.py::TestClassificarSeveridade::test_critica PASSED                                                                                   [ 67%]
testes/test_regras.py::TestClassificarSeveridade::test_alta PASSED                                                                                      [ 67%]
testes/test_regras.py::TestClassificarSeveridade::test_media PASSED                                                                                     [ 68%]
testes/test_regras.py::TestClassificarSeveridade::test_baixa PASSED                                                                                     [ 68%]
testes/test_regras.py::TestClassificarSeveridade::test_info PASSED                                                                                      [ 69%]
testes/test_regras.py::TestAvaliarRegra::test_r001_detecta_admin PASSED                                                                                 [ 69%]
testes/test_regras.py::TestAvaliarRegra::test_r001_alerta_tem_campos PASSED                                                                             [ 70%]
testes/test_regras.py::TestAvaliarRegra::test_r001_alerta_severidade_correta PASSED                                                                     [ 70%]
testes/test_regras.py::TestAvaliarRegra::test_r001_alerta_ip_correto PASSED                                                                             [ 71%]
testes/test_regras.py::TestAvaliarRegra::test_r001_ignora_usuario_normal PASSED                                                                         [ 71%]
testes/test_regras.py::TestAvaliarRegra::test_r001_ignora_fonte_errada PASSED                                                                           [ 72%]
testes/test_regras.py::TestAvaliarRegra::test_r002_detecta_porta_22 PASSED                                                                              [ 72%]
testes/test_regras.py::TestAvaliarRegra::test_r002_severidade_alta PASSED                                                                               [ 73%]
testes/test_regras.py::TestAvaliarRegra::test_r002_ignora_porta_normal PASSED                                                                           [ 73%]
testes/test_regras.py::TestAvaliarRegra::test_r003_detecta_traversal PASSED                                                                             [ 74%]
testes/test_regras.py::TestAvaliarRegra::test_r003_severidade_critica PASSED                                                                            [ 74%]
testes/test_regras.py::TestAvaliarRegra::test_r003_ignora_url_normal PASSED                                                                             [ 75%]
testes/test_regras.py::TestAvaliarRegra::test_r004_detecta_xss PASSED                                                                                   [ 75%]
testes/test_regras.py::TestAvaliarRegra::test_r004_severidade_alta PASSED                                                                               [ 76%]
testes/test_regras.py::TestAvaliarRegra::test_r005_detecta_wp_admin PASSED                                                                              [ 76%]
testes/test_regras.py::TestAvaliarRegra::test_r005_severidade_media PASSED                                                                              [ 77%]
testes/test_regras.py::TestAvaliarRegra::test_r005_ignora_url_normal PASSED                                                                             [ 77%]
testes/test_regras.py::TestAplicarRegras::test_retorna_lista PASSED                                                                                     [ 78%]
testes/test_regras.py::TestAplicarRegras::test_gera_alerta_para_evento_suspeito PASSED                                                                  [ 78%]
testes/test_regras.py::TestAplicarRegras::test_nao_gera_alerta_para_evento_normal PASSED                                                                [ 79%]
testes/test_regras.py::TestAplicarRegras::test_evento_pode_violar_multiplas_regras PASSED                                                               [ 79%]
testes/test_regras.py::TestAplicarRegras::test_multiplos_eventos_multiplos_alertas PASSED                                                               [ 80%]
testes/test_regras.py::TestAplicarRegras::test_lista_vazia_de_eventos PASSED                                                                            [ 80%]
testes/test_regras.py::TestAplicarRegras::test_lista_vazia_de_regras PASSED                                                                             [ 81%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtrar_por_fonte_auth PASSED                                                                       [ 81%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtrar_por_fonte_firewall PASSED                                                                   [ 82%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtrar_por_fonte_web PASSED                                                                        [ 82%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtrar_por_tipo_fail PASSED                                                                        [ 83%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtrar_por_tipo_block PASSED                                                                       [ 83%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtrar_por_ip PASSED                                                                               [ 84%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtrar_por_fonte_e_tipo PASSED                                                                     [ 84%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtrar_por_fonte_tipo_e_ip PASSED                                                                  [ 85%]
testes/test_relatorios.py::TestFiltrarEventos::test_sem_filtros_retorna_todos PASSED                                                                    [ 85%]
testes/test_relatorios.py::TestFiltrarEventos::test_filtro_sem_match PASSED                                                                             [ 86%]
testes/test_relatorios.py::TestFiltrarEventos::test_lista_vazia PASSED                                                                                  [ 86%]
testes/test_relatorios.py::TestTopIps::test_retorna_lista PASSED                                                                                        [ 87%]
testes/test_relatorios.py::TestTopIps::test_retorna_tuplas PASSED                                                                                       [ 87%]
testes/test_relatorios.py::TestTopIps::test_ordenado_decrescente PASSED                                                                                 [ 88%]
testes/test_relatorios.py::TestTopIps::test_ip_mais_ativo_primeiro PASSED                                                                               [ 88%]
testes/test_relatorios.py::TestTopIps::test_limita_a_n PASSED                                                                                           [ 89%]
testes/test_relatorios.py::TestTopIps::test_n_maior_que_total PASSED                                                                                    [ 89%]
testes/test_relatorios.py::TestTopIps::test_lista_vazia PASSED                                                                                          [ 90%]
testes/test_relatorios.py::TestExportarRelatorioJson::test_cria_arquivo PASSED                                                                          [ 90%]
testes/test_relatorios.py::TestExportarRelatorioJson::test_conteudo_valido PASSED                                                                       [ 91%]
testes/test_relatorios.py::TestExportarRelatorioJson::test_cria_diretorio_se_necessario PASSED                                                          [ 91%]
testes/test_relatorios.py::TestExportarRelatorioJson::test_json_formatado PASSED                                                                        [ 92%]
testes/test_relatorios.py::TestExportarRelatorioJson::test_suporta_caracteres_especiais PASSED                                                          [ 92%]
testes/test_relatorios.py::TestResumoGeral::test_nao_trava_com_dados PASSED                                                                             [ 93%]
testes/test_relatorios.py::TestResumoGeral::test_nao_trava_com_dados_vazios PASSED                                                                      [ 93%]
testes/test_relatorios.py::TestExibirMenu::test_opcao_valida PASSED                                                                                     [ 94%]
testes/test_relatorios.py::TestExibirMenu::test_opcao_zero PASSED                                                                                       [ 94%]
testes/test_relatorios.py::TestExibirMenu::test_opcao_invalida PASSED                                                                                   [ 95%]
testes/test_relatorios.py::TestExibirTabela::test_nao_trava PASSED                                                                                      [ 95%]
testes/test_relatorios.py::TestExibirTabela::test_lista_vazia PASSED                                                                                    [ 96%]
testes/test_servidor.py::TestFormatarAlerta::test_retorna_string PASSED                                                                                 [ 96%]
testes/test_servidor.py::TestFormatarAlerta::test_contem_severidade PASSED                                                                              [ 97%]
testes/test_servidor.py::TestFormatarAlerta::test_contem_ip PASSED                                                                                      [ 97%]
testes/test_servidor.py::TestFormatarAlerta::test_contem_nome_regra PASSED                                                                              [ 98%]
testes/test_servidor.py::TestFormatarAlerta::test_contem_horario PASSED                                                                                 [ 98%]
testes/test_servidor.py::TestServidorIntegracao::test_servidor_aceita_conexao PASSED                                                                    [ 99%]
testes/test_servidor.py::TestServidorIntegracao::test_broadcast_envia_para_multiplos PASSED                                                             [100%]

==================================================================== 197 passed in 0.90s =====================================================================
```

## Divisão de tarefas

### [Elias Matos]
- **Módulos:** 1
- **O que fez:** Implementei o coletor.py, que é a base de tudo: três parsers separados auth, firewall e web que leem
  cada formato de linha e devolvem um dicionário padronizado com timestamp, fonte, tipo, ip, detalhes e linha_original.
  A função carregar_todos_os_logs percorre a pasta e infere a fonte pelo nome do arquivo. Como bônus fiz o
  gerador_logs.py, que cria logs sintéticos com mistura controlada de tráfego normal e cenários de ataque (com seed
  reproduzível).
- **Dificuldades:** O mais difícil foi tratar linhas malformadas sem o programa travar — uma linha de auth.log com campo
  faltando podia gerar IndexError. Resolvi com try/except em cada parser e um helper _extrair_kv que valida os campos
  obrigatórios via dicionário de chave=valor. Quando falta algo, o parser retorna None e o carregador ignora a linha e
  continua, em vez de quebrar tudo.

### [Guilherme Costa — Pessoa B]
- **Módulos:** 2
- **O que fez:** Implementei o motor de regras (regras.py): ele carrega o regras.json filtrando só as regras com ativa:
  true, e a função avaliar_regra faz dispatch pela condicao da regra — usuario_privilegiado, porta_critica,
  path_traversal, xss e reconhecimento. Cada condição extrai o campo certo do detalhes do evento e devolve um alerta
  padronizado quando a regra é violada. Como bônus, fiz a função criar_regra_interativa que permite o operador adicionar
   novas regras pelo menu, sem editar código.
- **Dificuldades:** A parte chata foi cada tipo de regra precisar de um pedaço diferente do detalhes: porta_critica precisa
   de dport como int, path_traversal precisa da URL inteira, e assim por diante. Criei um helper _extrair_kv que parseia
   o campo detalhes num dict, daí cada condição só busca a chave que precisa, e a função _montar_alerta garante que
  todo alerta saia com os mesmos 6 campos.

### [Gustavo Cesar]
- **Módulos:** 3
- **O que fez:** Implementei o detector.py com três análises que só aparecem quando você correlaciona vários eventos:
  detectar_brute_force conta FAILs por IP, detectar_port_scan conta portas únicas por IP usando set, e
  verificar_blacklist faz interseção de sets com a lista de IPs maliciosos conhecidos. A gerar_resumo_ameacas consolida
  tudo numa pontuação (5 pontos por detecção). Como bônus, fiz a detectar_brute_force_temporal com janela deslizante,
  que detecta picos de FAIL em janelas configuráveis de segundos.
- **Dificuldades:** Tive um empate chato na pontuação: o IP 185.220.101.1 e o 91.240.118.172 caíam nas 3 detecções e
  empatavam em 15 pontos, mas o 185 era claramente mais perigoso (11 tentativas vs 5, 7 portas vs 3). O teste exigia que
   o 185 viesse primeiro. Resolvi adicionando um critério de desempate no sorted: a soma das métricas brutas (tentativas
   + portas + eventos blacklist) entra como segundo critério, então o IP mais intenso sobe naturalmente.

### [Italo Henrique]
- **Módulos:** 4
- **O que fez:** Implementei o servidor_alertas.py e o cliente_alertas.py. O servidor é TCP multithread na porta 9999,
  aceita vários clientes em paralelo, mantém um dicionário clientes compartilhado protegido por threading.Lock(), e
  oferece broadcast_alerta pra empurrar mensagens pra todo mundo conectado. O cliente roda uma thread de recebimento em
  paralelo com o input() do usuário, e suporta /status, /historico (últimos 10 alertas) e /sair.
- **Dificuldades:** Duas coisas. Primeiro a concorrência: segurar o lock durante o sendall() podia travar o servidor
  inteiro se um cliente lento bloqueasse a escrita. Resolvi tirando um snapshot da lista de clientes dentro do lock e
  fazendo o I/O fora dele. Segundo, no Windows o Ctrl+C não interrompe socket.accept() bloqueante — o servidor ficava
  preso. A solução foi settimeout(1.0) no socket de escuta: o accept retorna a cada 1 segundo, e nessas pausas o Python
  processa o KeyboardInterrupt.

### [Pedro Rossi]
- **Módulos:** 5, 6
- **O que fez:** No enriquecimento.py, implementei a classificação RFC 1918 de IPs privados/públicos e a consulta à API do
  ipinfo.io com cache, tratando Timeout, ConnectionError, rate limit 429 e JSON inválido. No relatorios.py, fiz o menu
  CLI, os filtros (filtrar_eventos, top_ips, buscar_ip), a exportação JSON e a tabela formatada com colunas alinhadas.
  Como bônus, escrevi o integridade.py que calcula SHA-256 dos logs e compara contra um baseline em config/hashes.json,
  detectando se algum log foi alterado.
- **Dificuldades:** O cache do enriquecimento exigiu cuidado: a primeira versão guardava qualquer resultado, mas isso
  'envenenava' o cache se a primeira chamada caísse num timeout — a falha ficava lá pra sempre, bloqueando novas
  tentativas. Corrigi pra só cachear resultados determinísticos (sucesso da API, IP privado, IP inválido) e deixar erros
   de rede fora do cache. No relatórios, o pega foi a serialização — set e tuple quebram o json.dump, então fiz um
  helper _serializar recursivo que converte set em lista antes de gravar.

## Funcionalidades bônus implementadas

- [X] Correlação temporal (brute force por janela de tempo)
- [X] Hash de integridade dos logs (hashlib)
- [X] Geração automática de logs para teste
- [X] Criação de regras customizadas pelo menu
