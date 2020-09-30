library(tidyverse)

df.geral <- read.csv2("data/informe_epidemiologico_02_09_2020_geral.csv")
df.casos.obitos <- read_csv2("data/informe_epidemiologico_02_09_2020_casos_obitos_municipios.csv")

cwb.reg <- c("ADRIANOPOLIS", "AGUDOS DO SUL", "ALMIRANTE TAMANDARE",
             "ARAUCARIA", "BALSA NOVA", "BOCAIUVA DO SUL",
             "CAMPINA GRANDE DO SUL","CAMPO DO TENENTE", "CAMPO LARGO",
             "CAMPO MAGRO","CERRO AZUL", "COLOMBO", "CONTENDA",
             "CURITIBA", "DOUTOR ULYSSES","FAZENDA RIO GRANDE","ITAPERUCU",
             "LAPA","MANDIRITUBA","PIEN", "PINHAIS", "PIRAQUARA",
             "QUATRO BARRAS", "QUITANDINHA", "RIO BRANCO DO SUL",
             "RIO NEGRO", "SAO JOSE DOS PINHAIS", "TIJUCAS DO SUL",
             "TUNAS DO PARANA")

df.cwb.reg <- df.geral %>% filter(df.geral$MUN_RESIDENCIA == cwb.reg)


df.cwb.reg$IDADE_ORIGINAL <- as.integer(df.cwb.reg$IDADE_ORIGINAL)

