Diretoria de Infraestrutura de TIC – DIT 
Superintendência de Planejamento e Suporte de TIC – SUPS 
Departamento de Qualidade de Infraestrutura – DEQI 

Artigo técnico de Infraestrutura de TIC

CONFIGURAÇÃO DE WORKLOADS PARA A REALIZAÇÃO DE TESTES DE DESEMPENHO VIA SILK PERFORMER

Autor: João Bernardo Müller de Mesquita
Responsável: Eduardo Fritzen 

SUMÁRIO

	O presente artigo tem como objetivo principal analisar os modelos de workloads existentes no Silk Performer 9.5 destacando a importância da definição de tais modelos para a engenharia de desempenho.

DESAFIOS

	O artigo considera a seleção de um modelo de workload adequado aos objetivos do teste como uma das principais dificuldades existentes atualmente no planejamento de testes de desempenho. 

BENEFÍCIOS

	O artigo procura contribuir para um melhor entendimento acerca dos modelos de carga de trabalho disponíveis na ferramenta Silk Performer e sua adequação a determinados tipos de teste de desempenho. 

1. VISÃO GERAL DO SILK PERFORMER

	O Silk Performer é uma ferramenta desenvolvida pela empresa Borland para a elaboração, execução e análise de testes automatizados de desempenho. Entre os recursos oferecidos pela solução encontram-se o suporte a diversos frameworks de desenvolvimento, a realização de testes para a plataforma móvel e ambiente em nuvem e a customização de testes por meio da definição de tipos de usuários e da configuração de workloads.
	O Silk Performer permite a criação de projetos de teste. Todo projeto é composto basicamente por seis componentes principais: 
Profiles: Contém o perfil dos grupos de usuários virtuais participantes do projeto. 
Scripts: Reúne os scripts de testes em linguagem BDL gerados de forma manual ou automatizada.
Include Files: Armazena arquivos BDH que permitem a criação de bibliotecas de código e o seu reúso em outros projetos de teste de desempenho.
Data Files: Agrupa todos os arquivos externos utilizados como massa de dados no teste.
Agents: Lista as máquinas configuradas para a simulação dos usuários virtuais nos testes de desempenho.
Workloads: Contém as estratégias de carga de trabalho utilizadas no projeto.

2. CONFIGURAÇÃO DE WORKLOADS

	A criação de workloads constitui uma etapa fundamental na preparação de um teste. Sob o ponto de vista da engenharia de desempenho, eleger um modelo de workload adequado aos objetivos do teste torna-se um fator essencial para uma avaliação mais precisa do comportamento da aplicação quando submetida a uma determinada carga de usuários virtuais.
	Segundo o cofundador da empresa PretotypeLabs e ex-diretor da Google, Alberto Savoia1, um dos principais problemas relacionados aos testes de desempenho consiste na leitura simplista de  cenários ou situações hipotéticas nas quais se deseja avaliar o comportamento de uma aplicação. Para Rico Mariani2, engenheiro de software da Microsoft, uma das dificuldades mais comuns neste tipo de situação residiria na escolha do foco de análise do teste, dada a miríade de aspectos de um sistema que podem ser avaliados. Em ambos os casos, a seleção do modelo de workload correto torna-se crucial para que os resultados dos testes condigam com a realidade.
	Sob o ponto de vista prático, a configuração de um workload exige a definição de uma série de informações que poderão variar segundo o modelo escolhido. No geral, as cargas de trabalho apresentam os seguintes parâmetros: tipo e quantidade máxima de usuários virtuais utilizados; estratégia de crescimento de carga; tempos de warmup, espera, simulação, medição e início do teste, entre outros.

3. TIPOS DE WORKLOAD DO SILK PERFORMER

	Dada a importância dos workloads para análise de um teste, seguem abaixo os principais modelos de carga de trabalho disponibilizados pelo Silk Performer 9.5: 

Increasing (Incremental): Neste modelo, a quantidade de usuários virtuais aumenta gradativamente até atingir o limite máximo definido. Esta modalidade é indicada quando o objetivo do teste consiste em determinar o nível de carga no qual a aplicação começa a apresentar problemas como interrupção de funcionamento, produção de erros, aumento do tempo de resposta acima do limiar aceitável pelo projeto e etc.
Steady State (Fixo): Nesta categoria, o número de usuários virtuais se mantém constante durante todo o período do teste. Os usuários virtuais executam diversas vezes as transações definidas nos scripts de teste e o tempo total de teste é pré-determinado. Este tipo de modelo é geralmente utilizado quando o teste almeja avaliar o comportamento do sistema em uma carga de trabalho específica. 
Dynamic (Dinâmico): Esta estratégia permite que a carga de trabalho seja alterada dinamicamente durante a realização do teste, desde que respeitando o limite máximo de usuários virtuais preestabelecido. Além disto, não existe um tempo determinado de teste, pois o analista é quem deverá interrompê-lo manualmente. Este modelo é recomendado quando se deseja analisar o desempenho do sistema em um cenário com carga diversificada e manter o controle sobre o aumento ou diminuição do número de usuários virtuais.
All Day (Diário): Este tipo é indicado para cenários mais complexos que simulam um período diário de funcionamento da aplicação. Para cada tipo de usuário, a carga pode ser distribuída de maneira flexível, permitindo atribuir diferentes quantidades de usuários virtuais em momentos distintos. Este modelo de carga pode simular picos de utilização e identificar os horários em que o sistema apresenta problemas de desempenho.
Queuing (Fila): Modelo indicado para aplicações que utilizam mecanismos de enfileiramento para o processamento de requisições concorrentes. As transações são geradas  por uma taxa que é calculada randomicamente e que está baseada no tempo total de teste e no número máximo de transações, ambos definidos previamente. O teste é finalizado quando todos os usuários virtuais houverem completado suas tarefas.
Verification (Verificação): Este modelo de carga é recomendado para a realização de testes de sanidade, cujo objetivo é verificar através de uma quantidade mínima de usuários virtuais a existência de algum erro funcional na aplicação ou de problemas no ambiente de execução do teste. O teste de sanidade geralmente é executado antes do teste de desempenho propriamente dito.

CONCLUSÃO

	Além dos padrões exibidos acima, o Silk Performer 9.5 permite também a customização de workloads, oferecendo deste modo aos analistas de teste a possibilidade de se configurar cenários muito mais complexos.

REFERÊNCIAS

MEIER, J.D. et.al. Performance Testing Guidance for Web Applications: patterns & practices. [S.I], Microsoft Corporation, 2007. Disponível em: http://msdn.microsoft.com/en-us/library/bb924375.aspx . Acesso em: 30 jan. 2014.

DIAS, Felipe; SHIKANAI, Hamilton; GOUVEIA, Rodrigo. Silk Performer Guia básico do Silk Performer versão 1.1.1. Disponível em: http://www-processos/ativos_processo/padrao_desenvolvimento_software/head/arquivos/testes/gui_Uso_Silk_Performer.pdf Acesso em: 29 jan. 2014

SILK PERFORMER 9.5. Adjust the workload of your load test.



















 

